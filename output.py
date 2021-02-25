import os

outputs_files = {
    "a": os.path.join("outputs", "a.txt"),
    "b": os.path.join("outputs", "b.txt"),
    "c": os.path.join("outputs", "c.txt"),
    "d": os.path.join("outputs", "d.txt"),
    "e": os.path.join("outputs", "e.txt"),
    "f": os.path.join("outputs", "f.txt"),
}

def write_file(file_path, intersections_entrant):
    string = ""
    string += str(len(intersections_entrant))
    string += "\n"
    for i, inters in enumerate(intersections_entrant):
        string += str(i)
        string += "\n"
        string += str(len(inters))
        string += "\n"
        for street in inters:
            string += street.street_name
            string += " "
            string += "1\n"

    with open(file_path, "w") as file:
        content = file.write(string)
