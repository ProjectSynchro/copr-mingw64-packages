%global mingw_build_ucrt64 1
%{?mingw_package_header}

Name:           mingw-libvorbis
Version:        1.3.7
Release:        14%{?dist}
Summary:        MinGW Windows libvorbis library

License:        BSD
URL:            https://www.xiph.org/vorbis/
Source0:        https://downloads.xiph.org/releases/vorbis/libvorbis-%{version}.tar.xz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libogg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-libogg

BuildRequires:  ucrt64-filesystem >= 95
BuildRequires:  ucrt64-gcc
BuildRequires:  ucrt64-binutils
BuildRequires:  ucrt64-libogg

%description
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

This package contains the MinGW Windows cross compiled libvorbis library.


# Win32
%package -n mingw32-libvorbis
Summary:        MinGW Windows libvorbis library

%description -n mingw32-libvorbis
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

This package contains the MinGW Windows cross compiled libvorbis library.

%description -n mingw32-libvorbis-static
Static version of the MinGW Win32 compiled libvorbis library.

# Win64
%package -n mingw64-libvorbis
Summary:        MinGW Windows libvorbis library

%description -n mingw64-libvorbis
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

This package contains the MinGW Windows cross compiled libvorbis library.

%description -n mingw64-libvorbis-static
Static version of the MinGW Win64 compiled libvorbis library.

# UCRT64
%package -n ucrt64-libvorbis
Summary:        MinGW Windows libvorbis library

%description -n ucrt64-libvorbis
Ogg Vorbis is a fully open, non-proprietary, patent- and royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

This package contains the MinGW Windows cross compiled libvorbis library.

%description -n ucrt64-libvorbis-static
Static version of the MinGW UCRT64 compiled libvorbis library.

%{?mingw_debug_package}


%prep
%autosetup -n libvorbis-%{version} -p1


%build
%mingw_configure --enable-shared --enable-static
%mingw_make_build


%install
%mingw_make_install

rm -rf %{buildroot}%{mingw32_libdir}/*.la
rm -rf %{buildroot}%{mingw64_libdir}/*.la
rm -rf %{buildroot}%{ucrt64_libdir}/*.la
rm -rf %{buildroot}%{mingw32_datadir}/doc/
rm -rf %{buildroot}%{mingw64_datadir}/doc/
rm -rf %{buildroot}%{ucrt64_datadir}/doc/

# Win32
%files -n mingw32-libvorbis
%license COPYING
%{mingw32_bindir}/libvorbis-0.dll
%{mingw32_bindir}/libvorbisenc-2.dll
%{mingw32_bindir}/libvorbisfile-3.dll
%{mingw32_includedir}/vorbis/
%{mingw32_libdir}/libvorbis.dll.a
%{mingw32_libdir}/libvorbisenc.dll.a
%{mingw32_libdir}/libvorbisfile.dll.a
%{mingw32_libdir}/pkgconfig/vorbis.pc
%{mingw32_libdir}/pkgconfig/vorbisenc.pc
%{mingw32_libdir}/pkgconfig/vorbisfile.pc
%{mingw32_datadir}/aclocal/vorbis.m4

%files -n mingw32-libvorbis-static
%{mingw32_libdir}/libvorbis
%{mingw32_libdir}/libvorbisfile.a
%{mingw32_libdir}/libvorbisenc.a

# Win64
%files -n mingw64-libvorbis
%license COPYING
%{mingw64_bindir}/libvorbis-0.dll
%{mingw64_bindir}/libvorbisenc-2.dll
%{mingw64_bindir}/libvorbisfile-3.dll
%{mingw64_includedir}/vorbis/
%{mingw64_libdir}/libvorbis.dll.a
%{mingw64_libdir}/libvorbisenc.dll.a
%{mingw64_libdir}/libvorbisfile.dll.a
%{mingw64_libdir}/pkgconfig/vorbis.pc
%{mingw64_libdir}/pkgconfig/vorbisenc.pc
%{mingw64_libdir}/pkgconfig/vorbisfile.pc
%{mingw64_datadir}/aclocal/vorbis.m4

%files -n mingw64-libvorbis-static
%{mingw64_libdir}/libvorbis
%{mingw64_libdir}/libvorbisfile.a
%{mingw64_libdir}/libvorbisenc.a

# UCRT64
%files -n ucrt64-libvorbis
%license COPYING
%{ucrt64_bindir}/libvorbis-0.dll
%{ucrt64_bindir}/libvorbisenc-2.dll
%{ucrt64_bindir}/libvorbisfile-3.dll
%{ucrt64_includedir}/vorbis/
%{ucrt64_libdir}/libvorbis.dll.a
%{ucrt64_libdir}/libvorbisenc.dll.a
%{ucrt64_libdir}/libvorbisfile.dll.a
%{ucrt64_libdir}/pkgconfig/vorbis.pc
%{ucrt64_libdir}/pkgconfig/vorbisenc.pc
%{ucrt64_libdir}/pkgconfig/vorbisfile.pc
%{ucrt64_datadir}/aclocal/vorbis.m4

%files -n ucrt64-libvorbis-static
%{ucrt64_libdir}/libvorbis
%{ucrt64_libdir}/libvorbisfile.a
%{ucrt64_libdir}/libvorbisenc.a

%changelog
* Sun Jan 26 2025 Jack Greiner <jack@emoss.org> - 1.3.7-14
- Enabled static builds

* Mon Aug 19 2024 Jack Greiner <jack@emoss.org> - 1.3.7-13
- Add ucrt64 builds to spec.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.3.7-6
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 David King <amigadave@amigadave.com> - 1.3.7-1
- Update to 1.3.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Kalev Lember <klember@redhat.com> - 1.3.6-2
- Sync with git (CVE-2017-14160, CVE-2018-10392,
  CVE-2018-10393, #1516379)

* Wed Jan 09 2019 Kalev Lember <klember@redhat.com> - 1.3.6-1
- Update to 1.3.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 1.3.5-1
- Update to 1.3.5
- Use license macro for COPYING

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Kalev Lember <kalevlember@gmail.com> - 1.3.4-1
- Update to 1.3.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.3.3-1
- Update to 1.3.3

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Mar 18 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.2-5
- Added win64 support (contributed by Marc-André Lureau)
- Use mingw macros without leading underscore

* Tue Feb 28 2012 Kalev Lember <kalevlember@gmail.com> - 1.3.2-4
- Remove the .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.3.2-3
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 17 2011 Kalev Lember <kalevlember@gmail.com> - 1.3.2-1
- Initial RPM release
