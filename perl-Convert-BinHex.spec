%define module	Convert-BinHex
%define name	perl-%{module}
%define version 1.119
%define release %mkrel 6

Summary:	Extract data from Macintosh BinHex files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Requires:	perl
URL:		http://www.cpan.org
Source:		%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

%description
Convert::BinHex is used to extract data from Macintosh BinHex files

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="$RPM_OPT_FLAGS" 
# (sb) can't really do this - need a Radius server
#make test

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall_std 

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/Convert


