# sitelib for noarch packages
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}


Name:           python-phacter
Version:        0.2.0
Release:        1%{?dist}
Summary:        System fact look up tool

Group:          Applications/System
License:        GPLv2
URL:            https://github.com/radez/phacter
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools, python-netifaces
Requires:       python, python-netifaces


%description
A python tool to report system facts


%prep
%setup -q -n %{name}-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_usr}/bin
mkdir -p $RPM_BUILD_ROOT/%{_var}/lib/phacter
mkdir -p $RPM_BUILD_ROOT/%{python_sitelib}/phacter

%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING LICENSE
%{_usr}/bin/phacter
%{python_sitelib}/*
%dir %{_var}/lib/phacter/


%changelog
* Fri Nov 18 2011 Dan Radez <dradez@redhat.com> - 0.2.0-1
- Initial spec
