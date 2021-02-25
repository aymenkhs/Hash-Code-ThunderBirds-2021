


class Street:

    def __init__(self, start, end, string_name, L):
        self.start = start
        self.end = end
        self.string_name = string_name
        self.L = L
        self.light = False


class Car:

    def __init__(self, ns, streets, string_name, L):
        self.streets = streets
        self.ns = ns
        self.start = streets[0]
        self.actual_street = self.start
