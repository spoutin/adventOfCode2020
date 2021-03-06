import pytest

INPUT = '''\
BFFFBBFRRR'''


def compute(input: str):
    seats = [0] * 1023
    lines = input.split("\n")
    for line in lines:
        mask = ''
        for l in line[:7]:
            if l == 'F':
                mask = mask + '0'
            else:
                mask = mask + '1'
        row = int(mask, 2)
        mask = ''
        for l in line[-3:]:
            if l == 'L':
                mask = mask + '0'
            else:
                mask = mask + '1'
        seat = int(mask, 2)
        seats[row * 8 + seat] = row * 8 + seat
    last = sorted(seats, reverse=True)[0]
    for x in sorted(seats):
        if x != 0:
            first = x
            break
    for i, s in enumerate(seats[first:last]):
        if s == 0:
            ss = i
    return ss+first




# @pytest.mark.parametrize("expected", [567, ])
# def test_results(expected):
#     assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))

