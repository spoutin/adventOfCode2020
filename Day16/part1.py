from __future__ import annotations
import pytest
from collections import namedtuple, Counter, defaultdict
from typing import List, Dict
import re

INPUT = '''\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

Data = namedtuple('data', ['rules', 'ticket', 'nearby'])

def load(input_string: str) -> Data:
    lines = input_string.split('\n\n')
    rules = {re.search(r'^(.+): (.+)', raw).group(1): re.search(r'^(.+): (.+?) or (.+?)$', raw).groups()[1:] for raw in lines[0].splitlines()}
    ticket = lines[1].splitlines()[1].split(",")
    nearby = [x.split(",") for x in lines[2].splitlines()[1:]]
    data = Data(rules=rules, ticket=ticket, nearby=nearby)
    return data


def loop_ticket_numbers(ticket: List, rules: Dict) -> list:
    results = []
    for c, t in enumerate(ticket):
        if not apply_rule(t, rules):
            results.append(int(t))
    return results


def apply_rule(ticket: str, rules: Dict) -> bool:
    for rule, value in rules.items():
        for v in value:
            a, b = v.split("-")
            if int(a) <= int(ticket) <= int(b):
                return True
    return False

def compute(input_string: str):
    data = load(input_string)

    results = []
    for ticket in data.nearby:
        results += loop_ticket_numbers(ticket, data.rules)


    return sum(results)


@pytest.mark.parametrize("expected", [71])
def test_results(expected):
    assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
