import matplotlib.pyplot as plt

BOARD_SIZE = 10

def is_valid_position(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def make_ship_positions(start_x, start_y, size, direction):
    positions = []

    if direction == "가로":
        for i in range(size):
            positions.append((start_x + i, start_y))
    elif direction == "세로":
        for i in range(size):
            positions.append((start_x, start_y + i))

    return positions

def can_place_ship(ship_positions, occupied_positions):
    for x, y in ship_positions:
        if not is_valid_position(x, y):
            return False
        if (x, y) in occupied_positions:
            return False
    return True

def place_ships(player_name):
    occupied_positions = []
    ship_sizes = [2, 3, 4]

    print(f"\n{player_name}의 함선 배치를 시작합니다.")

    for size in ship_sizes:
        while True:
            print(f"\n길이 {size}짜리 함선을 배치하세요.")
            number = input("시작 위치를 두 자리 자연수로 입력하세요 (예: 34): ")
            direction = input("가로 또는 세로로 입력하세요: ")

            if len(number) != 2 or not number.isdigit():
                print("입력이 잘못됐어. 예: 34처럼 두 자리 숫자로 입력해.")
                continue

            if direction not in ["가로", "세로"]:
                print("가로 또는 세로만 입력할 수 있어.")
                continue

            start_x = int(number[0])
            start_y = int(number[1])

            ship_positions = make_ship_positions(start_x, start_y, size, direction)

            if not can_place_ship(ship_positions, occupied_positions):
                print("맵 밖으로 나가거나 다른 함선과 겹쳐서 배치할 수 없어. 다시 입력해.")
                continue

            occupied_positions.extend(ship_positions)
            print(f"길이 {size} 함선 배치 완료: {ship_positions}")
            break

    return occupied_positions

def show_positions(player_name, ship_positions, hit_positions=None, miss_positions=None):
    if hit_positions is None:
        hit_positions = []
    if miss_positions is None:
        miss_positions = []

    ship_x = [pos[0] for pos in ship_positions]
    ship_y = [pos[1] for pos in ship_positions]

    plt.figure(figsize=(6, 6))
    plt.xlim(-0.5, BOARD_SIZE - 0.5)
    plt.ylim(-0.5, BOARD_SIZE - 0.5)
    plt.xticks(range(BOARD_SIZE))
    plt.yticks(range(BOARD_SIZE))
    plt.grid(True)
    plt.title(f"{player_name}의 맵")
    plt.xlabel("x")
    plt.ylabel("y")

    if ship_positions:
        plt.scatter(ship_x, ship_y, s=200, marker='s', label="내 함선")

    if hit_positions:
        hit_x = [pos[0] for pos in hit_positions]
        hit_y = [pos[1] for pos in hit_positions]
        plt.scatter(hit_x, hit_y, s=120, marker='x', label="명중한 위치")

    if miss_positions:
        miss_x = [pos[0] for pos in miss_positions]
        miss_y = [pos[1] for pos in miss_positions]
        plt.scatter(miss_x, miss_y, s=80, marker='o', label="빗나간 위치")

    plt.legend()
    plt.show()

def attack(player_name, enemy_ships, attacked_positions):
    while True:
        reply = input(
            f"\n{player_name}, 공격할 위치를 두 자리 자연수로 입력해. "
            f"'위치 보기'를 입력하면 네 함선 위치를 볼 수 있어: "
        )

        if reply == "위치 보기":
            return "show", None

        if len(reply) != 2 or not reply.isdigit():
            print("입력이 잘못됐어. 예: 34처럼 두 자리 숫자로 입력해.")
            continue

        attack_x = int(reply[0])
        attack_y = int(reply[1])

        if not is_valid_position(attack_x, attack_y):
            print("맵 범위를 벗어났어. 0~9 사이 좌표만 가능해.")
            continue

        if (attack_x, attack_y) in attacked_positions:
            print("이미 공격한 위치야. 다른 곳을 입력해.")
            continue

        attacked_positions.append((attack_x, attack_y))

        if (attack_x, attack_y) in enemy_ships:
            enemy_ships.remove((attack_x, attack_y))
            print("명중!")
            return "hit", (attack_x, attack_y)
        else:
            print("빗나감!")
            return "miss", (attack_x, attack_y)

def main():
    print("=== 배틀십 게임 시작 ===")
    print("맵 크기는 10x10이고 좌표는 00부터 99까지 사용해.")
    print("함선 길이는 2, 3, 4야.\n")

    player1_ships = place_ships("Player 1")
    print("\n" * 30)
    player2_ships = place_ships("Player 2")
    print("\n" * 30)

    player1_attacked_positions = []
    player2_attacked_positions = []

    player1_hit_positions = []
    player1_miss_positions = []

    player2_hit_positions = []
    player2_miss_positions = []

    turn = 0

    while True:
        if turn == 0:
            result, pos = attack("Player 1", player2_ships, player1_attacked_positions)

            if result == "show":
                show_positions("Player 1", player1_ships, player2_hit_positions, player2_miss_positions)
                continue

            if result == "hit":
                player2_hit_positions.append(pos)
            elif result == "miss":
                player2_miss_positions.append(pos)

            if len(player2_ships) == 0:
                print("\nPlayer 1 승리!")
                break

            turn = 1

        else:
            result, pos = attack("Player 2", player1_ships, player2_attacked_positions)

            if result == "show":
                show_positions("Player 2", player2_ships, player1_hit_positions, player1_miss_positions)
                continue

            if result == "hit":
                player1_hit_positions.append(pos)
            elif result == "miss":
                player1_miss_positions.append(pos)

            if len(player1_ships) == 0:
                print("\nPlayer 2 승리!")
                break

            turn = 0

main()
