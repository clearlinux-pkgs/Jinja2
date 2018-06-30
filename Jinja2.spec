#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : Jinja2
Version  : 2.10
Release  : 48
URL      : http://pypi.debian.net/Jinja2/Jinja2-2.10.tar.gz
Source0  : http://pypi.debian.net/Jinja2/Jinja2-2.10.tar.gz
Source99 : http://pypi.debian.net/Jinja2/Jinja2-2.10.tar.gz.asc
Summary  : A small but fast and easy to use stand-alone template engine written in pure python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Jinja2-python3
Requires: Jinja2-license
Requires: Jinja2-python
Requires: Babel
Requires: MarkupSafe
BuildRequires : MarkupSafe
BuildRequires : MarkupSafe-legacypython
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
Jinja2
        ~~~~~~
        
        Jinja2 is a template engine written in pure Python.  It provides a
        `Django`_ inspired non-XML syntax but supports inline expressions and
        an optional `sandboxed`_ environment.
        
        Nutshell
        --------

%package legacypython
Summary: legacypython components for the Jinja2 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the Jinja2 package.


%package license
Summary: license components for the Jinja2 package.
Group: Default

%description license
license components for the Jinja2 package.


%package python
Summary: python components for the Jinja2 package.
Group: Default
Requires: Jinja2-python3
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
%setup -q -n Jinja2-2.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530374104
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1530374104
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/Jinja2
cp LICENSE %{buildroot}/usr/share/doc/Jinja2/LICENSE
cp docs/_themes/LICENSE %{buildroot}/usr/share/doc/Jinja2/docs__themes_LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/Jinja2/LICENSE
/usr/share/doc/Jinja2/docs__themes_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
