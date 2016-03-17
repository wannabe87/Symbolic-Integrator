class NumNode :
    def __init__(self,num):
        self.num = num

    def eval(self):
        return self.num

    def inorder(self):
        return str(self.num)

class MulNode:
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self):
        return self.e1.eval() * self.e2.eval()

    def inorder(self):
        return "("+self.e1.inorder()+" * "+self.e2.inorder()+")"

class AddNode:
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2

    def eval(self):
        return self.e1.eval() + self.e2.eval()

    def inorder(self):
        return "("+self.e1.inorder()+" + "+self.e2.inorder()+")"
