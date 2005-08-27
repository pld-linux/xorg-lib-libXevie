# $Rev: 3305 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	X Evie extension library
Summary(pl):	Biblioteka rozszerzenia X Evie
Name:		xorg-lib-libXevie
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXevie-%{version}.tar.bz2
# Source0-md5:	590c46ff5efb88d16c17511158b04078
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-proto-evieext-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXevie-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
X Evie extension library.

%description -l pl
Biblioteka rozszerzenia X Evie.


%package devel
Summary:	Header files libXevie development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXevie
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXevie = %{version}-%{release}
Requires:	xorg-proto-evieext-devel
Requires:	xorg-lib-libXext-devel

%description devel
X Evie extension library

This package contains the header files needed to develop programs that
use these libXevie.

%description devel -l pl
Biblioteka rozszerzenia X Evie.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXevie.


%package static
Summary:	Static libXevie libraries
Summary(pl):	Biblioteki statyczne libXevie
Group:		Development/Libraries
Requires:	xorg-lib-libXevie-devel = %{version}-%{release}

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
%doc AUTHORS ChangeLog
%attr(755,root,wheel) %{_libdir}/libXevie.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXevie.la
%attr(755,root,wheel) %{_libdir}/libXevie.so
%{_pkgconfigdir}/xevie.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXevie.a
