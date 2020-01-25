%define		pkgname	log
%define		php_min_version 5.3.3
Summary:	Common interface for logging libraries
Name:		php-psr-log
Version:	1.0.1
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/php-fig/log/archive/%{version}/psr-log-%{version}.tar.gz
# Source0-md5:	05c07390eba4c449e430c1c8811aa6d9
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

mv Psr/Log/Test .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a Psr $RPM_BUILD_ROOT%{php_data_dir}

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
