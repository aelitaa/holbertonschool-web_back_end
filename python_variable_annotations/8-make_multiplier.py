#!/usr/bin/env python3
""" Contains func make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], [float]]:
    """ multiplier returning func """
    def multiplier_function(x: float) -> float:
        return float(x * multiplier)

    return multiplier_function
