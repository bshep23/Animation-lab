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
class Fish:
  """Definition for a fish with a body, eye, and tail"""
  def __init__(self, win, position):
    """constructs a fish made of 1 oval centered at `position`,
    a second oval for the tail, and a circle for the eye"""
    
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    
    # body
    p1 = Point(position.getX()-40, position.getY()-20)
    p2 = Point(position.getX()+40, position.getY()+20)
    self.body = Oval( p1, p2 )
    self.body.setFill(color_rgb(red, green, blue))
    
    # tail
    p1 = Point(position.getX()+30, position.getY()-30)
    p2 = Point(position.getX()+50, position.getY()+30)
    self.tail = Oval( p1, p2 )
    self.tail.setFill( "black" )
    
    # eye
    center2 = Point( position.getX()-15, position.getY()-5 )
    self.eye = Circle( center2, 5 )
    self.eye.setFill( "black" )
  
  def draw( self, win ):
    """draw the fish to the window"""
    self.body.draw( win )
    self.tail.draw( win )
    self.eye.draw( win )
