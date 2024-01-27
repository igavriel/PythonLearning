from logic.Flight import *
from models.Airplanes import *
from models.Person import *
from utils import *

# Constants
TOTAL_PLANES = 3
TOTAL_PERSON = 50


def make_flights(aircraft, passengers):
    f = Flight(random_flight_number(), aircraft)
    for person in passengers:
        try:
            seat = random_seat(f.row_numbers(), f.seat_letters())
            f.allocate_seat(seat, person)
        except Exception as e:
            print(f"Failed to allocate {person} because {e}")

    # print(f.make_boarding_cards(console_card_printer))
    print(aircraft)
    print(f.make_boarding_cards(console_card_list))


# Randomize
airbus = [AirbusA319(random_registration()) for _ in range(TOTAL_PLANES)]
cntA = 0

for a in airbus:
    peopleA = [Person() for _ in range(TOTAL_PERSON)]
    peopleA.append(Person(f"Mr. XXX{++cntA}", "Male"))
    make_flights(a, peopleA)

boeing = [Boeing777(random_registration()) for _ in range(TOTAL_PLANES)]
cntB = 0

for b in boeing:
    peopleB = [Person() for _ in range(TOTAL_PERSON)]
    peopleB.append(Person(f"Mrs. YYY{++cntB}", "Female"))
    make_flights(b, peopleB)
