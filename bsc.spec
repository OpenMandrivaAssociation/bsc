Name:       	bsc
Version:    	4.1.0
Release:    	%mkrel 2
Summary:    	Beesoft Commander file manager
License:    	GPLv2+
Group:      	File tools
URL:        	http://www.beesoft.org/index.php?id=bsc
Source:     	http://www.beesoft.org/download/%{name}_%{version}_src.tar.bz2
BuildRoot:  	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel
BuildRequires:	imagemagick

%description
Beesoft Commander is a file manager (like Norton Commander) for Linux. It is
based on Qt4-GUI.

%files
%defattr(-,root,root,-)
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png

# ----------------------------------------------------------

%prep
%setup -q -n bsc

%build
%qmake_qt4
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 0755 %{name} %{buildroot}%{_datadir}/%{name}
install -m 0644 help.en.html %{buildroot}%{_datadir}/%{name}
cp -R img %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -s  ../../%{_datadir}/%{name}/%{name} %{name}
popd 

# menu entry

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Beesoft Commander
Comment=Beesoft Commander file manager
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-FileTools;System;FileManager;Qt;
EOF

# icon

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48}/apps
convert -resize 16x16 BeesoftCommander.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
convert -resize 48x48 BeesoftCommander.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install BeesoftCommander.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%clean
rm -rf %{buildroot}

