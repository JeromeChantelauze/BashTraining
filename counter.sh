#!/bin/bash

Pattern=$1
File=$2

Count=0


grep $Pattern $File | while read Line; do
	while echo "$Line" | grep $Pattern &> /dev/null; do
		Count=$(( Count  + 1 ))
		Line=$(echo "$Line" | sed -e "s/$Pattern//")
		echo "Count=$Count" > tmp
	done
done

. tmp
rm tmp

echo $Count

exit 0

