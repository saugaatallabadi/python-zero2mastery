# MRO- Method Resolution Order


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print(D.num)  # prints 1 from C; Order -> B>C>A

# Whenever in doubt, use this
print(D.mro())  # Depth First Search


'''

    A
  /    \
 /      \
B        C
 \      /
  \    /
     D


'''
