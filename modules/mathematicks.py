def fact(v):
    i = 1
    for factorial in range(1, v+1):
     i = i*factorial
    return i

def discriminant(a, b, c):
   D = int((b**2)-4*a*c)
   return D
