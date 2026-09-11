#!/bin/bash
echo "choose the number of files"
read N
for i in $( seq 0 $N)
do 
	cd 
	cd Desktop
	cd mikl
	touch file$i.txt
	a=$RANDOM
	b=$RANDOM
	c=$(( $a+$b ))
	echo $a+$b=$c > file$i.txt
done

