%{?scl:%scl_package perl-Test-Deep}

Name:           %{?scl_prefix}perl-Test-Deep
Version:        1.120
Release:        4%{?dist}
Summary:        Extremely flexible deep comparison
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Deep/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Test-Deep-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util) >= 1.09
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::Builder)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Test Suite
BuildRequires:  %{?scl_prefix}perl(if)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.88
BuildRequires:  %{?scl_prefix}perl(Test::Tester) >= 0.04
# Runtime
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Test::Builder)

%description
Test::Deep gives you very flexible ways to check that the result you
got is the result you were expecting. At its simplest it compares two
structures by going through each level, ensuring that the values
match, that arrays and hashes have the same elements and that
references are blessed into the correct class. It also handles
circular data structures without getting caught in an infinite loop.

%prep
%setup -q -n Test-Deep-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%clean
rm -rf %{buildroot}

%files
%doc Changes README TODO
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Deep.3*
%{_mandir}/man3/Test::Deep::NoTest.3*

%changelog
* Mon Jul 18 2016 Petr Pisar <ppisar@redhat.com> - 1.120-4
- SCL

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.120-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.120-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Paul Howarth <paul@city-fan.org> - 1.120-1
- Update to 1.120
  - Add none() test; it's like any(), but negative
  - Fix stringification of any() expectations

* Wed Sep 30 2015 Paul Howarth <paul@city-fan.org> - 0.119-1
- Update to 0.119
  - Overloading of & and | no longer can change All or Any objects found as
    arguments
  - An All as an argument to an All constructed is flattened out into its
    All-ed values; the same goes for Any
  - Remove use of Test::NoWarnings for user-facing tests

* Mon Jun 22 2015 Paul Howarth <paul@city-fan.org> - 0.117-1
- Update to 0.117
  - Do not lose argument(s) to import
    (https://github.com/rjbs/Test-Deep/issues/29)

* Sun Jun 21 2015 Paul Howarth <paul@city-fan.org> - 0.116-1
- Update to 0.116
  - On its own, :preload options uses default group of exports

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.115-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.115-2
- Perl 5.22 rebuild

* Sat Jan 10 2015 Paul Howarth <paul@city-fan.org> - 0.115-1
- Update to 0.115
  - Worked around a bug in chained goto on 5.8.5

* Mon Dec 15 2014 Paul Howarth <paul@city-fan.org> - 0.114-1
- Update to 0.114
  - Improve prereqs metadata
  - Add a noneof() set test
  - regexponly hasn't worked... ever; now it does
  - Passing :preload to import loads all plugins up front
  - A few more tests have been documented
  - The many exports of Test::Deep are now documented!

* Thu Nov 13 2014 Paul Howarth <paul@city-fan.org> - 0.113-1
- Update to 0.113
  - Fix a compile error (!!) in RegexpOnly
  - Fix some documentation typos
  - Add license to META file

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.112-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Nov 30 2013 Paul Howarth <paul@city-fan.org> - 0.112-1
- Update to 0.112
  - When printing diagnostics, differentiate the type of a blessed object from
    the name of the class itself (CPAN RT#78288)
  - Typo fixes
  - Fixes to clarity and accuracy of documentation
  - Add metadata links to repo and issue tracker
  - Added obj_isa for testing ->isa without falling back to ref($x)
  - Added the *experimental* ":v1" export group to skip importing Isa, isa, and
    blessed

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.110-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.110-2
- Perl 5.18 rebuild

* Wed Feb 20 2013 Paul Howarth <paul@city-fan.org> - 0.110-1
- Update to 0.110
  - Allow methods() and listmethods() to work again on class methods
    (CPAN RT#77804)
- Drop redundant BR: perl(Data::Dumper)
- Drop arrayeach patch - similar change introduced upstream
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot
- Don't use macros for commands
- Use DESTDIR rather than PERL_INSTALL_ROOT
- Make %%files list more explicit

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.108-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.108-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.108-6
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.108-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.108-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.108-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.108-2
- Rebuild to fix problems with vendorarch/lib (#661697)

* Sat Dec 18 2010 Steven Pritchard <steve@kspei.com> 0.108-1
- Update to 0.108.
- Update Source0 URL.

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.106-3
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.106-2
- rebuild against perl 5.10.1

* Fri Oct 30 2009 Stepan Kasal <skasal@redhat.com> - 0.106-1
- new upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 22 2008 Lubomir Rintel <lubo.rintel@gooddata.com> 0.103-2
- Fix crash on matching array_each() against non-array

* Wed Jun 04 2008 Steven Pritchard <steve@kspei.com> 0.103-1
- Update to 0.103.

* Sat May 31 2008 Steven Pritchard <steve@kspei.com> 0.102-1
- Update to 0.102.

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 0.101-1
- Update to 0.101.

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.100-2
- rebuild for new perl

* Mon Jan 28 2008 Steven Pritchard <steve@kspei.com> 0.100-1
- Update to 0.100.

* Sat Jan 12 2008 Steven Pritchard <steve@kspei.com> 0.099-1
- Update to 0.099.
- Update License tag.

* Tue Sep 18 2007 Steven Pritchard <steve@kspei.com> 0.098-1
- Update to 0.098.

* Fri Aug 10 2007 Steven Pritchard <steve@kspei.com> 0.097-1
- Update to 0.097.

* Wed Apr 18 2007 Steven Pritchard <steve@kspei.com> 0.096-2
- Use fixperms macro instead of our own chmod incantation.
- BR ExtUtils::MakeMaker.

* Tue Sep 26 2006 Steven Pritchard <steve@kspei.com> 0.096-1
- Update to 0.096.

* Sat Sep 16 2006 Steven Pritchard <steve@kspei.com> 0.095-2
- Fix find option order.

* Fri Apr 21 2006 Steven Pritchard <steve@kspei.com> 0.095-1
- Update to 0.095.

* Sat Apr 08 2006 Steven Pritchard <steve@kspei.com> 0.093-1
- Specfile autogenerated by cpanspec 1.64.
- Improve description.
- Fix License.
- Remove explicit dependency on Test::Tester and Test::NoWarnings.
