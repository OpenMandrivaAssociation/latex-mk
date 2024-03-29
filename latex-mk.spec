# (mandian) doc compilation fails due to a bug in texinfo
%bcond_with	doc

Summary:	Utility simplifying latex document managment
Name:		latex-mk
Version:	2.1
Release:	3
License:	BSD
Group:		Publishing
Url:		https://latex-mk.sourceforge.net/
Source0:	https://downloads.sourceforge.net/latex-mk/latex-mk/%name-%version/%name-%version.tar.gz
%if !%{with doc}
Patch0:		latex-mk-exclude_doc.patch
%endif
# (debian)
Patch5:		fix-documentation.patch

BuildRequires:	texlive-latex
BuildRequires:	texlive
BuildRequires:	texlive-dvipdfm
BuildRequires:	texlive-dvips
#BuildRequires:	gv
#BuildRequires:	hevea
Buildrequires:	imagemagick
BuildRequires:	latex2html
BuildRequires:	ghostscript
BuildRequires:	transfig
BuildRequires:	texinfo

Requires:	make
Requires:	texlive
Requires:	texlive-latex
Requires:	texlive-dvipdfm
Requires:	texlive-dvips
#Requires:	gv
#Requires:	hevea
Requires:	imagemagick
Requires:	latex2html
Requires:	ghostscript
Requires:	transfig
Requires:	texlive-xdvi
Requires:	texinfo

Buildarch:	noarch

%description
LaTeX-Mk is a collection of makefile fragments and shell scripts
for simplifying the management of small to large sized LaTeX documents.

%files
%{_bindir}/ieee-copyout
%{_bindir}/latex-mk
%dir %{_datadir}/latex-mk
%{_datadir}/latex-mk/*
%if %{with doc}
%{_infodir}/%{name}*
%endif

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
# configure macro doesn't work ( Buildarch: noarch )
%if %{with doc}
#rm -f doc/texinfo.tex
%endif

%configure \
	--program-prefix= \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--infodir=%{_infodir} \
	--libdir=%{_libdir}
%make_build

%install
%make_install

