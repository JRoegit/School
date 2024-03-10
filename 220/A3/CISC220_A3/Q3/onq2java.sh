#!/bin/bash

if [ $# -lt 1 ]; then
    echo "At least one fully qualified class name is required"
    exit 1
fi

for dir in */; do
    for arg in "$@"; do
        ./mkpkg.sh "$arg"
        if ! mv "${arg%%.*}" "$dir"; then
            rm -r "${arg%%.*}"
        fi 2>/dev/null
        file="${arg##*.}"
        tmp="${arg%.*}"
        path="${tmp//./\/}"
        cp "$dir/$file.java" "$dir/$path" 2>/dev/null
    done
done