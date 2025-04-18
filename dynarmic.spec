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
BuildRequires: fmt-devel
BuildRequires: mcl-devel
BuildRequires: oaknut-devel
BuildRequires: robin-map-devel
%ifarch %{x86_64} x86_64
BuildRequires: xbyak-devel
%endif
BuildRequires: zydis-devel
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

#%files
#%_libdir/lib%{name}.so.0

%files devel
%_includedir/%{name}
%_libdir/cmake/%{name}
#%_libdir/lib%{name}.so
