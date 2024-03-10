#!/usr/bin/env bash

# mkpkg.sh fully-qualified-class-name
#
# Creates the package directory structure for a fully qualified
# Java class name. Assumes that the fully qualified class name
# is in fact a legal class name.


# fully qualified class name
qname=$1

# does the fully qualified class name contain a package?
if [[ $qname =~ [.] ]]; then
    # yes, get package name
    pkg=${qname%.*}
else
    # no, no package name
    pkg=""
fi

# make package directories in the current working directory
if [[ -n $pkg ]]; then
    # replace . with /
    dir=${pkg//[.]//}
    mkdir -p $dir
fi