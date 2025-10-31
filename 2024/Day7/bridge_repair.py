import re
from collections import defaultdict


def extract_calibrations(filename):
    calibrations = defaultdict(lambda: [])
    with open(filename, 'r') as file:
        for line in file:
            str = line.strip()
            lst = re.split(':| ', str)
            key = lst.pop(0)
            calibrations[int(key)] = [int(num) for num in lst if num != '']
    
    return calibrations

def concatOp(a, b):
    return int( str(a) + str(b) )

def determine_true_calibration(value, variables):

    copy_variables = [x for x in variables]
    explored_nodes = [(copy_variables.pop(0), 0)]

    

    while (value not in [i[0] for i in explored_nodes] or len(copy_variables) not in [i[1] for i in explored_nodes if i[0] == value]) and explored_nodes:
        node_to_expand = explored_nodes.pop(0)
        
        if node_to_expand[1] < len(copy_variables):
            explored_nodes.append((node_to_expand[0] + copy_variables[node_to_expand[1]], node_to_expand[1] + 1))
            explored_nodes.append((node_to_expand[0] * copy_variables[node_to_expand[1]], node_to_expand[1] + 1))
            explored_nodes.append((concatOp(node_to_expand[0], copy_variables[node_to_expand[1]]), node_to_expand[1] + 1))

        for nodes in explored_nodes:
            if nodes[0] > value:
                explored_nodes.remove(nodes)
        
        explored_nodes.sort(key=lambda i: (i[1], i[0]), reverse=True)
    
    if value in [i[0] for i in explored_nodes]:
        return True
    else:
        return False
    

def count_valid_calibrations(filename):
    count = 0
    calibrations = extract_calibrations(filename)
    sum_values = 0

    for value in calibrations.keys():
        if determine_true_calibration(value=value, variables=calibrations[value]):
            count += 1
            sum_values += value
    
    return count, sum_values



filename = "Day7/input.txt"
number_valid_calibrations, sum_of_values = count_valid_calibrations(filename)
print("Number of valid calibrations: ", number_valid_calibrations)
print("Sum of factors of those calibrations: ", sum_of_values)



