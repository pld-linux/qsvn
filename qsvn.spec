Summary:	QSvn - Subversion Client
Summary(de.UTF-8):	QSvn - Ein Subversion Klient
Summary(pl.UTF-8):	QSvn - Klient Subversion
Name:		qsvn
Version:	0.8.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.anrichter.net/projects/qsvn/chrome/site/%{name}-%{version}-src.tar.gz
# Source0-md5:	e3ed92cbea9af08f8a8a471656b511dd
Source1:	%{name}.desktop
URL:		http://www.anrichter.net/projects/qsvn/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	cmake >= 2.4.0
BuildRequires:	mysql-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRequires:	subversion-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QSvn is a graphical Subversion Client for Linux, UNIX, Windows and Mac
OS X. We use the Subversion API for all Subversion actions and the Qt4
C++ toolkit from Trolltech for platform independent programming.

%description -l de.UTF-8
QSvn ist ein graphischer Subversion Klient für Linux, Unix, Windows
und Mac OS X. Es benutzt die Subversion API für alle Befehle die etwas
mit Subversion zu tun haben, Qt4 und C++ um auf sovielen Platformen
wie möglich zu programieren.

%description -l pl.UTF-8
QSvn jest graficznym klientem Subversion dla Linuksa, Uniksa, Windows
oraz Mac OS X. Używa API Subversion dla wszystkich czynności
związanych z svnem, Qt4 i C++ do wieloplatformowego programowania.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE="Release" \
	../src
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_desktopdir},%{_pixmapsdir}}
install build/bin/qsvn $RPM_BUILD_ROOT%{_bindir}
install build/%{_lib}/libsvnqt4.so.*.*.* $RPM_BUILD_ROOT%{_libdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install src/images/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
