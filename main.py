import argparse

import input


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="""name of file can be 'a' or 'b' or 'c' or 'd' or 'e' or 'f'""")
    return parser.parse_args()

def main():

    args = parse_arguments()
    if args.file not in ('a','b','c','d','e', 'f'):
        raise ValueError("argument file (-f) must be equal to 'a' or 'b' or 'c' or 'd' or 'e' or 'f'")

    # read the file
    content = input.read_file(input.path_files[args.file])
    # separate the first line
    first_line, content = input.separate_first_line(content)
    # extract content from the first line
    D, I, S, V, F = input.first_line_content(first_line)
    # separate the folowing lines
    Slines, Vlines = input.separate_content(content, S)
    # extract the content from each line
    for i in range(S):
        B, E, street_name, L = input.Sline_content(Slines[i])
        print(B,E,street_name,L)

    for i in range(V):
        P, streets_names = input.Vline_content(Vlines[i])
        print(P, streets_names)




if __name__ == '__main__':
    main()
