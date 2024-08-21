%global mingw_build_ucrt64 1
%{?mingw_package_header}

# Build the programs like cjpeg, etc.
# https://bugzilla.redhat.com/show_bug.cgi?id=467401#c7
%global build_programs 0

Name:           mingw-enet
Version:        1.3.18
Release:        1%{?dist}
Summary:        MinGW Windows enet library

License:        MIT
URL:            https://github.com/lsalzman/enet
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

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
Summary:        Free and portable font rendering engine

%description -n mingw32-enet
MinGW Windows enet library.

%package -n mingw32-enet-static
Summary:        Static version of the MinGW Windows enet library
Requires:       mingw32-enet = %{version}-%{release}

%description -n mingw32-enet-static
Static version of the MinGW Windows enet library.

# Win64
%package -n mingw64-enet
Summary:        Free and portable font rendering engine

%description -n mingw64-enet
MinGW Windows enet library.

%package -n mingw64-enet-static
Summary:        Static version of the MinGW Windows enet library
Requires:       mingw64-enet = %{version}-%{release}

%description -n mingw64-enet-static
Static version of the MinGW Windows enet library.

# UCRT64
%package -n ucrt64-enet
Summary:        Free and portable font rendering engine

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

# Remove win32 native binaries if wanted
%if %build_programs == 0
rm -f %{buildroot}%{mingw32_bindir}/*.exe
rm -f %{buildroot}%{mingw64_bindir}/*.exe
rm -f %{buildroot}%{ucrt64_bindir}/*.exe
%endif

# Win32
%files -n mingw32-enet
#%license LICENSE.md
#%doc README.* ChangeLog.md
%if %build_programs
#%{mingw32_bindir}/*.exe
%endif
#%{mingw32_bindir}/libjpeg-62.dll
#%{mingw32_includedir}/jconfig.h
#%{mingw32_includedir}/jerror.h
#%{mingw32_includedir}/jmorecfg.h
#%{mingw32_includedir}/jpeglib.h
#%{mingw32_includedir}/jpegint.h
#%{mingw32_libdir}/cmake/libjpeg-turbo/
#%{mingw32_libdir}/libjpeg.dll.a
#%{mingw32_libdir}/pkgconfig/libjpeg.pc

%files -n mingw32-enet-static
#%{mingw32_libdir}/libjpeg.a

# Win64
%files -n mingw64-enet
#%license LICENSE.md
#%doc README.* ChangeLog.md
%if %build_programs
#%{mingw64_bindir}/*.exe
%endif
#%{mingw64_bindir}/libjpeg-62.dll
#%{mingw64_includedir}/jconfig.h
#%{mingw64_includedir}/jerror.h
#%{mingw64_includedir}/jmorecfg.h
#%{mingw64_includedir}/jpeglib.h
#%{mingw64_includedir}/jpegint.h
#%{mingw64_libdir}/cmake/libjpeg-turbo/
#%{mingw64_libdir}/libjpeg.dll.a
#%{mingw64_libdir}/pkgconfig/libjpeg.pc

%files -n mingw64-enet-static
#%{mingw64_libdir}/libjpeg.a

# UCRT64
%files -n ucrt64-enet
#%license LICENSE.md
#%doc README.* ChangeLog.md
%if %build_programs
#%{ucrt64_bindir}/*.exe
%endif
#%{ucrt64_bindir}/libjpeg-62.dll
#%{ucrt64_includedir}/jconfig.h
#%{ucrt64_includedir}/jerror.h
#%{ucrt64_includedir}/jmorecfg.h
#%{ucrt64_includedir}/jpeglib.h
#%{ucrt64_includedir}/jpegint.h
#%{ucrt64_libdir}/cmake/libjpeg-turbo/
#%{ucrt64_libdir}/libjpeg.dll.a
#%{ucrt64_libdir}/pkgconfig/libjpeg.pc

%files -n ucrt64-enet-static
#%{ucrt64_libdir}/libjpeg.a

%changelog
* Tue Aug 20 2024 Jack Greiner <jack@emoss.org> - 1.3.18-1
- Add initial enet mingw spec
