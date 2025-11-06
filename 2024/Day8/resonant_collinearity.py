from collections import defaultdict

filename = "Day8/test_input.txt"


map = []
antenna_type = []
antenna_positons_by_type = defaultdict(lambda: [])
with open(filename, 'r') as file:
    for line in file:
        line_list = list(line)
        map.append(line_list)
        antenna_on_line = 
