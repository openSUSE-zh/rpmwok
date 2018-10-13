Name:           webtorrent-desktop
Version:        0.20.0
Release:        1
Summary:        The streaming torrent app. For Mac, Windows, and Linux.
License:        MIT
Group:          Productivity/Networking/Other
Url:            https://github.com/webtorrent/%{name}
Source0:        https://github.com/webtorrent/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  zip
Requires:       nodejs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

Whether it's video from the Internet Archive, music from Creative Commons, or 
audiobooks from Librivox, you can play it right away. You don't have to wait for
it to finish downloading.

%prep
%setup -q
npm install

%build
npm run build
npm run package linux zip

%install
mkdir -p %buildroot%{_libdir}/%{name}
cp -r dist/WebTorrent-linux-x64/* %buildroot%{_libdir}/%{name}

mkdir -p %buildroot%{_bindir}
ln -s %{_libdir}/%{name}/WebTorrent %buildroot%{_bindir}/WebTorrent

sed -i s~/opt/%{name}~%{_libdir}/%{name}~g static/linux/share/applications/%{name}.desktop
mkdir -p %buildroot%{_datadir}
cp -r static/linux/share/* %buildroot%{_datadir}

%clean
rm -rf %buildroot/*

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/WebTorrent
%{_libdir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
