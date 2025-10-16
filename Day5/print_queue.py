import re
from collections import defaultdict
from functools import cmp_to_key

def clean_input_file(filename):
    updates = []
    pages_order_rules = defaultdict(lambda: {'l': [], 'r': []})
    pattern = r'\d{2}\|\d{2}'

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove newline characters
            if re.match(pattern, line): 
                pages_number = line.split('|')
                x,y = int(pages_number[0]), int(pages_number[1])
                pages_order_rules[x]['r'].append(y)
                pages_order_rules[y]['l'].append(x)
            elif not line.strip() == '':
                updates_pages = line.split(',')
                updates.append([int(page) for page in updates_pages])

    return pages_order_rules, updates

def valid_pages_order(pages_order_rules, updates):
    valid_updates = []
    corrected_updates = []

    def compare_order(x,y):
        if x in pages_order_rules and y in pages_order_rules[x]['l']:
            return 1
        elif x in pages_order_rules and y in pages_order_rules[x]['r']:
            return -1
        else:
            return 0

    for update in updates:
        right_order = True
        for i in range(len(update)):
            if update[i] in pages_order_rules.keys():
                if any(page in update[:i] for page in pages_order_rules[update[i]]['r']) or any(page in update[i:] for page in pages_order_rules[update[i]]['l']):
                    right_order = False
                    break
        if right_order:
            valid_updates.append(update)
        else:
            corrected_update = sorted(update, key=cmp_to_key(compare_order))
            corrected_updates.append(corrected_update)
    return valid_updates, corrected_updates



def sum_middle_pages_number(pages_order_rules, updates):
    valid_updates, corrected_updates = valid_pages_order(pages_order_rules, updates)
    sum_middle_pages_valid_updates = 0
    sum_middle_pages_corrected_updates = 0
    for update in valid_updates:
        sum_middle_pages_valid_updates += update[len(update) // 2]
    for update in corrected_updates:
        sum_middle_pages_corrected_updates += update[len(update) // 2]
    return sum_middle_pages_valid_updates, sum_middle_pages_corrected_updates
                

pages_order_rules, updates = clean_input_file("Day5/input.txt")
valid_updates, corrected_updates = valid_pages_order(pages_order_rules, updates)
sum_middle_pages_valid_updates, sum_middle_pages_corrected_updates = sum_middle_pages_number(pages_order_rules, updates)
print("Sum of middle pags number for valid updates:", sum_middle_pages_valid_updates)
print("Sum of middle pages number for corrected updates:", sum_middle_pages_corrected_updates)
