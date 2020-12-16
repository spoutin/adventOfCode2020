from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from operator import add

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


def get_seating_value(area: dict, pos: tuple, max_x: int, max_y) -> str:
    counter = Counter()
    comb = [x for x in product([0, 1, -1], repeat=2)]
    comb.pop(comb.index((0, 0)))
    num = 0

    while len(comb) > 0:
        num += 1
        offset_xy = tuple([x * num for x in comb[:1][0]])
        temp_xy = tuple(map(add, pos, offset_xy))

        if temp_xy[0] < 0 or temp_xy[1] < 0 or temp_xy[0] > max_x or temp_xy[1] > max_y:
            comb.remove(comb[:1][0])
            num = 0
            continue

        temp = area[temp_xy]
        if temp in "L#":
            counter[temp] += 1
            comb.remove(comb[:1][0])
            num = 0
            continue
        if temp != '.':
            raise ValueError()

    # determine what to return
    if area[pos] == 'L' and counter['#'] == 0:
        return '#'
    if area[pos] == '#' and counter['#'] > 4:
        return 'L'
    else:
        return area[pos]


def load_input(input_string: str) -> dict:
    seating = defaultdict(lambda: '.')
    lines = input_string.splitlines()
    for row, value in enumerate(lines):
        for column, spot in enumerate(value):
            seating[(row, column)] = spot
    return seating


def compute(input_string: str):
    seating = dict(load_input(input_string))
    results = Counter()
    count = 0
    max_x = max(seating.keys())[0]
    max_y = max(seating.keys())[1]
    while True:
        count += 1
        seating_copy = {**seating}
        results_prev = Counter(**results)
        results = Counter()
        for seat in seating:
            seating_copy[seat] = get_seating_value(seating, seat, max_x, max_y)
            results[seating_copy[seat]] += 1
        seating = seating_copy

        if results == results_prev:
            break
        print(f"round: {count}, prev_L:{results_prev['L']}, res_L:{results['L']}")

    return results['#']


@pytest.mark.parametrize("expected", [26])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
