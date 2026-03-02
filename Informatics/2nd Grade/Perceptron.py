def perceptron(x_1, x_2):
    w_1=0 # weight
    w_2=0 # weight
    b=0 #bias
    u=w_1*x_1+w_2*x_2+b
    if(u>0): # 활성화 함수
        return 1
    else:
        return 0

print(perceptron(0, 0))
print(perceptron(0, 1))
print(perceptron(1, 0))
print(perceptron(1, 1))

# w, b를 바꿔서 AND, OR, NAND(Negative AND), (XOR)