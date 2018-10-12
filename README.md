# Electron RPMbuild - RPM repository for openSUSE & SLE

## Packages

Ordered by names

- electron-ssr
- electronic-wechat

## FAQ

### Why Electron applications cannot be packaged in openSUSE Build Service

NodeJS programs consist of scripts, which doesn't need a compiler and build
process. But...

Most Electron applications use `electron-builder` to compile application inside
a binary. It downloads precompiled Electron binary files from a Electron server.
This is NOT allowed by openSUSE Build Service.

So... we do not have any Electron applications in official repository.

### What we do here

We write specs of those Electron applications. We also have some scripts to build
packages while allow internet access in the process.

### Can you trust these packages

You decide.

All scripts we use are here. You can know how we exactly build these packages.
You can build all packages by yourselves with these scripts, and even have your
own repository. If you don't trust us, build your own!

Electron binary is built by GitHub. If you don't trust it, this solution is not
for you.

Even with the same scripts and specs, the build result can be different. That is
because Node package dependencies are usually not locked. These dependencies are
huge and deep. Nobody, neither us nor the authors of applications, know what is
going on in all depended packages. This is the biggest risk of all Electron
applications.
