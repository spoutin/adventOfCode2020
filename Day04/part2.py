import pytest
import re
from collections import namedtuple, Counter
from typing import Union

INPUT = '''\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''


def compute(input: str):

    def get_match(s: str, l: str) -> Union[None, str, int]:
        a = re.search(s, str(l))
        if a:
            return a.group(1)
        else:
            return 0

    c = 0
    lines = input.split("\n\n")
    for line in lines:
        byr = get_match(r'byr:(\d+)', line)
        iyr = get_match(r'iyr:(\d+)', line)
        eyr = get_match(r'eyr:(\d+)', line)
        hgt = get_match(r'hgt:(\d+(?:cm|in))', line)
        hgt_1 = get_match(r'(\d+)', hgt)
        hgt_2 = get_match(r'(cm|in)', hgt)
        hcl = get_match(r'hcl:(#[a-f0-9]{6})', line)
        ecl = get_match(r'ecl:(\S+)', line)
        pid = get_match(r'pid:(\d{9})(?:\s|$)', line)
        cid = get_match(r'cid:(\S+)\s', line)
        if (1920 <= int(byr) <= 2002) \
                and (2010 <= int(iyr) <= 2020) \
                and (2020 <= int(eyr) <= 2030) \
                and (((150 <= int(hgt_1) <= 193) and hgt_2 == 'cm')
                     or
                     ((59 <= int(hgt_1) <= 76) and hgt_2 == 'in')) \
                and hcl and ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') \
                and pid:
            c = c + 1
    return c


@pytest.mark.parametrize("expected", [4])
def test_results(expected):
    assert compute(INPUT) == expected


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
