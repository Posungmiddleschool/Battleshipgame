class Battelfild():
    Battelfild:list[list[int]]

    def attack(pos:tuple):
        c_block = Battelfild[pos[0]][pos[1]]
        if c_block == 2 or c_block ==2:
            return False
        elif c_block == 0:
            c_block = 2
        elif c_block == 1:
            c_block = 3
    def get():
        tmp = []
        for i in Battelfild:
            for j in i:
                tmp.append(j)
        return tmp