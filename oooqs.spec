Summary:	Open Office Quickstarter
Summary(pl):	Szybszy start Open Office
Name:		oooqs
Version:	0.9.5.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/segfaultskde/%{name}-%{version}.tar.gz
URL:		http://segfaultskde.berlios.de/oooqs/
BuildRequires:	kdebase-devel >= 3.0.2
BuildRequires:	qt-devel >= 3.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
OpenOffice.org Quickstarter is a small application that runs in the
KDE SystemTray. It is used to quickly start the different
OpenOffice.org modules without having to go through the K-Menu.

%description -l pl
Szybszy start Open Office jest ma³± aplikacj±, która uruchamia siê w
KDE System Tray. Mo¿na go u¿ywaæ do przy¶pieszania startu modu³ów Open
Office bez wchodzeni± w menu.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
export CXXFLAGS

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/pixmaps

%{__make} DESTDIR=$RPM_BUILD_ROOT install

cp -R $RPM_BUILD_ROOT%{_datadir}/icons/* $RPM_BUILD_ROOT%{_datadir}/pixmaps

%find_lang oooqs --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f oooqs.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pixmaps/*/*/*/*.png
%{_datadir}/doc/HTML/en/oooqs/*
%{_applnkdir}/Applications/oooqs.desktop
