Name:       	bsc
Version:    	2.27
Release:    	%mkrel 1
Summary:    	Beesoft Commander file manager 
License:    	GPL
Group:      	File tools
URL:        	http://www.beesoft.org/bsc.html
Source:     	http://www.beesoft.org/download/bsc_%{version}_src.tar.gz
BuildRoot:  	%_tmppath/%name-buildroot
BuildRequires:	libqt-devel
Requires(post,postun): desktop-common-data

%description
Beesoft Commander is a file manager (like Norton Commander) for Linux. It is
based on Qt-GUI.

%prep
%setup -q -n bsc

%build
qmake -o Makefile bsc.pro
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
install -m 0755 bsc $RPM_BUILD_ROOT/%_bindir

mkdir -p $RPM_BUILD_ROOT/%_datadir/applications
cat > $RPM_BUILD_ROOT/%_datadir/applications/mandriva-%name.desktop << EOF
[Desktop Entry]
Name=Beesoft Commander
Comment=Beesoft Commander file manager
Exec=%_bindir/bsc
Icon=%name
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-FileTools;System;FileManager;
EOF

mkdir -p $RPM_BUILD_ROOT/%_datadir/pixmaps
install images/%name.png $RPM_BUILD_ROOT/%_datadir/pixmaps

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc *.txt
%attr(0755,root,root) %_bindir/bsc
%_datadir/applications/mandriva-bsc.desktop
%_datadir/pixmaps/%name.png
