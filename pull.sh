#!/bin/bash

URL="git@github.com:USER/REPOSITORY.git"
DST_FILES=()
DST_FILES[0]="FROM TO"
DST_FILES[1]="FROM2 TO2"

rm -rf "pull/"
git clone $URL "pull/"
for i in "${DST_FILES[@]}"; do
	args=($i)

	rm -rf "${args[1]}";
	cp -R "pull/${args[0]}" "${args[1]}";
	echo "Copied "$i;
done