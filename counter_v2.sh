#!/bin/bash

Pattern=$1
shift

for File in $@; do

	if grep "$Pattern" $File &> /dev/null; then
		echo
		echo $File
		echo
		grep "$Pattern" $File
	fi
done


exit 0

