%global mingw_build_ucrt64 1
%{?mingw_package_header}

Name:           mingw-enet
Version:        1.3.18
Release:        1%{?dist}
Summary:        MinGW Windows enet library

License:        MIT
URL:            https://github.com/lsalzman/enet
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

# Fix DLL builds
Patch1:         001-no-undefined.patch
# Fix linker flags.
Patch2:         002-win-libs.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

BuildRequires:  ucrt64-filesystem >= 95
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-gcc-c++
BuildRequires:  ucrt64-binutils

BuildRequires: make
BuildRequires: automake autoconf libtool


%description
MinGW Windows enet library.

# Win32
%package -n mingw32-enet
Summary:        Thin, simple and robust network layer on top of UDP

%description -n mingw32-enet
MinGW Windows enet library.

%package -n mingw32-enet-static
Summary:        Static version of the MinGW Windows enet library
Requires:       mingw32-enet = %{version}-%{release}

%description -n mingw32-enet-static
Static version of the MinGW Windows enet library.

# Win64
%package -n mingw64-enet
Summary:        Thin, simple and robust network layer on top of UDP

%description -n mingw64-enet
MinGW Windows enet library.

%package -n mingw64-enet-static
Summary:        Static version of the MinGW Windows enet library
Requires:       mingw64-enet = %{version}-%{release}

%description -n mingw64-enet-static
Static version of the MinGW Windows enet library.

# UCRT64
%package -n ucrt64-enet
Summary:        Thin, simple and robust network layer on top of UDP

%description -n ucrt64-enet
MinGW Windows enet library.

%package -n ucrt64-enet-static
Summary:        Static version of the MinGW Windows enet library
Requires:       ucrt64-enet = %{version}-%{release}

%description -n ucrt64-enet-static
Static version of the MinGW Windows enet library.


%{?mingw_debug_package}


%prep
%autosetup -n enet-%{version} -p1

# We are using a Github snapshot so we have to run autoreconf ourselves.
autoreconf -vif

%build
%mingw_configure \
           --enable-static \
           --enable-shared

%mingw_make_build

%install
%mingw_make_install

# Drop all .la files
find %{buildroot} -name "*.la" -delete

# Remove manual pages and docs which duplicate Fedora native.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{ucrt64_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{ucrt64_docdir}

# Win32
%files -n mingw32-enet

%files -n mingw32-enet-static

# Win64
%files -n mingw64-enet

%files -n mingw64-enet-static

# UCRT64
%files -n ucrt64-enet

%files -n ucrt64-enet-static

%changelog
* Tue Aug 20 2024 Jack Greiner <jack@emoss.org> - 1.3.18-1
- Add initial enet mingw spec
