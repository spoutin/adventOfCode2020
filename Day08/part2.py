from __future__ import annotations
from copy import deepcopy

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
            try:
                instruction, number, count = self.stack[self.position]
                self.stack[self.position][2] += 1
                getattr(self, instruction)(number)
                if self.stack[self.position][2] >= 1:
                    return None
            except IndexError:
                return self.var

    def nop(self, *args, **kwargs):
        self.position += 1

    def acc(self, count, *args, **kwargs):
        self.var += int(count)
        self.position += 1

    def jmp(self, number, *args, **kwargs):
        self.position += int(number)


def invert(stack, position, value) -> list:
    new_stack = deepcopy(stack)
    new_stack[position][0] = value
    return new_stack


def compute(input_string: str):
    lines = input_string.split('\n')
    stack = []
    for line in lines:
        instruction, number = line.split(' ')
        stack.append([instruction, number, 0])

    for key, s in enumerate(stack):
        if s[0] == 'jmp':
            new_stack = invert(stack, position=key, value='nop')
        elif s[0] == 'nop':
            new_stack = invert(stack, position=key, value='jmp')
        else:
            continue
        results = Stack(new_stack).run()
        if results:
            return results



    return 0


@pytest.mark.parametrize("expected", [8])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
