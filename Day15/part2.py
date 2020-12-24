from __future__ import annotations
import pytest
import collections
from typing import List, Dict

INPUT = '''\
0,3,6'''


def load(input_string: str) -> list:
    lines = input_string.split(',')
    return lines

def compute(input_string: str):
    prev_seen: Dict[int, List[int]] = collections.defaultdict(list)
    numbers = [int(n) for n in load(input_string)]

    for turn in range(2020):
        if turn < len(numbers):
            n = numbers[turn]
        elif len(prev_seen[n]) == 1:
            n = 0
        else:
            n = prev_seen[n][-1] - prev_seen[n][-2]

        prev_seen[n].append(turn)

    return n


@pytest.mark.parametrize("expected", [436])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
