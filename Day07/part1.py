from __future__ import annotations

import re

import pytest

INPUT = '''\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''


def looper(bags: dict, color: str) -> dict:
    d = {}
    for parent_color, children in bags.items():
            for child_color, child in children.items():
                if color == child_color:
                    d = {**d, **{parent_color: None}, **looper(bags, parent_color)}
    return d

def compute(input_string: str):
    bags = {}
    for line in input_string.split('\n'):
        parent_color = re.match(r'^(.+) bags contain', line).group(1)
        children = {c[1]: c[0] for c in re.findall(r'(?:(\d+) (.+?)\sbags*(?:\,|\.))+', line)}

        if parent_color in bags:
            bags[parent_color] = {**bags[parent_color], ** children}
        else:
            bags[parent_color] = children

    count = looper(bags, "shiny gold")
    return len(count)

@pytest.mark.parametrize("expected", [4])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
