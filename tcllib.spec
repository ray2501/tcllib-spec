#
# spec file for package tcllib
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           tcllib
Url:            http://tcllib.sf.net
BuildRequires:  tcl
Version:        1.20
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Tcl Standard Library
License:        TCL
Group:          Development/Libraries/Tcl
BuildRequires:  ed
Requires:       /bin/sh
BuildArch:      noarch
Source0:        %name-%version.tar.gz
Source1:        %name-rpmlintrc

%description
This package is intended to be a collection of Tcl packages that
provide utility functions useful to a large collection of Tcl
programmers.

%prep
%setup -q
# upstream typo
chmod 644 examples/mapproj/ncar780.txt

# fix DOS lineendings
ed -s modules/math/kruskal.tcl 2>/dev/null <<'EOF'
,s/$//
w
EOF
# remove shebang from module
ed -s modules/pki/pki.tcl 2>/dev/null <<'EOF'
1g/^#!/d
w
EOF
# do not use /usr/bin/env in shebang
for script in examples/logger/logtofile.tcl examples/logger/logtotext.tcl \
        modules/stringprep/tools/gen_stringprep_data.tcl \
        examples/ldap/ldifdump modules/stringprep/tools/gen_unicode_data.tcl apps/pt apps/tcldocstrip apps/nnsd apps/nns apps/nnslog apps/dtplite apps/page; do
    ed -s "${script}" 2>/dev/null <<'EOF'
1s/^#! *\/usr\/bin\/env */#!\/usr\/bin\//
w
EOF
done

sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/csv/*
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/ftp/*
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/ftpd/*
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/irc/*
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/ldap/*
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/mapproj/*
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/math/*
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/mime/mbot/*.tcl
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/nntp/*
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/oreilly-oscon2001/*
sed -i 's/\/usr\/bin\/env tclsh/\/usr\/bin\/tclsh/' examples/term/*

%build

%install
tclsh ./installer.tcl -no-examples -no-html \
 -app-path   %buildroot/%_bindir \
 -pkg-path   %buildroot/%_datadir/tcl/%name%version \
 -nroff-path %buildroot%_mandir/mann \
 -no-wait -no-gui

%files
%defattr(-,root,root)
%doc license.terms ChangeLog
%doc support/releases/history/README-*
%_datadir/tcl
%_bindir/*
%doc examples
%doc %_mandir/mann/*

%changelog

