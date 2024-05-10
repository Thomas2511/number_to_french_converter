"""Convert numbers to French."""
import argparse
from collections import deque

from data.numbers import NUMBERS


def convert(num: int) -> str:
    """Split thousands from the rest and check for special rules."""
    thousands = num // 1000
    rest = num % 1000

    if thousands > 1 and rest > 0:
        return convert_3_digits(thousands) + "-mille-" + convert_3_digits(rest)

    if thousands > 1 and rest == 0:
        return convert_3_digits(thousands) + "-milles"
    
    if thousands == 1 and rest > 0:
        return "mille-" + convert_3_digits(rest)

    if thousands == 1 and rest == 0:
        return "mille"
    
    if thousands == 0 and rest > 0:
        return convert_3_digits(rest)
    
    return "zéro"


def convert_3_digits(num: int) -> str:
    """Check the value of the hundreds and last 2 digits for rules then convert to string."""
    first = num // 100
    last_2 = num % 100

    if first > 1:
        if last_2 == 0:
            return NUMBERS[first] + "-cents"
        return NUMBERS[first] + "-cent-" + NUMBERS[last_2]

    if first == 1:
        if last_2 == 0:
            return "cent"
        return "cent-" + NUMBERS[last_2]
    
    return NUMBERS[last_2]
    

def display(converts: str):
    """Display translation for each input."""
    for converted in converts:
        print(converted)


def main():
    """Parse args, convert values, and display them."""
    parser = argparse.ArgumentParser("number to french converter")
    parser.add_argument("numbers", help="The numbers which will be converted to french.", metavar='N', type=int, nargs='+')
    args = parser.parse_args()
    converts = [convert(nb) for nb in args.numbers]
    display(converts)


if __name__ == "__main__":
    main()
