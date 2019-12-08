#!/bin/bash
foo="${1}/*i"
echo "$foo"

for file in $foo
do
    test -f "$file" || continue
    qsub ~/Serpent/scripts/bash/job.qsub "$file"
done
