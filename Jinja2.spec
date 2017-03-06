#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Jinja2
Version  : 2.9.5
Release  : 26
URL      : http://pypi.debian.net/Jinja2/Jinja2-2.9.5.tar.gz
Source0  : http://pypi.debian.net/Jinja2/Jinja2-2.9.5.tar.gz
Summary  : A small but fast and easy to use stand-alone template engine written in pure python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Jinja2-python
Requires: Babel
Requires: MarkupSafe
BuildRequires : MarkupSafe
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Flask Sphinx Styles
===================
This repository contains sphinx styles for Flask and Flask related
projects.  To use this style in your Sphinx documentation, follow
this guide:

%package python
Summary: python components for the Jinja2 package.
Group: Default
Provides: jinja2-python

%description python
python components for the Jinja2 package.


%prep
%setup -q -n Jinja2-2.9.5

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488816646
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1488816646
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
