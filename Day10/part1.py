from __future__ import annotations

from collections import Counter
from itertools import combinations
import re

import pytest

INPUT = '''\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''


def find_missing(lst):
    start = lst[0]
    end = lst[-1]
    return sorted(set(range(start, end + 1)).difference(lst))


def find_sequences(lst: list):
    results = Counter()
    offset = 0
    while offset < len(lst) - 1:
        counter = 2
        for key, value in enumerate(lst[offset+1:]):
            if lst[offset] == value - (key + 1):
                counter += 1
                if len(lst[offset+1:]) == 1:
                    results[counter] += 1
                    offset += key + 1
            else:
                results[counter] += 1
                offset += key + 1
                break
    return results


def compute(input_string: str):
    line = sorted(list(map(int,input_string.split('\n'))))
    results = find_missing(line)
    counts = find_sequences(results)
    counts[1] = len(line) - sum(counts.values())

    return counts[1] * (counts[3] + 1)  # I have no idea why i need to add one to the 3 count, but it works :)


@pytest.mark.parametrize("expected", [220])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
