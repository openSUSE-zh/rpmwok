Name:           electron-ssr
Version:        0.2.4
Release:        1
Summary:        Shadowsocksr client using Electron
License:        MIT
Group:          Productivity/Networking/Web/Proxy
Url:            https://github.com/erguotou520/%{name}
Source0:        https://github.com/erguotou520/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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

# TODO add icons and application file

%clean
rm -rf %buildroot/*

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}

%changelog
