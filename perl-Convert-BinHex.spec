%define module	Convert-BinHex
%define modver	1.119

Summary:	Extract data from Macintosh BinHex files
Name:		perl-%{module}
Version:	%perl_convert_version %{modver}
Release:	16
License:	GPLv2
Group:		Development/Perl
Requires:	perl
Url:		http://www.cpan.org
Source0:	%{module}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Convert::BinHex is used to extract data from Macintosh BinHex files

%prep
%setup -qn %{module}-%{modver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="$RPM_OPT_FLAGS" 

%check
# (sb) can't really do this - need a Radius server
#make test

%install
%makeinstall_std 

%files
%doc README
%{perl_vendorlib}/Convert
%{_mandir}/man3/*

