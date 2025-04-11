%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6Wallet
%define devname %mklibname KF6Wallet -d
#define git 20240217

Name: kf6-kwallet
Version: 6.13.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kwallet/-/archive/master/kwallet-master.tar.bz2#/kwallet-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/kwallet-%{version}.tar.xz
%endif
Summary: Safe desktop-wide storage for passwords
URL: https://invent.kde.org/frameworks/kwallet
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(Qca-qt6)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Crash)
BuildRequires: pkgconfig(libgcrypt)
BuildRequires: cmake(Gpgmepp)
# Just to make sure the plasma5 version isn't pulled in
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

%description
Safe desktop-wide storage for passwords

%package -n %{libname}
Summary: Safe desktop-wide storage for passwords
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Safe desktop-wide storage for passwords

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Safe desktop-wide storage for passwords

%prep
%autosetup -p1 -n kwallet-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kwallet.*
%{_bindir}/kwallet-query
%{_bindir}/kwalletd6
%{_datadir}/applications/org.kde.kwalletd6.desktop
%{_datadir}/dbus-1/interfaces/kf6_org.kde.KWallet.xml
%{_datadir}/dbus-1/services/org.kde.kwalletd6.service
%{_datadir}/dbus-1/services/org.kde.kwalletd5.service
%{_datadir}/knotifications6/kwalletd6.notifyrc
%{_datadir}/xdg-desktop-portal/portals/kwallet.portal
%{_mandir}/man1/kwallet-query.1*

%files -n %{devname}
%{_includedir}/KF6/KWallet
%{_libdir}/cmake/KF6Wallet
%{_qtdir}/doc/KF6Wallet.*

%files -n %{libname}
%{_libdir}/libKF6Wallet.so*
%{_libdir}/libKF6WalletBackend.so*
