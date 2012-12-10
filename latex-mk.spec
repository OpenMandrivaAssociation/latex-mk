%define name latex-mk
%define version 2.1
%define release 1

Summary: Utility simplifying latex document managment
Name: latex-mk
Version: 2.1
Release: 1
Source0: http://switch.dl.sourceforge.net/project/latex-mk/latex-mk/latex-mk-%version/latex-mk-%version.tar.gz
License: BSD
Group: Publishing
Url: http://latex-mk.sourceforge.net/
Requires: make
Requires: texlive-latex, texlive, texlive-dvipdfm, texlive-dvips, gv, hevea
Requires: imagemagick, latex2html, ghostscript, transfig, texlive-xdvi, texinfo

BuildRequires: texlive-latex, texlive, texlive-dvipdfm, texlive-dvips, gv, hevea
Buildrequires: imagemagick, latex2html, ghostscript, transfig, texinfo

Buildarch: noarch
%description
LaTeX-Mk is a collection of makefile fragments and shell scripts
for simplifying the management of small to large sized LaTeX documents.

%prep
%setup -q

%build
# configure macro doesn't work ( Buildarch: noarch )
./configure --program-prefix= --prefix=/usr --exec-prefix=/usr --bindir=%{_bindir} --sysconfdir=/etc --datadir=%{_datadir} --infodir=%{_infodir} --libdir=%{_libdir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%defattr(-,root,root)
%{_bindir}/ieee-copyout
%{_bindir}/latex-mk
%dir %{_datadir}/latex-mk
%{_datadir}/latex-mk/*
%{_infodir}/%{name}*



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.1-5mdv2011.0
+ Revision: 620049
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.9.1-4mdv2010.0
+ Revision: 429701
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.9.1-3mdv2009.0
+ Revision: 248318
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 22 2007 Jérôme Soyer <saispo@mandriva.org> 1.9.1-1mdv2008.1
+ Revision: 101084
- New release 1.9.1
- import latex-mk


* Thu Aug 31 2006 Couriousous <couriousous@mandriva.org> 1.8-1mdv2007.0
- 1.8

* Sat Apr 15 2006 Couriousous <couriousous@mandriva.orv> 1.6-1mdk
- 1.6

* Fri Mar 17 2006 Couriousous <couriousous@mandriva.org> 1.5-1mdk
- 1.5

* Sun Dec 19 2004 Couriousous <couriousous@mandrake.org> 1.3-1mdk
- First Mandrakelinux release
