from graphic import graphics
import logic
import matplotlib.pyplot as plt
'''배틀필드 사용'''

'''그래픽 초기 세팅'''
graphics()
'''맷플롯립을 사용하기 위해 각각 2개의 리스트를 만들었습니다.'''
'''player1_battleship_list_x와 player1_battleship_list_y는 player1이 배치한 battleship의 x좌표와 y좌표를 알려줍니다.'''
'''player2도 똑같습니다'''
player1_battleship_list_x = []
player1_battleship_list_y = []
player2_battleship_list_x=[]
player2_battleship_list_y=[]
size = 2
'''함선 추가하는 코드입니다.'''

for i in range (4):
    '''길이가 2,3,4,5인 함선을 추가하는 코드입니다.'''
    player1number = input("Player 1, 너의 Battleship을 어디에 놓을 것이니 두자리 자연수로 입력: ")
    player1putmethod = input("Player 1, 너의 Battleship을 가로 또는 세로로 놓을것인지 선택: ")
    '''사칙연산을 위해 값을 정수로 변환합니다.'''
    start_x = int(player1number[0])
    start_y = int(player1number[1])
    if player1putmethod == "가로":
        for i in range (size):
            player1_battleship_list_x.append(start_x + i)
            player1_battleship_list_y.append(start_y)
    else:
        for i in range (size):
            player1_battleship_list_x.append(start_x + i)
            player1_battleship_list_y.append(start_y)
    size += 1

size = 2
for i in range (4):
    player2number = input("Player 2, 너의 Battleship을 어디에 놓을 것이니 두자리 자연수로 입력: ")
    player2putmethod = input("Player 2, 너의 Battleship을 가로 또는 세로로 놓을것인지 선택: ")
    start_x = int(player1number[0])
    start_y = int(player1number[1])
    if player2putmethod == "가로":
        for i in (0, size):
            player2_battleship_list_x.append(start_x)
            player2_battleship_list_y.append(start_y + i)
    else:
        repeat = 0
        player2_battleship_list_x.append(start_x)
        player2_battleship_list_y.append(int(player2number[1]) + repeat)
size = 1
gameover = 0
turn = 0

'''적의 모든 함선이 격침되면 player1 스일시 gameover을 1, player2승리시 2로 설정해 주세요.'''
'''turn변수는 각각 0과 1로 정해 player1과 player2의 차례를 나타내는걸로 쓰려고 합니다.'''
while gameover == 0:
    if turn == 0:
        reply = input("어느 위치를 공격할거니? 두자리 자연수로 입력해. 만약 너가 모르겠다면 위치 보기로 너 함선의 위치를 알 수 있어.")
        if reply == "위치 보기":
            plt.scatter(player1_battleship_list_x, player1_battleship_list_y)
            plt.xlabel('x')
            plt.ylabel('y')        
            plt.show()
            continue
        '''공격할 x좌표와 y좌표 설정'''
        attackx = int(reply[0])
        attacky = int(reply[1])
    else:
        reply = input("어느 위치를 공격할거니? 두자리 자연수로 입력해. 만약 너가 모르겠다면 위치 보기로 너 함선의 위치를 알 수 있어.")
        if reply == "위치 보기":
            plt.scatter(player1_battleship_list_x, player1_battleship_list_y)
            plt.xlabel('x')
            plt.ylabel('y')        
            plt.show()
            continue
    
        
