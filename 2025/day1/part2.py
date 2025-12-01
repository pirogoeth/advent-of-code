#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import math
import sys


class Dial:
    value: int = 50
    crossed_zero: int = 0

    def is_zero(self) -> int:
        return self.value == 0

    def calculate_crossings(self, magnitude: int) -> int:
        num_crossings = math.floor(abs(magnitude) / 100)
        remainder = abs(magnitude) % 100
        # Left
        if magnitude < 0 and 0 < self.value <= remainder:
            return num_crossings + 1
        # Right
        elif magnitude > 0 and (remainder + self.value) > 99:
            return num_crossings + 1

        return num_crossings

    def turn_left(self, amount: int):
        self.crossed_zero += self.calculate_crossings(amount * -1)

        amount = amount % 100
        if amount > self.value:
            self.value = 100 - (amount - self.value)
        else:
            self.value -= amount

    def turn_right(self, amount: int):
        self.crossed_zero += self.calculate_crossings(amount)

        self.value = (self.value + amount) % 100


if __name__ == "__main__":
    dial = Dial()
    with io.open(sys.argv[1], "r") as directions_file:
        for line in directions_file.readlines():
            direction, amount = line[0], int(line[1:])
            prev = dial.value
            if direction.lower() == "l":
                dial.turn_left(amount)
                print(f"{prev=} turned left {amount} -> {dial.value}")
            elif direction.lower() == "r":
                dial.turn_right(amount)
                print(f"{prev=} turned right {amount} -> {dial.value}")

            print(f"Crossing counter: {dial.crossed_zero}")

    print(dial.crossed_zero)
