Summary:	KIso - which makes it easy to extract, create and manipulate ISO-Images
Name:		kiso
Version:	0.8.3
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/kiso/%{name}-%{version}.tar.gz
# Source0-md5:	6f32662f5c1ade8df9b6a76b7403cede
URL:		http://kiso.sourceforge.net/
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libcdio-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KIso is a graphical user interface for KDE which has the purpose to
make it as easy as possible to:
- Open ISO and NRG images.
- Create an ISO image from CD.
- Easy and convenient creation of own ISO images.
- Convert NRG to ISO images.
- Convert BIN/CUE to ISO images.
- Convert MDF to ISO images.
- Convert CDI to ISO images.
- Convert CCD/IMG to ISO images.
- Convert C2D to ISO images.
- Mount ISO/NRG images as virtual drive.
- Extract the content of an ISO/NRG image.
- Create bootable images.

%prep
%setup -q

%build
%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog Thanks\ to
%attr(755,root,root) %{_bindir}/kiso
%{_datadir}/apps/kiso
%{_datadir}/apps/konqueror/servicemenus/kiso_konqy.desktop
%{_datadir}/mimelnk/application/*.desktop
%{_desktopdir}/kiso.desktop
%{_iconsdir}/hicolor/*/*/*.png
