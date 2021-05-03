from queue import PriorityQueue


class State(object):
    def __init__(self, value, parent, start=0, goal=0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal


def getDist(self):
    pass


def createChildren(self):
    pass


class State_string(State):
    def __init__(self, value, parent, start=0, goal=0):
        super(State_string, self).__init__(value, parent, start, goal)
        self.dist = self.getDist()

    def getDist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist +=0

# def check_grid(grid, board_size):
#     numOfBolck = 0
#     for i in grid:
#        numOfBolck+=len(i)
#     if(numOfBolck != (board_size * board_size)):
#         print("there are missing info to solve the problem please fix and try again ")
#     return
# def foundStart(grid , board_size):
#     countFailure = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#          if grid[i][j] == 'A':
#              return j
#         else:
#             countFailure+=1
#     if countFailure == board_size:
#         print("there is no start position please check the input file")
#     return
#
# def runRobot(start,grid,cost,movement):
#     road=[]
#     #for i in range
#
#
# def main():
#     input_file = open('files\input.txt','r')
#     lines = input_file.read().splitlines()
#     algorithem_type=lines[0]
#     borad_size = int(lines[1])
#     grid=[]
#     currentBoard = 0
#     count = 0
#     for line in lines[2:]:
#         grid.append(list(line))
#     print(grid)
#     movement =['U','D','R','L']
#     cost={'road': 1 , 'dirt_road' : 4}
#     check_grid(grid ,borad_size)
#     start = foundStart(grid,borad_size)
#     runRobot(start,grid,cost,movement)
#
# if __name__ == '__main__':
#     main()
