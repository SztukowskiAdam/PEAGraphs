class Matrix():
	def __init__(self, directed):
		self.matrix = []
		self.indexes = []
		self.directed = directed

	def printMatrix(self):
		for i in range(len(self.matrix)):
			print(self.matrix[i])

	def addPeak(self, peakNumber):
		self.indexes.append(peakNumber)
		self.matrix.append([0 for x in range(len(self.indexes)-1)])
		for i in range(len(self.matrix)):
			self.matrix[i].append(0)
		self.matrix[-1][-1] = -1

	def addEdge(self, startingPeak, endingPeak, weight):
		self.matrix[self.indexes.index(startingPeak)][self.indexes.index(endingPeak)] = weight

		if self.directed is False:
			self.matrix[self.indexes.index(endingPeak)][self.indexes.index(startingPeak)] = weight

	def removePeak(self, peakNumber):
		for peaks in self.matrix:
			peaks.pop(self.indexes.index(peakNumber))
		self.matrix.pop(self.indexes.index(peakNumber))
		self.indexes.remove(peakNumber)

	def removeEdge(self, startingPeak, endingPeak):
		self.matrix[self.indexes.index(startingPeak)][self.indexes.index(endingPeak)] = 0

		if self.directed is False:
			self.matrix[self.indexes.index(endingPeak)][self.indexes.index(startingPeak)] = 0



matrix = Matrix(False)

for line in open('peaks.txt'):
	matrix.addPeak(int(line[:-1]))

for line in open('graph2.txt'):
	edgeList = line.split()
	matrix.addEdge(int(edgeList[0]), int(edgeList[1]), int(edgeList[2]))

matrix.printMatrix()
