import os

outputs_files = {
    "a": os.path.join("outputs", "a_example"),
    "b": os.path.join("outputs", "b_by the ocean.in"),
    "c": os.path.join("outputs", "c_checkmate.in"),
    "d": os.path.join("outputs", "d_daily commute.in"),
    "e": os.path.join("outputs", "e_etoiles.in"),
    "f": os.path.join("outputs", "f_forever_jammed.in"),
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
