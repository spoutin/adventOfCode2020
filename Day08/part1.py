from __future__ import annotations

import re

import pytest

INPUT = '''\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

class Stack:
    def __init__(self, stack: list):
        self.stack = stack
        self.position = 0
        self.var = 0

    def run(self):
        while True:
            instruction, number, completed = self.stack[self.position]
            if not completed:
                self.stack[self.position][2] = True
                getattr(self, instruction)(number)
            else:
                break
        return self.var

    def nop(self, *args, **kwargs):
        self.position += 1

    def acc(self, count, *args, **kwargs):
        self.var += int(count)
        self.position += 1

    def jmp(self, number, *args, **kwargs):
        self.position += int(number)


def compute(input_string: str):
    lines = input_string.split('\n')
    stack = []
    for line in lines:
        instruction, number = line.split(' ')
        stack.append([instruction, number, False])
    results = Stack(stack).run()
    return results


@pytest.mark.parametrize("expected", [5])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
