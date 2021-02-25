import os

path_files = {
    "a": os.path.join("inputs", "a.txt"),
    "b": os.path.join("inputs", "b.txt"),
    "c": os.path.join("inputs", "c.txt"),
    "d": os.path.join("inputs", "d.txt"),
    "e": os.path.join("inputs", "e.txt"),
    "f": os.path.join("inputs", "f.txt"),
}

def read_file(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def separate_first_line(content):
    # find the index of the first '\n'
    index = content.find('\n')
    first_line = content[:index]
    content = content[index+1:]
    return first_line, content

def separate_content(content, S):
    lines = content.split("\n")
    Slines = lines[:S]
    Vlines = lines[S:-1]
    return Slines, Vlines

def first_line_content(first_line):
    values = first_line.split(' ')
    D = int(values[0])
    I = int(values[1])
    S = int(values[2])
    V = int(values[3])
    F = int(values[4])
    return D, I, S, V, F

def Sline_content(line):
    values = line.split(' ')
    B = int(values[0])
    E = int(values[1])
    street_name = values[2]
    L = int(values[3])
    return B, E, street_name, L

def Vline_content(line):
    values = line.split(' ')
    P = int(values[0])
    streets_names = values[1:]

    return P, streets_names
