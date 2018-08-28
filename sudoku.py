



def main():
    filename = input('Enter sudoku puzzle file name: ')
    with open( filename, 'r' ) as f:
       plines = [line.split() for line in f]
    

if __name__ == "__main__":
    main()