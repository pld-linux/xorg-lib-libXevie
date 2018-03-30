Summary:	X Evie extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X Evie
Name:		xorg-lib-libXevie
Version:	1.0.3
Release:	3
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXevie-%{version}.tar.bz2
# Source0-md5:	ffa3f82595211609140440505b0e6301
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-evieproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Evie extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia X Evie.

%package devel
Summary:	Header files for libXevie library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXevie
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-evieext-devel

%description devel
X Evie extension library

This package contains the header files needed to develop programs that
use libXevie.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia X Evie.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXevie.

%package static
Summary:	Static libXevie library
Summary(pl.UTF-8):	Biblioteka statyczna libXevie
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
X Evie extension library

This package contains the static libXevie library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia X Evie.

Pakiet zawiera statyczną bibliotekę libXevie.

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXevie.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXevie.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXevie.so
%{_libdir}/libXevie.la
%{_includedir}/X11/extensions/Xevie.h
%{_pkgconfigdir}/xevie.pc
%{_mandir}/man3/Xevie*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXevie.a
