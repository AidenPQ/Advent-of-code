import numpy as np
import re

def decipher_file(filename):
    # Take the input file and transform it into 2 list corresponding to each column of the file
    
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            ln = re.split(' |\n', line)
            ln = [el for el in ln if el != '']
            left_list.append(int(ln[0]))
            right_list.append(int(ln[1]))

    return left_list, right_list

def distance_list(list1, list2):
    left_list = sorted(list1)
    right_list = sorted(list2)
    dist = 0

    if len(left_list) != len(right_list):
        raise IndexError
    else:
        for i in range(len(left_list)):
            dist += abs(left_list[i] - right_list[i])
    return dist

def similarity_list(list1, list2):
    sim = 0
    
    for i in range(len(list1)):
        sim += list2.count(list1[i]) * list1[i]

    return(sim)


left_list, right_list = decipher_file("Day1/input.txt")
distance = distance_list(list1=left_list, list2=right_list)
similarity = similarity_list(list1=left_list, list2=right_list)
print("Distance between the two lists:", distance)
print("Similarity between the two lists:", similarity)

