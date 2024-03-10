# Name: Jacob Roe
# Student Num : 20351389
# I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity

import random

class Node:
    def __init__(self, val):
        self.val = val       #Value of node
        self.left = None     #Left child node  
        self.right = None    #right child node

class Tree:
    def __init__(self,array : list):   
        self.root = self.array_to_tree(array,0,len(array) - 1) 

    def print_tree(self,n : Node): #Print the tree (Testing purposes)
        if(n != None):
            self.print_tree(n.left)
            print(n.val)
            self.print_tree(n.right)

    def array_to_tree(self,array,start,end): #Recursively builds and balances the tree 
        if (start > end):
            return
        mid = (start + end) // 2
        root = Node(array[mid])

        root.left = self.array_to_tree(array,start,mid-1)
        root.right = self.array_to_tree(array,mid + 1, end)

        return root
    
    def insert(self,x): #Insert element based off lecture example
        self.root = self.rec_insert(self.root,x)

    def rec_insert(self,current : Node,x): #Insert element recursively based off lecture example
        if (current == None):
            current = Node(x)
        elif(current.val >= x):
            current.left = self.rec_insert(current.left,x)
        else:
            current.right = self.rec_insert(current.right,x)
        return current

    def height(self, n : Node): #Recursively finds the height of the tree
        if (n == None):
            return 0
        else: 
            left = self.height(n.left)
            right = self.height(n.right)
            return 1 + max(left,right)

    def total_height(self, n : Node): #Recursively finds the sum of all of the heights of all of the nodes in the tree
        if (n == None):
            return 0  
        else:
            return (self.total_height(n.left) + self.height(n) + self.total_height(n.right)) 

def randarray(n): #Generates an array from 1...n and randomizes its order
    array = list(range(1,n))
    random.shuffle(array)
    return array

def main(): #Part 2
    for n in [100,200,300,400,500,600,700,800,900,1000]:
        average_height = 0
        for x in range(500):
            array = randarray(n)
            tree = Tree(array)
            average_height += tree.height(tree.root)
        average_height /= 500
        print(f"Average height for n={n} is {average_height}")

main()