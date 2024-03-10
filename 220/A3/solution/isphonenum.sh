#!/bin/bash

number=$1
re='^[0-9]{3}[- ]?[0-9]{3}[- ]?[0-9]{4}$'

if [[ $number =~ $re ]]; then
    echo 1
else
    echo 0
fi