%define	libname		pygtkglext

Summary:	Python bindings for GtkGLExt
Name:		python-gtkglext
Version:	1.1.0
Release:	11
License:	BSD
Group:		System/Libraries
URL:		http://www.k-3d.org/gtkglext/Main_Page
Source:		http://prdownloads.sourceforge.net/sourceforge/gtkglext/%{libname}-%{version}.tar.bz2
Requires:	gtkglext, python-opengl
BuildRequires:	gtkglext-devel
BuildRequires:  pygtk2.0-devel
BuildRequires:  python-devel
 
%description
Python bindings for GtkGTLExt

%prep
%setup -q -n %{libname}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
%if %_lib != lib
mv %{buildroot}%{py_puresitedir}/gtk-2.0/gtk/gdkgl/* %{buildroot}%{py_platsitedir}/gtk-2.0/gtk/gdkgl/
mv %{buildroot}%{py_puresitedir}/gtk-2.0/gtk/gtkgl/* %{buildroot}%{py_platsitedir}/gtk-2.0/gtk/gtkgl/
%endif

%files
%doc AUTHORS ChangeLog COPYING COPYING.LIB INSTALL README README.win32 examples/
%{python_sitearch}/gtk-2.0/gtk/gtkgl
%{python_sitearch}/gtk-2.0/gtk/gdkgl
%{_datadir}/pygtk/2.0/defs/*
%{_libdir}/pkgconfig/*.pc

