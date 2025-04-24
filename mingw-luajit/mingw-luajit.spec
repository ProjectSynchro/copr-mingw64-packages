%global mingw_build_ucrt64 1
# Can't seem to get 32-bit cross-builds working.
%global mingw_build_win32 0

%global snapshot 20250117

%{?mingw_package_header}

Name:           mingw-luajit
Version:        2.1
Release:        2.%{snapshot}%{?dist}
Summary:        Just-in-time compiler and drop-in replacement for Lua 5.1 (MinGW Windows)
License:        spdx:MIT
URL:            http://luajit.org/
Source0:        https://github.com/openresty/luajit2/archive/refs/tags/v%{version}-%{snapshot}.tar.gz
Patch1:         001-fix-windows-install-suffix.patch

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

BuildRequires: make git gcc gcc-c++ sed

%description
LuaJIT just-in-time compiler and drop-in replacement for Lua 5.1.

# Win32
%package -n mingw32-luajit
Summary:        Dynamic build of the MinGW Windows LuaJIT library

%description -n mingw32-luajit
MinGW Windows LuaJIT dynamic library and executables.

# Win64
%package -n mingw64-luajit
Summary:        Dynamic build of the MinGW Windows LuaJIT library

%description -n mingw64-luajit
MinGW Windows LuaJIT dynamic library and executables.

# UCRT64
%package -n ucrt64-luajit
Summary:        Dynamic build of the UCRT64 LuaJIT library

%description -n ucrt64-luajit
UCRT64 build of LuaJIT dynamic library and executables.

%prep
%autosetup -p1 -n luajit2-%{version}-%{snapshot}

mkdir /tmp/luajit2-%{version}-%{snapshot}-build_win
cp -rT %{_builddir}/luajit2-%{version}-%{snapshot} /tmp/luajit2-%{version}-%{snapshot}-build_win
pushd %{_builddir}/luajit2-%{version}-%{snapshot}
    %if 0%{?mingw_build_win32}
    mkdir -p build_win32
    %endif
    %if 0%{?mingw_build_win64}
    mkdir -p build_win64
    %endif
    %if 0%{?mingw_build_ucrt64}
    mkdir -p build_ucrt64
    %endif
popd

%if 0%{?mingw_build_win32}
cp -rT /tmp/luajit2-%{version}-%{snapshot}-build_win %{_builddir}/luajit2-%{version}-%{snapshot}/build_win32
%endif
%if 0%{?mingw_build_win64}
cp -rT /tmp/luajit2-%{version}-%{snapshot}-build_win %{_builddir}/luajit2-%{version}-%{snapshot}/build_win64
%endif
%if 0%{?mingw_build_ucrt64}
cp -rT /tmp/luajit2-%{version}-%{snapshot}-build_win %{_builddir}/luajit2-%{version}-%{snapshot}/build_ucrt64
%endif

rm -rf /tmp/luajit2-%{version}-%{snapshot}-build_win

%build

# We need to set the CFLAGS and LDFLAGS to empty strings so that
# the build system doesn't try to use the host compiler when cross compiling.

export HOST_CFLAGS="$CFLAGS"
export CFLAGS=""
export HOST_LDFLAGS="$LDFLAGS"
export LDFLAGS=""

# Set the target system to Windows
export TARGET_SYS=Windows

%if 0%{?mingw_build_win64}
export CROSS="%{mingw64_target}-"

export TARGET_CFLAGS="%{mingw64_cflags}"
export TARGET_LDFLAGS="%{mingw64_ldflags}"
export TARGET_LD="%{mingw64_cc}"

make -C build_win64 amalg BUILDMODE=static
make -C build_win64
%endif

%if 0%{?mingw_build_ucrt64}
export CROSS="%{ucrt64_target}-"

export TARGET_CFLAGS="%{ucrt64_cflags}"
export TARGET_LDFLAGS="%{ucrt64_ldflags}"
export TARGET_LD="%{ucrt64_cc}"

make -C build_ucrt64 amalg BUILDMODE=static
make -C build_ucrt64
%endif

%if 0%{?mingw_build_win32}

export HOST_CC="gcc -m32"
export CROSS="%{mingw32_target}-"

export TARGET_CFLAGS="%{mingw32_cflags}"
export TARGET_LDFLAGS="%{mingw32_ldflags}"
export TARGET_LD="%{mingw32_cc}"

CC="" make -C build_win32 amalg BUILDMODE=static
CC="" make -C build_win32
%endif

%install

# We need to set the CFLAGS and LDFLAGS to empty strings so that
# the build system doesn't try to use the host compiler when cross compiling.

export HOST_CFLAGS="$CFLAGS"
export CFLAGS=""
export HOST_LDFLAGS="$LDFLAGS"
export LDFLAGS=""

%if 0%{?mingw_build_win64}
export CROSS="%{mingw64_target}-"

export TARGET_SYS=Windows 
export TARGET_CFLAGS="%{mingw64_cflags}"
export TARGET_LDFLAGS="%{mingw64_ldflags}"
export TARGET_LD="%{mingw64_cc}"

make INSTALL="/usr/bin/install -p" DESTDIR=$RPM_BUILD_ROOT PREFIX="%{mingw64_prefix}" -C build_ucrt64 install

%endif

%if 0%{?mingw_build_ucrt64}
export CROSS="%{ucrt64_target}-"

export TARGET_SYS=Windows 
export TARGET_CFLAGS="%{ucrt64_cflags}"
export TARGET_LDFLAGS="%{ucrt64_ldflags}"
export TARGET_LD="%{ucrt64_cc}"

make INSTALL="/usr/bin/install -p" DESTDIR=$RPM_BUILD_ROOT PREFIX="%{ucrt64_prefix}" -C build_ucrt64 install

%endif

%if 0%{?mingw_build_win32}
export HOST_CC="gcc -m32"
export CROSS="%{mingw32_target}-"

export TARGET_SYS=Windows 
export TARGET_CFLAGS="%{mingw32_cflags}"
export TARGET_LDFLAGS="%{mingw32_ldflags}"
export TARGET_LD="%{mingw32_cc}"

make INSTALL="/usr/bin/install -p" DESTDIR=$RPM_BUILD_ROOT PREFIX="%{mingw32_prefix}" -C build_win32 install

%endif

# Drop all libtool (.la) files if present:
find %{buildroot} -name "*.la" -delete

# Remove manual pages and docs which duplicate Fedora native.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{ucrt64_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{ucrt64_docdir}

%if 0%{?mingw_build_win32}
# Win32 files
%files -n mingw32-luajit
%license COPYRIGHT
%{mingw32_bindir}/lua51.dll
%{mingw32_libdir}/libluajit-5.1.dll.a
%{mingw32_bindir}/luajit*.exe
%{mingw32_includedir}/luajit-2.1/*.h
%{mingw32_includedir}/luajit-2.1/*.hpp
%{mingw32_datadir}/luajit-2.1/jit/*.lua
%{mingw32_libdir}/pkgconfig/{lua51,luajit}.pc
%endif

%if 0%{?mingw_build_win64}
# Win64 files
%files -n mingw64-luajit
%license COPYRIGHT
%{mingw64_bindir}/lua51.dll
%{mingw64_libdir}/libluajit-5.1.dll.a
%{mingw64_bindir}/luajit*.exe
%{mingw64_includedir}/luajit-2.1/*.h
%{mingw64_includedir}/luajit-2.1/*.hpp
%{mingw64_datadir}/luajit-2.1/jit/*.lua
%{mingw64_libdir}/pkgconfig/{lua51,luajit}.pc
%endif

%if 0%{?mingw_build_ucrt64}
# UCRT64 files
%files -n ucrt64-luajit
%license COPYRIGHT
%{ucrt64_bindir}/lua51.dll
%{ucrt64_libdir}/libluajit-5.1.dll.a
%{ucrt64_bindir}/luajit*.exe
%{ucrt64_includedir}/luajit-2.1/*.h
%{ucrt64_includedir}/luajit-2.1/*.hpp
%{ucrt64_datadir}/luajit-2.1/jit/*.lua
%{ucrt64_libdir}/pkgconfig/{lua51,luajit}.pc
%endif

%changelog
* Thu Apr 24 2025 Jack Greiner <jack@emoss.org> - 2.1-20250117-2
- Fix missing libluajit-5.1.dll.a in build
* Sun Apr 20 2025 Jack Greiner <jack@emoss.org> - 2.1-20250117-1
- Add initial luajit mingw spec
