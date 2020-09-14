# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.


class GroundVehicle:

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

    def __init__(self, num_wheels=4):
        super().__init__()
        self.num_wheels = num_wheels

    def drive(self):
        return "vroooom"

    def __repr__(self):
        return f"<GroundVehicle: {self.make}, {self.model}, {self.year}, {self.num_wheels}>"

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"


class Motorcycle(GroundVehicle):

    """Child class of GroundVehicle

    Attributes:
    :var make: str
    :var model: str
    :var year: int
    :var num_wheels: int


    Methods:
    - drive
        - Go 'BRAAAP!!'

    """

    #  Class Variables

    """
    make = None
    model = None
    year = None
    num_wheels = None
    """

    def __init__(self, num_wheels=2):
        super().__init__()
        self.num_wheels = num_wheels

    def drive(self):
        return 'BRAAAP!!'

    def __repr__(self):
        return f"<Motorcycle: {self.make}, {self.model}, {self.year}, {self.num_wheels}>"

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

for vehicle in vehicles:
    print(vehicle.drive())
