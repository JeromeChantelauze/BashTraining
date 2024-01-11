#!/bin/bash

awk 'NR >= 63 && NR <= 69 { origin = $6; print origin, " was repaced  by ith the letter: [A, U, T, O, M, A, T, I, O, N]" }' log.txt > change.log

gawk -i inplace 'NR < 63 { print $0 }
                 NR >= 63 && NR <= 69 { $6 = "AUTOMATION"; print $0 }
                 NR > 69 { print $0 }' log.txt

exit 0
