#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:05:52 2021

@author: wnangziqi
"""

a=[i for i in range(1,100)]

b=[]

b=a[::2]

c=sum(b)

print(c,b)

d=[i for i in range(1,100) if i%2!=0]
print(sum(d))
