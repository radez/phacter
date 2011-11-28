# sitelib for noarch packages
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}


Name:           python-phacter
Version:        0.2.0
Release:        2%{?dist}
Summary:        System fact look up tool

Group:          Applications/System
License:        GPLv2
URL:            https://github.com/radez/phacter
# source tarball can also be generated with ./setup.py rpm
Source0:        http://radez.fedorapeople.org/%{name}-%{version}.tar.gz
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
mkdir -p $RPM_BUILD_ROOT/%{_sharedstatedir}/phacter/
mkdir -p %{buildroot}%{_mandir}/man1/

%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
cp phacter.1 %{buildroot}%{_mandir}/man1/phacter.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING LICENSE
%doc %{_mandir}/man1/phacter.1.gz
%{_bindir}/phacter
%{python_sitelib}/*
%dir %{_sharedstatedir}/phacter


%changelog
* Mon Nov 28 2011 Dan Radez <dradez@redhat.com> - 0.2.0-2
- rpmlint reports no errors or warnings
* Fri Nov 18 2011 Dan Radez <dradez@redhat.com> - 0.2.0-1
- Initial spec
