from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy, copy
from itertools import product
from operator import sub
import re

import pytest

INPUT = '''\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''


def get_seating_value(area: dict, pos: tuple) -> str:
    counter = Counter()
    comb = product([0, 1, -1], repeat=2)
    if area[pos] == '.':
        return '.'
    else:
        for xy in comb:
            if xy != (0, 0):
                counter[area[tuple(map(sub, pos, xy))]] += 1
        if area[pos] == 'L' and counter['#'] == 0:
            return '#'
        if area[pos] == '#' and counter['#'] > 3:
            return 'L'
        else:
            return area[pos]


def load(input_string: str) -> dict:
    seating = defaultdict(lambda: '.')
    lines = input_string.splitlines()
    for row, value in enumerate(lines):
        for column, spot in enumerate(value):
            seating[(row, column)] = spot
    return seating


def compute(input_string: str):
    seating = load(input_string)
    results = Counter()
    count = 0
    while True:
        count += 1
        seating_copy = defaultdict(lambda: '.', seating)
        results_prev = Counter(**results)
        results = Counter()
        for seat in seating:
            seating_copy[seat] = get_seating_value(defaultdict(lambda: '.', seating), seat)
            results[seating_copy[seat]] += 1
        seating = seating_copy

        if results == results_prev:
            break
        print(f"round: {count}, prev_L:{results_prev['L']}, res_L:{results['L']}")

    return results['#']


@pytest.mark.parametrize("expected", [37])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
