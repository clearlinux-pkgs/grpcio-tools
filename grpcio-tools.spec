#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grpcio-tools
Version  : 1.41.1
Release  : 10
URL      : https://files.pythonhosted.org/packages/3c/9b/cf7092cbcf60930f36a204301640be0b95470d358cd53b57c84578cbb16c/grpcio-tools-1.41.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3c/9b/cf7092cbcf60930f36a204301640be0b95470d358cd53b57c84578cbb16c/grpcio-tools-1.41.1.tar.gz
Summary  : Protobuf code generator for gRPC
Group    : Development/Tools
License  : Apache-2.0
Requires: grpcio-tools-python = %{version}-%{release}
Requires: grpcio-tools-python3 = %{version}-%{release}
Requires: grpcio
Requires: protobuf
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : grpcio
BuildRequires : protobuf
BuildRequires : setuptools

%description
=================
        
        Package for gRPC Python tools.
        
        Supported Python Versions
        -------------------------
        Python >= 3.6
        
        Installation
        ------------
        
        The gRPC Python tools package is available for Linux, Mac OS X, and Windows.
        
        Installing From PyPI
        ~~~~~~~~~~~~~~~~~~~~
        
        If you are installing locally...

%package python
Summary: python components for the grpcio-tools package.
Group: Default
Requires: grpcio-tools-python3 = %{version}-%{release}

%description python
python components for the grpcio-tools package.


%package python3
Summary: python3 components for the grpcio-tools package.
Group: Default
Requires: python3-core
Provides: pypi(grpcio_tools)
Requires: pypi(grpcio)
Requires: pypi(protobuf)
Requires: pypi(setuptools)

%description python3
python3 components for the grpcio-tools package.


%prep
%setup -q -n grpcio-tools-1.41.1
cd %{_builddir}/grpcio-tools-1.41.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635205664
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
