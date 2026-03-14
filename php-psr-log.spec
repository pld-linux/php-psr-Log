%define		pkgname	log
%define		php_min_version 8.0.0
Summary:	Common interface for logging libraries
Name:		php-psr-log
Version:	3.0.2
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/php-fig/log/archive/%{version}/psr-log-%{version}.tar.gz
# Source0-md5:	e1f2bd318a160fc9de69a729bf554093
URL:		https://github.com/php-fig/log
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Provides:	php-psr-Log = %{version}-%{release}
Obsoletes:	php-psr-Log < 1.0.0-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains interfaces/classes/traits related to PSR-3.

Note that this is not a logger of its own. It is merely an interface
that describes a logger. See the specification for more details.

%prep
%setup -q -n log-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Psr/Log
cp -a src/*.php $RPM_BUILD_ROOT%{php_data_dir}/Psr/Log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%dir %{php_data_dir}/Psr
%dir %{php_data_dir}/Psr/Log
%{php_data_dir}/Psr/Log/AbstractLogger.php
%{php_data_dir}/Psr/Log/InvalidArgumentException.php
%{php_data_dir}/Psr/Log/LogLevel.php
%{php_data_dir}/Psr/Log/LoggerAwareInterface.php
%{php_data_dir}/Psr/Log/LoggerAwareTrait.php
%{php_data_dir}/Psr/Log/LoggerInterface.php
%{php_data_dir}/Psr/Log/LoggerTrait.php
%{php_data_dir}/Psr/Log/NullLogger.php
