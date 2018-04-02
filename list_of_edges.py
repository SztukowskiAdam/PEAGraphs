class ListOfEdges():

	def __init__(self):
		self.list = []

	def printList(self):
		for edge in self.list:
			print(edge)

	def addEdge(self, startingPeak, endingPeak, weight):
		self.list.append([startingPeak, endingPeak, weight])

	def removePeak(self, peak):
		for edge in reversed(self.list):
			if (edge[0] == peak) or (edge[1] == peak):
				self.list.remove(edge)

	def removeEdge(self, startingPeak, endingPeak):
		for edge in reversed(self.list):
			if (edge[0] == startingPeak) and (edge[1] == endingPeak):
				self.list.remove(edge)


lista = ListOfEdges()


for line in open('graph1.txt'):
	edgeList = line.split()
	lista.addEdge(int(edgeList[0]), int(edgeList[1]), int(edgeList[2]))


lista.printList()


