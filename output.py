import os 

outputs_files = {
    "a": os.path.join("outputs", "a_example"),
    "b": os.path.join("outputs", "b_by the ocean.in"),
    "c": os.path.join("outputs", "c_checkmate.in"),
    "d": os.path.join("outputs", "d_daily commute.in"),
    "e": os.path.join("outputs", "e_etoiles.in"),
    "f": os.path.join("outputs", "f_forever_jammed.in"),
}

def write_file(file_path, intersections):
    string = ""
    string += str(len(intersections))
    string += "\n"
    for intersection in intersections:
        string += str(intersection.id) + "\n"
        string += str(len(intersection.incomingSt)) + "\n"
        for i in intersection.incomingSt:
            string += str(i.nameStreet) + str(i.lightTime) + "\n"

    with open(file_path, "w") as file:
        content = file.write(string)