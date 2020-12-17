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
        270: "W",
        -180: "S",
        -270: "E",
        -90: "W"
    }
}

ROTATION = {
    "R": add,
    "L": sub
}


def load(input_string: str) -> list:
    lines = input_string.splitlines()
    return lines

def go_to_waypoint():
    ...


def rotate_waypoint(waypoint: Counter, command, direction) -> Counter:
    new_waypoint = Counter()

    for c in "NESW":
        temp_rotation = ROTATION[command](COMPASS["comp_to_dec"][c], direction) % 360
        temp_direction = COMPASS["dec_to_comp"][temp_rotation]
        new_waypoint[temp_direction] = waypoint[c]

    return new_waypoint


def compute(input_string: str):
    lines = load(input_string)
    ship = Counter()
    waypoint = Counter({"E": 10, "N": 1})
    for line in lines:
        command, option = re.match(r'(.)(\d+)', line).groups()
        option = int(option)
        if command in "LR":
            waypoint = rotate_waypoint(waypoint, command, option)
        elif command in "F":
            for c in "NESW":
                ship[c] += waypoint[c] * option
        elif command in "NSEW":
            waypoint[command] += option
        else:
            raise ValueError()
    return abs(ship["E"] - ship["W"]) + abs(ship["S"] - ship["N"])


@pytest.mark.parametrize("expected", [286])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
