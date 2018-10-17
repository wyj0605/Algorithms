#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Bubble_Sort(alist):
    n=len(alist)
    for i in range(n):
        for j in range(n-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist


alist=[2,5,1,6,34534,345345,345,345,34,63,456]

Bubble_Sort(alist)

print (alist)
