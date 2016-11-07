Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 
>>> 
>>> myname = "Sir Hugo North
SyntaxError: EOL while scanning string literal
>>> myname = "Sir Hugo North"
>>> myage = "is 14"
>>> Print (myname,myage)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Print (myname,myage)
NameError: name 'Print' is not defined
>>> myname = "Sir Hugo North"
>>> myage = "is 14"
>>> print (myname,myage)
Sir Hugo North is 14
>>> myeyes = ". His eyes are deep blue"
>>> myheight = "and he is 1.65 metres tall.
SyntaxError: EOL while scanning string literal
>>> myheight = "and he is 1.65 metres tall."
SyntaxError: EOL while scanning string literal
>>> myheight = "and he is 1.65 metres tall"
>>> print (myname,myage,myeyes,myheight)
Sir Hugo North is 14 . His eyes are deep blue and he is 1.65 metres tall
>>> 
