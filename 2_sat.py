from z3 import *

s = Solver() 

x_1 = Bool("x_1")
x_2 = Bool("x_2")
x_3 = Bool("x_3")
x_4 = Bool("x_4")
x_5 = Bool("x_5")
x_6 = Bool("x_6")
x_7 = Bool("x_7")
x_8 = Bool("x_8")
x_9 = Bool("x_9")
x_10 = Bool("x_10")

eq_1_1 = And(Not(x_1),x_2,x_3,x_4)
eq_1_2 = And(x_1,Not(x_2),x_3,x_4)
eq_1_3 = And(x_1,x_2,Not(x_3),x_4)
eq_1_4 = And(x_1,x_2,x_3,Not(x_4))

eq_1 = Or(eq_1_1, eq_1_2, eq_1_3, eq_1_4)

eq_2_1 = And(Not(x_1),x_5,x_6,x_7)
eq_2_2 = And(x_1,Not(x_5),x_6,x_7)
eq_2_3 = And(x_1,x_5,Not(x_6),x_7)
eq_2_4 = And(x_1,x_5,x_6,Not(x_7))

eq_2 = Or(eq_2_1, eq_2_2, eq_2_3, eq_2_4)

eq_3_1 = And(Not(x_2),x_5,x_8,x_9)
eq_3_2 = And(x_2,Not(x_5),x_8,x_9)
eq_3_3 = And(x_2,x_5,Not(x_8),x_9)
eq_3_4 = And(x_2,x_5,x_8,Not(x_9))

eq_3 = Or(eq_3_1, eq_3_2, eq_3_3, eq_3_4)

eq_4_1 = And(Not(x_3),x_6,x_8,Not(x_10))
eq_4_2 = And(Not(x_3),Not(x_6),x_8,x_10)
eq_4_3 = And(x_3,x_6,Not(x_8),Not(x_10))
eq_4_4 = And(Not(x_3),x_6,Not(x_8),x_10)
eq_4_5 = And(x_3,Not(x_6),x_8,Not(x_10))
eq_4_6 = And(x_3,Not(x_6),Not(x_8),x_10)

eq_4 = Or(eq_4_1, eq_4_2, eq_4_3, eq_4_4, eq_4_5, eq_4_6)


eq_5_1 = And(Not(x_4),x_7,x_9,Not(x_10))
eq_5_2 = And(Not(x_4),Not(x_7),x_9,x_10)
eq_5_3 = And(x_4,x_7,Not(x_9),Not(x_10))
eq_5_4 = And(Not(x_4),x_7,Not(x_9),x_10)
eq_5_5 = And(x_4,Not(x_7),x_9,Not(x_10))
eq_5_6 = And(x_4,Not(x_7),Not(x_9),x_10)

eq_5 = Or(eq_5_1, eq_5_2, eq_5_3, eq_5_4, eq_5_5, eq_5_6)

s.add(eq_1)
s.add(eq_2)
s.add(eq_3)
s.add(eq_4)
s.add(eq_5)

print(s.check())

model = s.model()

print(model)