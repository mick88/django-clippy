%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%define real_name django-clippy

Name: python-django-clippy
Version: 1.1
Release: 1%{?dist}
Summary: Flash based template tag for Django to allow copying the clipboard
Group: Development/Languages
License: MIT
URL: http://github.com/mdornseif/django-clippy#readme

Source: https://github.com/downloads/Eyepea/django-clippy/django-clippy-1.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-setuptools

Requires: python-django

Provides: %{name} = %{version}-%{release}

%description
django-clippy provides a template tag for the Django Web Framework to allow copying the Clipboard.
Functionality is implemented in Flash.

%prep
%setup -n %{real_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{python_sitelib}/*
# if arch-specific
# %{python_sitearch}/*

%changelog
* Mon Sep 10 2012 Xavier Devlamynck <xd@eyepea.eu> 1.1-1
- Update to 1.1

* Thu Sep 06 2012 Xavier Devlamynck <xd@eyepea.eu> - 1.01p1-1
- Initial package.

