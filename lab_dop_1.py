print("Введите коэффициенты ax^2 + bx + c = 0")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

D = b**2 - 4 * a * c
print('D= ', D)
if D > 0:
  x1 = ((-b + (D**0.5)) / (2 * a))
  x2 = ((-b - (D**0.5)) / (2 * a))
  print(f"x1 = {x1}, x2 = {x2}")
elif D == 0:
  x = -b / (2 * a)
  print("x= ", x2)
else:
  print("нет корней")