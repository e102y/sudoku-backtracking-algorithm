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
                tmp.append(self.plines[row + ((r//3)*3)%9][col + ((c//3)*3)%9])
        return tmp
    
    def getVal(self, r, c):
        return int(self.plines[r][c])
    
    ##By: Trent
    def setVal(self, r, c, v):
        self.plines[r][c] = str(v)
        
    ##By: Trent
    def getNextVal(self, r, c):
        R = r
        C = c
        while(C < 9 and self.getVal(R, C) != 0):
            R = R+1
            if(R >= 9):
                R = 0
                C = C+1
        if(C >= 9):
            return (-1, -1)
        else:
            return (R, C)

    ##By: Trent
    def GISB(self, n, m):
        current = self.getVal(n, m)
        okay = False
        used = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        
        print("++test++")
        print("[", n, ", ", m, "]: ")
        self.show()
    
        for elements in self.getCol(m):
            used[int(elements)] = 1

        for stnemele in self.getRow(n):
            used[int(stnemele)] = 1

        for mentsele in self.getSq(n, m):
            used[int(mentsele)] = 1

        for p in range(10):
            q = -1
            if(used[p] == 0):
                q = p
                used[q] = 1
                break
        #print(used[0], " ",used[1], " ",used[2], " ",used[3], " ",used[4], " ",
        #    used[5], " ",used[6], " ",used[7], " ",used[8], " ",used[9])

        print("++test++")
        while(not okay):
            
            if(q == -1):
                self.setVal(n, m, 0)
                return False;
            #set Value
            self.setVal(n, m, q)
            (r, c) = self.getNextVal(n, m)
            if((r, c) == (-1, -1)):
                return True;
            okay = self.GISB(r, c)
            #select next valid number
            for p in range(10):
                q = -1
                if(used[p] == 0):
                    q = p
                    used[q] = 1
                    break
        return okay;

def main():
    #TODO input('Enter sudoku puzzle filename: ') 
    filename = 'puzzle'
    b = sudokuBoard(filename)
    b.show()
    print('#######################')
    print( b.getSq(6,3) )
    print( b.getVal(6,3))
    #commit sudoku
    print('#######################')
    print(b.GISB(0, 0))
    print('#######################')
    b.show()
    

if __name__ == "__main__":
    main()
