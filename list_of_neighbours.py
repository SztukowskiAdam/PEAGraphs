class ListOfNeighbours():
	def __init__(self, directed):
		self.list = []
		self.indexes = []
		self.directed = directed

	def printList(self):

		for i in range(len(self.indexes)):
			peak = '['+str(self.indexes[i]) + '] -> '
			for neighbours in self.list[i]:
				peak += str(neighbours)
				peak += ' '
			print(peak)
			peak = ''

	def addPeak(self, peakNumber):
		self.indexes.append(peakNumber)
		self.list.append([])

	def addEdge(self, startingPeak, endingPeak, weight):
		self.list[self.indexes.index(startingPeak)].append([endingPeak, weight])

		if self.directed is False:
			self.list[self.indexes.index(endingPeak)].append([startingPeak, weight])

	def removeEdge(self, startingPeak, endingPeak):
		for edge in self.list[self.indexes.index(startingPeak)]:
			if edge[0] == endingPeak:
				self.list[self.indexes.index(startingPeak)].remove(edge)
	def removePeak(self, peakNumber):
		self.list.pop(self.indexes.index(peakNumber))

		for peak in self.list:
			for edge in peak:
				if edge[0] == peakNumber:
					peak.remove(edge)

		self.indexes.remove(peakNumber)


lista = ListOfNeighbours(False)

for line in open('peaks.txt'):
	lista.addPeak(int(line[:-1]))


for line in open('graph2.txt'):
	edgeList = line.split()
	lista.addEdge(int(edgeList[0]), int(edgeList[1]), int(edgeList[2]))


lista.removePeak(2)
lista.printList()

	

