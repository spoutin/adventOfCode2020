from __future__ import annotations
import re
import pytest

INPUT = '''\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''


def load(input_string: str) -> list:
    lines = input_string.splitlines()
    return lines


def apply_mask(value: str, mask: list[tuple[int, int]]) -> list:
    value = f'{int(value):036b}'
    result = [x for x in value]
    for m in mask:
        result[m[0]] = m[1]
    return result


def load_mask(mask:str) -> list[tuple[int,int]]:
    result = [(pos, int(value)) for pos, value in enumerate(mask) if value != "X"]
    return result


def compute(input_string: str):
    memory = {}
    lines = load(input_string)
    regex_mask = re.compile(r'^mask = (.+)$')
    regex_mem = re.compile(r'^mem\[(\d+)\] = (.+)$')
    mask = None
    for line in lines:
        m = re.search(regex_mask, line)
        if m:
            mask = load_mask(m.group(1))
        else:
            mem, value = re.search(regex_mem, line).groups()
            memory[mem] = apply_mask(value, mask)

    dec_results = [int("".join(str(x) for x in b), 2) for b in memory.values()]
    return sum(dec_results)


@pytest.mark.parametrize("expected", [165])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
