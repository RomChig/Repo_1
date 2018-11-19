a=int(input("Введите число от 0 до 1000: "))
while a<0 or a>1000:
	a = int(input("Неверный ввод,введите строго [0;1000] "))
if a%2!=0 or a==2:
	print(True)
else:
	print(False)


