import random

board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
]

def checking(player, a):    ## a는 O 또는 X
    for l in range(3):  ##가로
        if board[l][0] == board[l][1] == board[l][2] == a:
            print(player, "win!")
            return
    for l in range(3):  ##세로
        if board[0][l] == board[1][l] == board[2][l] == a:
            print(player, "win!")
            return
    if board[0][0] == board[1][1] == board[2][2] == a:  ##왼->오 대각선
        print(player, "win!")
        return
    if board[0][2] == board[1][1] == board[2][0] == a:  ##오->왼 대각선
        print(player, "win!")
        return
    for l in range(3):      ##무승부
        for m in range(3):
            if board[l][m] != ' ':
                if l == 2 and m == 2:
                    print("draw!")
                    return
                else:
                    continue
            else:
                break

while True:
    for r in range(3):
        print(" "+board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if (r!= 2):
            print("---|---|---")
    
    player = 'user'
    x = int(input("x좌표 입력(0~2): "))
    y = int(input("y좌표 입력(0~2): "))

    if board[x][y] == 'O' or board[x][y] == 'X':
        print("잘못된 위치 입력")
        continue
    else:
        board[x][y] = 'O'
        checking(player, 'O')
    
    done = False
    player = 'com'
    while done != True:
        i = random.randrange(0, 3)
        j = random.randrange(0, 3)
        if board[i][j] == ' ':
            board[i][j] = 'X'
            done = True
            checking(player, 'X')
    done = False
