import copy

class Entry:
    '''
    Entry for every square
    '''
    def __init__(self, i):
        self.options = set()
        self.num = i
        
def search(grid, mappings, index):
    if index == len(mappings):
        solution = []
        for entry in grid:
            solution.append(entry.num)
        print solution
        return True 
    
    if index > len(mappings):
        return False;
    
    currentEntry = mappings[index][0]
    
    if not grid[currentEntry].options:
        return False;
    
    '''
    I could also update mappings after every successful iteration, but the algorithm
    is already more complex than it needs to be for such a small state problem.
    '''
    for option in grid[currentEntry].options:
        gridCopy = copy.deepcopy(grid)
        gridCopy[currentEntry].num = option
        updateGrid(gridCopy, currentEntry, option)
        
        if search(gridCopy, mappings, index + 1) == True:
            grid = gridCopy
            return True;

    return False

def updateGrid(grid, currentEntry, option):
    row = currentEntry / 9
    col = currentEntry % 9
    offset = (row / 3) * 3 + (col / 3) * 27
    print row, col
    for j in range(9):
        '''
        I think this works
        '''
        l1 = grid[row * 9 + j].options
        l2 = grid[col + 9 * j].options
        if not l1:
            for i, n in enumerate(l1):
                if n == option:
                    del l1[i]
            
        if not l2:
            for i, n in enumerate(l2):
                if n == option:
                    del l2[i]
        
        jRow = j / 3
        jCol = j % 3
        print jRow * 9 + jCol + offset, offset
        lb = grid[jRow * 9 + jCol + offset].options
        if not lb:
            for i, n in enumerate(lb):
                if n == option:
                    del lb[i]
            
                    
def sameRow(i, j): 
    return (i / 9 == j / 9)

def sameCol(i, j): 
    return (i - j) % 9 == 0

def sameBlock(i, j): 
    return (i / 27 == j / 27 and i % 9 / 3 == j % 9 / 3)

def setupGrid(grid):
    for i, entry in enumerate(grid):
        if entry.num != '0':
            continue
        
        for j in range(81):
            if sameBlock(i, j) or sameCol(i, j) or sameRow(i, j):
                entry.options.add(grid[j].num)
                
        tempList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        tempSet = set([n for n in tempList if n not in entry.options])
        entry.options = tempSet

def getGridMappings(grid):
    mappings = []
    for i, entry in enumerate(grid):
        if entry.num == '0':
            obj = (i, len(entry.options)) 
            mappings.append(obj)
    mappings.sort(key=lambda x:x[1])
    return mappings

if __name__ == '__main__':
    '''
    Read file and create list
    '''
    inputFile = raw_input("Enter your input Sudoku file: ");
    fo = open(inputFile)
    line = fo.readline()
    fo.close()
    print line
    '''
    Setup list and create mappings for zero entries
    '''
    grid = [Entry(i) for i in line]
    setupGrid(grid)
    mappings = getGridMappings(grid)
    print mappings
    '''
    Search for solution
    '''
    solution = []
    if search(grid, mappings, 0) == True:
        for entry in grid:
            solution.append(entry.num)
    print solution
    pass
