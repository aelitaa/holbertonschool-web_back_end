#!/usr/bin/env python3
""" Contains func make_multiplier """


def make_multiplier(multiplier: float) -> Callable[[float], [float]]:
    """ multiplier returning func """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
