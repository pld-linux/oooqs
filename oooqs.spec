Summary:	Open Office Quickstarter
Summary(pl):	Szybszy start Open Office
Name:		oooqs
Version:	2.0.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/segfaultskde/%{name}-%{version}.tar.gz
# Source0-md5:	5d401aa7250f80734d785d4c286f635b
URL:		http://segfaultskde.berlios.de/oooqs/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 3.0.5a
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenOffice.org Quickstarter is a small application that runs in the
KDE SystemTray. It is used to quickly start the different
OpenOffice.org modules without having to go through the K-Menu.

%description -l pl
Szybszy start Open Office jest ma³± aplikacj±, która uruchamia siê w
KDE System Tray. Mo¿na go u¿ywaæ do przy¶pieszania startu modu³ów Open
Office bez wchodzenia w menu.

%prep
%setup -q

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"
export CXXFLAGS

%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang oooqs --with-kde

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
cp src/oooqs.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f oooqs.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/[!l]*/*/*/*
%{_desktopdir}/kde/oooqs.desktop
%{_datadir}/autostart/oooqs.desktop
