def fact(v):
    i = 1
    for factorial in range(1, v+1):
     i = i*factorial
    return i

def discriminant(a, b, c):
   D = int((b**2)-4*a*c)
   return D

def discKorni(a, b, c, D):
    if D > 0 :
     x1 = (-b + (D**0.5))/2a 
     x2 = (-b - (D**0.5))/2a
     return x1, x2
    elif == 0 :
     x = -(b\2a)
     return x
    else :
     return False