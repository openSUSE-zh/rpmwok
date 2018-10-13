Name:           electronic-wechat
Version:        2.0
Release:        2
Summary:        A better WeChat on macOS and Linux. Built with Electron.
License:        MIT
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/geeeeeeeeek/%{name}
Source0:        https://github.com/geeeeeeeeek/%{name}/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  nodejs
BuildRequires:  npm
Requires:       nodejs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

* Modern UI and all features from Web WeChat.
* Block message recall.
* Stickers showing support.
* Share subscribed passages on Weibo, Qzone, Facebook, Twitter, Evernote, and email.
* Mention users in a group chat.
* Drag and drop to send photos.
* Behaves like a native app, based on dozens of optimization.
* Removes URL link redirects and takes you directly to blocked websites (e.g. taobao.com).

%prep
%setup -q
npm install

%build
npm run build:linux

%install
mkdir -p %buildroot%{_libdir}/%{name}
cp -r dist/%{name}-linux-x64/* %buildroot%{_libdir}/%{name}

mkdir -p %buildroot%{_bindir}
ln -s %{_libdir}/%{name}/%{name} %buildroot%{_bindir}/%{name}

mkdir -p %buildroot%{_datadir}/icons/hicolor/512x512/apps
cp assets/icon.png %buildroot%{_datadir}/icons/hicolor/512x512/apps/%{name}.png

mkdir -p %buildroot%{_datadir}/applications
cp %{SOURCE1} %buildroot%{_datadir}/applications

%clean
rm -rf %buildroot/*

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
