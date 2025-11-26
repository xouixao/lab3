#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    if x > y:
        maks = x*x*y
    else:
        maks = x*y*y
    if x - y < x + 2*y:
        mini = x - y
    else:
        mini = x + 2*y
    u = maks*maks + mini*mini
    print(u)
    