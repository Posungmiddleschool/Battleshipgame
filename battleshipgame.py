from graphic import graphics
import matplotlib.pyplot as plt
'''그래픽 초기 세팅'''
graphics()
'''맷플롯립을 사용하기 위해 각각 2개의 리스트를 만들었습니다.'''
player1_battleship_list_x = []
player1_battleship_list_y = []
player2_battleship_list_x=[]
player2_battleship_list_y=[]
size = 1
'''함선 추가하는 코드입니다.'''
for i in range (0,4):
    size = size + 1
    player1number = input("Player 1, 너의 Battleship을 어디에 놓을 것이니 두자리 자연수로 입력")
    player1putmethod = input("Player 1, 너의 Battleship을 가로로 놓을 것이니 세로로 놓을 것이니")
    if player1putmethod == "가로":
        repeat = 0
        for i in (1, size):
            player1_battleship_list_x.append(int(player1number[0]) + repeat)
            player1_battleship_list_y.append(int(player1number[1]))
        repeat = repeat + 1
    else:
        for i in (1,size):
            player1_battleship_list_x.append(int(player1number[0]))
            player1_battleship_list_y.append(int(player1number[1]) + repeat)
size = 1
for i in range (0,4):
    size = size + 1
    player2number = input("Player 2, 너의 Battleship을 어디에 놓을 것이니 두자리 자연수로 입력")
    player2putmethod = input("Player 2, 너의 Battleship을 가로로 놓을 것이니 세로로 놓을 것이니")
    if player2putmethod == "가로":
        repeat = 0
        for i in (1, size):
            player2_battleship_list_x.append(int(player2number[0])+ repeat)
            player2_battleship_list_y.append(int(player2number[1]))
    else:
        repeat = 0
        player2_battleship_list_x.append(int(player2number[0]))
        player2_battleship_list_y.append(int(player2number[1]) + repeat)
size = 1
gameover = 0
turn = 0

while gameover == 0:
    if turn == 0:
        reply = input("어느 위치를 공격할거니? 두자리 자연수로 입력해. 만약 너가 모르겠다면 위치 보기로 너 함선의 위치를 알 수 있어.")
        if reply == "위치 보기":
            plt.scatter(player1_battleship_list_x, player1_battleship_list_y)
            plt.xlabel('x')
            plt.ylabel('y')        
            plt.show()
