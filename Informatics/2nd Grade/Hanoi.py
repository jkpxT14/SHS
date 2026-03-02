def hanoi(n, from_pos, to_pos, aux_pos):
    if n==1:
        print("{} -> {}".format(from_pos, to_pos))
        return
    else:
        hanoi(n-1, from_pos, aux_pos, to_pos)
        hanoi(1, from_pos, to_pos, aux_pos)
        hanoi(n-1, aux_pos, to_pos, from_pos)
hanoi(5, 1, 3, 2)