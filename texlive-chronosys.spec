# revision 24609
# category Package
# catalog-ctan /macros/latex/contrib/chronosys
# catalog-date 2011-11-15 07:10:45 +0100
# catalog-license lppl1.3
# catalog-version 1.01
Name:		texlive-chronosys
Version:	1.01
Release:	2
Summary:	Drawing time-line diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chronosys
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chronosys.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chronosys.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Macros to produce time line diagrams. Interfaces for Plain TeX,
Context and LaTeX are provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/chronosys/chronosys.sty
%{_texmfdistdir}/tex/generic/chronosys/chronosys.tex
%{_texmfdistdir}/tex/generic/chronosys/chronosyschr.tex
%{_texmfdistdir}/tex/generic/chronosys/x-chronosys.tex
%doc %{_texmfdistdir}/doc/generic/chronosys/README
%doc %{_texmfdistdir}/doc/generic/chronosys/docchronosys_en.pdf
%doc %{_texmfdistdir}/doc/generic/chronosys/docchronosys_en.tex
%doc %{_texmfdistdir}/doc/generic/chronosys/docchronosys_fr.pdf
%doc %{_texmfdistdir}/doc/generic/chronosys/docchronosys_fr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
