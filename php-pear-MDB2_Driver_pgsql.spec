%define        _class           MDB2
%define        _subclass        Driver_pgsql
%define        upstream_name    %{_class}_%{_subclass}

Name:           php-pear-%{upstream_name}
Version:        1.5.0b1
Release:        %mkrel 6
Summary: Pgsql MDB2 driver
Epoch:          0
License:        PHP License
Group:          Development/PHP
URL:            http://pear.php.net/package/MDB2_Driver_pgsql/
Source0:        http://download.pear.php.net/package/MDB2_Driver_pgsql-%{version}.tgz
Requires:	php-pgsql
Requires(post): php-pear
Requires(preun): php-pear
Requires:       php-pear
Requires:       php-pear-MDB2
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
MDB2 pgsql driver.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
%{__rm} -rf %{buildroot}

cd %{upstream_name}-%{version}
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
