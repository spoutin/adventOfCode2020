import pytest
import re
from collections import namedtuple, Counter
from typing import Union

INPUT = '''\
0byr:1983 iyr:2017
pid:796082981 cid:129 eyr:2030
ecl:oth hgt:182cm

1iyr:2019
cid:314
eyr:2039 hcl:#cfa07d hgt:171cm ecl:#0180ce byr:2006 pid:8204115568

1byr:1991 eyr:2022 hcl:#341e13 iyr:2016 pid:729933757 hgt:167cm ecl:gry

0hcl:231d64 cid:124 ecl:gmt eyr:2039
hgt:189in
pid:#9c3ea1

0ecl:#1f58f9
pid:#758e59
iyr:2022
hcl:z
byr:2016 hgt:68 eyr:1933

1hcl:#fffffd ecl:gry eyr:2022
hgt:172cm pid:781914826 byr:1930 iyr:2018

1hcl:#08df7e ecl:grn byr:1942
eyr:2028 iyr:2011 cid:141 pid:319110455
hgt:186cm

0pid:991343040 hgt:179cm
hcl:#a97842 iyr:2020
eyr:2024
byr:1984 cid:181

1pid:188cm byr:2005
hgt:170cm cid:163 ecl:#a08502 hcl:2964fb eyr:1994
iyr:2005

1ecl:grn hcl:#fffffd iyr:2013
pid:705547886
byr:1928 hgt:168cm eyr:2030

1cid:219
pid:016251942 hcl:#602927 hgt:163cm
byr:1943 eyr:2029 ecl:oth iyr:2019

1ecl:gry hgt:184cm eyr:2026
iyr:2010
pid:117647952 hcl:#efcc98
byr:1942

1cid:243 hcl:#888785 ecl:blu eyr:2027 pid:362697676
iyr:2011 byr:1962 hgt:154cm

0hgt:154cm byr:1965 ecl:blu eyr:2030
pid:779104554 iyr:2016 hcl:#435634

1hcl:z eyr:1996 iyr:1993
pid:#50f768
ecl:zzz hgt:62cm byr:2017

1ecl:grn byr:1988 iyr:2016
hgt:167cm
hcl:#cfa07d
eyr:2030 pid:951967790

1pid:320348494 iyr:2018 cid:281
byr:2004
hcl:#06a58b
eyr:2033
ecl:zzz
hgt:76cm

1cid:83 ecl:brn eyr:2028
byr:1941 iyr:2016
hcl:#341e13 pid:806979833
hgt:179cm

0ecl:brn
byr:1982 iyr:2010 eyr:2029 pid:535752324 hcl:#efcc98

1ecl:oth
hgt:70in hcl:#866857 eyr:2025 pid:203320330 iyr:2018 byr:2000

1hgt:70cm byr:2015 pid:#218eb5 hcl:#0ec4fe iyr:2014 cid:228 ecl:#c8533a
eyr:2035

1hcl:#6b5442
eyr:2020 ecl:hzl iyr:2017 hgt:173cm
cid:330 byr:1988 pid:173148327

0iyr:2011 byr:1964 hgt:83 ecl:grn hcl:#c0946f pid:931162400 eyr:2028

0cid:239
byr:1960 ecl:hzl
hgt:164cm
hcl:#51040b iyr:2018 eyr:2025

0cid:163 hgt:154cm
iyr:2015 eyr:2027 pid:838964596
byr:1972 ecl:oth hcl:#efcc98

1hgt:181cm
eyr:2028 ecl:blu
pid:853714682 hcl:#623a2f byr:1976 iyr:2020

1cid:225 byr:1957
hcl:#a97842 iyr:2013 eyr:2025
pid:511588647 hgt:173cm ecl:blu

1hcl:#efcc98
byr:1993
ecl:oth
pid:871652492 eyr:2028 hgt:177cm iyr:2016
cid:220

1ecl:hzl
hgt:165cm
hcl:#733820 eyr:2028 cid:57 byr:1973 iyr:2018 pid:018982018

1pid:491710153 iyr:2012 ecl:#c85046 hcl:#b6652a
eyr:2040 hgt:175cm byr:1981

0pid:917105765 eyr:2021 hgt:181cm iyr:2019 cid:159 byr:1995
ecl:gry

1hcl:#9d2ec4 iyr:2011
eyr:2028 pid:149288934 hgt:63in ecl:blu byr:1960

1byr:1923 pid:705818464 eyr:2024 cid:221 ecl:oth hcl:#7d3b0c hgt:193cm iyr:2014

1pid:117111015 eyr:2030
byr:1967 hcl:#ceb3a1 ecl:blu
hgt:157cm
iyr:2011

0iyr:2019 ecl:oth
hcl:#fffffd hgt:172cm pid:215010680
eyr:2025

1pid:157cm cid:277
iyr:1976 hgt:159in hcl:#341e13 ecl:#6c7644 eyr:2029 byr:1965

1pid:787186482 ecl:brn
byr:1980 hcl:#f5dfb9 eyr:2020
iyr:2018 hgt:188cm

1cid:168
eyr:2023 hcl:#07c809
iyr:2013
hgt:169cm pid:250679100 byr:1945 ecl:gry

0hcl:#6b5442 pid:683134187 iyr:2013 eyr:2023 byr:1965 hgt:171cm ecl:hzl

1eyr:2028 hgt:180cm ecl:blu byr:1952 cid:314 iyr:2016
pid:720794393 hcl:#602927

1byr:1982 iyr:2016
ecl:brn eyr:2027
hgt:156cm pid:185583837 hcl:#ddbf30

1hcl:#ceb3a1 pid:987624973
eyr:2026
iyr:2013 byr:1988 hgt:175cm ecl:grn'''


def compute(input: str):
    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    cid = None

    def get_match(s: str, l: str) -> Union[None, str]:
        r = re.escape(s) + r':(\S+)'
        a = re.search(r, l)
        if a:
            return a.group(1)
        else:
            return None

    c = 0
    lines = input.split("\n")
    for line in lines:
        if line != "":
            if not byr:
                byr = get_match('byr', line)
            if not iyr:
                iyr = get_match('iyr', line)
            if not eyr:
                eyr = get_match('eyr', line)
            if not hgt:
                hgt = get_match('hgt', line)
            if not hcl:
                hcl = get_match('hcl', line)
            if not ecl:
                ecl = get_match('ecl', line)
            if not pid:
                pid = get_match('pid', line)
            if not cid:
                cid = get_match('cid', line)

            if byr is not None and \
                    iyr is not None and \
                    eyr is not None and \
                    hgt is not None and \
                    hcl is not None and \
                    ecl is not None and \
                    pid is not None:
                c = c + 1
                byr = None
                iyr = None
                eyr = None
                hgt = None
                hcl = None
                ecl = None
                pid = None
                cid = None
        else:
            byr = None
            iyr = None
            eyr = None
            hgt = None
            hcl = None
            ecl = None
            pid = None
            cid = None
    return c


@pytest.mark.parametrize("expected", [35])
def test_results(expected):
    assert compute(INPUT) == expected


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))
