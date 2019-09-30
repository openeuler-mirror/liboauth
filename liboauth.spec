Name:           liboauth
Version:        1.0.3
Release:        12
Summary:        OAuth library functions
License:        MIT
URL:            http://liboauth.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc curl-devel nss-devel

%description
a POSIX-C implementation of the http://oauth.net/ protocol. libOauth provides
functionality to encode URLs and sign HTTP request data according to the oAuth standard.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
Libraries and header files for developing applications.

%package	help
Summary:	help package for %{name} with man docs

%description	help
document files for %{name}

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure --disable-static --enable-nss
make


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING.MIT README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/oauth.pc

%files help
%{_mandir}/man3/oauth.*
%doc ChangeLog

%changelog
* Fri Sep 6 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.0.3-12
- Package init

