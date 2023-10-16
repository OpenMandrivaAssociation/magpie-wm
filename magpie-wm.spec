%global glib_version 2.69.0
%global gtk3_version 3.19.8
%global gsettings_desktop_schemas_version 40~alpha
%global json_glib_version 0.12.0
%global libinput_version 1.19.0
%global pipewire_version 0.3.33
%global lcms2_version 2.6
%global colord_version 1.4.5
%global magpie_abi_version magpie-0
 
Name:          magpie
Version:       0.9.2
Release:       1%{?dist}
Summary:       Window manager for Budgie Desktop
 
License:       GPL-2.0-or-later
URL:           https://github.com/BuddiesOfBudgie/magpie
Source0:       %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
 
Patch0:        meson-add-back-default-driver-option.patch
Patch1:        Remove-support-for-window-shading.patch
 
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.41.0
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xtst)
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGLES-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pam-devel
BuildRequires: pkgconfig(libpipewire-0.3) >= %{pipewire_version}
BuildRequires: pkgconfig(sysprof-capture-4)
BuildRequires: sysprof-devel
BuildRequires: pkgconfig(libsystemd)
BuildRequires: xorg-x11-server-Xorg
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: zenity
BuildRequires: desktop-file-utils
# Bootstrap requirements
BuildRequires: gtk-doc gettext-devel git-core
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(gsettings-desktop-schemas) >= %{gsettings_desktop_schemas_version}
BuildRequires: pkgconfig(gnome-settings-daemon)
BuildRequires: meson
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(lcms2) >= %{lcms2_version}
BuildRequires: pkgconfig(colord) >= %{colord_version}
 
BuildRequires: pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires: pkgconfig(libinput) >= %{libinput_version}
 
Requires: control-center-filesystem
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gnome-settings-daemon
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: json-glib%{?_isa} >= %{json_glib_version}
Requires: libinput%{?_isa} >= %{libinput_version}
Requires: pipewire%{_isa} >= %{pipewire_version}
Requires: startup-notification
Requires: dbus
Requires: zenity
Requires: mutter-common
 
Recommends: mesa-dri-drivers%{?_isa}
 
Provides: firstboot(windowmanager) = magpie
 
# Cogl and Clutter were forked at these versions, but have diverged
# significantly since then.
Provides: bundled(cogl) = 1.22.0
Provides: bundled(clutter) = 1.26.0
 
%description
Magpgie is the window manager used by Budgie Desktop.
 
%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# for EGL/eglmesaext.h that's included from public cogl-egl-defines.h header
Requires: mesa-libEGL-devel
 
%description devel
Header files and libraries for developing against Magpie.
 
%prep
%autosetup -S git
 
%build
%meson -Degl_device=true
%meson_build
%install
%meson_install
%find_lang %{name}
 
%files -f %{name}.lang
%license COPYING
%{_libdir}/lib%{magpie_abi_version}.so.0
%{_libdir}/lib%{magpie_abi_version}.so.0.0.0
%{_libdir}/%{magpie_abi_version}/Cally-0.*
%{_libdir}/%{magpie_abi_version}/Clutter-0.*
%{_libdir}/%{magpie_abi_version}/Cogl-0.*
%{_libdir}/%{magpie_abi_version}/CoglPango-0.*
%{_libdir}/%{magpie_abi_version}/Meta-0.*
%{_libdir}/%{magpie_abi_version}/lib%{name}-clutter-0.*
%{_libdir}/%{magpie_abi_version}/lib%{name}-cogl-0.*
%{_libdir}/%{magpie_abi_version}/lib%{name}-cogl-pango-0.*
 
%files devel
%{_includedir}/%{magpie_abi_version}
%{_libdir}/lib%{magpie_abi_version}.so
%{_libdir}/pkgconfig/lib%{magpie_abi_version}.pc
%{_libdir}/pkgconfig/%{name}-clutter-0.pc
%{_libdir}/pkgconfig/%{name}-cogl-0.pc
%{_libdir}/pkgconfig/%{name}-cogl-pango-0.pc
