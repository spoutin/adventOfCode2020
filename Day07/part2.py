from __future__ import annotations

import re

import pytest

INPUT = '''\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''


def looper(bags: dict, color: str, count) -> int:
    total = 0
    results = 0
    for parent_color, children in bags.items():
            if parent_color == color:
                for children_color, child_count in children.items():
                    c = looper(bags, children_color, child_count)
                    results += (c * child_count) + child_count
                    total
    return results


def compute(input_string: str):
    bags = {}
    for line in input_string.split('\n'):
        parent_color = re.match(r'^(.+) bags contain', line).group(1)
        children = {c[1]: int(c[0]) for c in re.findall(r'(?:(\d+) (.+?)\sbags*(?:\,|\.))+', line)}

        if parent_color in bags:
            bags[parent_color] = {**bags[parent_color], **children}
        else:
            bags[parent_color] = children

    count = looper(bags, "shiny gold", 1)
    return count


@pytest.mark.parametrize("expected", [126])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
