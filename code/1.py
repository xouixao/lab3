#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    x = int(input())
    match x:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            print(31)
        case 2:
            print(28)
        case _:
            print(30)
