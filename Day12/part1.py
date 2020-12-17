from __future__ import annotations

from collections import Counter
import re
from operator import add, sub
from typing import Union

import pytest

INPUT = '''\
F10
N3
F7
R90
F11'''

COMPASS = {
    "comp_to_dec": {
        "N" : 0,
        "S": 180,
        "E": 90,
        "W": 270
    },
    "dec_to_comp": {
        0: "N",
        180: "S",
        90: "E",
        270: "W"
    }
}

ROTATION = {
    "R": add,
    "L": sub
}


def load(input_string: str) -> list:
    lines = input_string.splitlines()
    return lines


def compute(input_string: str):
    lines = load(input_string)
    counter = Counter()
    direction = "E"
    for line in lines:
        command, option = re.match(r'(.)(\d+)', line).groups()
        option = int(option)
        if command in "LR":
            direction = get_direction(direction, command, option)
        elif command in "F":
            counter[direction] += option
        elif command in "NSEW":
            counter[command] += option
        else:
            raise ValueError()
    return abs(counter["E"] - counter["W"]) + abs(counter["S"] - counter["N"])


def get_direction(current_direction: str, command: str, direction: int) -> str:
    new_direction = ROTATION[command](COMPASS["comp_to_dec"][current_direction], direction) % 360
    if new_direction < 0:
        new_direction = new_direction + 360
    t = COMPASS["dec_to_comp"][new_direction]
    return t

@pytest.mark.parametrize("expected", [25])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
