Summary:	QSvn - Subversion Client
Summary(pl):	QSvn - Klient Subversion
Name:		qsvn
Version:	0.4.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/qsvn/%{name}-%{version}-src.tar.gz
# Source0-md5:	a96d635b4494ce629c2e095b0d078d61
Source1:	%{name}.desktop
# Source1-md5:	c0b998ade1a72f40733e38a4f905b3c6
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}
install bin/qsvn $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
