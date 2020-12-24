from __future__ import annotations
import pytest
from collections import namedtuple, Counter, defaultdict
from typing import List, Dict
import re

INPUT = '''\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''

Data = namedtuple('data', ['rules', 'ticket', 'nearby'])

def load(input_string: str) -> Data:
    lines = input_string.split('\n\n')
    rules = {re.search(r'^(.+): (.+)', raw).group(1): re.search(r'^(.+): (.+?) or (.+?)$', raw).groups()[1:] for raw in lines[0].splitlines()}
    ticket = lines[1].splitlines()[1].split(",")
    nearby = [x.split(",") for x in lines[2].splitlines()[1:]]
    data = Data(rules=rules, ticket=ticket, nearby=nearby)
    return data


def loop_ticket_numbers(ticket: List, rules: Dict) -> defaultdict:
    for c, t in enumerate(ticket):
        if not check_rule(t, rules):
            return defaultdict(Counter)
    return apply_rule(ticket, rules)


def check_rule(ticket: str, rules: Dict) -> bool:
    for rule, value in rules.items():
        for v in value:
            a, b = v.split("-")
            if int(a) <= int(ticket) <= int(b):
                return True
    return False


def apply_rule(ticket: List, rules: Dict):
    results = defaultdict(Counter)
    value: str
    for c, t in enumerate(ticket):
        counter = Counter()
        for rule, value in rules.items():
            for v in value:
                a, b = v.split("-")
                if int(a) <= int(t) <= int(b):
                    counter[rule] += 1
        results[c] += counter
    return results


def compute(input_string: str):
    data = load(input_string)

    results = defaultdict(Counter)
    for ticket in data.nearby:
        res = loop_ticket_numbers(ticket, data.rules)
        for k, r in res.items():
            results[k] += r
    return results


# @pytest.mark.parametrize("expected", [436])
# def test_results(expected):
#     assert expected == compute(INPUT)


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
