#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : Jinja2
Version  : 3.0.1
Release  : 83
URL      : https://files.pythonhosted.org/packages/39/11/8076571afd97303dfeb6e466f27187ca4970918d4b36d5326725514d3ed3/Jinja2-3.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/39/11/8076571afd97303dfeb6e466f27187ca4970918d4b36d5326725514d3ed3/Jinja2-3.0.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/39/11/8076571afd97303dfeb6e466f27187ca4970918d4b36d5326725514d3ed3/Jinja2-3.0.1.tar.gz.asc
Summary  : A very fast and expressive template engine.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Jinja2-license = %{version}-%{release}
Requires: Jinja2-python = %{version}-%{release}
Requires: Jinja2-python3 = %{version}-%{release}
Requires: Babel
Requires: MarkupSafe
BuildRequires : Babel
BuildRequires : MarkupSafe
BuildRequires : buildreq-distutils3

%description
=====
        
        Jinja is a fast, expressive, extensible templating engine. Special
        placeholders in the template allow writing code similar to Python
        syntax. Then the template is passed data to render the final document.

%package license
Summary: license components for the Jinja2 package.
Group: Default

%description license
license components for the Jinja2 package.


%package python
Summary: python components for the Jinja2 package.
Group: Default
Requires: Jinja2-python3 = %{version}-%{release}
Provides: jinja2-python

%description python
python components for the Jinja2 package.


%package python3
Summary: python3 components for the Jinja2 package.
Group: Default
Requires: python3-core
Provides: pypi(jinja2)
Requires: pypi(markupsafe)

%description python3
python3 components for the Jinja2 package.


%prep
%setup -q -n Jinja2-3.0.1
cd %{_builddir}/Jinja2-3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621434296
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Jinja2
cp %{_builddir}/Jinja2-3.0.1/LICENSE.rst %{buildroot}/usr/share/package-licenses/Jinja2/c4dbdbc12926d4d52c9156e690640f372615c234
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Jinja2/c4dbdbc12926d4d52c9156e690640f372615c234

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
