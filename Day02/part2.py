import pytest
import re
from collections import namedtuple, Counter

INPUT = '''\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''


def compute(input: str):
    Policy = namedtuple('Policy', ['lower_count', 'upper_count', 'letter', 'password'])
    lines = input.split("\n")
    c = 0
    for line in lines:
        a = re.search(r'^(\d+)-(\d+) ([a-zA-Z]): (.+)$', line)
        policy = Policy(lower_count=int(a.group(1)), upper_count=int(a.group(2)), letter=a.group(3), password=a.group(4))
        if (policy.password[policy.lower_count-1] == policy.letter) ^ (policy.password[policy.upper_count-1] == policy.letter):
            c = c + 1
    return c


@pytest.mark.parametrize("expected", [1])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
