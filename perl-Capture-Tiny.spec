#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Capture
%define		pnam	Tiny
%include	/usr/lib/rpm/macros.perl
Summary:	Capture::Tiny - Capture STDOUT and STDERR from Perl, XS or external programs
#Summary(pl.UTF-8):
Name:		perl-Capture-Tiny
Version:	0.11
Release:	1
License:	apache
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DA/DAGOLDEN/Capture-Tiny-%{version}.tar.gz
# Source0-md5:	afbd9be69e4691ba8316545d216abdc8
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Capture-Tiny/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Capture::Tiny provides a simple, portable way to capture anything sent
to STDOUT or STDERR, regardless of whether it comes from Perl, from XS
code or from an external program. Optionally, output can be teed so
that it is captured while being passed through to the original
handles. Yes, it even works on Windows. Stop guessing which of a dozen
capturing modules to use in any particular situation and just use this
one.

This module was heavily inspired by IO::CaptureOutput, which provides
similar functionality without the ability to tee output and with more
complicated code and API.



# %description -l pl.UTF-8 # TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Capture
%{perl_vendorlib}/Capture/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
