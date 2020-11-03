# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:53:03 2020

@author: straw
"""
class Hanoi:
    def __init__(self, n):
        self.towers = ['A', 'B', 'C']
        self.n = n
        self.board = {
                        "towers": self.towers,
                        "disks": [[i for i in range(self.n,0,-1)], [], []]
                        }
        
    def print_game(self):
        print("Game of {0} disks and 3 towers.".format(self.n))
    
    def solve(self, n, start, middle, end):
        if n == 0:
        # No more discs to move in this step
            return
        # move disc from start to middle with end
        self.solve(n-1, start, end, middle)
        if start:
            # move disc from start to end with middle
            end.append(start.pop())
            #print("Move disk %i from tower %s to tower %s" %(n, start, end))
            print('Tower {0} {1} | Tower {2} {3} | Tower {4} {5}'.format(self.board['towers'][0],start,self.board['towers'][1],middle,self.board['towers'][2],end))
    
        # move n-1 discs from middle to end with start
        self.solve(n-1, middle, start, end)


if __name__ == '__main__':
    n = 3
    h = Hanoi(n)
    print('Board\'s current state : {}'.format(h.board['disks']))
    print()
    h.solve(n, h.board['disks'][0], h.board['disks'][1], h.board['disks'][2])


