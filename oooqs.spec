Summary:	Open Office Quickstarter
Summary(pl):	Szybszy start Open Office
Name:		oooqs
Version:	1.0
%define		_rc	rc3
Release:	0.%{_rc}.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/segfaultskde/%{name}-%{version}_%{_rc}.tar.gz
# Source0-md5: d1eecb568523748ee8489c9d61ffadc6
URL:		http://segfaultskde.berlios.de/oooqs/
BuildRequires:	kdebase-devel >= 3.0.5a
BuildRequires:	qt-devel >= 3.0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%description
OpenOffice.org Quickstarter is a small application that runs in the
KDE SystemTray. It is used to quickly start the different
OpenOffice.org modules without having to go through the K-Menu.

%description -l pl
Szybszy start Open Office jest ma³± aplikacj±, która uruchamia siê w
KDE System Tray. Mo¿na go u¿ywaæ do przy¶pieszania startu modu³ów Open
Office bez wchodzeni± w menu.

%prep
%setup -q -n %{name}-%{version}_%{_rc}

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
export CXXFLAGS
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang oooqs --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f oooqs.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/[!l]*/*/*/*
%{_applnkdir}/Office/oooqs.desktop
