%global tl_name chronosys
%global tl_revision 26700

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Drawing time-line diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chronosys
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chronosys.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chronosys.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Macros to produce time line diagrams. Interfaces for Plain TeX, ConTeXt
and LaTeX are provided.

