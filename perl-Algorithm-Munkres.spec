#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Algorithm-Munkres
Version  : 0.08
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/T/TP/TPEDERSE/Algorithm-Munkres-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TP/TPEDERSE/Algorithm-Munkres-0.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libalgorithm-munkres-perl/libalgorithm-munkres-perl_0.08-3.debian.tar.xz
Summary  : Munkres.pm
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Algorithm-Munkres-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::More)

%description
NAME
Algorithm-Munkres : Perl extension for Munkres' solution to
classical Assignment problem for square and rectangular matrices
This module extends the solution of Assignment problem for square
matrices to rectangular matrices by padding zeros. Thus a rectangular
matrix is converted to square matrix by padding necessary zeros.

%package dev
Summary: dev components for the perl-Algorithm-Munkres package.
Group: Development
Provides: perl-Algorithm-Munkres-devel = %{version}-%{release}
Requires: perl-Algorithm-Munkres = %{version}-%{release}

%description dev
dev components for the perl-Algorithm-Munkres package.


%package license
Summary: license components for the perl-Algorithm-Munkres package.
Group: Default

%description license
license components for the perl-Algorithm-Munkres package.


%prep
%setup -q -n Algorithm-Munkres-0.08
cd ..
%setup -q -T -D -n Algorithm-Munkres-0.08 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Algorithm-Munkres-0.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Algorithm-Munkres
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Algorithm-Munkres/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Algorithm/Munkres.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Algorithm::Munkres.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Algorithm-Munkres/deblicense_copyright
