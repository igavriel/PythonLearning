"""Model fro aircraft"""
import sys
from pprint import pprint as pp

class Flight:
    """Flight class"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code in '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()



class Aircraft:
    def __init__(self, reg, model, rows, seats_per_row):
        self._reg = reg
        self._model = model
        self._rows = rows
        self._seats_per_row = seats_per_row

    def registration(self):
        return self._reg

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._rows+1), 
                "ABCDEFGHJK"[:self._seats_per_row])


#################################################
def TestFlight(flight):
    try:
        f = Flight(flight, Aircraft("GASD", "Airbus", 22, 6) )
        print("Flight number is '{}' Airline '{}' ".format(
            f.number(), f.airline()))
        print("       model is '{}' ".format(f.aircraft_model() ))
        pp(f._seating)

    except ValueError as e:
        print("Error: {0}".format(str(e)))

#################################################
def main(flight):
    TestFlight('aaaa')
    TestFlight('aa11')
    TestFlight('AA11')
    TestFlight(flight)

#################################################
if __name__ == '__main__':
    if len(sys.argv) == 1:
        main('LY123')
    else:
       main(sys.argv[1])   # the '0' argument is the module file name
