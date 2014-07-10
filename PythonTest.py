class Test:
    def __init__(self):
        self.listVar = [0, 1, 2, 3, 4, 5]
        self.intVar = 0
        
def modList(var):
    var.listVar.remove(2)
    
def modInt(var):
    var.intVar = 1;
    var.listVar[0] = 1;

def recurseNreturn(obj, var):
    if obj.listVar[var] == 3:
        return True
    obj.listVar[var] = 0;
    return recurseNreturn(obj, var + 1)
    
if __name__ == '__main__':
    
    temp = Test()
    modList(temp)
    print temp.listVar
    modInt(temp)
    print temp.intVar
    print temp.listVar
    tempBool = recurseNreturn(temp, 0)
    print tempBool
    print temp.listVar
    
    set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    set2 = [1, 4, 3, 2, 5]
    set1 = set1.difference(set2)
    print set1
    pass
