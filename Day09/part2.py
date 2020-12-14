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

NUMBER = 20874512

def checker(number: int, previous:list) -> int:
    found = False
    for a in combinations(previous, 2):
        if int(a[0]) + int(a[1]) == number:
            found = True
            continue
    return found


def compute(input_string: str):
    line = input_string.split('\n')
    l = []
    for key, value in enumerate(line):
        l = [int(value)]
        for v in line[key + 1:]:
            l.append(int(v))
            if sum(l) == NUMBER and len(l) > 1:
                return sum(sorted(l)[0:1] + sorted(l)[-1:])
            elif sum(l) > NUMBER:
                break



@pytest.mark.parametrize("expected", [62])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
