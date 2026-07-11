%global tl_name stringstrings
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.24
Release:	%{tl_revision}.1
Summary:	String manipulation for cosmetic and programming application
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/stringstrings
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stringstrings.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stringstrings.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stringstrings.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a large and sundry set of macros for the
manipulation of strings. The macros are developed not merely for
cosmetic application (such as changing the case of letters and string
substitution), but also for programming applications such as character
look-ahead, argument parsing, conditional tests on various string
conditions, etc. The macros were designed all to be expandable (note
that things such as \uppercase and \lowercase are not expandable), so
that the macros may be strung together sequentially and nested (after a
fashion) to achieve rather complex manipulations.

