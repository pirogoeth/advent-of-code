#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from collections import namedtuple
from copy import copy
from pprint import pprint
from typing import Dict, Iterable, List, Tuple

Point = namedtuple("Point", ["x", "y"])
_PAPER_ROLL = "@"
_EMPTY = "."
_ACCESSIBLE = "x"

positions: List[List[str]] = []


def debug(*args, **kw):
    if os.getenv("DEBUG") == "1":
        print(*args, **kw)


def get_adjacent_points(point: Point) -> Iterable[Point]:
    """ Returns the points adjacent to `point` excluding any 
        that would fall out-of-bounds
    """

    maxY = len(positions)
    maxX = len(positions[0])

    adjacent = [
        # Above
        Point(x=point.x-1, y=point.y-1),
        Point(x=point.x,   y=point.y-1),
        Point(x=point.x+1, y=point.y-1),
        # Side-by-side
        Point(x=point.x-1, y=point.y),
        Point(x=point.x+1, y=point.y),
        # Below
        Point(x=point.x-1, y=point.y+1),
        Point(x=point.x,   y=point.y+1),
        Point(x=point.x+1, y=point.y+1),
    ]

    return filter(
        lambda p: not any([
            p.x < 0,
            p.y < 0,
            p.x >= maxX,
            p.y >= maxY,
        ]),
        adjacent,
    )


def get_full_adjacent_spots(point: Point) -> List[Point]:
    """ Checks all adjacent points, returning whether the point is full
    """

    debug(f"Getting adjacent points for {point=}")

    spots = []
    for adjacent in get_adjacent_points(point):
        loc = positions[adjacent.y][adjacent.x]
        debug(f" {adjacent=}, {loc=}")
        if loc == _PAPER_ROLL:
            spots.append(point)

    return spots


def find_accessible_paper_rolls() -> List[Point]:
    """ Iterate over the 'map' finding rolls that are forklift-accessible
    """

    accessible = []
    for y, row in enumerate(positions):
        for x, item in enumerate(row):
            if item == _PAPER_ROLL:
                debug(f"Location {x=}, {y=}, {item=}")
                point = Point(x=x, y=y)
                if len(get_full_adjacent_spots(point)) < 4:
                    accessible.append(point)

    return accessible


def render_accessible_overlay(accessible: List[Point]):
    """ Overlay accessible points on top of the initial map
    """

    accessible_map = copy(positions)
    for point in accessible:
        accessible_map[point.y][point.x] = _ACCESSIBLE

    for row in accessible_map:
        print("".join(row))


if __name__ == "__main__":
    with io.open(sys.argv[1], "r") as input_file:
        for line in input_file.readlines():
            line = line.strip()
            positions.append(["" for _ in line])
            for idx, content in enumerate(line):
                positions[-1][idx] = content

    debug(positions)

    accessible = find_accessible_paper_rolls()
    debug(accessible)

    render_accessible_overlay(accessible)
    print(f"{len(accessible)} rolls are accessible")
