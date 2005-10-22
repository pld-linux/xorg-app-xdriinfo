Summary:	xdriinfo application
Summary(pl):	Aplikacja xdriinfo
Name:		xorg-app-xdriinfo
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/xdriinfo-%{version}.tar.bz2
# Source0-md5:	cef02cf2f930fbe3b144d20ca6630b4d
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdriinfo application.

%description -l pl
Aplikacja xdriinfo.

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
	DESTDIR=$RPM_BUILD_ROOT \
	appmandir=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1x*
