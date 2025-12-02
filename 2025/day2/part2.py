#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import math
import sys
from typing import Iterator, List, Set

invalid_ids = []


def generate_potential_repetition_sequences(haystack: str) -> List[str]:
    """ We're searching for IDs that consist of at least two or more sequences
        of repetitions, so use a sliding window starting at len(num_str)/2 to generate
        the potential repetition sequences

        Returns the sequences set as a list in reverse order to reduce the amount of matching
        needed
    """

    sequences: Set[str] = set()

    split_size = 2
    while (idx := int(len(haystack) / split_size)) >= 1:
        needle = haystack[:idx]
        sequences.add(needle)
        if len(needle) == 1:
            break

        split_size += 1

    return sorted(list(sequences), reverse=True)


def chunked_haystack(haystack: str, chunk_size: int) -> List[str]:
    """ Takes a haystack and splits it into `n` chunks of `chunk_size` strings
    """

    chunks = []
    for idx in range(0, len(haystack), chunk_size):
        chunks.append(haystack[idx:idx+chunk_size])

    return chunks


def check_repetitions(haystack: str, needle: str) -> bool:
    """ Given a haystack and needle, check if the haystack is made of
        repetitions of the needle
    """

    needle_len = len(needle)
    chunks = chunked_haystack(haystack, needle_len)
    if all(map(lambda chunk: chunk == needle, chunks)):
        return True

    return False


if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as input_file:
        contents = ",".join(input_file.readlines())
        for id_range in contents.split(","):
            id_range = id_range.strip()
            begin, end = id_range.split("-")
            print(f"{begin=}, {end=}")

            for num in range(int(begin), int(end)+1):
                num_str = str(num)
                needles = generate_potential_repetition_sequences(num_str)
                for needle in needles:
                    if check_repetitions(num_str, needle):
                        print(f"found invalid id {num}")
                        invalid_ids.append(num)
                        break

print(sum(invalid_ids))
