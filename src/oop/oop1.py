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
    pass

class FlightVehicle(Vehicle):
    # Vehicle is the parent class
    pass

class Starship(FlightVehicle):
    # FlightVehicle is the parent class
    pass

class Airplane(FlightVehicle):
    # FlightVehicle is the parent class
    pass


class GroundVehicle(Vehicle):
    # Vehicle is the parent class
    pass


class Car(GroundVehicle):
    # GroundVehicle is the parent class
    pass

class Motorcycle(GroundVehicle):
    # GroundVehicle is the parent class
    pass


