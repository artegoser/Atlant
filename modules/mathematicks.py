def fact(v):
    i = 1
    for factorial in range(1, v+1):
     i = i*factorial
    return i 
def discriminant(a, b, c):
   D = int((b**2)-4*a*c)
   return D
def diskRoots(a, b, c, D):
    if D > 0 :
     x1 = (-b + (D**0.5))/(2*a)
     x2 = (-b - (D**0.5))/(2*a)
     return x1, x2
    elif D == 0 :
     x = (-(b/(2*a)))
     return x
    else :
     return False
def ARect(x, y):
    #площадь прямоугольника
    return x*y
def PRect(x, y):
    #периметр прямоугольника
    return (2*x)+(2*y)
def PCube (x):
    # периметр куба ,Общая длинна куба
    return 12*x
def ASquare (x):
    #Площадь квадрата
    return x**2
def ACube (x):
    #Площадь куба(поверхность)
    return 6*(x**2)
def VCube (x):
    #Объем куба
    return x**3

   