from __future__ import annotations
from itertools import combinations
import re

import pytest

INPUT = '''\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''


def checker(number: int, previous:list) -> int:
    found = False
    for a in combinations(previous, 2):
        if int(a[0]) + int(a[1]) == number:
            found = True
            continue
    return found


def compute(input_string: str):
    line = input_string.split('\n')
    offset = 25
    for key, value in enumerate(line[offset:]):
        previous = line[key:offset+key]
        results = checker(int(value), previous)
        if not results:
            return int(value)
    return


@pytest.mark.parametrize("expected", [127])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
