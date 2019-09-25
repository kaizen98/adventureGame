import sys

class adventureGame:

	def startGame(self, map):
		self.map = map
		self.currentPosition = self.findPlayerPosition()

	def endGame(self):
		pass

	def getStatus(self):
		jsMap = []
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				if self.map[i][j] == "-":
					jsMap.append("hwall")
				elif self.map[i][j] == "|":
					jsMap.append("vwall")
				elif self.map[i][j] == " ":
					jsMap.append("space")
			jsMap.append("newline")
		return jsMap

	def findPlayerPosition(self):
		for row in self.map:
			join_list = "".join(row)
			if join_list.find("x") != -1:
				return [self.map.index(row), row.index("x"[0])]

	def move(self, direction):
		if direction == "w":
			coordinates = [(self.currentPosition[0]-1),(self.currentPosition[1])]
		elif direction == "a":
			coordinates = [(self.currentPosition[0]),(self.currentPosition[1]-1)]
		elif direction == "d":
			coordinates = [(self.currentPosition[0]),(self.currentPosition[1]+1)]
		elif direction == "s":
			coordinates = [(self.currentPosition[0]+1),(self.currentPosition[1])]

		canMove = False if self.map[coordinates[0]][coordinates[1]] in ["-","|"] else True

		if canMove:
			self.map[coordinates[0]][coordinates[1]] = self.map[self.currentPosition[0]][self.currentPosition[1]]
			self.map[self.currentPosition[0]][self.currentPosition[1]] = " "
			self.currentPosition = self.findPlayerPosition()
		else:
			print("There's a wall there! Try again.")