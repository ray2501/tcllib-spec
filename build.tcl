#!/usr/bin/tclsh

set arch "x86_64"
set base "tcllib-2.0"
set fileurl "https://core.tcl-lang.org/tcllib/uv/tcllib-2.0.tar.xz"

set var [list curl -L $fileurl -o $base.tar.xz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.xz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcllib.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete $base.tar.xz
