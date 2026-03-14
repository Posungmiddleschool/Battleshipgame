import matplotlib as plt
player1_battleship_list = []
player2_battleship_list=[]
size = 1
for i in range (0,3):
    size = size + 1
    player1number = int(print("Player 1, 너의 Battleship을 어디에 놓을 것이니 두자리 자연수로 입력"))
    player1putmethod = print("Player 1, 너의 Battleship을 가로로 놓을 것이니 세로로 놓을 것이니")
    if player1putmethod == "가로":
        repeat = 0
        for i in (1, size):
            player1_battleship_list.append([player1number[0] + repeat, player1number[1]])
    else:
        repeat = 0
        player1_battleship_list.append([player1number[0], player1number[1]+repeat])
size = 1
for i in range (0,3):
    size = size + 1
    player2number = int(print("Player 2, 너의 Battleship을 어디에 놓을 것이니 두자리 자연수로 입력"))
    player2putmethod = print("Player 2, 너의 Battleship을 가로로 놓을 것이니 세로로 놓을 것이니")
    if player2putmethod == "가로":
        repeat = 0
        for i in (1, size):
            player1_battleship_list.append([player2number[0] + repeat, player2number[1]])
    else:
        repeat = 0
        player1_battleship_list.append([player2number[0], player2number[1]+repeat])
        