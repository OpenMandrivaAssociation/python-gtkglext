%define	libname		pygtkglext
%define	name		python-gtkglext
%define	version		1.1.0
%define	release		%mkrel 9

Summary:	Python bindings for GtkGLExt
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		System/Libraries
URL:		http://www.k-3d.org/gtkglext/Main_Page
Source:		http://prdownloads.sourceforge.net/sourceforge/gtkglext/%{libname}-%{version}.tar.bz2
BuildRoot:	%_tmppath/%{name}-%{version}
Requires:	gtkglext, python-opengl
BuildRequires:	gtkglext-devel
BuildRequires:  pygtk2.0-devel
%py_requires
 
%description
Python bindings for GtkGTLExt

%prep
%setup -q -n %{libname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%if %_lib != lib
mv %buildroot%py_puresitedir/gtk-2.0/gtk/gdkgl/* %buildroot%py_platsitedir/gtk-2.0/gtk/gdkgl/
mv %buildroot%py_puresitedir/gtk-2.0/gtk/gtkgl/* %buildroot%py_platsitedir/gtk-2.0/gtk/gtkgl/
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING COPYING.LIB INSTALL README README.win32 examples/
%python_sitearch/gtk-2.0/gtk/gtkgl
%python_sitearch/gtk-2.0/gtk/gdkgl
%{_datadir}/pygtk/2.0/defs/*
%_libdir/pkgconfig/*.pc


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-8mdv2011.0
+ Revision: 667935
- mass rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-7mdv2011.0
+ Revision: 523818
- rebuilt for 2010.1

* Tue May 19 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1.0-6mdv2010.0
+ Revision: 377628
- Drop useless calls to autoreconf

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 1.1.0-6mdv2009.1
+ Revision: 318907
- rebuild for new python

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.1.0-5mdv2009.0
+ Revision: 219569
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 27 2007 Funda Wang <fwang@mandriva.org> 1.1.0-4mdv2008.0
+ Revision: 71845
- Rebuild to fix dir inclusion


* Thu Dec 07 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.1.0-3mdv2007.0
+ Revision: 91904
- move more files on x86_64
- fix file list on x86_64
- rebuild
- Import python-gtkglext

* Wed Dec 06 2006 Götz Waschk <waschk@mandriva.org> 1.1.0-1mdv2007.1
- fix build and installation
- new version

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.1-3mdk
- buildrequires fix

* Sat May 14 2005 Michael Scherer <misc@mandriva.org> 1.0.1-2mdk
- from Tigrux <tigrux@ximian.com> 
  - Do not require python = 2.5
  - Patch to enable compilation with dsextras of pygtk 2.6.2

* Mon Dec 06 2004 Tigrux <tigrux@ximian.com> 1.0.1-1mdk
- First rpm for Mandrake

