# (a)
P = "Phong has Visa"
S1 = "If Phong can fly, Phong will go to America"
S2 = "If Phong has Visa, Phong will go to America"
S3 = "If Phong can speak English, Phong will go to America"
C = "Phong goes to America"

if P and S2:
    print("P and S2 -> C")
    print("P:", P)
    print("S2:", S2)
    print("C:", C)
elif P and S1:
    print("P and S1 -> C")
    print("P:", P)
    print("S1:", S1)
    print("C:", C)
elif P and S3:
    print("P and S3 -> C")
    print("P:", P)
    print("S3:", S3)
    print("C:", C)
else:
    print("Conclusion C cannot be proven or disproven with the given data.")

# (b)
P = "It's hot yesterday"
S1 = "If it's hot, it will rain the next day"
S2 = "If and only if it's not rain, Nam goes outside"
S3 = "If it's not hot, Nam will go outside"
C = "Nam goes outside"

if P and S3:
    print("P and S3 -> C")
    print("P:", P)
    print("S3:", S3)
    print("C:", C)
elif P and S2:
    print("P and S2 -> C")
    print("P:", P)
    print("S2:", S2)
    print("C:", C)
elif P and S1:
    print("P and S1 -> C")
    print("P:", P)
    print("S1:", S1)
    print("C:", C)
else:
    print("Conclusion C cannot be proven or disproven with the given data.")

# (c)
Q = "An wake up late"
R = "The traffic is flowing smooth"
S1 = "The traffic is always heavy on school day"
S2 = "If An wake up late, he will be late for school on school day"
S3 = "An only have to go to school on school day"
S4 = "If An don't have to go to school, An can't be late for school"
C = "An is late for school"

if Q and S2 and S3 and S4:
    print("Q, S2, S3, and S4 -> C")
    print("Q:", Q)
    print("S2:", S2)
    print("S3:", S3)
    print("S4:", S4)
    print("C:", C)
elif R and S1:
    print("R and S1 -> C")
    print("R:", R)
    print("S1:", S1)
    print("C:", C)
else:
    print("Conclusion C cannot be proven or disproven with the given data.")

#(d)
P = "tồn tại ít nhất một x, y thuộc R, (x+y)^2 <= x^2 + y^(2n)"
Q = "với mọi x, y thuộc Z+, x + y >= x + y"
R = "với mọi x, y thuộc Z+, x + y + 2 x (xy)^(1/2) >= x + y"
T = "với mọi x, y thuộc Z+, (x+y)^(1/2) >= 0"
S1 = "với mọi x, y thuộc Z+, x^2 >= y^2 -> x >= y"
S2 = "với mọi x, y thuộc Z+, x >= y -> x^2 >= y^2"
S3 = "với mọi x, y thuộc R+, x >= y -> x^2 >= y^2"
S4 = "với mọi x, y thuộc R+, x^2 >= y^2 -> x >= y"
C = "với mọi x, y thuộc Z+, x^(1/2) + y^(1/2) >= (x+y)^(1/2)"

if P and Q and R and T and S2 and S3 and S4:
    print("P, Q, R, T, S2, S3, and S4 -> C")
    print("P:", P)
    print("Q:", Q)
    print("R:", R)
    print("T:", T)
    print("S2:", S2)
    print("S3:", S3)
    print("S4:", S4)
    print("C:", C)
elif P and Q and R and T and S1 and S2:
    print("P, Q, R, T, S1, and S2 -> C")
    print("P:", P)
    print("Q:", Q)
    print("R:", R)
    print("T:", T)
    print("S1:", S1)
    print("S2:", S2)
    print("C:", C)
else:
    print("Conclusion C cannot be proven or disproven with the given data.")
