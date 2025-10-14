import re


def extract_word_search_txt(filename):
    word_search_text = []
    with open(filename, 'r') as file:
        for line in file:
            word_search_text.append(line)
    return word_search_text

def xmas_search(txt):
    number_of_columns = len(txt[0])
    number_of_lines = len(txt)

    number_of_word_occurence = 0

    for i in range(number_of_lines):
        for occ in re.finditer('X', txt[i]):
            y = occ.start()

            possible_words = []
            if y + 3 < number_of_columns:
                possible_words.append(txt[i][y]+ txt[i][y+1] + txt[i][y+2] + txt[i][y+3])
                if i + 3 < number_of_lines:
                    possible_words.append(txt[i][y]+ txt[i+1][y+1] + txt[i+2][y+2] + txt[i+3][y+3])
                if i - 3 >= 0:
                    possible_words.append(txt[i][y]+ txt[i-1][y+1] + txt[i-2][y+2] + txt[i-3][y+3])
            if y - 3 >= 0:
                possible_words.append(txt[i][y]+ txt[i][y-1] + txt[i][y-2] + txt[i][y-3])
                if i + 3 < number_of_lines:
                    possible_words.append(txt[i][y]+ txt[i+1][y-1] + txt[i+2][y-2] + txt[i+3][y-3])
                if i - 3 >= 0:
                    possible_words.append(txt[i][y]+ txt[i-1][y-1] + txt[i-2][y-2] + txt[i-3][y-3])
            if i + 3 < number_of_lines:
                possible_words.append(txt[i][y]+ txt[i+1][y] + txt[i+2][y] + txt[i+3][y])
            if i - 3 >= 0:
                possible_words.append(txt[i][y]+ txt[i-1][y] + txt[i-2][y] + txt[i-3][y])

            number_of_word_occurence += possible_words.count('XMAS')
    
    return number_of_word_occurence

def x_mas_search(txt):
    number_of_columns = len(txt[0])
    number_of_lines = len(txt)

    number_of_occurence = 0

    for i in range(1, number_of_lines - 1):
        for occ in re.finditer('A', txt[i]):
            y = occ.start()

            if y > 0 and y < number_of_columns - 1:
                if txt[i-1][y-1] == 'M' and txt[i-1][y+1] == 'M' and txt[i+1][y-1] == 'S' and txt[i+1][y+1] == 'S':
                    number_of_occurence += 1
                elif txt[i-1][y-1] == 'M' and txt[i-1][y+1] == 'S' and txt[i+1][y-1] == 'M' and txt[i+1][y+1] == 'S':
                    number_of_occurence += 1
                elif txt[i-1][y-1] == 'S' and txt[i-1][y+1] == 'M' and txt[i+1][y-1] == 'S' and txt[i+1][y+1] == 'M':
                    number_of_occurence += 1
                elif txt[i-1][y-1] == 'S' and txt[i-1][y+1] == 'S' and txt[i+1][y-1] == 'M' and txt[i+1][y+1] == 'M':
                    number_of_occurence += 1
    
    return number_of_occurence

word_search_txt = extract_word_search_txt('Day4/input.txt')
test_word_search_txt = ['MMMSXXMASM', 'MSAMXMSMSA', 'AMXSXMAAMM', 'MSAMASMSMX', 'XMASAMXAMM', 'XXAMMXXAMA', 'SMSMSASXSS', 'SAXAMASAAA', 'MAMMMXMMMM', 'MXMXAXMASX']

number_of_xmas_occurence = xmas_search(word_search_txt)
print("Number of XMAS occurences:", number_of_xmas_occurence)

number_x_mas_occurence = x_mas_search(word_search_txt)
print("Number of X-MAS occurences:", number_x_mas_occurence)
