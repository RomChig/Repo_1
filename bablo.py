a=input()
c=input()
class Money:
	def __init__(self,a,c):
		self.a=float(a)
		self.c=c

	'''def check(self):
		if self.a>100:
			print("Good money)")
			if self.c=="$":
				print("Very good")
		else :
			print("small money")
	'''
	def check(self):
		if self.c=='$':
			self.a/=28
		print(self.a)


valut_1=Money(a,c)
valut=Money(a,c)
valut.check()
