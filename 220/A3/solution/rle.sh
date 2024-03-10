#!/bin/bash

# Encodes the elements of the array arr storing the
# result in the array enc
encode() {
    enc=()
    n=${#arr[@]}
    if [[ $n -gt 0 ]]; then  
        start=0
        val=${arr[$start]}
        finished=0
        while ((finished == 0)); do
            fin=$(next $start)
            if [[ $fin =~ ^[-][1]$ ]]; then
                fin=$n
                finished=1
            fi
            (( count = fin - start ))       
            enc+=("$count" "$val")
            start=$fin
            val=${arr[$start]}           
        done
    fi
}

# Finds the index of the next element in arr that is
# different (not equal to) from the element located at the
# specified starting index; e.g.,
#
# next 3
#
# finds the index of the next element in arr that is not
# equal to the element at the starting index 3.
#
# The value of the found index is always greater than the
# specified index, or is -1 if all of the remaining
# elements in arr starting from the specified index are equal.
#
# The found index is printed to standard output.
next() {
    index=$1
    len=${#arr[@]}
    for (( i = index + 1; i <= len; i++ )); do
    if ((i == len)) ; then #checks if fin of array
        echo "-1"
        return 0
    elif [[ "${arr[i-1]}" != "${arr[i]}" ]]; then
        echo $i
        return 0
    fi
done
}


# create array arr from command line arguments
arr=("$@")
# encode the array
encode

# print elements of enc on one line with one space between elements
echo "${enc[@]}"