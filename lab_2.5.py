a = int(input("первое число: ")) 
b = int(input("второе число: ")) 
if b!= 0 and a%b == 0: 
    print(f'{a} делится на {b}, ответ:', a/b) 
elif b == 0: 
  print (f"ответ: при делении на {b} получается {b}") 
else: 
    print(f'{a} не делится на {b}, остаток:', a%b) 
if b!= 0:     
  print(f' Частное:', a//b)