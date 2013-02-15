%global __python /usr/bin/python27

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname pip

Name:           python27-%{srcname}
Version:        1.2.1
Release:        1.vortex%{?dist}
Summary:        Pip installs packages.  Python packages.  An easy_install replacement

Group:          Development/Libraries
License:        MIT
URL:            http://pip.openplans.org
Source0:        http://pypi.python.org/packages/source/p/pip/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python27-devel, python27-setuptools
Requires:       python27-setuptools

%description

Pip is a replacement for `easy_install
<http://peak.telecommunity.com/DevCenter/EasyInstall>`_.  It uses mostly the
same techniques for finding packages, so packages that were made
easy_installable should be pip-installable as well.

pip is meant to improve on easy_install.bulletin boards, etc.).

%prep
%setup -q -n %{srcname}-%{version}
%{__sed} -i '1d' pip/__init__.py

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{__rm} -rf %{buildroot}%{_bindir}/pip-*
mv %{buildroot}%{_bindir}/pip %{buildroot}%{_bindir}/pip-2.7

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc PKG-INFO docs LICENSE.txt AUTHORS.txt
%attr(755,root,root) %{_bindir}/pip-2.7
%{python_sitelib}/pip*

%changelog
* Fri Feb 15 2013 Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.2.1-1.vortex
- Update to 1.2.1 and rebuild with Python 2.7.

* Mon Aug 30 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.8-1
- update to 0.8 of pip

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 7 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.2-1
- update to 0.7.2 of pip

* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.7.1-1
- update to 0.7.1 of pip

* Fri Jan 1 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1.4
- fix dependency issue

* Tue Dec 18 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-2
- fix spec file 

* Mon Dec 17 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.1-1
- upgrade to 0.6.1 of pip

* Mon Aug 31 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.4-1
- Initial package

