Name:           riot-web
Version:        1.0.6
Release:        1
Summary:        A glossy Matrix collaboration client for the web
License:        MIT
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/vector-im/%{name}
Source0:        https://github.com/vector-im/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  nodejs
BuildRequires:  npm
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Atom is a hackable text editor for the 21st century, built on Electron, and
based on everything we love about our favorite editors. We designed it to be
deeply customizable, but still approachable using the default configuration.

Visit vector-im.io to learn more or visit the Atom forum.

Follow @AtomEditor on Twitter for important announcements.

This project adheres to the Contributor Covenant code of conduct. By
participating, you are expected to uphold this code. Please report unacceptable
behavior to vector-im@github.com.

%prep
%setup -q
cp config.sample.json config.json

%build
sed -i 's/-wml --ia32/-l/g' package.json
npm install
npm run build:electron

%install
mkdir -p %buildroot%{_libdir}/%{name}
cp -r electron_app/dist/linux-unpacked/* %buildroot%{_libdir}/%{name}

mkdir -p %buildroot%{_bindir}
ln -s %{_libdir}/%{name}/%{name} %buildroot%{_bindir}/%{name}

mkdir -p %buildroot%{_datadir}/icons/hicolor/16x16/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/24x24/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/64x64/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/96x96/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/128x128/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/256x256/apps
mkdir -p %buildroot%{_datadir}/icons/hicolor/512x512/apps
cp electron_app/build/icons/16x16.png %buildroot%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
cp electron_app/build/icons/24x24.png %buildroot%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
cp electron_app/build/icons/48x48.png %buildroot%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
cp electron_app/build/icons/64x64.png %buildroot%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
cp electron_app/build/icons/96x96.png %buildroot%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
cp electron_app/build/icons/128x128.png %buildroot%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
cp electron_app/build/icons/256x256.png %buildroot%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
cp electron_app/build/icons/512x512.png %buildroot%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

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
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
