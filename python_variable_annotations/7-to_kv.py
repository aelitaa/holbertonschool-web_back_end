#!/usr/bin/env python3
""" Comtains function to_kv """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ takes str, int/float, returns tuple """
    return (k, v ** 2)
