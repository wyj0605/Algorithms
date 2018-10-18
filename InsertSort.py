#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insert_sort(alist):
    for i in range(1,(len(alist))):
        curvalue = alist[i]
        pos=i
        while pos >0 and  alist[pos-1] > curvalue:
            alist[pos]=alist[pos-1]
            pos=pos-1
        alist[pos] = curvalue

    return alist


alist=[2,5,1,6,6,34534,345345,345,345,34,63,456]

insert_sort(alist)
print (alist)
