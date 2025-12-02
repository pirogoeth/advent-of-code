#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import sys

invalid_ids = []


if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as input_file:
        contents = ",".join(input_file.readlines())
        for id_range in contents.split(","):
            id_range = id_range.strip()
            begin, end = id_range.split("-")
            print(f"{begin=}, {end=}")

            for num in range(int(begin), int(end)+1):
                num_str = str(num)
                num_len = len(num_str)
                # If the length of the number is odd, skip.
                if num_len % 2 == 1:
                    continue

                fh_end = int((num_len/2))
                fh = num_str[:fh_end]

                lh_begin = int(num_len/2)
                lh = num_str[lh_begin:]

                print(f"{fh=}, {lh=}")
                if fh == lh:
                    invalid_ids.append(num)
                    print(f"found invalid ID {num=}")

print(sum(invalid_ids))
