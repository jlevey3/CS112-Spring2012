#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""

from pygame import Rect

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False

def poly_in_rect(poly, rect):
    "check if polygon is within rectangle"
	inside = False
    for (x,y) in poly:
		if rect.collidepoint((x,y)):
			inside = True
		else:
			inside = False
	return inside


# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect

def surround_poly(poly):
    "create a rectangle which surrounds a polygon"
	xmin, ymin = xmax, ymax = poly[0]
	for point in poly:
		x,y = point
		
		if x<=xmin:
			x=xmin
		if x>=xmax:
			x=xmax
		if y<=ymin:
			y=ymin
		if y>=ymax:
			y=ymax
		return Rect(xmin,ymin,(xmax-xmin+1),(ymax-ymin+1))

