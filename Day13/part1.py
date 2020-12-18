from __future__ import annotations

import pytest

INPUT = '''\
939
7,13,x,x,59,x,31,19'''


def load(input_string: str) -> list:
    lines = input_string.splitlines()
    return lines


def compute(input_string: str):
    lines = load(input_string)
    arrival_time = int(lines[0])
    bus_times = lines[1].split(',')
    pickup_time = {}
    for bus in bus_times:
        if bus == "x":
            continue
        bus = int(bus)
        t = bus - (arrival_time % bus)
        pickup_time[str(t)] = bus
    lowest = min([int(x) for x in pickup_time])
    return lowest * pickup_time[str(lowest)]



@pytest.mark.parametrize("expected", [295])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
