# revision 16460
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-poly
# catalog-date 2009-12-20 19:36:06 +0100
# catalog-license lppl
# catalog-version 1.61
Name:		texlive-pst-poly
Version:	1.61
Release:	2
Summary:	Polygons with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-poly
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poly.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poly.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poly.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This PSTricks package provides a really rather simple command
\PstPolygon that will draw various regular and non-regular
polygons (according to command parameters); various shortcuts
to commonly-used polygons are provided, as well as a command
\pspolygonbox that frames text with a polygon. The package uses
the xkeyval package for argument decoding.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.61-2
+ Revision: 755401
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.61-1
+ Revision: 719382
- texlive-pst-poly
- texlive-pst-poly
- texlive-pst-poly
- texlive-pst-poly

