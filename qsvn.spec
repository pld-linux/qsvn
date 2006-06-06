Summary:	QSvn - Subversion Client
Summary(de):	QSvn - Ein Subversion Klient
Summary(pl):	QSvn - Klient Subversion
Name:		qsvn
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/qsvn/%{name}-%{version}-src.tar.gz
# Source0-md5:	a96d635b4494ce629c2e095b0d078d61
Source1:	%{name}.desktop
Patch0:		%{name}-includes.patch
URL:		http://ar.oszine.de/projects/qsvn/
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	subversion-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QSvn is a graphical Subversion Client for Linux, UNIX, Windows and Mac
OS X. We use the Subversion API for all Subversion actions and the Qt4
C++ toolkit from Trolltech for platform independent programming.

%description -l de
QSvn ist ein graphischer Subversion Klient für Linux, Unix, Windows
und Mac OS X. Es benutzt die Subversion API für alle Befehle die etwas
mit Subversion zu tun haben, Qt4 und C++ um auf sovielen Platformen
wie möglich zu programieren.

%description -l pl
QSvn jest graficznym klientem Subversion dla Linuksa, Uniksa, Windowsa
oraz Mac OS X. U¿ywa API Subversion dla wszystkich czynno¶ci
zwi±zanych z svnem, Qt4 i C++ do wieloplatformowego programowania.

%prep
%setup -q
%patch0 -p0

%build
export QTDIR=%{_prefix}
qt4-qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}
install bin/qsvn $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install images/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
