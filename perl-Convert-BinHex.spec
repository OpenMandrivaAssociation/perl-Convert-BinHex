%define module	Convert-BinHex

Summary:	Extract data from Macintosh BinHex files
Name:		perl-%{module}
Version:	1.125
Release:	2
License:	GPLv2
Group:		Development/Perl
Requires:	perl
Url:		http://www.cpan.org
Source0:	http://www.cpan.org/modules/by-module/Convert/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Convert::BinHex is used to extract data from Macintosh BinHex files

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor 

%build
%make_build OPTIMIZE="$RPM_OPT_FLAGS" 

%check
# (sb) can't really do this - need a Radius server
#make test

%install
%make_install

%files
%doc README
%{_bindir}/*
%{perl_vendorlib}/Convert
%{_mandir}/man1/*
%{_mandir}/man3/*
