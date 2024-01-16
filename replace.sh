#!/bin/bash

Count=63
AWK_S1=""
AWK=$AWK"NR < 63 { print \$0 }\n"

rm -f change.log && touch change,log

for Name in A U T O M A T I O N; do
	AWK=$AWK"NR ==$Count { origin = \$6;  \$6 = \"$Name\"; print origin, \" was repaced  by ith the letter $Name\" >> \"change.log\" ; print \$0 }\n"
	Count=$(( Count + 1 ))
done

AWK=$AWK"NR >= $Count { print \$0 }\n"

echo -e $AWK > /tmp/$$.awk
gawk -i inplace -f /tmp/$$.awk log.txt
#rm /tmp/$$.awk

exit 0
