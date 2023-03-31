Name:           unar
Version:        1.10.7
Release:        5
Summary:        Multi format application for uncompressing archive files
License:        LGPLv2+
Group:          Archiving/Compression
URL:            https://theunarchiver.com/command-line
Source0:        https://github.com/MacPaw/XADMaster/archive/v%{version}/XADMaster-%{version}.tar.gz
Source2:	https://github.com/MacPaw/universal-detector/archive/1.1/universal-detector-1.1.tar.gz

BuildRequires:  gnustep-make
BuildRequires:	pkgconfig(libobjc)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  gnustep-base-devel
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(wavpack)

%description
The command-line utilities lsar and unar are capable of listing and extracting
files respectively in several formats including RARv3 and RARv5. 
unar can serve as a free and open source replacement of unrar.
It was originally a Mac OS X application. This package
contains a command-line variant of it. Unarchiver handles ZIP, ZIPX,
RAR, 7z, tar, gzip, bzip2, lzma, xz, CAB, MSI, NSIS, some
self-extracting EXEs, cpio, and further obscure and old formats, as
well as disc images in ISO, BIN, MDF, NRG, CDI. It supports filenames
in foreign character sets.

%prep
%autosetup -c
tar -xf %{SOURCE2} 
# compilation depends on the exact case sensitive name of the SOURCE2 folder
ln -s universal-detector-1.1 UniversalDetector
rm -fr __MACOSX The\ Unarchiver
# recursively remove executable bit from every file, skipping directories
find . -type f -print0 | xargs -0 chmod -x

%build
export OBJCFLAGS=`gnustep-config --objc-flags`
make -C XADMaster-%{version} -f Makefile.linux CC=clang OBJCC=clang CXX=clang++

%install
install -d %{buildroot}%{_bindir}
install -pm755 XADMaster-%{version}/unar XADMaster-%{version}/lsar %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -pm644 XADMaster-%{version}/Extra/*.1 %{buildroot}%{_mandir}/man1

install -d %{buildroot}%{_datadir}/bash-completion/completions
install -pm644 XADMaster-%{version}/Extra/lsar.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/lsar
install -pm644 XADMaster-%{version}/Extra/unar.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/unar

%files
%{_bindir}/lsar
%{_bindir}/unar
%{_mandir}/man1/*.1*
%{_datadir}/bash-completion/completions/lsar
%{_datadir}/bash-completion/completions/unar
%license XADMaster-%{version}/LICENSE
