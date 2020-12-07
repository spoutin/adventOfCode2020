import pytest

INPUT = '''\
1721
979
366
299
675
1456'''


def compute(input: str):
    lines = input.split("\n")
    lines = [int(x) for x in lines]
    for line in lines:
        for l in lines:
            for l2 in lines:
                if l2 + l + line == 2020:
                    results = l * l2 * line
                    return results
    raise ValueError


@pytest.mark.parametrize("expected", [241861950])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))