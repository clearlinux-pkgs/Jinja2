#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : Jinja2
Version  : 2.10.1
Release  : 60
URL      : https://files.pythonhosted.org/packages/93/ea/d884a06f8c7f9b7afbc8138b762e80479fb17aedbbe2b06515a12de9378d/Jinja2-2.10.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/ea/d884a06f8c7f9b7afbc8138b762e80479fb17aedbbe2b06515a12de9378d/Jinja2-2.10.1.tar.gz
Source99 : https://files.pythonhosted.org/packages/93/ea/d884a06f8c7f9b7afbc8138b762e80479fb17aedbbe2b06515a12de9378d/Jinja2-2.10.1.tar.gz.asc
Summary  : A small but fast and easy to use stand-alone template engine written in pure python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Jinja2-license = %{version}-%{release}
Requires: Jinja2-python = %{version}-%{release}
Requires: Jinja2-python3 = %{version}-%{release}
Requires: Babel
Requires: MarkupSafe
BuildRequires : MarkupSafe
BuildRequires : buildreq-distutils3

%description
Flask Sphinx Styles
===================
This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

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

%description python3
python3 components for the Jinja2 package.


%prep
%setup -q -n Jinja2-2.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554587358
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
cp LICENSE %{buildroot}/usr/share/package-licenses/Jinja2/LICENSE
cp docs/_themes/LICENSE %{buildroot}/usr/share/package-licenses/Jinja2/docs__themes_LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Jinja2/LICENSE
/usr/share/package-licenses/Jinja2/docs__themes_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
