"""
Name : Jacob Roe
Student Number : 20351389
I confirm that this submission is my own work and is consistent
with the Queen's regulations on Academic Integrity.
"""
import random
import string

global const1
global const2 
global T
global tableSize
global insertionAvg

insertionAvg = []
tableSize = 2150
T = [None] * tableSize
const1 = 1
const2 = 1

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
THESE ARE ALL SIZE 8 STRINGS
For c1 = 1, c2 = 1,     a tablesize of 2150 works w avg ~2.2 comps
For c1 = 2, c2 = 0.5,   a tablesize of 2075 works w avg ~3.2 comps
For c1 = 3, c2 = 0.33,  a tablesize of 2025 works w avg ~3.8 comps
"""
def part_2(k):
    i = 0
    v = part_1(k)
    while (i < tableSize) :
        index = int((v + const1*i + const2*i**2) % tableSize)
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

"""
def part_3(k):
    pass

def main():
    codenames = []
    for x in range(2000):
        w = ''.join(random.choice(string.ascii_letters) for i in range(8))
        codenames.append(w)
        print(w)
        part_2(w)
    print(len(codenames))

    for x in T:
        print(x)
    print("Number of codenames inserted:",tableSize - T.count(None))
    print("Average number of comparisons:", sum(insertionAvg) / len(insertionAvg))

main()