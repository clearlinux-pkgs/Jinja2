#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Jinja2
Version  : 2.8
Release  : 16
URL      : https://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.8.tar.gz
Source0  : https://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.8.tar.gz
Summary  : A small but fast and easy to use stand-alone template engine written in pure python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Jinja2-python
BuildRequires : MarkupSafe-python
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
Requires: MarkupSafe-python

%description python
python components for the Jinja2 package.


%prep
%setup -q -n Jinja2-2.8

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
