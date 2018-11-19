a=int(input())
while a<0:
	a = int(input("Введите заново,строго >0"))
x=int(input())
def a_1(x):
	x**=x
	print(x)
	print(a)
	a_1(x)
	if x.isnotdigit():
		print("ergerg")






















