#
# spec file for package Ryujinx
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           Ryujinx
Version:        0~git20200516
Release:        0
Summary:        A simple, experimental Nintendo Switch emulator
License:        MIT
URL:            https://github.com/Ryujinx/Ryujinx
Source:         https://github.com/Ryujinx/Ryujinx/archive/master.tar.gz#/Ryujinx-master.tar.gz

BuildRequires:  dotnet-sdk-3.1
Requires:       mono

%description
It is an open source Nintendo Switch Emulator written in C# created by gdkchan.
This emulator aims at providing good performance and accuracy, a friendly
interface, and consistent builds.

%prep
%setup -q -n Ryujinx-master

%build
dotnet publish -c Release -r linux-x64

%install

%files

%changelog

