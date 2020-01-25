%define		pkgname	pgettext
%define		php_min_version 4.2.0
Summary:	pgettext wrapper for php gettext
Name:		php-%{pkgname}
Version:	0.1
Release:	1
# assume MIT https://github.com/azatoth/php-pgettext/pull/1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/azatoth/php-pgettext/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	1b388f9379954a0156aeb7b9d322c38d
URL:		https://github.com/azatoth/php-pgettext
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
Requires:	php(gettext)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default installation of gettext in PHP lacks support for pgettext et
al. This PHP script adds support for those, as well as an gettext_noop
wrapper.

Following functions are exported:
- pgettext($msg_ctxt, $msgid)
- dpgettext($domain, $msg_ctxt, $msgid)
- dcpgettext($domain, $msg_ctxt, $msgid, $category)
- npgettext($msg_ctxt, $msgid, $msgid_plural, $n)
- dnpgettext($domain, $msg_ctxt, $msgid, $msgid_plural, $n)
- dcnpgettext($domain, $msg_ctxt, $msgid, $msgid_plural, $n, $category)
- gettext_noop($msgid)

%prep
%setup -qc
mv %{name}-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p pgettext.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{php_data_dir}/pgettext.php
