print(25*'=')
print('Simple Calculator')
print(25*'=')
while True:
 x, y, z = input().split()
 if y == '+':
   print(25*'=')
   print(int(x) + int(z))
   print(25*'=')
 elif y == '-':
   print(25*'=')
   print(int(x) - int(z))
   print(25*'=')
 elif y == 'x' or y == '*':
   print(25*'=')
   print(int(x) * int(z))
   print(25*'=')
 elif y == '/':
   print(25*'=')
   print(int(x) / int(z))
   print(25*'=')
 else:
   print('wrong code!!')
  