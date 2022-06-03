#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Twig
Version  : 3.52
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIROD/XML-Twig-3.52.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIROD/XML-Twig-3.52.tar.gz
Summary  : 'XML, The Perl Way'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-XML-Twig-bin = %{version}-%{release}
Requires: perl-XML-Twig-man = %{version}-%{release}
Requires: perl-XML-Twig-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(XML::Parser)

%description
NAME
XML::Twig - Tree interface to XML documents allowing processing chunk
by chunk of huge documents.

%package bin
Summary: bin components for the perl-XML-Twig package.
Group: Binaries

%description bin
bin components for the perl-XML-Twig package.


%package dev
Summary: dev components for the perl-XML-Twig package.
Group: Development
Requires: perl-XML-Twig-bin = %{version}-%{release}
Provides: perl-XML-Twig-devel = %{version}-%{release}
Requires: perl-XML-Twig = %{version}-%{release}

%description dev
dev components for the perl-XML-Twig package.


%package man
Summary: man components for the perl-XML-Twig package.
Group: Default

%description man
man components for the perl-XML-Twig package.


%package perl
Summary: perl components for the perl-XML-Twig package.
Group: Default
Requires: perl-XML-Twig = %{version}-%{release}

%description perl
perl components for the perl-XML-Twig package.


%prep
%setup -q -n XML-Twig-3.52
cd %{_builddir}/XML-Twig-3.52

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

%install
rm -rf %{buildroot}
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

%files bin
%defattr(-,root,root,-)
/usr/bin/xml_grep
/usr/bin/xml_merge
/usr/bin/xml_pp
/usr/bin/xml_spellcheck
/usr/bin/xml_split

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Twig.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xml_grep.1
/usr/share/man/man1/xml_merge.1
/usr/share/man/man1/xml_pp.1
/usr/share/man/man1/xml_spellcheck.1
/usr/share/man/man1/xml_split.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
