from cmath import pi
import math
from re import A
incoming = float(input('Please enter the number:\n '))
whatis = float(input('for Conversion to Radian Press 1 and for Degree Press 2 \n' ))

if whatis == 2:
    a= (incoming*180) / pi
    print(incoming, "is ",a,' Degrees')
else:
    a = (incoming*pi)/180
    print(incoming, "is ",a,' Radians')


