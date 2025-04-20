%global mingw_build_ucrt64 1
%{?mingw_package_header}

Name:           mingw-luajit
Version:        2.1-20250117
Release:        1%{?dist}
Summary:        Just-in-time compiler and drop-in replacement for Lua 5.1 (MinGW Windows)
License:        spdx:MIT
URL:            http://luajit.org/
Source0:        https://github.com/openresty/luajit2/archive/refs/tags/v%{version}.tar.gz

Patch1:         001-mintty-cygpty-isatty.patch
Patch2:         002-fix-pkg-config-file.patch
Patch3:         003-lua51-modules-paths.patch
Patch4:         004-fix-default-cc.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 113
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 113
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

BuildRequires:  ucrt64-filesystem >= 113
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-gcc-c++
BuildRequires:  ucrt64-binutils

BuildRequires: make
BuildRequires: automake autoconf libtool sed


%description
LuaJIT just-in-time compiler and drop-in replacement for Lua 5.1.

# Win32
%package -n mingw32-luajit
Summary:        Dynamic build of the MinGW Windows LuaJIT library

%description -n mingw32-luajit
MinGW Windows LuaJIT dynamic library and executables.

%package -n mingw32-luajit-static
Summary:        Static build of the MinGW Windows LuaJIT library
Requires:       mingw32-luajit = %{version}-%{release}

%description -n mingw32-luajit-static
Static build of the MinGW Windows LuaJIT library.

# Win64
%package -n mingw64-luajit
Summary:        Dynamic build of the MinGW Windows LuaJIT library

%description -n mingw64-luajit
MinGW Windows LuaJIT dynamic library and executables.

%package -n mingw64-luajit-static
Summary:        Static build of the MinGW Windows LuaJIT library
Requires:       mingw64-luajit = %{version}-%{release}

%description -n mingw64-luajit-static
Static build of the MinGW Windows LuaJIT library.

# UCRT64
%package -n ucrt64-luajit
Summary:        Dynamic build of the UCRT64 LuaJIT library

%description -n ucrt64-luajit
UCRT64 build of LuaJIT dynamic library and executables.

%package -n ucrt64-luajit-static
Summary:        Static build of the UCRT64 LuaJIT library
Requires:       ucrt64-luajit = %{version}-%{release}

%description -n ucrt64-luajit-static
Static build of the UCRT64 LuaJIT library.

%prep
%autosetup -n luajit-%{version} -p1
# Remove unwanted files and apply patches
rm -f src/iscygpty.{c,h} || true
%autopatch -m 1

%build

XCFLAGS="-DLUAJIT_ENABLE_GC64"
if [ "$CARCH" = "i686" ]; then
    XCFLAGS="$XCFLAGS -DLUAJIT_NO_UNWIND"
fi
%{mingw_make} amalg BUILDMODE=static XCFLAGS="$XCFLAGS"
%{mingw_make} XCFLAGS="$XCFLAGS"

%install
%{mingw_make_install}

# Drop all libtool (.la) files if present:
find %{buildroot} -name "*.la" -delete

# Remove manual pages and docs which duplicate Fedora native.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{ucrt64_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{ucrt64_docdir}

# Win32 files
%files -n mingw32-luajit
%license COPYRIGHT
%{mingw32_bindir}/lua51.dll
%{mingw32_bindir}/luajit.exe
%{mingw32_libdir}/lib/libluajit-5.1.dll.a
%{mingw32_libdir}/pkgconfig/{lua51,luajit}.pc

%files -n mingw32-luajit-static
%{mingw32_libdir}/lib/libluajit.a

# Win64 files
%files -n mingw64-luajit
%license COPYRIGHT
%{mingw64_bindir}/lua51.dll
%{mingw64_bindir}/luajit.exe
%{mingw64_libdir}/lib/libluajit-5.1.dll.a
%{mingw64_libdir}/pkgconfig/{lua51,luajit}.pc

%files -n mingw64-luajit-static
%{mingw64_libdir}/lib/libluajit.a

# UCRT64 files
%files -n ucrt64-luajit
%license COPYRIGHT
%{ucrt64_bindir}/lua51.dll
%{ucrt64_bindir}/luajit.exe
%{ucrt64_libdir}/lib/libluajit-5.1.dll.a
%{ucrt64_libdir}/pkgconfig/{lua51,luajit}.pc

%files -n ucrt64-luajit-static
%{ucrt64_libdir}/lib/libluajit.a

%changelog
* Sun Apr 20 2025 Jack Greiner <jack@emoss.org> - 2.1-20250117-1
- Add initial luajit mingw spec
