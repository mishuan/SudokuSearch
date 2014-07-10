class Entry:
    '''
    Entry for every square
    '''
    def __init__(self, i):
        self.options = set()
        self.num = i
        
def search(grid):
    
    pass

def sameRow(i, j): 
    return (i / 9 == j / 9)

def sameCol(i, j): 
    return (i - j) % 9 == 0

def sameBlock(i, j): 
    return (i / 27 == j / 27 and i % 9 / 3 == j % 9 / 3)

def setupGrid(grid):
    count = 0
    for i, entry in enumerate(grid):
        if entry.num != '0':
            continue
        
        for j in range(81):
            if sameBlock(i, j) or sameCol(i, j) or sameRow(i, j):
                entry.options.add(grid[j].num)
                
        tempList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        tempSet = set([n for n in tempList if n not in entry.options])
        entry.options = tempSet
        count += 1
    return count
    
if __name__ == '__main__':
    
    inputFile = raw_input("Enter your input Sudoku file: ");
    fo = open(inputFile)
    '''
    lines = [line.strip() for line in open(inputFile)]
    grid = [map(int, str(line)) for line in lines]
    print grid
    '''
    line = fo.readline()
    fo.close()
    print line
    grid = [Entry(i) for i in line]
    emptySquares = setupGrid(grid)
    for entry in grid:
        print entry.options
    print emptySquares
    pass
