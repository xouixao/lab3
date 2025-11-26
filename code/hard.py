#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
eps = 1e-10
if __name__ == '__main__':
    x = int(input())
    n = int(input())
    f = (x/2) ** n
    a = 1 / math.factorial(n)
    s, k = a, 0
    while math.fabs(a) > eps:
        k += 1
        a *= (-x**2 / 4) / (k * (k + n))
        s += a
    f *= s
    print(f)
