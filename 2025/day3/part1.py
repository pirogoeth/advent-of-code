#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import sys
from collections import namedtuple
from functools import reduce
from typing import List

BankCellJoltage = namedtuple("BankCellJoltage", ["idx", "joltage"])


def find_largest_battery_joltage(bank: List[int]) -> BankCellJoltage:
    """ Find the battery in the bank with the highest joltage value,
        returning the battery joltage value and the index within the bank
    """

    largest = BankCellJoltage(-1, 0)
    for idx, joltage in enumerate(bank):
        if joltage > largest.joltage:
            largest = BankCellJoltage(idx, joltage)

    return largest


def find_largest_bank_joltage(bank: List[int]) -> str:
    """ Find the first largest joltage in he battery bank. After that,
        find the next largest joltage within the cells following the largest
    """

    largest = find_largest_battery_joltage(bank)
    if largest.idx == len(bank) - 1:
        # We can not use the largest battery as our last battery.
        # In this case, find the second largest to use as the first
        largest = find_largest_battery_joltage(bank[:-1])
    next_largest = find_largest_battery_joltage(bank[largest.idx+1:])

    return f"{largest.joltage}{next_largest.joltage}"


if __name__ == "__main__":
    largest_joltages = []
    with io.open(sys.argv[1], "r") as input_file:
        for bank in input_file.readlines():
            bank = [int(cell) for cell in bank.strip()]
            bank_joltage = find_largest_bank_joltage(bank)
            largest_joltages.append(bank_joltage)

    print(largest_joltages)
    print(reduce(
        lambda l, r: int(l) + int(r),
        largest_joltages,
        0,
    ))
