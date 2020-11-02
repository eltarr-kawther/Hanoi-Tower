# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:53:03 2020

@author: straw
"""
class Hanoi:
    def __init__(self, disques, batonnets):
        self.disques = disques
        self.batonnets = batonnets
        
    def print_game(self):
        print("Partie a {0} disques et {1} batonnets.".format(self.disques, self.batonnets))
        