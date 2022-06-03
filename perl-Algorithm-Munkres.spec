#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Algorithm-Munkres
Version  : 0.08
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/T/TP/TPEDERSE/Algorithm-Munkres-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TP/TPEDERSE/Algorithm-Munkres-0.08.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liba/libalgorithm-munkres-perl/libalgorithm-munkres-perl_0.08-3.debian.tar.xz
Summary  : Munkres.pm
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Algorithm-Munkres-license = %{version}-%{release}
Requires: perl-Algorithm-Munkres-perl = %{version}-%{release}
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


%package perl
Summary: perl components for the perl-Algorithm-Munkres package.
Group: Default
Requires: perl-Algorithm-Munkres = %{version}-%{release}

%description perl
perl components for the perl-Algorithm-Munkres package.


%prep
%setup -q -n Algorithm-Munkres-0.08
cd %{_builddir}
tar xf %{_sourcedir}/libalgorithm-munkres-perl_0.08-3.debian.tar.xz
cd %{_builddir}/Algorithm-Munkres-0.08
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Algorithm-Munkres-0.08/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Algorithm-Munkres
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Algorithm-Munkres/e4263455f1c2bafee69226bd358a27dfd3a9f587
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Algorithm::Munkres.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Algorithm-Munkres/e4263455f1c2bafee69226bd358a27dfd3a9f587

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
