if __name__ == '__main__':
    
    inputFile = raw_input("Enter your input Sudoku file: ");
    fo = open(inputFile)
    print "Name of the file: ", fo.name
    lines = [line.strip() for line in open(inputFile)]
    grid = [map(int, str(line)) for line in lines]
    print grid
    
    pass
