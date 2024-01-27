import string
import random


def random_registration():
    letters = string.ascii_uppercase
    char = random.choice(letters)
    random_string = ''.join(random.choice(letters) for i in range(4))
    return f"{char}-{random_string}"


def random_flight_number():
    letters = string.ascii_uppercase
    digits = string.digits
    return ''.join(random.choice(letters) for i in range(2)) + \
        ''.join(random.choice(digits) for i in range(3))


def random_seat(row_range, seat_letters):
    row = random.randint(row_range.start, row_range.stop-1)
    position = random.randint(1, len(seat_letters))
    return f"{row}{seat_letters[position-1]}"


def console_card_printer(passenger, seat, flight_number, aircraft):
    outputPlane = f"| Flight: {flight_number}" \
                  f"  Seat: {seat}" \
                  f"  Aircraft: {aircraft} |"
    outputPerson = f"| {passenger}"
    spaces = len(outputPlane) - len(outputPerson) - 1
    outputPerson += ' ' * int(spaces) + '|'
    banner = '+' + '-' * (len(outputPlane) - 2) + '+'
    border = '|' + ' ' * (len(outputPlane) - 2) + '|'
    lines = [banner, border, outputPerson, outputPlane, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


def console_card_list(passenger, seat, flight_number, aircraft):
    outputPlane = f"Flight: {flight_number}" \
                  f"  Seat: {seat}" \
                  f"  Aircraft: {aircraft}"
    outputPerson = f"{passenger}"
    print("* " + outputPlane + " - ", outputPerson)
