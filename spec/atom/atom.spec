Name:           atom
Version:        1.31.2
Release:        1
Summary:        The hackable text editor
License:        MIT
Group:          Productivity/Text/Editors
Url:            https://github.com/atom/%{name}
Source0:        https://github.com/atom/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  nodejs
BuildRequires:  nodejs-devel
BuildRequires:  npm
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  git-core
BuildRequires:  libsecret-devel
BuildRequires:  rpmdevtools
BuildRequires:  libX11-devel
BuildRequires:  libxkbfile-devel
Requires:       nodejs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Atom is a hackable text editor for the 21st century, built on Electron, and
based on everything we love about our favorite editors. We designed it to be
deeply customizable, but still approachable using the default configuration.

Visit atom.io to learn more or visit the Atom forum.

Follow @AtomEditor on Twitter for important announcements.

This project adheres to the Contributor Covenant code of conduct. By
participating, you are expected to uphold this code. Please report unacceptable
behavior to atom@github.com.

%prep
%setup -q
script/bootstrap

%build
script/build

%install
mkdir -p %buildroot%{_libdir}/%{name}
cp -r build/linux-unpacked/* %buildroot%{_libdir}/%{name}

mkdir -p %buildroot%{_bindir}
ln -s %{_libdir}/%{name}/%{name} %buildroot%{_bindir}/%{name}

mkdir -p %buildroot%{_datadir}/icons/hicolor/16x16/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/24x24/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/64x64/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/96x96/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/128x128/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/256x256/apps
cp build/icons/16x16.png %buildroot%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
cp build/icons/24x24.png %buildroot%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
cp build/icons/32x32.png %buildroot%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
cp build/icons/48x48.png %buildroot%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
cp build/icons/64x64.png %buildroot%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
cp build/icons/96x96.png %buildroot%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
cp build/icons/128x128.png %buildroot%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
cp build/icons/256x256.png %buildroot%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

mkdir -p %buildroot%{_datadir}/applications
cp %{SOURCE1} %buildroot%{_datadir}/applications

%clean
rm -rf %buildroot/*

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
