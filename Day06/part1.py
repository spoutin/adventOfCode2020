import pytest
import re
from collections import namedtuple, Counter

INPUT = '''\
abc

a
b
c

ab
ac

a
a
a
a

b'''


def compute(input: str):
    lines = input.split("\n\n")
    group_counts = []
    for line in lines:
        group_counts.append(Counter(line.replace('\n', '')))

    # Count Length
    result = 0
    for c in group_counts:
        result = result + len(c)

    return result

@pytest.mark.parametrize("expected", [11])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
