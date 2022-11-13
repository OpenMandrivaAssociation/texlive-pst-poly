Name:		texlive-pst-poly
Version:	35062
Release:	1
Summary:	Polygons with PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-poly
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poly.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-poly.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/generic/pst-poly
%{_texmfdistdir}/tex/latex/pst-poly
%doc %{_texmfdistdir}/doc/generic/pst-poly

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
