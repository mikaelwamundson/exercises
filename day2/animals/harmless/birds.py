class Birds:
	"""
	Class for representing birds.
	"""

	def __init__(self):
		self.members = ["Seagull", "Eagle", "Falcon"]

	def __str__(self):
		return("This is a bird!")

	def printMembers(self):
		print("Printing members of the Birds class.")
		for member in self.members:
			print("\t{:s} ".format(member))
