%define        _class           MDB2
%define        _subclass        Driver_pgsql
%define        upstream_name    %{_class}_%{_subclass}

Name:           php-pear-%{upstream_name}
Version:        1.5.0
Release:        %mkrel 0.0.b3.3
Summary:	Pgsql MDB2 driver
Epoch:          1
License:        PHP License
Group:          Development/PHP
URL:            http://pear.php.net/package/MDB2_Driver_pgsql/
Source0:        http://download.pear.php.net/package/MDB2_Driver_pgsql-%{version}b3.tgz
Requires:	php-pgsql
Requires(post): php-pear
Requires(preun): php-pear
Requires:       php-pear
BuildRequires:  php-pear
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
MDB2 pgsql driver.

%prep
%setup -q -c -n %{name}-%{version}b3
mv package.xml %{upstream_name}-%{version}b3/%{upstream_name}.xml

%install
%{__rm} -rf %{buildroot}

cd %{upstream_name}-%{version}b3
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.0-0.0.b3.1mdv2011.0
+ Revision: 679283
- 1.5.0b3

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.0-0.0.b2.3
+ Revision: 667597
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.0-0.0.b2.2mdv2011.0
+ Revision: 607118
- rebuild

* Fri Mar 26 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.5.0-0.0.b2.1mdv2010.1
+ Revision: 527644
- 1.5.0b2
- fix versioning

* Thu Nov 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0:1.5.0b1-6mdv2010.1
+ Revision: 470290
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0:1.5.0b1-6mdv2010.0
+ Revision: 426655
- rebuild

* Sun Sep 07 2008 Oden Eriksson <oeriksson@mandriva.com> 0:1.5.0b1-5mdv2009.0
+ Revision: 282106
- fix deps

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0:1.5.0b1-4mdv2009.0
+ Revision: 258998
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:1.5.0b1-3mdv2009.0
+ Revision: 246878
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Tue Mar 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0:1.5.0b1-1mdv2008.1
+ Revision: 189947
- status is really beta
- 1.5.0b1 (fixes CVE-2007-5934)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 Oden Eriksson <oeriksson@mandriva.com> 0:1.4.1-1mdv2008.0
+ Revision: 22356
- 1.4.1

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0:1.4.0-1mdv2008.0
+ Revision: 15776
- fix build
- 1.4.0


* Fri Dec 15 2006 David Walluck <walluck@mandriva.org> 1.3.0-1mdv2007.0
+ Revision: 97243
- Import php-pear-MDB2_Driver_pgsql

