Summary:	Fetchconfig device configuration retrieval software
Summary(pl.UTF-8):	fetchconfig - program do odczytu konfiguracji urządzeń
Name:		fetchconfig
Version:	0.24
Release:	1
License:	GPL v2
Group:		Applications/System
#Source0Download: https://github.com/udhos/fetchconfig/releases
Source0:	https://github.com/udhos/fetchconfig/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5a79110c1edbc71fe2a29269f7a7de8a
URL:		https://github.com/udhos/fetchconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	perl-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fetchconfig is a Perl script for retrieving the configuration of
multiple devices. It has been tested under Linux and Windows, and
currently supports a variety of devices.

With some simple Perl programming, it is easily adaptable to any
network devices which provides functionality similar to Cisco's "show
running-config" command.

%description -l pl.UTF-8
fetchconfig to skrypt Perla do odczytu konfiguracji z wielu
urządzeń. Był testowany pod Linuksem i Windows, aktualnie obsługuje
różne urządzenia.

Przy użyciu prostego programowania w Perlu można go łatwo przystosować
do dowolnych urządzeń sieciowych udostępniających funkcjonalność
podobną do polecenia "show running-config" z Cisco.

%prep
%setup  -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{perl_vendorlib}/fetchconfig/model}

install fetchconfig.pl $RPM_BUILD_ROOT%{_bindir}/fetchconfig
install fetchconfig/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/fetchconfig
install fetchconfig/model/*.pm $RPM_BUILD_ROOT%{perl_vendorlib}/fetchconfig/model

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README device_table.example
%attr(755,root,root) %{_bindir}/fetchconfig
%{perl_vendorlib}/fetchconfig
