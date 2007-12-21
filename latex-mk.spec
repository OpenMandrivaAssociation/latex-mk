%define name latex-mk
%define version 1.9.1
%define release %mkrel 1

Summary: Utility simplifying latex document managment
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: BSD
Group: Publishing
Url: http://latex-mk.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: make
Requires: tetex-latex, tetex, tetex-dvipdfm, tetex-dvips, gv, hevea
Requires: ImageMagick, latex2html, ghostscript, transfig, tetex-xdvi

BuildRequires: tetex-latex, tetex, tetex-dvipdfm, tetex-dvips, gv, hevea
Buildrequires: ImageMagick, latex2html, ghostscript, transfig

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

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %name.info

%postun
%_remove_install_info %name.info

%files
%defattr(-,root,root)
%{_bindir}/ieee-copyout
%{_bindir}/latex-mk
%dir %{_datadir}/latex-mk
%{_datadir}/latex-mk/*
%{_infodir}/%{name}*

