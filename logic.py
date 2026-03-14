class Battlefield():
    Battelfild:list[list[int]]

    def __init__(self):
        pass

    def attack(self,pos:tuple):
        c_block = Battlefield[pos[0]][pos[1]]
        if c_block == 2 or c_block ==2:
            return False
        elif c_block == 0:
            c_block = 2
        elif c_block == 1:
            c_block = 3

    def get(self):
        tmp = []
        for i in Battlefield:
            for j in i:
                tmp.append(j)
        return tmp