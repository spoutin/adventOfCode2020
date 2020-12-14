from collections import defaultdict

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


def compute(input_string: str):
    my_list = defaultdict(int, {0: 1})
    lines = sorted(list(map(int,input_string.split('\n'))))

    for line in lines:
        my_list[line] += my_list[line -3] + my_list[line - 2] + my_list[line -1]

    return my_list[lines[-1]]


@pytest.mark.parametrize("expected", [19208])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
