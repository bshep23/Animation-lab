# -------------------------------------------------
#        Name: Blake Shepherd and Lilana Linan
#    Filename: Animation.py
#        Date: July 31th, 2019 
#
# Description: Praticing with animation
#               
# -------------------------------------------------
from graphics import *
import random
from Fish import *


win = GraphWin("Hello", 600, 400)

def main():
  bob = Fish(win, Point(300,200))
  bob.draw(win)
  
  rick = Fish(win, Point(100,350))
  rick.draw(win)
  

  dory = Fish(win, Point(400,350))
  dory.draw(win)
  

  king = Fish(win, Point(75, 100))
  king.draw(win)
 
# Challenge 2 
  for i in range(100):
    bob.move(-20)
    rick.move(-50)
    dory.move(-10)
    king.move(-20)

  




if __name__ == "__main__":
  main()


  

