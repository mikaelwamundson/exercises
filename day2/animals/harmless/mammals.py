class Mammals:
	"""
	Class for representing mammals.
	"""

	def __init__(self):
		self.members = ["Dog", "Cat", "Badger"]

	def __str__(self):
		return("This is a mammal!")

	def printMembers(self):
		print("Printing members of the Mammals class.")
		for member in self.members:
			print("\t{:s} ".format(member))
