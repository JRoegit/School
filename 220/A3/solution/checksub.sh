#!/bin/bash

specfile=$1
flag=0

if [[ $# -lt 1 ]]; then
    echo "Usage: checksub.sh specfile" >&2
    exit 1
fi

if [[ -r $specfile ]]; then
    :
else
    echo "$specfile is missing or could not be read" >&2
    exit 2
fi

while read line; do
    if [[ -f "$line" ]] || [[ -z "$line" ]] || [[ $line =~ ^[#] ]]; then
        :
    else
        echo "$line missing " >&2
        flag=1
    fi
done < "$specfile"

if (( flag == 0 )); then
    exit 0
else
    exit 3
fi