%define devname %mklibname -d magpie-wm

%global glib_version 2.69.0
%global gtk3_version 3.19.8
%global gsettings_desktop_schemas_version 40~alpha
%global json_glib_version 0.12.0
%global libinput_version 1.19.0
%global pipewire_version 0.3.33
%global lcms2_version 2.6
%global colord_version 1.4.5
%global magpie_abi_version magpie-0

%define oname magpie
 
Name:          magpie-wm
Version:       0.9.3
Release:       2
Summary:       Window manager for Budgie Desktop
Group:		       Graphical desktop/Budgie
License:       GPL-2.0-or-later
URL:           https://github.com/BuddiesOfBudgie/magpie
Source0:       %{url}/releases/download/v%{version}/magpie-%{version}.tar.xz
 
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
BuildRequires: egl-devel
BuildRequires: pkgconfig(dri)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pam-devel
BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(sysprof-capture-4)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: x11-server-xorg
BuildRequires: x11-server-xvfb
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: zenity-gtk
BuildRequires: desktop-file-utils
BuildRequires: cvt
# Bootstrap requirements
BuildRequires: gtk-doc gettext-devel git-core
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gnome-settings-daemon)
BuildRequires: meson
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(colord)
 
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libinput) 

#Requires: control-center-filesystem
Requires: gsettings-desktop-schemas%{?_isa}
Requires: gnome-settings-daemon
Requires: gtk+3
Requires: json-glib
Requires: libinput
Requires: pipewire
Requires: %{_lib}startup-notification-1_0
Requires: dbus
Requires: zenity-gtk
Requires: mutter

Provides: firstboot(windowmanager) = magpie
 
# Cogl and Clutter were forked at these versions, but have diverged
# significantly since then.
Provides: bundled(cogl) = 1.22.0
Provides: bundled(clutter) = 1.26.0
 
%description
Magpgie is the window manager used by Budgie Desktop.
 
%package -n %{devname}
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# for EGL/eglmesaext.h that's included from public cogl-egl-defines.h header
Requires: egl-devel
 
%description -n %{devname}
Header files and libraries for developing against Magpie.
 
%prep
%autosetup -n magpie-%{version} -p1
 
%build
%meson -Degl_device=true
%meson_build
%install
%meson_install
%find_lang magpie
 
%files -f magpie.lang
%license COPYING
%{_libdir}/lib%{magpie_abi_version}.so.0
%{_libdir}/lib%{magpie_abi_version}.so.0.0.0
%{_libdir}/%{magpie_abi_version}/Cally-0.*
%{_libdir}/%{magpie_abi_version}/Clutter-0.*
%{_libdir}/%{magpie_abi_version}/Cogl-0.*
%{_libdir}/%{magpie_abi_version}/CoglPango-0.*
%{_libdir}/%{magpie_abi_version}/Meta-0.*
%{_libdir}/%{magpie_abi_version}/lib%{oname}-clutter-0.*
%{_libdir}/%{magpie_abi_version}/lib%{oname}-cogl-0.*
%{_libdir}/%{magpie_abi_version}/lib%{oname}-cogl-pango-0.*
 
%files -n %{devname}
%{_includedir}/%{magpie_abi_version}
%{_libdir}/lib%{magpie_abi_version}.so
%{_libdir}/pkgconfig/lib%{magpie_abi_version}.pc
%{_libdir}/pkgconfig/%{oname}-clutter-0.pc
%{_libdir}/pkgconfig/%{oname}-cogl-0.pc
%{_libdir}/pkgconfig/%{oname}-cogl-pango-0.pc
