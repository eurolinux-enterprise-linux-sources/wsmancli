Name:           wsmancli
Version:        2.3.0
Release:        4%{dist}
License:        BSD
Url:            http://www.openwsman.org/
Source:         http://downloads.sourceforge.net/project/openwsman/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1:        COPYING
Source2:        README
Source3:        AUTHORS
Group:          Applications/System
BuildRequires:  openwsman-devel >= 2.1.0 pkgconfig curl-devel
Requires:       openwsman curl
Patch0:         missing-pthread-symbols.patch
Summary:        WS-Management-Command line Interface

%description
Command line interface for managing 
systems using Web Services Management protocol.

%prep
%setup -q 
%patch0 -p1
cp -fp %SOURCE1 %SOURCE2 %SOURCE3 .;

%build
%configure --disable-more-warnings 
make %{?_smp_flags}

%install
make DESTDIR=%{buildroot} install

%files
%{_bindir}/wsman
%{_bindir}/wseventmgr
%doc COPYING README AUTHORS

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 2.3.0-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.3.0-3
- Mass rebuild 2013-12-27

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.3.0-1
- Update to wsmancli-2.3.0

* Tue Sep 18 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.7.1-3
- Fix issues found by fedora-review utility in the spec file

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.7.1-1
- Update to wsmancli-2.2.7.1

* Wed Mar 23 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.5-1
- Update to wsmancli-2.2.5

* Tue Feb 22 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.4-3
- Fix option issue on big endian architectures

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.4-1
- Update to wsmancli-2.2.4

* Wed Mar  3 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.3-1
- Update to wsmancli-2.2.3

* Mon Jan 25 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.0-5
- Fix Source URL
- Use tarball from upstream
- Add COPYING, README and AUTHORS to sources (previously placed in the modified tarball)

* Fri Nov  6 2009 Praveen K Paladugu <praveen_paladugu@dell.com> - 2.1.0-4
- Missing symbols from pthread library.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Tue Sep 30 2008  <srinivas_ramanatha@dell.com> - 2.1.0-1%{?dist}
- Modified the spec file to adhere to fedora packaging guidelines.

