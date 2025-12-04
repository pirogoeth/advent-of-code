#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import sys

if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as input_file:
        for line in input_file.readlines():
            pass
