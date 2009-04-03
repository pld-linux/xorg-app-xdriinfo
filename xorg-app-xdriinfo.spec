Summary:	xdriinfo application to query configuration information of DRI drivers
Summary(pl.UTF-8):	Aplikacja xdriinfo do sprawdzania konfiguracji sterowników DRI
Name:		xorg-app-xdriinfo
Version:	1.0.2
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xdriinfo-%{version}.tar.bz2
# Source0-md5:	a5ec51ed9f0a55dc3462d90d52ff899c
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdriinfo program can be used to query configuration information of
direct rendering drivers. If no command argument is specified it lists
the names of the direct rendering drivers for all screens.

%description -l pl.UTF-8
Program xdriinfo służy do odczytu informacji o konfiguracji
sterowników bezpośredniego renderingu (Direct Rendering, DRI). Jeśli
nie podano argumentu z linii poleceń, program wyświetla nazwy
sterowników DRI dla wszystkich ekranów.

%prep
%setup -q -n xdriinfo-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xdriinfo
%{_mandir}/man1/xdriinfo.1x*
