import os 

outputs_files = {
    "a": os.path.join("outputs", "a_example"),
    "b": os.path.join("outputs", "b_by the ocean.in"),
    "c": os.path.join("outputs", "c_checkmate.in"),
    "d": os.path.join("outputs", "d_daily commute.in"),
    "e": os.path.join("outputs", "e_etoiles.in"),
    "f": os.path.join("outputs", "f_forever_jammed.in"),
}

def write_file(file_path, schedules):
    string = ""
    string += str(len(schedules))
    string += "\n"
    for schedule in schedules:
        string += str(schedule.nb)
        string += " "
        lights = " ".join(schedule.index_lights)
        string += lights
        string += "\n"

    with open(file_path, "w") as file:
        content = file.write(string)