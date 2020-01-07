# Electron RPMbuild - RPM repository for openSUSE & SLE

## Packages

Ordered by names

- electron-ssr
- electronic-wechat

## System requirements

- openSUSE Tumbleweed or Leap 15+ (SLE, Fedora, CentOS should also be okay)
- git
- nodejs 8+
- npm
- rpm
- rpm-build
- createrepo
- wget

```
sudo zypper in git nodejs npm rpm rpm-build createrepo wget
sudo npm install -g yarn
```

## How to add and build a new package

Let's say you have a application Foobar and its package name is `foobar`, version
is 1.2.3, release is 1.

1. Create a new directory `foobar` under `spec`.
2. Create a new file `foobar.spec` under `spec/foobar`.
3. Write SPEC file content. You can copy from other packages and modify as needed.
4. Go back to project root directory. Run `./rpmbuild_spec foobar`.

If build succeeded, you should see new RPM file `foobar-1.2.3-1.x86_64.rpm` in
`repo` directory.

If build failed, you can check the console output and build directory
`~/rpmbuild/BUILD/foobar-1.2.3` to correct your spec file. If you have any
problem, [submit a new issue](https://gitlab.com/guoyunhe/electron-rpmbuild/issues/new).
We are happy to help you!

[List of Electron related projects on GitHub](https://github.com/topics/electron).

## How to create GPG key

You need a GPG key to sign packages. Unsigned packages are not trusted by most
system.

1. Create GPG key pair for signing packages `gpg --gen-key`. Default value should
   be enough. If you choose a password, then you have to manually publish
   repository every time. If you want to run an automatically script, don't use
   password.
2. You need to remember the key name, which looks like `3AA5C34371567BD2`.
3. Export public key `gpg -a -o RPM-GPG-KEY-ELECTRON --export 3AA5C34371567BD2`.
4. Move the public key file `RPM-GPG-KEY-ELECTRON` to `repo` directory.
5. Run `vi ~/.rpmmacros` and add `%_gpg_name 3AA5C34371567BD2`. This tell rpm
   which key to use for signing packages.

Usually a GPG key expires in two years. Remember to create a new key before the
old expires. Otherwise, users will get errors when fetching your repository.

## How to publish a repository

1. Clone this repository on your server.
2. Run `auto_repo`. It will build, sign and publish all packages.
3. Copy `repo/electron-rpmbuild.repo.example` to `repo/electron-rpmbuild.repo`
   and modify URL
4. Set up your web server. Point document root to `repo` directory.

You can create a Cron job to fetch new packages and rebuild repository every night.
If version and release in spec file didn't change, package build will be skipped.
So you only build updated packages and save a lot of time.

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
