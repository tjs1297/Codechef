# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 01:02:10 2019

@author: Tejasvi Sharma
"""

#!/usr/bin/python3

def reverse_indexed_map(myList):
    map_of_values = {}
    for index,val in enumerate(myList):
        if val not in map_of_values.keys():
            map_of_values[val] = [index]
        else:
            map_of_values[val] += [index]
    return map_of_values

def number_of_triplets(indexed_values):
    num = 0
    if(0 in indexed_values.keys()):
        indexed_values[0]+=[-1]

    for key, indices_list in indexed_values.items():
        indices_list.sort(reverse=True)
        length = len(indices_list)-1
        l = len(indices_list)
        for i in indices_list:
            num += (length*i)
            length -=2
        num -= int((l*(l-1))/2)
    return num

try:
    tests = int(input())
except:
    quit()

while(tests!=0):
    print(tests)
    number_of_integers = int(input())
    input_list = [int(x) for x in input().split()]
    for index, val in enumerate(input_list):
        if(index==0):
            continue
        else:
            input_list[index] = input_list[index-1]^(val)
    temp = reverse_indexed_map(input_list)
    answer = number_of_triplets(temp)
    print(answer)
    tests-=1
