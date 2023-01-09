class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.right = None
        self.left = None
        self.red = False


class RBTree:
    def __init__(self):
        self.nil = Node(0)
        self.root = self.nil

    def search(self, val):
        current = self.root
        flag = 0
        while current != self.nil :

            if val.casefold()==current.value.casefold():
                flag = 1
                break
            elif val.casefold() < current.value.casefold():
                current = current.left
            elif val.casefold() > current.value.casefold():
                current = current.right
        if flag == 0:
            return 0
        elif flag==1:
            return 1


    def rotateLeft(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def fixTree(self,node):
        while node!=self.root and node.parent.red :
            if node.parent==node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.red: #case 1
                    uncle.red=False
                    node.parent.red=False
                    node.parent.parent.red=True
                    node=node.parent.parent
                elif node==node.parent.right: #case 2
                    node=node.parent
                    self.rotateLeft(node)
                    node.parent.red=False
                    node.parent.parent.red=True
                    self.rotateRight(node.parent.parent)
                else:  #case 3
                    node.parent.red=False
                    node.parent.parent.red=True
                    self.rotateRight(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.red: #case 1
                    uncle.red=False
                    node.parent.red=False
                    node.parent.parent.red=True
                    node=node.parent.parent
                elif node==node.parent.left: #case 2
                    node=node.parent
                    self.rotateRight(node)
                    node.parent.red=False
                    node.parent.parent.red=True
                    self.rotateLeft(node.parent.parent)
                else:
                    node.parent.red=False
                    node.parent.parent.red=True
                    self.rotateLeft(node.parent.parent)
        self.root.red=False


    def insert(self, val):
        node = Node(val)
        node.parent = None
        node.value = val
        node.left = self.nil
        node.right = self.nil
        node.red = True

        parent=None
        x = self.root
        while x != self.nil:
            parent=x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent=parent
        if parent == None:
            self.root = node
            self.red = False

        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node

        if node.parent == None:
            return

        if node.parent.parent == None:
            return
        self.fixTree(node)


    def printTreeHeight(self,node):
        if node==self.nil:
            return 0
        else:
            return 1+max(self.printTreeHeight(node.right),self.printTreeHeight(node.left))


    def printTreeSize(self,node):
        if node==self.nil:
            return 0
        else:
            return 1+self.printTreeSize(node.right)+self.printTreeSize(node.left)

    def insertDictionary(tree):

        file_path = 'EN-US-Dictionary.txt'

        file_text = open(file_path, "r")

        a = True


        while a:
            file_line = file_text.readline().rstrip('\n')
            tree.insert(file_line.lower())


            if not file_line:
                print("End Of File")
                a = False
        file_text.close()

    def insertWord(self):
        keyInsert = input("please enter the word you want to insert")
        if (tree.search(keyInsert)==0):
            tree.insert(keyInsert)
            f = open("EN-US-Dictionary.txt", "a")
            f.write("\n"+keyInsert)
            f.close()

        else: print("ERROR:Word already in the dictionary!")

    def searchWord(self):
        keyF = input("please enter the word to be searched for")
        if(tree.search(keyF)==0):
            print("NO")
        else: print("YES")



tree=RBTree()
tree.insertDictionary()
print(tree.printTreeHeight(tree.root))
print(tree.printTreeSize(tree.root))
tree.insertWord()
tree.searchWord()

