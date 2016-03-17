import arith

one = arith.NumNode(1)
two = arith.NumNode(2)
three = arith.NumNode(3)

add2 = arith.AddNode(one,two)
print add2.inorder()
print add2.eval()
print '\n'

mul2 = arith.MulNode(two,three)
print mul2.inorder()
print mul2.eval() 
print '\n'

comp = arith.MulNode(add2,mul2)
print comp.inorder()
print comp.eval()
print '\n'

comp2 = arith.AddNode(comp,arith.MulNode(arith.NumNode(10),arith.NumNode(20)))
print comp2.inorder()
print comp2.eval()
print '\n'


