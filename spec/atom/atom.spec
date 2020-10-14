Name:           atom
Version:        1.52.0
Release:        1
Summary:        The hackable text editor
License:        MIT
Group:          Productivity/Text/Editors
Url:            https://github.com/atom/atom
Source0:        https://github.com/atom/atom/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
BuildRequires:  gconf2-devel
BuildRequires:  libXss-devel
BuildRequires:  pkgconfig(nss)
Requires:       nodejs
Requires:       gconf2
Requires:       libXss1
Requires:       libsecret
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
cp -r out/%{name}-%{version}-amd64/* %buildroot%{_libdir}/%{name}

mkdir -p %buildroot%{_bindir}
# /usr/bin/atom
ln -s %{_libdir}/%{name}/%{name} %buildroot%{_bindir}/%{name}
# /usr/bin/apm
ln -s %{_libdir}/%{name}/resources/app/apm/node_modules/.bin/apm %buildroot%{_bindir}/apm

mkdir -p %buildroot%{_datadir}/icons/hicolor/16x16/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/24x24/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/32x32/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/64x64/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/128x128/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/256x256/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/512x512/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/1024x1024/apps
cp resources/app-icons/stable/png/16.png %buildroot%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
cp resources/app-icons/stable/png/24.png %buildroot%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
cp resources/app-icons/stable/png/32.png %buildroot%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
cp resources/app-icons/stable/png/48.png %buildroot%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
cp resources/app-icons/stable/png/64.png %buildroot%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
cp resources/app-icons/stable/png/128.png %buildroot%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
cp resources/app-icons/stable/png/256.png %buildroot%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
cp resources/app-icons/stable/png/512.png %buildroot%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
cp resources/app-icons/stable/png/1024.png %buildroot%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png

mkdir -p %buildroot%{_datadir}/applications
cp %{SOURCE1} %buildroot%{_datadir}/applications

%clean
rm -rf %buildroot/*

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_bindir}/apm
%{_libdir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
