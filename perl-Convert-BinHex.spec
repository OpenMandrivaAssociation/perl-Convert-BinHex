%define module	Convert-BinHex
%define name	perl-%{module}
%define version 1.119
%define release 11

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
rm -rf %{buildroot} 
%makeinstall_std 

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/Convert




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.119-9mdv2012.0
+ Revision: 765111
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.119-8
+ Revision: 763568
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.119-7
+ Revision: 667054
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.119-6mdv2010.1
+ Revision: 426434
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.119-5mdv2009.0
+ Revision: 223578
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 1.119-4mdv2008.1
+ Revision: 166034
- fix spacing at top of description
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.119-4mdv2008.0
+ Revision: 67819
- rebuild


* Thu Dec 28 2006 Stew Benedict <sbenedict@mandriva.com> 1.119-3mdv2007.0
+ Revision: 102261
- rebuild, %%mkrel

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Convert-BinHex

* Wed Nov 09 2005 Stew Benedict <sbenedict@mandrakesoft.com> 1.119-2mdk
- birthday rebuild

* Sat Oct 30 2004 Stew Benedict <sbenedict@mandrakesoft.com> 1.119-1mdk
- first Mandrakelinux release, optional feature for perl-MIME-tools

