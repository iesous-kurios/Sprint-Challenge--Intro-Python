# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:

    """Base class for all Vehicles

    Attributes:
    :var make: str
    :var model: str
    :var year: int


    Methods:
    - None
        - None
    """

    #  Class Variables

    """make = None
    model = None
    year = None"""

    """def __init__(self, make = None, year = None):
        self.make = make
        self.model = model
        self.year = year"""

    def __repr__(self):
        return f"<Vehicle: {self.make}, {self.model}, {self.year}>"


class FlightVehicle(Vehicle):

    """Child class of Vehicles

    Attributes:
    :var make: str
    :var model: str
    :var year: int
    :var num_wings: int


    Methods:
    - None
        - None
    """

    #  Class Variables

    """make = None
    model = None
    year = None
    num_wings = None"""

    def __init__(self):
        super().__init__()
#        self.num_wings = num_wings

    def __repr__(self):
        return (f"< FlightVehicle: {self.make}, {self.model}, {self.year}, {self.num_wings} >")


class Starship(FlightVehicle):

    """Child class of FlightVehicle

    Attributes:
    :var make: str
    :var model: str
    :var year: int
    :var num_wings: int
    :var num_laserguns: int


    Methods:
    - blast
        - Fire lasers "pew pew!"
    """

    #  Class Variables

    """make = None
    model = None
    year = None
    num_wings = None
    num_laserguns = None"""

    def __init__(self):
        super().__init__()
        """self.num_wings = num_wings
        self.num_laserguns = num_laserguns"""

    def blast(self):
        return "pew pew!"

    def __repr__(self):
        return (f" < Starship: {self.make}, {self.model}, {self.year}, {self.num_wings}, {self.num_lasers} >")


class Airplane(FlightVehicle):

    """Child class of FlightVehicle

    Attributes:
    :var make: str
    :var model: str
    :var year: int
    :var num_wings: int


    Methods:
    - None
        -none
    """

    #  Class Variables

    """make = None
    model = None
    year = None
    num_wings = None
    """

    def __init__(self):
        super().__init__()
        """self.num_wings = num_wings
        """

    def __repr__(self):
        return (f"< Airplane: {self.make}, {self.model}, {self.year}, {self.num_wings} >")


class GroundVehicle(Vehicle):

    """Child class of Vehicles

    Attributes:
    :var make: str
    :var model: str
    :var year: int
    :var num_wheels: int


    Methods:
    - drive
        - Go 'vroooom'
    """

    #  Class Variables

    make = None
    model = None
    year = None
    num_wheels = None

    def __init__(self):
        super().__init__()
#        self.num_wheel = num_wheels

    def drive(self):
        return "vroooom"

    def __repr__(self):
        return (f"< GroundVehicle: {self.make}, {self.model}, {self.year}, {self.num_wheels} >")


class Car(GroundVehicle):

    """Child class of GroundVehicle

    Attributes:
    :var make: str
    :var model: str
    :var year: int
    :var num_wheels: int
    :var name: str


    Methods:
    - drive
        - Go 'vroooom'

    - show_off
        - Say 'look at me!'
    """

    #  Class Variables

    """make = None
    model = None
    year = None
    num_wheels = None
    name = None"""

    def __init__(self):
        super().__init__()
        """self.num_wheel = num_wheels
        self.name = name"""

    def show_off(self):
        return "look at me!"

    def __repr__(self):
        return (f"< Car: {self.make}, {self.model}, {self.year}, {self.num_wheels}, {self.name} >")


class Motorcycle(GroundVehicle):

    """Child class of GroundVehicle

    Attributes:
    :var make: str
    :var model: str
    :var year: int
    :var num_wheels: int
    :var name: str
    :var seats: int


    Methods:
    - drive
        - Go 'vroooom'

    - show_off
        - Say 'look at me!'

    - wheelie
        - go 'weeeeee!'
    """

    #  Class Variables

    """make = None
    model = None
    year = None
    num_wheels = None
    name = None"""

    def __init__(self):
        super().__init__()
        """self.num_wheel = num_wheels
        self.name = name"""

    def wheelie(self):
        return "weeeeee!"

    def __repr__(self):
        return (f"< Motorcycle: {self.make}, {self.model}, {self.year}, {self.num_wheels}, {self.name} >")
