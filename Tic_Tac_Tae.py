def default():
    print("\nWelcome! Let's play TIC TAC TOE!\n")


def rules():
    print("The board will look like this!")
    print("The positions of this 3 x 3 board is same as the right side of your key board.\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\nYou just have to input the position(1-9).")


def play():
    return input("\nAre you ready to play the game? Enter [Y]es or [N]o.\t").upper().startswith('Y')


def names():
    p1_name = input("\nEnter NAME of Gamer 1:\t").capitalize()
    p2_name = input("Enter NAME of Gamer 2:\t").capitalize()
    return (p1_name, p2_name)


def choice():
    p1_choice = ' '
    p2_choice = ' '
    while p1_choice != 'X' or p1_choice != 'O':

        p1_choice = input(f"\n{p1_name}, Do you want to be X or O?\t")[0].upper()

        if p1_choice == 'X' or p1_choice == 'O':
            break
        print("INVALID INPUT! Please Try Again!")

    if p1_choice == 'X':
        p2_choice = 'O'
    elif p1_choice == 'O':
        p2_choice = 'X'

    return (p1_choice, p2_choice)


def first_player():
    import random
    return random.choice((0, 1))


def display_board(board, avail):
    print("    " + " {} | {} | {} ".format(board[7], board[8], board[9]) + "            " + " {} | {} | {} ".format(
        avail[7], avail[8], avail[9]))
    print("    " + "===========" + "            " + "===========")
    print("    " + " {} | {} | {} ".format(board[4], board[5], board[6]) + "            " + " {} | {} | {} ".format(
        avail[4], avail[5], avail[6]))
    print("    " + "===========" + "            " + "===========")
    print("    " + " {} | {} | {} ".format(board[1], board[2], board[3]) + "            " + " {} | {} | {} ".format(
        avail[1], avail[2], avail[3]))


def player_choice(board, name, choice):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input(f'\n{name} ({choice}), Choose your next position: (1-9) \t'))

        if position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position) or position == "":
            print(f"YOU HAVE ENTERED INVALID INPUT. Please Can Try It Again!\n")
    print("\n")
    return position


def CompAI(board, name, choice):
    position = 0
    possibilities = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]

    for let in ['O', 'X']:
        for i in possibilities:
            boardCopy = board[:]
            boardCopy[i] = let
            if (win_check(boardCopy, let)):
                position = i
                return position

    openCorners = [x for x in possibilities if x in [1, 3, 7, 9]]

    if len(openCorners) > 0:
        position = selectRandom(openCorners)
        return position

    if 5 in possibilities:
        position = 5
        return position

    openEdges = [x for x in possibilities if x in [2, 4, 6, 8]]

    if len(openEdges) > 0:
        position = selectRandom(openEdges)
        return position


def selectRandom(board):
    import random
    ln = len(board)
    r = random.randrange(0, ln)
    return board[r]


def place_marker(board, avail, choice, position):
    board[position] = choice
    avail[position] = ' '


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def win_check(board, choice):
    return (
            (board[1] == choice and board[2] == choice and board[3] == choice)
            or (board[4] == choice and board[5] == choice and board[6] == choice)
            or (board[7] == choice and board[8] == choice and board[9] == choice)
            or (board[1] == choice and board[4] == choice and board[7] == choice)
            or (board[2] == choice and board[5] == choice and board[8] == choice)
            or (board[3] == choice and board[6] == choice and board[9] == choice)
            or (board[1] == choice and board[5] == choice and board[9] == choice)
            or (board[3] == choice and board[5] == choice and board[7] == choice))


def delay(mode):
    if mode == 2:
        import time
        time.sleep(2)


def replay():
    return input('\nDo you want to play again? Enter [Y]es or [N]o: ').lower().startswith('y')


print("\n\t\t Hi! Are you Interested in Playing Tic Tac Tae Game! \n")
input("Press ENTER to start!")

default()
rules()

while True:
    ####################################################################################

    theBoard = [' '] * 10

    available = [str(num) for num in range(0, 10)]  # a List Comprehension
    # available = '0123456789'

    print("\n[0]. Player vs. Bot")
    print("[1]. Player vs. Player")
    print("[2]. Bot vs. Bot")
    mode = int(input("\nSelect an option [0]-[2]: "))
    if mode == 1:

        p1_name, p2_name = names()
        p1_choice, p2_choice = choice()
        print(f"\n{p1_name}:", p1_choice)
        print(f"{p2_name}:", p2_choice)

    elif mode == 0:
        p1_name = input("\nEnter NAME of GAMER who will go against the Bot:\t").capitalize()
        p2_name = "Bot"
        p1_choice, p2_choice = choice()
        print(f"\n{p1_name}:", p1_choice)
        print(f"{p2_name}:", p2_choice)

    else:
        p1_name = "Bot-1"
        p2_name = "Bot-2"
        p1_choice, p2_choice = "X", "O"
        print(f"\n{p1_name}:", p1_choice)
        print(f"\n{p2_name}:", p2_choice)

    if first_player():
        turn = p2_name
    else:
        turn = p1_name

    print(f"\n{turn} will go first!")

    if (mode == 2):
        ent = input("\nThis is going to be fast! Press Enter for the battle to begin!\n")
        play_game = 1
    else:
        play_game = play()

    while play_game:

        ############################
        if turn == p1_name:

            display_board(theBoard, available)

            if mode != 2:
                position = player_choice(theBoard, p1_name, p1_choice)
            else:
                position = CompAI(theBoard, p1_name, p1_choice)
                print(f'\n{p1_name} ({p1_choice}) has placed on {position}\n')

            place_marker(theBoard, available, p1_choice, position)

            if win_check(theBoard, p1_choice):
                display_board(theBoard, available)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                if (mode):
                    print(f'\n\nCONGRATULATIONS {p1_name}! YOU HAVE WON THE GAME!\n\n')
                else:
                    print('\n\nTHE Bot HAS WON THE GAME!\n\n')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                play_game = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard, available)
                    print("~~~~~~~~~~~~~~~~~~")
                    print('\nThe game is a DRAW!\n')
                    print("~~~~~~~~~~~~~~~~~~")
                    break
                else:
                    turn = p2_name


        ############################
        # PLAYER2
        elif turn == p2_name:

            display_board(theBoard, available)

            if (mode == 1):
                position = player_choice(theBoard, p2_name, p2_choice)
            else:
                position = CompAI(theBoard, p2_name, p2_choice)
                print(f'\n{p2_name} ({p2_choice}) has placed on {position}\n')

            place_marker(theBoard, available, p2_choice, position)

            if win_check(theBoard, p2_choice):
                display_board(theBoard, available)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                if (mode):
                    print(f'\n\nCONGRATULATIONS {p2_name}! YOU HAVE WON THE GAME!\n\n')
                else:
                    print('\n\nTHE Bot HAS WON THE GAME!\n\n')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                play_game = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard, available)
                    print("~~~~~~~~~~~~~~~~~~")
                    print('\nThe game is a DRAW!\n')
                    print("~~~~~~~~~~~~~~~~~~")
                    break
                else:
                    turn = p1_name

    if replay():
        continue
    else:
        break
print("\n\n\t\t\tTHE END!")
