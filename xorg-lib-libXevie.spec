Summary:	X Evie extension library
Summary(pl):	Biblioteka rozszerzenia X Evie
Name:		xorg-lib-libXevie
Version:	0.99.3
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/lib/libXevie-%{version}.tar.bz2
# Source0-md5:	b3ddbc0170b987278a213a51df15bc99
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-evieext-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Evie extension library.

%description -l pl
Biblioteka rozszerzenia X Evie.

%package devel
Summary:	Header files libXevie development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXevie
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-evieext-devel

%description devel
X Evie extension library

This package contains the header files needed to develop programs that
use these libXevie.

%description devel -l pl
Biblioteka rozszerzenia X Evie.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXevie.

%package static
Summary:	Static libXevie library
Summary(pl):	Biblioteka statyczna libXevie
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
X Evie extension library

This package contains the static libXevie library.

%description static -l pl
Biblioteka rozszerzenia X Evie.

Pakiet zawiera statyczn± bibliotekê libXevie.

%prep
%setup -q -n libXevie-%{version}

%build
%{__libtoolize}
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
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXevie.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXevie.so
%{_libdir}/libXevie.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xevie.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXevie.a
