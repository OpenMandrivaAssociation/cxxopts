Name: cxxopts
Version: 3.2.1
Release: 1
Source0: https://github.com/jarro2783/cxxopts/archive/refs/tags/v%{version}.tar.gz
Summary: Lightweight C++ option parser library
URL: https://github.com/jarro2783/cxxopts
License: MIT
Group: System/Libraries
BuildArch: noarch
BuildSystem: cmake

%description
Lightweight C++ option parser library

%files
%{_includedir}/cxxopts.hpp
%{_libdir}/cmake/cxxopts
%{_libdir}/pkgconfig/cxxopts.pc
