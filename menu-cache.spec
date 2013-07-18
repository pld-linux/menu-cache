Summary:	Library for caching freedesktop defined application menus
Summary(pl.UTF-8):	Biblioteka do buforowania menu freedesktop.org
Name:		menu-cache
Version:	0.5.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	3a757b0a8a668081eb8685140c0e69e8
URL:		http://www.lxde.org/
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm >= 4.4.9-56
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libmenu-cache is a library creating and utilizing caches to speed up
the manipulation for freedesktop.org defined application menus. It can
be used as a replacement of libgnome-menu of gnome-menus.

%description -l pl.UTF-8
Libmenu-cache jest biblioteką do tworzenia i używania buforów
(caches), które przyspieszają wczytywanie i zapisywanie menu zgodnego
z freedesktop.org. Libmenu-cache może zastępować libgnome-menu.

%package devel
Summary:	Header files and libraries for menu-cache development
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do menu-cache
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Libmenu-cache is a library creating and utilizing caches to speed up
the manipulation for freedesktop.org defined application menus. It can
be used as a replacement of libgnome-menu of gnome-menus.

This package contains the header files needed to develop programs that
use these menu-cache.

%description devel -l pl.UTF-8
Libmenu-cache jest biblioteką do tworzenia i używania buforów
(caches), które przyspieszają wczytywanie i zapisywanie menu zgodnego
z freedesktop.org. Libmenu-cache może zastępować libgnome-menu.

Pakiet ten zawiera pliki nagłowkowe i dokumentację potrzebną przy
tworzeniu własnych programów wykorzystujących menu-cache.

%package static
Summary:	Static library for menu-cache development
Summary(pl.UTF-8):	Biblioteka statyczna do menu-cache
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Libmenu-cache is a library creating and utilizing caches to speed up
the manipulation for freedesktop.org defined application menus. It can
be used as a replacement of libgnome-menu of gnome-menus.

This package contains the header files and libraries needed to develop
programs that use these menu-cache.

%description static -l pl.UTF-8
Libmenu-cache jest biblioteką do tworzenia i używania buforów
(caches), które przyspieszają wczytywanie i zapisywanie menu zgodnego
z freedesktop.org. Libmenu-cache może zastępować libgnome-menu.

Pakiet ten zawiera bibliotekę statyczną potrzebną przy tworzeniu
własnych programów wykorzystujących menu-cache.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libmenu-cache.so.3*
%attr(755,root,root) %{_libdir}/menu-cache*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmenu-cache.so
%{_libdir}/libmenu-cache.la
%dir %{_includedir}/menu-cache
%{_includedir}/menu-cache/menu-cache.h
%{_pkgconfigdir}/libmenu-cache.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmenu-cache.a
