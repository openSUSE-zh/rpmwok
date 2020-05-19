Name:           motrix
Version:        1.5.10
Release:        1
Summary:        A full-featured download manager
License:        MIT
Group:          Productivity/Networking/Other
Url:            https://github.com/agalwood/Motrix
Source0:        https://github.com/agalwood/Motrix/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
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
%setup -q -n Motrix-%{version}
npm install

%build
npm run build:dir

%install
mkdir -p %buildroot%{_libdir}/%{name}
cp -r release/linux-unpacked/* %buildroot%{_libdir}/%{name}

mkdir -p %buildroot%{_bindir}
ln -s %{_libdir}/%{name}/%{name} %buildroot%{_bindir}/%{name}

mkdir -p %buildroot%{_datadir}/icons/hicolor/256x256/apps
cp build/256x256.png %buildroot%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

mkdir -p %buildroot%{_datadir}/applications
cp %{S:1} %buildroot%{_datadir}/applications

%clean
rm -rf %buildroot/*

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
