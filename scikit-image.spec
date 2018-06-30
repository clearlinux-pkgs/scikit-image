#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scikit-image
Version  : 0.14.0
Release  : 32
URL      : http://pypi.debian.net/scikit-image/scikit-image-0.14.0.tar.gz
Source0  : http://pypi.debian.net/scikit-image/scikit-image-0.14.0.tar.gz
Summary  : Image processing routines for SciPy
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: scikit-image-bin
Requires: scikit-image-python3
Requires: scikit-image-python
Requires: Pillow
Requires: PyWavelets
Requires: cloudpickle
Requires: dask
Requires: matplotlib
Requires: networkx
Requires: scipy
BuildRequires : Cython
BuildRequires : Pillow
BuildRequires : PyWavelets
BuildRequires : dask
BuildRequires : networkx
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : scikit-learn
BuildRequires : setuptools

%description
Image processing algorithms for SciPy, including IO, morphology, filtering,
        warping, color manipulation, object detection, etc.
        
        Please refer to the online documentation at

%package bin
Summary: bin components for the scikit-image package.
Group: Binaries

%description bin
bin components for the scikit-image package.


%package python
Summary: python components for the scikit-image package.
Group: Default
Requires: scikit-image-python3

%description python
python components for the scikit-image package.


%package python3
Summary: python3 components for the scikit-image package.
Group: Default
Requires: python3-core

%description python3
python3 components for the scikit-image package.


%prep
%setup -q -n scikit-image-0.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527749303
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/skivi

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
