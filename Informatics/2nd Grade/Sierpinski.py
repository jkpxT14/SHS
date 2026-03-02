from vpython import *

def sierpinski_triangle(v0, v1, v2, depth):
    if depth==1:
        triangle(vs=[vertex(pos=v0), vertex(pos=v1), vertex(pos=v2)])
    else:
        m0=(v1+v2)/2
        m1=(v0+v2)/2
        m2=(v0+v1)/2
        sierpinski_triangle(v0, m1, m2, depth-1)
        sierpinski_triangle(v1, m0, m2, depth-1)
        sierpinski_triangle(v2, m0, m1, depth-1)

v0=vec(0, -1, 0)
v1=vec(-1, 1, 0)
v2=vec(1, 1, 0)

sierpinski_triangle(v0, v1, v2, 5)