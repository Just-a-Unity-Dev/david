class writer():
	def __init__(self) -> None:
		self.disk = "bank1"
		self.output = None

	def write(self, iterator, data):
		return f"write {iterator} {self.disk} {data}"

	def fullwrite(self, rdata):
		tempOutput = []
		data = [x.strip() for x in rdata]
		i = 0

		for f in data:
			tempOutput.append(self.write(i, data[i]))
			i += 1

		self.output = tempOutput