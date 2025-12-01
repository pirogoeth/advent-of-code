#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io
import sys


class Dial:
    value: int = 50

    def is_zero(self) -> int:
        return self.value == 0

    def turn_left(self, amount: int):
        amount = amount % 100
        if amount > self.value:
            self.value = 100 - (amount - self.value)
        else:
            self.value -= amount

    def turn_right(self, amount: int):
        self.value = (self.value + amount) % 100


print("H")

dial = Dial()
password = 0
with io.open(sys.argv[1], "r") as directions_file:
    for line in directions_file.readlines():
        direction, amount = line[0], int(line[1:])
        if direction.lower() == "l":
            dial.turn_left(amount)
            print(f"Turned left {amount} -> {dial.value}")
        elif direction.lower() == "r":
            dial.turn_right(amount)
            print(f"Turning right {amount} -> {dial.value}")

        if dial.is_zero():
            password += 1

print(password)
