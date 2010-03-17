%define	libname		pygtkglext
%define	name		python-gtkglext
%define	version		1.1.0
%define	release		%mkrel 7

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
