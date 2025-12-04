#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import sys
from collections import namedtuple
from functools import reduce
from typing import List

BankCellJoltage = namedtuple("BankCellJoltage", ["idx", "joltage"])


def find_bank_max_joltage(bank: List[int]) -> BankCellJoltage:
    """ Returns the largest joltage found in a cell in the bank (or segment of a bank) """

    largest = BankCellJoltage(-1, 0)
    for idx, cell in enumerate(bank):
        if cell > largest.joltage:
            largest = BankCellJoltage(idx, cell)

    return largest


def collect_largest_cells(bank: List[int]) -> List[BankCellJoltage]:
    """ Collect all of the cells within the bank, optimizing for largest joltage
        values, returning the list of `BankCellJoltage`s ordered by bank index
    """

    largest_cells = []
    window_size = len(bank) - 11
    print(f"Starting {window_size=}")
    idx = 0
    while idx < len(bank) and len(largest_cells) < 12:
        bank_window = bank[idx:idx+window_size]
        print(f"{bank_window=}")
        window_largest = find_bank_max_joltage(bank_window)
        print(f"largest within window {window_largest}")
        largest_cells.append(window_largest)
        # Shrink the window size to (window_largest.idx - idx)
        window_size = window_size - window_largest.idx
        print(f"new window size {window_size}")
        idx = idx + window_largest.idx + 1

    return largest_cells


if __name__ == "__main__":
    largest_joltages = []
    with io.open(sys.argv[1], "r") as input_file:
        for bank in input_file.readlines():
            bank = [int(cell) for cell in bank.strip()]
            bank_joltages = collect_largest_cells(bank)
            print(bank_joltages)
            largest_joltages.append("".join([
                str(cell.joltage) for cell in bank_joltages
            ]))

    print(largest_joltages)
    print(reduce(
        lambda l, r: int(l) + int(r),
        largest_joltages,
        0,
    ))
