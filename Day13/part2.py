from __future__ import annotations

import pytest
from sympy.ntheory.modular import crt

INPUT = '''\
939
7,13,x,x,59,x,31,19'''


def load(input_string: str) -> list:
    lines = input_string.splitlines()
    return lines


def compute_crt(input_string: str):
    lines = input_string.splitlines()
    parsed = [
        (int(s), i)
        for i, s in enumerate(lines[1].split(','))
        if s != 'x'
    ]
    buses = [pt[0] for pt in parsed]
    mods = [-1 * pt[1] for pt in parsed]

    return crt(buses, mods)[0]


def compute(input_string: str):
    lines = load(input_string)
    bus_times: list = lines[1].split(',')

    bus_times_temp = [int(bus) for bus in bus_times if bus != "x"]
    counter = -4
    increment = max(bus_times_temp)
    while True:
        counter += increment
        # t = bus - (arrival_time % bus)
        for scheduled, bus in enumerate(bus_times[1:]):
            if bus == "x":
                continue
            elif (int(bus) - counter % int(bus)) == scheduled + 1:
                if len(bus_times[1:]) == scheduled + 1:
                    if counter % int(bus_times[:1][0]) == 0:
                        return counter
            else:
                break


@pytest.mark.parametrize("expected", [1068781])
def test_results(expected):
    assert expected == compute_crt(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute_crt(i))
