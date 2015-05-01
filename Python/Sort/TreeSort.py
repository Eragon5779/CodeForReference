class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class tree:
    def __init__(self):
        self.root = None

    def insert(self, num):
        current = self.root
        parent = None
        while current != None:
            parent = current
            if (num > current.value):
                current = current.right
            else:
                current = current.left
        newNode = node(num)
        newNode.parent = parent
        if (parent == None):
            self.root = newNode
        elif (parent.value < num):
            parent.right = newNode
        else:
            parent.left = newNode

def fillTree(sortTree, sortablelist):
    for x in sortablelist:
        sortTree.insert(x)
    return sortTree

def runTree(sortTree, current):
    sortedList = []
    if (current.left != None):
        temp = runTree(sortTree, current.left)
        sortedList += temp
    sortedList.append(current.value)
    if (current.right != None):
        temp = runTree(sortTree, current.right)
        sortedList += temp
    return sortedList
