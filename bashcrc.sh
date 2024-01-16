#!/bin/bash

grep "=" bashcrc.txt | while read LINE; do
	while ! echo $LINE | grep "^[0-9_A-Z]*=" &> /dev/null; do
		LINE=$(echo "$LINE" | sed -e "s/.[^ ]* //")
	done

	VAR=$(echo $LINE | sed -e "s/\(^[0-9_A-Z]*\)=.*$/\1/")
	VAL=$(echo $LINE | sed -e "s/.*=//")

	sed -i -e "s|\(^[^#].*$VAR=\).*$|\1$VAL|" bashcrc
done
