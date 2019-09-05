Name:           electron-ssr
Version:        0.2.6
Release:        1
Summary:        Shadowsocksr client using Electron
License:        MIT
Group:          Productivity/Networking/Web/Proxy
Url:            https://github.com/erguotou520/electron-ssr
Source0:        https://github.com/erguotou520/electron-ssr/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  nodejs
BuildRequires:  npm
Requires:       nodejs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
这是一个跨平台（支持Windows MacOS Linux系统）的 ShadowsocksR 客户端桌面应用，它功能丰富，
支持 Windows 版大部分功能，更有更多人性化功能。它是开源的，它来源于开源，回馈以开源。

%prep
%setup -q
npm install

%build
npm run build

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
