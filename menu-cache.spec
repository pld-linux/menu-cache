Summary:	Library for caching freedesktop defined application menus
Summary(pl.UTF-8):	Biblioteka do buforowania menu freedesktop.org
Name:		menu-cache
Version:	1.1.0
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	99999a0bca48b980105208760c8fd893
Patch0:		upstream-libmenu-cache_Fix-memory-leaks.patch
Patch1:		menu-cache-1.1.0-0001-Support-gcc10-compilation.patch
URL:		http://www.lxde.org/
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	libfm-extra-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.16.0
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
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.16.0

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

Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
tworzeniu własnych programów wykorzystujących menu-cache.

%package static
Summary:	Static library for menu-cache development
Summary(pl.UTF-8):	Biblioteka statyczna do menu-cache
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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

%package apidocs
Summary:	API documentation for menu-cache library
Summary(pl.UTF-8):	Dokumentacja API biblioteki menu-cache
Group:		Documentation

%description apidocs
API documentation for menu-cache library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki menu-cache.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmenu-cache.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libmenu-cache.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmenu-cache.so.3
%dir %{_libexecdir}/menu-cache
%attr(755,root,root) %{_libexecdir}/menu-cache/menu-cache-gen
%attr(755,root,root) %{_libexecdir}/menu-cache/menu-cached

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmenu-cache.so
%dir %{_includedir}/menu-cache
%{_includedir}/menu-cache/menu-cache.h
%{_pkgconfigdir}/libmenu-cache.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmenu-cache.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmenu-cache
