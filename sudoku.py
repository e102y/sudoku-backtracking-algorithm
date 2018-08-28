
class sudokuBoard():
    def __init__(self, filename):
        with open( filename, 'r' ) as f:
            self.plines = [line.split() for line in f]
    
    def show(self):
        for line in self.plines:
            print(line)

    def getRow(self,r):
        return self.plines[r]

    def getCol(self,c):
        tmp = []
        for row in range(9):
            tmp.append(self.plines[row][c])
        return tmp
    def getSq(self,r,c):
        tmp = []
        for row in range(3):
            for col in range(3):
                tmp.append(self.plines[row + r][col + c])
        return tmp

def main():
    #TODO input('Enter sudoku puzzle filename: ') 
    filename = 'puzzle'
    b = sudokuBoard(filename)
    b.show()
    print('#######################')
    print( b.getSq(1,1) )

if __name__ == "__main__":
    main()