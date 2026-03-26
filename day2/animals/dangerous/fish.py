class Fish:
	"""
	Class for representing fish.
	"""

	def __init__(self):
		self.members = ["Pike", "Shark", "Salmon"]

	def __str__(self):
		return("This is a fish!")

	def printMembers(self):
		print("Printing members of the Fish class.")
		for member in self.members:
			print("\t{:s} ".format(member))
