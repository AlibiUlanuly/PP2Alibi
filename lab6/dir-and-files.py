import os

#TASK 1
"""
def list_path(path):
    if os.path.exists(path):
        items = os.listdir(path)
        directories = [item for item in items if os.path.isdir(os.path.join(path, item))]
        files = [item for item in items if os.path.isfile(os.path.join(path, item))]
        for directory in directories:
            print(directory)
        for item in items:
            print(item)
        for file in files:
            print(files)
    else:
        print("Path doesn't exist")    
"""

#TASK 2

"""
def check_path(path):
    if os.path.exists(path):
        modes = {'Readibility': os.R_OK, 'Writability': os.W_OK, 'Executability': os.X_OK}
        for mode, flag in modes:
            if os.access(path, flag):
                print(f'{mode}: OK')
            else:
                print(f'{mode}: X')
    else:
        print("Path doesn't exist")
"""

#TASK 3

"""
def check_path(path):
    if os.path.exists(path):
        directory, filename = os.path.split(path)
        print(f'Directory: {directory}', f'Filename: {filename}', sep= "\n")
    else:
        print("Path doesn't exist")
"""

#TASK 4

"""
with open('task4-file.txt', 'r') as file:
    line_count = 0
    for x in file:
        if x.strip():
            line_count += 1
    print(line_count)
"""

#TASK 5

"""
lst = [1, 43, 53, 7, 5]
with open('task5-file.txt', 'a') as file:
    file.write(str(lst) + '\n')
"""

#TASK 6

"""
for ascii_value in range(65, 91):
    letter = chr(ascii_value)
    filename = letter + ".txt"
    with open(filename, 'w') as file:
        file.write(letter)
"""

#TASK 7

"""
with open('task7-file.txt', 'r') as file:
    content = file.read()
with open('task7-file2.txt', 'a') as file2:
    file2.write(content + '\n')
"""

#TASK 8

"""
def deletion(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("Path doesn't exist")
"""