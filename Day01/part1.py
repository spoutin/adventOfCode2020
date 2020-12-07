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
            if l + line == 2020:
                results = l * line
                return results
    raise ValueError


@pytest.mark.parametrize("expected", [514579])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))

