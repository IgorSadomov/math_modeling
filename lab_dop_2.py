a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))

if a+b <= c or a+c <= b or b+c <= a:
    print("такого треугольника не существует")
elif a==b and b==c and a==c:
    print("треугольник равносторонний")
elif a != b and a != c and b != c:
    print("треугольник разносторонний")
else:
    print("треугольник равнобедренный")