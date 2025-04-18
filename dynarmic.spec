%global debug_package %{nil}
Name: dynarmic
Version: 1.2.2
Release: 0
Summary: C++ implementation of a fast hash map and hash set using robin hood hashing
URL: https://github.com/azahar-emu/mcl
License: MIT
BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: rpm_macro(cmake)
BuildRequires: rpm_macro(cmake_build)
BuildRequires: rpm_macro(cmake_install)
BuildRequires: cmake
BuildRequires: cmake(fmt)
BuildRequires: cmake(mcl)
BuildRequires: cmake(oaknut)
BuildRequires: cmake(tsl-robin-map)
%ifarch %{x86_64} x86_64
BuildRequires: cmake(xbyak)
%endif
%ifnarch s390x
BuildRequires: cmake(zydis)
%endif
BuildRequires: boost-devel

Source: https://github.com/huakim/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%package devel
Summary: %{summary}.

%description devel
%{summary}.

%description
%{summary}.


%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_libdir/lib%{name}.so.*

%files devel
%_includedir/%{name}
%_libdir/cmake/%{name}
%_libdir/lib%{name}.so
