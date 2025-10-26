import re

def import_map(filename):
    map = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            map.append(list(line))
    return map

def find_last_occurrence(lst, value):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == value:
            return i
    return None

def detect_cycle_start(my_list, min_pattern_length=1):
    """
    Detects if the end of the list contains a repeating pattern.
    Returns the index where the cycle starts, or None if no cycle detected.
    """
    list_len = len(my_list)
    

    for pattern_length in range(min_pattern_length, list_len // 2 + 1):

        if list_len < pattern_length * 2:
            continue
        
        last_pattern = my_list[-pattern_length:]
        previous_pattern = my_list[-2*pattern_length:-pattern_length]
        
        if last_pattern == previous_pattern:
            if list_len >= pattern_length * 3:
                third_pattern = my_list[-3*pattern_length:-2*pattern_length]
                if third_pattern == last_pattern:
                    cycle_start = list_len - 3 * pattern_length
                    return cycle_start, pattern_length
            else:
                cycle_start = list_len - 2 * pattern_length
                return cycle_start, pattern_length
    
    return None, None

def map_roam_by_guard(map):

    guard_coordinates = [0,0]
    guard_rep = '^'

    for i in range(len(map)):
        if guard_rep in map[i]:
            guard_coordinates[0] = i
            guard_coordinates[1] = map[i].index(guard_rep)
            break

    continue_roaming = True
    number_of_explored_positions = 1
    loop_identifier = []
    cycle_start = None 
    pattern_length = None

    while(continue_roaming):
        next_move = ''
        if guard_rep == '^':
            if guard_coordinates[0] == 0:
                break
            else:
                trajectory = [row[guard_coordinates[1]] for row in map]
                if '#' in trajectory[0:guard_coordinates[0]]:
                    index_obstacle = find_last_occurrence(trajectory[0:guard_coordinates[0]], '#')
                    number_of_explored_pos_in_trajectory = trajectory[index_obstacle + 1:guard_coordinates[0]].count('X')
                    number_of_explored_positions += (len(trajectory[index_obstacle + 1:guard_coordinates[0]]) - number_of_explored_pos_in_trajectory)

                    next_move = str(len(trajectory[index_obstacle + 1:guard_coordinates[0]])) + 'u'

                    for i in range(index_obstacle + 1, guard_coordinates[0] + 1):
                        if map[i-1][guard_coordinates[1]] == '#':
                            guard_rep = '>'
                            map[i][guard_coordinates[1]] = guard_rep
                        else:
                            map[i][guard_coordinates[1]] = 'X'
                    guard_coordinates[0] = index_obstacle + 1

                    
                else:
                    number_of_explored_pos_in_trajectory = trajectory[0:guard_coordinates[0]].count('X')
                    number_of_explored_positions += (len(trajectory[0:guard_coordinates[0]]) - number_of_explored_pos_in_trajectory)

                    next_move = str(len(trajectory[0:guard_coordinates[0]])) + 'u'

                    for i in range(0, guard_coordinates[0] + 1):
                        if i == 0:
                            guard_rep = '^'
                            map[i][guard_coordinates[1]] = guard_rep
                        else:
                            map[i][guard_coordinates[1]] = 'X'
                    guard_coordinates[0] = 0
                    
        elif guard_rep == '>':
            if guard_coordinates[1] == len(map[0]) - 1:
                break
            else:
                trajectory = map[guard_coordinates[0]]
                if '#' in trajectory[guard_coordinates[1] + 1:]:
                    index_obstacle = trajectory[guard_coordinates[1] + 1:].index('#') + guard_coordinates[1] + 1
                    number_of_explored_pos_in_trajectory = trajectory[guard_coordinates[1] + 1:index_obstacle].count('X')
                    number_of_explored_positions += (len(trajectory[guard_coordinates[1] + 1:index_obstacle]) - number_of_explored_pos_in_trajectory)

                    next_move = str(len(trajectory[guard_coordinates[1] + 1:index_obstacle])) + 'r'

                    for i in range(guard_coordinates[1], index_obstacle):
                        if map[guard_coordinates[0]][i+1] == '#':
                            guard_rep = 'v'
                            map[guard_coordinates[0]][i] = guard_rep
                        else:
                            map[guard_coordinates[0]][i] = 'X'
                    guard_coordinates[1] = index_obstacle - 1
                else:
                    number_of_explored_pos_in_trajectory = trajectory[guard_coordinates[1] + 1:].count('X')
                    number_of_explored_positions += (len(trajectory[guard_coordinates[1] + 1:]) - number_of_explored_pos_in_trajectory)
                    
                    next_move = str(len(trajectory[guard_coordinates[1] + 1:])) + 'r'
                    for i in range(guard_coordinates[1], len(trajectory)):
                        if i == len(trajectory) - 1:
                            guard_rep = '>'
                            map[guard_coordinates[0]][i] = guard_rep
                        else:
                            map[guard_coordinates[0]][i] = 'X'
                    guard_coordinates[1] = len(trajectory) - 1
                    
        elif guard_rep == 'v':
            if guard_coordinates[0] == len(map) - 1:
                break
            else:
                trajectory = [row[guard_coordinates[1]] for row in map]
                if '#' in trajectory[guard_coordinates[0] + 1:]:
                    index_obstacle = trajectory[guard_coordinates[0] + 1:].index('#') + guard_coordinates[0] + 1
                    number_of_explored_pos_in_trajectory = trajectory[guard_coordinates[0] + 1:index_obstacle].count('X')
                    number_of_explored_positions += (len(trajectory[guard_coordinates[0] + 1:index_obstacle]) - number_of_explored_pos_in_trajectory)

                    next_move = str(len(trajectory[guard_coordinates[0] + 1:index_obstacle])) + 'd'

                    for i in range(guard_coordinates[0], index_obstacle):
                        if map[i+1][guard_coordinates[1]] == '#':
                            guard_rep = '<'
                            map[i][guard_coordinates[1]] = guard_rep
                        else:
                            map[i][guard_coordinates[1]] = 'X'
                    guard_coordinates[0] = index_obstacle - 1
                else:
                    number_of_explored_pos_in_trajectory = trajectory[guard_coordinates[0] + 1:].count('X')
                    number_of_explored_positions += (len(trajectory[guard_coordinates[0] + 1:]) - number_of_explored_pos_in_trajectory)

                    next_move = str(len(trajectory[guard_coordinates[0] + 1:])) + 'd'

                    for i in range(guard_coordinates[1], len(trajectory)):
                        if i == len(trajectory) - 1:
                            guard_rep = 'v'
                            map[i][guard_coordinates[1]] = guard_rep
                        else:
                            map[i][guard_coordinates[1]] = 'X'
                    guard_coordinates[0] = len(trajectory) - 1

        elif guard_rep == '<':
            if guard_coordinates[1] == 0:
                break
            else:
                trajectory = map[guard_coordinates[0]]
                if '#' in trajectory[0:guard_coordinates[1]]:
                    index_obstacle = find_last_occurrence(trajectory[0:guard_coordinates[1]], '#')
                    number_of_explored_pos_in_trajectory = trajectory[index_obstacle + 1:guard_coordinates[1]].count('X')
                    number_of_explored_positions += (len(trajectory[index_obstacle + 1:guard_coordinates[1]]) - number_of_explored_pos_in_trajectory)

                    next_move = str(len(trajectory[index_obstacle + 1:guard_coordinates[1]])) + 'l'

                    for i in range(index_obstacle + 1, guard_coordinates[1] + 1):
                        if map[guard_coordinates[0]][i-1] == '#':
                            guard_rep = '^'
                            map[guard_coordinates[0]][i] = guard_rep
                        else:
                            map[guard_coordinates[0]][i] = 'X'
                    guard_coordinates[1] = index_obstacle + 1
                else:
                    number_of_explored_pos_in_trajectory = trajectory[0:guard_coordinates[1]].count('X')
                    number_of_explored_positions += (len(trajectory[0:guard_coordinates[1]]) - number_of_explored_pos_in_trajectory)

                    next_move = str(len(trajectory[index_obstacle + 1:guard_coordinates[1]])) + 'l'

                    for i in range(0, guard_coordinates[1] + 1):
                        if i == 0:
                            guard_rep = '<'
                            map[guard_coordinates[0]][i] = guard_rep
                        else:
                            map[guard_coordinates[0]][i] = 'X'
                    guard_coordinates[1] = 0
        
        loop_identifier.append(next_move)
        cycle_start, pattern_length = detect_cycle_start(loop_identifier)

        if cycle_start is not None:
            break

    return number_of_explored_positions, map, pattern_length

def create_loop_in_map(filename):
    test_map = import_map(filename=filename)
    number_of_explored_positions, initially_complete_map, pattern_length = map_roam_by_guard(test_map)

    number_of_potential_loop = 0
    new_obstacle_pos = []

    for i in range(len(initially_complete_map)):
        potential_guard_pos = [j for j, x in enumerate(initially_complete_map[i]) if x == 'X' or x == '<' or x == '>' or x == '^' or x == 'v']
        for pos in potential_guard_pos:
            test_map_i = import_map(filename=filename)
            test_map_i[i][pos] = '#'
            number_of_explored_positions_i, new_complete_map, new_pattern_length = map_roam_by_guard(test_map_i)
            if new_pattern_length is not None:
                
                number_of_potential_loop += 1
                new_obstacle_pos.append([i, pos])
    
    return number_of_potential_loop, new_obstacle_pos


map =  import_map('Day6/input.txt')
number_of_explored_positions, completed_map, pattern_length = map_roam_by_guard(map)
print("Number of explored positions by the guard:", number_of_explored_positions)


number_of_potential_loop, new_obstacle_pos = create_loop_in_map('Day6/input.txt')
print("Number of possible positions for obstruction:", number_of_potential_loop)

print(new_obstacle_pos)


