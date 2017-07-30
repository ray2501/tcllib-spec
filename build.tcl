#!/usr/bin/tclsh

set arch "noarch"
set base "tcllib-1.18"
set fileurl "https://sourceforge.net/projects/tcllib/files/tcllib/1.18/tcllib-1.18.tar.gz/download"

set var [list wget $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force tcllib-rpmlintrc build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcllib.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete $base.tar.gz
