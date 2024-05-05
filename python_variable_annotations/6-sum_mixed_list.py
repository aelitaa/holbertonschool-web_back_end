#!/usr/bin/env python3
""" Contains sum_mixed_list func """
from typing import List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sum of mxd_lst of integers and floats """
    return sum(mxd_lst)
