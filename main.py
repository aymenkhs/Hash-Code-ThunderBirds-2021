import argparse

import input

from classes import *

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
    D,I, S, V, F = input.first_line_content(first_line)
    # separate the folowing lines
    Slines, Vlines = input.separate_content(content, S)
    # extract the content from each line


    intersections_sortant = [[] for _ in range(I)]
    intersections_entrant = [[] for _ in range(I)]


    streets = []
    for i in range(S):
        B, E, street_name, L = input.Sline_content(Slines[i])
        # we store the value
        street = Street(B, E, street_name, L)
        intersections_sortant[B].append(street)
        intersections_entrant[E].append(street)
        streets.append(street)

    cars = []
    for i in range(V):
        P, streets_names = input.Vline_content(Vlines[i])
        car_street = []
        for street_name in streets_names:
            for street in streets:
                if(street.street_name == street_name)
                    car_street.append(street)
        car = Car(P, streets)
        cars.append(car)


if __name__ == '__main__':
    main()


# car {ns : number of streets, [street] : list of streets}

# street {s : int , e : int , l : L}

# function ( [cars] , ST : simulation time) {
#   for i in [cars]:
#       sum = 0
#       for j in cars.[street] :
#           sum = sum + j.l
#       if sum > ST [cars].remove(i)
# }
