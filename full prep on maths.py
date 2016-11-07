Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
print ('\t8 cats have 4 legs each\n   The cats have 8*4 legs in total!')
	8 cats have 4 legs each
   The cats have 8*4 legs in total!
>>> print ('\t8 cats have 4 legs each\n   The cats have '8*4' legs in total!')
SyntaxError: invalid syntax
>>> 8*4
32
>>> print ('\t8 cats have 4 legs each\n   The cats have 32 legs in total!')
	8 cats have 4 legs each
   The cats have 32 legs in total!
>>> print (' A farmer with 1089 sheep sells 56 of them\n\t The farmer has 1089-56 sheep left')
 A farmer with 1089 sheep sells 56 of them
	 The farmer has 1089-56 sheep left
>>> 1089-56
1033
>>> print (' A farmer with 1089 sheep sells 56 of them\n    The farmer has 1033 sheep left')
 A farmer with 1089 sheep sells 56 of them
    The farmer has 1033 sheep left
>>> print (' A farmer with 1089 sheep sells 56 of them\n    The farmer has 1033 sheep left!')
 A farmer with 1089 sheep sells 56 of them
    The farmer has 1033 sheep left!
>>> print ('\t 4 children pick 56 flowers each
       
SyntaxError: EOL while scanning string literal
>>> print ('\t 4 children pick 56 flowers each\n The children each have 56 flowers')
	 4 children pick 56 flowers each
 The children each have 56 flowers
>>> print ('\t     4 children pick 56 flowers each\n      The children each have 56 flowers')
	     4 children pick 56 flowers each
      The children each have 56 flowers
>>> print ('\t 4 children pick 56 flowers each\n      The children each have 56 flowers')
	 4 children pick 56 flowers each
      The children each have 56 flowers
>>> print ('Predictions for question 1 = 7 and for question 2 = 0.333333')
Predictions for question 1 = 7 and for question 2 = 0.333333
>>> 5+3/6*4
7.0
>>> (5+3)/(6*4)
0.3333333333333333
>>> print('both prediction right. YAY! ')
both prediction right. YAY! 
>>> 
