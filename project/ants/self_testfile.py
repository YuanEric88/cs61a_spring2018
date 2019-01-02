class superclass():
	def __init__(self):
		return
	def remove(self, a = 10):
		self.a = a
		assert isinstance(self, superclass), "the object is not a instance of superclass"
	def newmethod(self):
		return


class subclass(superclass):
	def __init__(self):
		return

	def remove(self, b):
		superclass.remove(self, b)

a = subclass()
a.remove(20)
print(a.a)
print(isinstance(a, superclass))
print(isinstance(a, subclass))
print(subclass.newmethod)
