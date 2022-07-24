%define _empty_manifest_terminate_build 0

%define upstream_name    Syntax-Keyword-Try
%define upstream_version 0.27

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    A C<try/catch/finally> syntax for perl
License:    GPLv1+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    https://www.cpan.org/modules/by-module/Syntax/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build) >= 0.400.400
BuildRequires: perl(Test::More) >= 0.880.0
BuildRequires: perl(XS::Parse::Keyword) >= 0.60.0
BuildRequires: perl(XS::Parse::Keyword::Builder) >= 0.60.0
BuildRequires: perl-devel

%description
This module provides a syntax plugin that implements exception-handling
semantics in a form familiar to users of other languages, being built on a
block labeled with the 'try' keyword, followed by at least one of a 'catch'
or 'finally' block.

As well as providing a handy syntax for this useful behaviour, this module
also serves to contain a number of code examples for how to implement
parser plugins and manipulate optrees to provide new syntax and behaviours
for perl code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL --installdirs=vendor

./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot}

%files
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%perl_vendorarch/*
