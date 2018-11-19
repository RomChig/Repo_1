a=int(input("Ведите 1-ое число: "))
b=int(input("Ведите 2-ое число: "))
c=input("Ведите операцию ('+','-','/','*'): ")
def arithmetic(a,b,c):
	if c=='+':
		print(a+b)
	elif c=='-':
		print(a-b)
	elif c=='/':
		print(a/b)
	elif c=='*':
		print(a*b)
	else :
		print("Неизвестная операция ")
arithmetic(a,b,c)







