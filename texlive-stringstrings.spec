# revision 30093
# category Package
# catalog-ctan /macros/latex/contrib/stringstrings
# catalog-date 2012-10-10 00:01:11 +0200
# catalog-license lgpl
# catalog-version 1.21
Name:		texlive-stringstrings
Version:	1.21
Release:	5
Summary:	String manipulation for cosmetic and programming application
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stringstrings
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stringstrings.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stringstrings.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stringstrings.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a large and sundry set of macros for the
manipulation of strings. The macros are developed not merely
for cosmetic application (such as changing the case of letters
and string substitution), but also for programming applications
such as character look-ahead, argument parsing, conditional
tests on various string conditions, etc. The macros were
designed all to be expandable (note that things such as
\uppercase and \lowercase are not expandable), so that the
macros may be strung together sequentially and nested (after a
fashion) to achieve rather complex manipulations.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/stringstrings/stringstrings.sty
%doc %{_texmfdistdir}/doc/latex/stringstrings/README
%doc %{_texmfdistdir}/doc/latex/stringstrings/stringstrings.pdf
#- source
%doc %{_texmfdistdir}/source/latex/stringstrings/stringstrings.dtx
%doc %{_texmfdistdir}/source/latex/stringstrings/stringstrings.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
