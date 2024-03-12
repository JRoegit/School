"""
Name : Jacob Roe
Student Number : 20351389
I confirm that this submission is my own work and is consistent
with the Queen's regulations on Academic Integrity.
"""
import random
import string
import math

global const1
global const2 
global T
global tableSize
global insertionAvg

insertionAvg = []
tableSize = 2050
T = [None] * tableSize
const1 = 3
const2 = 0.33

"""
Computes index using a constant c that is the length of the codename, 
as well as the numerical value of the character being computed. 
"""
def part_1(k): #k is a string
    index = 0
    c = len(k)
    for x in k:
        index = index * c + ord(x)
    return index % tableSize

"""
For c1 = 1, c2 = 1,     a tablesize of 2125 works w avg ~2.5 comps
For c1 = 2, c2 = 0.5,   a tablesize of 2075 works w avg ~3.2 comps
For c1 = 3, c2 = 0.33,  a tablesize of 2025 works w avg ~3.8 comps
"""
def part_2(k):
    i = 0
    h1 = part_1(k)
    while (i < tableSize) :
        index = int((h1 + const1*i + const2*i**2) % tableSize)
        if (T[index] == k):
            print("Attempt to insert duplicate key")
            break
        elif(T[index] == None):
            T[index] = k
            break
        else:
            i += 1
    insertionAvg.append(i)
    if (i == tableSize):
        print("Table full")

"""
For h' = h1, h" = h2,   A table size of 2500 provides an average of ~3 comps
For h' = h2, h" = h3,   A table size of 2050 provides an average of ~2.85 comps  
For h' = h1, h" = h3,   A table size of 2050 provides an average of ~2.8 comps
"""
def part_3_hash1(k): #sum all numerical values of each character multiplied by a constant
    hash = 0
    c = len(k)
    for x in k:
        hash = hash * c + ord(x)
    return hash % tableSize

def part_3_hash2(k): #multiply all numerical values of characters
    hash = 0
    for x in k:
        hash = hash + ord(x) * ord(x)
    return hash % tableSize

def part_3_hash3(k): #sum of square root of numerical values of characters squared
    hash = 0
    for x in k:
        hash = hash + math.sqrt(ord(x))
    return (hash * hash) % tableSize

def part_3(k):
    i = 0
    h1 = part_3_hash1(k)
    h2 = part_3_hash2(k)
    h3 = part_3_hash3(k)
    while (i < tableSize) :
        index = int((h1 + h3*i) % tableSize)
        if (T[index] == k):
            print("Attempt to insert duplicate key")
            break
        elif(T[index] == None):
            T[index] = k
            break
        else:
            i += 1
    insertionAvg.append(i)
    if (i == tableSize):
        print("Table full")

def main():
    codenames = []
    for x in range(1000): 
        w = ''.join(random.choice(string.ascii_letters) for i in range(8)) # 1000 length 8's
        codenames.append(w) #does not need to save them...
        print(w)
        part_3(w)
        w = ''.join(random.choice(string.ascii_letters) for i in range(7)) # 1000 length 7's
        codenames.append(w) #not needed
        print(w)
        part_3(w)
    
   

    for x in T:
        print(x)
    print("Number of codenames inserted:",tableSize - T.count(None))
    print("Average number of comparisons:", sum(insertionAvg) / len(insertionAvg))
main()