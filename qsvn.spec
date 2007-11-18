Summary:	QSvn - Subversion Client
Summary(de.UTF-8):	QSvn - Ein Subversion Klient
Summary(pl.UTF-8):	QSvn - Klient Subversion
Name:		qsvn
Version:	0.5.0
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/qsvn/%{name}-%{version}-src.tar.gz
# Source0-md5:	03927a26532996fbb79a47c40b8bf181
Source1:	%{name}.desktop
Patch0:		%{name}-qt4tools.patch
URL:		http://ar.oszine.de/projects/qsvn/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	cmake >= 2.4.0
BuildRequires:	mysql-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
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
%patch0 -p1

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
install build/bin/libsvnqt-qt4.so.3.0.0 $RPM_BUILD_ROOT%{_libdir}
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
