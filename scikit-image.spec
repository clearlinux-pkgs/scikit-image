#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scikit-image
Version  : 0.12.3
Release  : 4
URL      : http://pypi.debian.net/scikit-image/scikit-image-0.12.3.tar.gz
Source0  : http://pypi.debian.net/scikit-image/scikit-image-0.12.3.tar.gz
Summary  : Image processing routines for SciPy
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: scikit-image-bin
Requires: scikit-image-python
BuildRequires : cython-python
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : scikit-learn
BuildRequires : setuptools

%description
No detailed description available

%package bin
Summary: bin components for the scikit-image package.
Group: Binaries

%description bin
bin components for the scikit-image package.


%package python
Summary: python components for the scikit-image package.
Group: Default

%description python
python components for the scikit-image package.


%prep
%setup -q -n scikit-image-0.12.3

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -fno-semantic-interposition -O3 -falign-functions=32 "
export FCFLAGS="$CFLAGS -fno-semantic-interposition -O3 -falign-functions=32 "
export FFLAGS="$CFLAGS -fno-semantic-interposition -O3 -falign-functions=32 "
export CXXFLAGS="$CXXFLAGS -fno-semantic-interposition -O3 -falign-functions=32 "
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/skivi

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
