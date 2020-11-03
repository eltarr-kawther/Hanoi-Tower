# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:26:37 2020

@author: straw
"""
def hanoi(n, start, end, middle):
    if n == 1 :
        print("Move disk %i from tower %s to tower %s" %(n, start, end))
    else:
        hanoi(n-1, start, middle, end)
        print("Move disk %i from tower %s to tower %s" %(n, start, end))
        hanoi(n-1, middle, end, start)
        
hanoi(3, "A", "C", "B")

        