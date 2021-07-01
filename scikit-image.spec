#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : scikit-image
Version  : 0.18.2
Release  : 60
URL      : https://files.pythonhosted.org/packages/e1/e9/98185042c1c3cc6b20e2a5dd8cc74215b9fee7268c82781a7c4f7cc854f4/scikit-image-0.18.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e1/e9/98185042c1c3cc6b20e2a5dd8cc74215b9fee7268c82781a7c4f7cc854f4/scikit-image-0.18.2.tar.gz
Summary  : Image processing in Python
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: scikit-image-bin = %{version}-%{release}
Requires: scikit-image-license = %{version}-%{release}
Requires: scikit-image-python = %{version}-%{release}
Requires: scikit-image-python3 = %{version}-%{release}
Requires: Pillow
Requires: PyWavelets
Requires: cloudpickle
Requires: dask
Requires: imageio
Requires: matplotlib
Requires: networkx
Requires: scipy
BuildRequires : Cython
BuildRequires : Pillow
BuildRequires : PyWavelets
BuildRequires : buildreq-distutils3
BuildRequires : cloudpickle
BuildRequires : dask
BuildRequires : imageio
BuildRequires : matplotlib
BuildRequires : networkx
BuildRequires : numpy
BuildRequires : scikit-learn
BuildRequires : scipy

%description
# scikit-image: Image processing in Python
[![Image.sc forum](https://img.shields.io/badge/dynamic/json.svg?label=forum&url=https%3A%2F%2Fforum.image.sc%2Ftags%2Fscikit-image.json&query=%24.topic_list.tags.0.topic_count&colorB=brightgreen&suffix=%20topics&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAABPklEQVR42m3SyyqFURTA8Y2BER0TDyExZ+aSPIKUlPIITFzKeQWXwhBlQrmFgUzMMFLKZeguBu5y+//17dP3nc5vuPdee6299gohUYYaDGOyyACq4JmQVoFujOMR77hNfOAGM+hBOQqB9TjHD36xhAa04RCuuXeKOvwHVWIKL9jCK2bRiV284QgL8MwEjAneeo9VNOEaBhzALGtoRy02cIcWhE34jj5YxgW+E5Z4iTPkMYpPLCNY3hdOYEfNbKYdmNngZ1jyEzw7h7AIb3fRTQ95OAZ6yQpGYHMMtOTgouktYwxuXsHgWLLl+4x++Kx1FJrjLTagA77bTPvYgw1rRqY56e+w7GNYsqX6JfPwi7aR+Y5SA+BXtKIRfkfJAYgj14tpOF6+I46c4/cAM3UhM3JxyKsxiOIhH0IO6SH/A1Kb1WBeUjbkAAAAAElFTkSuQmCC)](https://forum.image.sc/tags/scikit-image)
[![Stackoverflow](https://img.shields.io/badge/stackoverflow-Ask%20questions-blue.svg)](https://stackoverflow.com/questions/tagged/scikit-image)
[![project chat](https://img.shields.io/badge/zulip-join_chat-brightgreen.svg)](https://skimage.zulipchat.com)
[![codecov.io](https://codecov.io/github/scikit-image/scikit-image/coverage.svg?branch=main)](https://codecov.io/github/scikit-image/scikit-image?branch=main)

%package bin
Summary: bin components for the scikit-image package.
Group: Binaries
Requires: scikit-image-license = %{version}-%{release}

%description bin
bin components for the scikit-image package.


%package license
Summary: license components for the scikit-image package.
Group: Default

%description license
license components for the scikit-image package.


%package python
Summary: python components for the scikit-image package.
Group: Default
Requires: scikit-image-python3 = %{version}-%{release}

%description python
python components for the scikit-image package.


%package python3
Summary: python3 components for the scikit-image package.
Group: Default
Requires: python3-core
Provides: pypi(scikit_image)
Requires: pypi(imageio)
Requires: pypi(matplotlib)
Requires: pypi(networkx)
Requires: pypi(numpy)
Requires: pypi(pillow)
Requires: pypi(pywavelets)
Requires: pypi(scipy)
Requires: pypi(tifffile)

%description python3
python3 components for the scikit-image package.


%prep
%setup -q -n scikit-image-0.18.2
cd %{_builddir}/scikit-image-0.18.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624989285
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mprefer-vector-width=256 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
#make test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/scikit-image
cp %{_builddir}/scikit-image-0.18.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/scikit-image/9c5c45c8433b83e2ac82898a64d41746dec6f2fc
cp %{_builddir}/scikit-image-0.18.2/doc/tools/LICENSE.txt %{buildroot}/usr/share/package-licenses/scikit-image/fb50fd87a0153fd93be5975f012fa41347306040
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/skivi

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/scikit-image/9c5c45c8433b83e2ac82898a64d41746dec6f2fc
/usr/share/package-licenses/scikit-image/fb50fd87a0153fd93be5975f012fa41347306040

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
