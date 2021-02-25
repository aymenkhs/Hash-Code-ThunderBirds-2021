class Intersection:

    def __init__(self,id,state):
        self.id = id
        self.state = state


class Street:

    def __init__(self, start, end, street_name, L):
        self.start = start
        self.end = end
        self.street_name = string_name
        self.L = L


class Car:

    def __init__(self, ns, streets):
        self.streets = streets
        self.ns = ns
