#!/bin/bash

BASE_TEMPLATE=template.py
YEAR=2016

# session.cookie must contain the cookie for adventofcode.com in Netscape format

day=$1

if [ -f $day.py ]; 
    then echo "Error: file $day.py exists!";
elif ! [[ "$day" =~ ^[0-9]+ ]] ;
    then echo "Error: \"$day\" is not an integer!";
else
    cp $BASE_TEMPLATE $day.py;
    sed -i s/CURRENT_DAY/$day/g $day.py;
    chmod u+x $day.py;
    touch inputs/sample_$day;
    wget --load-cookies=session.cookie http://adventofcode.com/$YEAR/day/$day/input -O inputs/input_$day;
fi
