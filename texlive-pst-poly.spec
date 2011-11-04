# revision 16460
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-poly
# catalog-date 2009-12-20 19:36:06 +0100
# catalog-license lppl
# catalog-version 1.61
Name:		texlive-pst-poly
Version:	1.61
Release:	1
Summary:	Polygons with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-poly
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poly.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poly.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poly.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This PSTricks package provides a really rather simple command
\PstPolygon that will draw various regular and non-regular
polygons (according to command parameters); various shortcuts
to commonly-used polygons are provided, as well as a command
\pspolygonbox that frames text with a polygon. The package uses
the xkeyval package for argument decoding.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-poly/pst-poly.tex
%{_texmfdistdir}/tex/latex/pst-poly/pst-poly.sty
%doc %{_texmfdistdir}/doc/generic/pst-poly/Changes
%doc %{_texmfdistdir}/doc/generic/pst-poly/README
%doc %{_texmfdistdir}/doc/generic/pst-poly/pst-poly-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-poly/pst-poly-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-poly/pst-poly-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-poly/Makefile
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
