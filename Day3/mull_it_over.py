import re

def extract_corrupted_memory(filename):
    corrupted_memory = ""
    with open(filename, 'r') as file:
        for line in file:
            corrupted_memory += line

    return corrupted_memory

def sum_of_multiplications(corrupt_mem):
    pattern_mul = r'mul\(\d{1,3},\d{1,3}\)'
    matches_mul_occ = re.findall(pattern_mul, corrupt_mem)

    pattern_number_mul = r'mul\((\d{1,3}),(\d{1,3})\)'

    sum = 0
    
    for occ in re.finditer(pattern_number_mul, corrupt_mem):
        pairs = [g for g in occ.groups() if g]
        num1, num2 = pairs[0], pairs[1]
        mul = int(num1) * int(num2)
        sum += mul

    return sum

def sum_of_multiplications_with_conditions(corrupt_mem):
    condition = r'do\(\)|don\'t\(\)'

    pattern_number_mul = r'mul\((\d{1,3}),(\d{1,3})\)'

    sum = 0
    starting_index = []
    last_condition = []

    for occ in re.finditer(pattern_number_mul, corrupt_mem):
        starting_index.append(occ.start())
        if len(starting_index) == 1:
            sub_corrupt_txt = corrupt_mem[0: starting_index[-1]]
        else:
            sub_corrupt_txt = corrupt_mem[starting_index[-2]: starting_index[-1]]
        
        find_conditons_occurences = re.findall(condition, sub_corrupt_txt)
        if len(starting_index) == 1 and len(find_conditons_occurences) == 0:
            last_condition.append(1)
        elif len(starting_index) > 1 and len(find_conditons_occurences) == 0:
            last_condition.append(last_condition[-1])
        else:
            if find_conditons_occurences[-1] == "do()":
                last_condition.append(1)
            else:
                last_condition.append(0)

        if last_condition[-1]:
            pairs = [g for g in occ.groups() if g]
            num1, num2 = pairs[0], pairs[1]
            mul = int(num1) * int(num2)
            sum += mul
    return sum


corrupted_memmory = extract_corrupted_memory("Day3/input.txt")
sum_of_mul_memory = sum_of_multiplications_with_conditions(corrupted_memmory)
print(sum_of_mul_memory)
    