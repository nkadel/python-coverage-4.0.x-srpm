# %%global prever b3
%global srcname coverage

Name:           python-coverage
Summary:        Code coverage testing module for Python 3
Version:        4.0.3
#Release:        5%%{?dist}
Release:        0.5%{?dist}
# jquery(MIT):
#  coverage/htmlfiles/jquery.min.js
# MIT or GPL:
#  coverage/htmlfiles/jquery.debounce.min.js
#  coverage/htmlfiles/jquery.hotkeys.js
#  coverage/htmlfiles/jquery.isonscreen.js
License:        ASL 2.0 and MIT and (MIT or GPL)
URL:            https://coverage.readthedocs.org/en/latest/
#Source0:        %pypi_source coverage %{version}%{?prever}
Source0:        https://pypi.python.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For docs - we're missing sphinxcontrib.spelling though
#BuildRequires:  python-sphinx_rtd_theme

%description
Coverage.py is a Python 3 module that measures code coverage during Python 
execution. It uses the code analysis tools and tracing hooks provided in the 
Python standard library to determine which lines are executable, and which 
have been executed.

%package -n python%{python3_pkgversion}-coverage
Summary:        Code coverage testing module for Python %{python3_pkgversion}
Group:          System Environment/Libraries
# As the "coverage" executable requires the setuptools at runtime (#556290),
# so the "python3-coverage" executable requires python3-setuptools:
Requires:       python%{python3_pkgversion}-setuptools
Provides:       bundled(js-jquery) = 1.11.1
Provides:       bundled(js-jquery-debounce) = 1.1
Provides:       bundled(js-jquery-hotkeys) = 0.8
Provides:       bundled(js-jquery-isonscreen) = 1.2.0
Provides:       bundled(js-jquery-tablesorter)

%description -n python%{python3_pkgversion}-coverage
Coverage.py is a Python %{python3_pkgversion} module that measures code coverage during Python
execution. It uses the code analysis tools and tracing hooks provided in the 
Python standard library to determine which lines are executable, and which 
have been executed.

%prep
%setup -q -n coverage-%{version}%{?prever}

find . -type f -exec chmod 0644 \{\} \;
sed -i 's/\r//g' README.rst


%build
%py3_build
#make dochtml


%install
%py3_install
rm %{buildroot}/%{_bindir}/coverage


%files -n python%{python3_pkgversion}-coverage
%license LICENSE.txt NOTICE.txt
%doc AUTHORS.txt CHANGES.rst howto.txt README.rst TODO.txt doc/*.rst
%{_bindir}/coverage3
%{_bindir}/coverage-%{python3_version}
%{python3_sitearch}/coverage/
%{python3_sitearch}/coverage-%{version}-py%{python3_version}.egg-info/



%changelog
* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com>
- Rebuilt to change main python from 3.4 to 3.6

* Tue Jul 03 2018 Carl George <carl@george.computer> - 4.0.3-4
- Enable python36 subpackage

* Wed Jan 13 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-3
- Note and update license
- Note bundled jquery libraries

* Wed Jan 13 2016 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-2
- Fix and install licenses
- Install docs

* Wed Dec 30 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-1
- Initial EPEL7 package
