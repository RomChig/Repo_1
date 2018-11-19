

class Money:
	def __init__(self,amount,currency):
		self.amount = float(amount)
		self.currency = currency



	def __str__(self):
		return str(self.amount)+self.currency

	def __check__(self,):
		if self.currency == '$':
			self.amount /= 28
		return str(self.amount)+self.currency

	def __add__(self, other):

		if self.currency != other.currency:
			print(self.currency,'!=',other.currency)
			raise ValueError

		if type(other)==int or type(other)==float:
			return __class__(self.amount+other,self.currency)
		if type(other)==Money:
			return __class__(self.amount + other.amount, self.currency)
		if type(other)==str:
			return __class__(self.amount,self.currency+other)

	'''def __except__(self):
		try:
			if bablo.currency == bablo_1.currency:
				pass
		except ValueError:
			print(False)
	'''

bablo = Money(100,'$')
bablo_1 = Money(100,'UAH')
bablo.__check__()
#summary=bablo+bablo_1
print(bablo+bablo_1)


