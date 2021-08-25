import random
import matplotlib.pyplot as plot

def run_test_suite():
    '''
        run_test_suite()
        A function containing all the unit tests that test different functions, this testing suite is called in the end of
        the main program to make sure that everything works.
    '''

    VERTICAL =  [[0, 1, 0]]*3
    VERTICAL2 = [[0, 0, 1]] * 3
    VERTICAL3 = [[1, 0, 0]] * 3
    HORIZONTAL =  [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    HORIZONTAL2 = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
    HORIZONTAL3 = [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
    LEFT_DIAGONAL =  [[1,0,0],[0,1,0],[0,0,1]]
    RIGHT_DIAGONAL = [[0,0,1],[0,1,0],[1,0,0]]

    # Check Valid Win Conditions:
    assert check_three_in_row(1, 1, VERTICAL,     3)  # Test case 1.1
    assert check_three_in_row(1, 2, VERTICAL2,    3)  # Test case 1.2
    assert check_three_in_row(1, 0, VERTICAL3,    3)  # Test case 1.3
    assert check_three_in_row(1,1, HORIZONTAL,    3)  # Test case 2.1
    assert check_three_in_row(0,1, HORIZONTAL2,   3)  # Test case 2.2
    assert check_three_in_row(0,1, HORIZONTAL2,   3)  # Test case 2.3
    assert check_three_in_row(1,1, LEFT_DIAGONAL, 3)  # Test case 3.
    assert check_three_in_row(1,1, RIGHT_DIAGONAL,3)  # Test case 4.


    WINNING_BOARD1 = [[1,1,2],[1,2,1],[2,2,1]]
    DRAW_BOARD =  [[1,2,1],[2,1,2],[2,1,2]]
    DRAW_BOARD2 = [[0,0,1],[0,1,0],[2,2,0]]
    DRAW_BOARD3 = [[1, 2, 1], [0, 1, 0], [2, 2, 0]]
    MEDIUM_WIN =  [[1,2,1,2,1], [1,2,1,2,1] ,[2,1,2,1,2],[1,2,1,2,1], [1,2,1,2,1]]

    # Check that only games where 3 in a row win condition is met is declared as a win:
    assert check_board(WINNING_BOARD1, 3)     == (True,  2) # Test case 5.1
    assert check_board(DRAW_BOARD,  3)        == (False, 0) # Test case 5.2
    assert check_board(DRAW_BOARD2, 3)        == (False, 0) # Test case 5.3
    assert check_board(DRAW_BOARD3, 3)        == (False, 0) # Test case 5.4
    assert not check_board(MEDIUM_WIN,  5)    == (False, 0) # Test case 5.5

    # Corner points:
    assert not check_three_in_row(2,2,[[0,0,0],[0,0,0],[0,0,1]], 3)[0]
    assert not check_three_in_row(2, 2, [[0, 0, 0], [0, 0, 0], [1, 0, 0]], 3)[0]
    assert not check_three_in_row(2, 2, [[1, 0, 0], [0, 0, 0], [0, 0, 0]], 3)[0]
    assert not check_three_in_row(2, 2, [[0, 0, 1], [0, 0, 0], [0, 0, 0]], 3)[0]

    assert get_center_coordinates(3) == 1             # Test case 6.1

    assert get_remaining_coordinates([[0,0],[0,0]],2) == [[0,0],[0,1],[1,0],[1,1]] # Test case 7.1
    assert get_remaining_coordinates([[0, 0], [1, 1]], 2) == [[0, 0], [0, 1]]      # Test case 7.2
    print("All tests passed!")

def get_remaining_coordinates(board, dimension):
    '''
        get_remaining_coordinates()
        A simple function that takes in the board and its corrosponding dimension d and simply iterates through the board,
        returning a list of coordinates of free space that is where no player has put their marker (0).
    '''

    remaining_coordinates = []
    for i in range(dimension):
        for j in range(dimension):
            if(board[i][j] == 0):
                remaining_coordinates.append([i,j])

    return remaining_coordinates

def get_center_coordinates(dimension):
    '''
        get_center_coordinates
        This function takes in the dimension d that spans the dxd board. Given d we can calculate the center of the board as
        a function to be used in scenario 2 etc. If d is odd we get the exact center point, (see test case 5.1).
        If d is even, on the other hand, there are multiple center points, however, since we only play with dimensions of
        3,5,7 we don't have to take even centerpoints into consideration, we simply return the center point.
    '''

    center_point = (dimension-1)//2
    return center_point

def check_three_in_row(x, y, board, dimension):
    '''
        check_three_in_row
        This is a helper function that looks specifically at two coordinates given a board and uses these coordinates to
        return either (False, 0), True 1, or True 2, where 1 marks player one as the winner and 2 player two. We try
        point (x,y) as a 'center point' meaning it is situated in the center of a three in a row, either horisontically,
        vertically, left-diagonally or right-diagonally respectively.
    '''

    # 1: Return false on points in the corner, as they cannot be a center point.
    if(x in [0,dimension-1] and y in [0, dimension-1]):
        return False, 0

    # 2: Set the center point to be belonging to a player or return false if no player has claimed the point:
    player = 0
    if(board[x][y] == 0):
        return False, 0
    elif(board[x][y] == 1):
        player = 1
    else:
        player = 2

    # 3: Make checks so that we remain within bounds:
    vertical_check   = x > 0 and x < dimension - 1
    horizontal_check = y > 0 and y < dimension - 1

    # 4.1: Checking Vertical Three in row, with (x,y) as center point:
    if(vertical_check):
        if(board[x-1][y] == player and board[x+1][y] == player):
            return True, player

    # 4.2: Checking Horizontal Three in row with (x,y) as center point:
    if(horizontal_check):
        if (board[x][y-1] == player and board[x][y+1] == player):
            return True, player

    if(vertical_check and horizontal_check):

        # 4.3 Checking Left Diagonal, from left top side to right bot side that is, with (x,y) as center point:
        if(board[x-1][y-1] == player and board[x+1][y+1] == player):
            return True, player

        # 4.4 Checking Left Diagonal, from left top side to right bot side that is, with (x,y) as center point:
        if (board[x - 1][y + 1] == player and board[x + 1][y - 1] == player):
            return True, player

    return False, 0


def check_board(board, dimension):
    '''
        check_board()
        check_board is a function that simply iterates through all the coordinates of the board and passes them into the
        previous function, check_three_in_row(). For all coordinates we can then surely check to see if there has been a
        three in a row and if it has the player who has it will be returned.
    '''

    for x in range(dimension):
        for y in range(dimension):
            has_won, player = check_three_in_row(x,y, board, dimension)
            if(has_won):
                return has_won, player

    return False, 0

def play_game(dimension, scenario):
    '''
        play_game()
        play_game() is the main body of the game itself, if one so will. It is a function that simulates a game playing
        until either all spots have been exhausted or one of the players, player one and player two respectively, have
        won.
    '''


    # 1: We start with initiating a DxD board and a counter:
    remaining_holes = dimension*dimension
    board = [[0 for j in range(dimension)] for i in range(dimension)]
    player_turn = 1

    # 2: If scenario 2 is set we adjust for that, setting the center point and passing the turn over:
    if scenario == 2:
        center_point = get_center_coordinates(dimension)
        board[center_point][center_point] = 1
        player_turn = 2
        remaining_holes -= 1

    # 3: For as long as there are markers to be placed, with no winning player, we iterate:
    while(remaining_holes > 0):

        # 4.1: Randomize a place to insert our marker as player one or player two respectively (alternating turns):
        available_spots = get_remaining_coordinates(board, dimension)
        index = random.randint(0, remaining_holes-1)
        x,y = available_spots[index]
        board[x][y] = player_turn

        # 4.2: Check if 4.1 triggers a win, and if so, we end the game by returning that winning player:
        has_won, winning_player = check_board(board, dimension)
        if(has_won):
            return winning_player

        # 4.3: If 4.2 does not occur, however, we decrement remaining spots to place markers and alternate the turn:
        remaining_holes -= 1
        player_turn = (player_turn%2) + 1

    # 5.0: Returning 0, indicating a draw if this statement is reached, as all spots surely have been exhausted:
    return 0

if __name__ == '__main__':
    # 1. Validating user data.
    valid_values = False
    while(not valid_values):
        valid_values = True
        try:
            dimension = int(input("What dimensions D should the board be in? (3/5/7)"))
            scenario =  int(input("Which scenario do you want to play? (1/2)"))
            games =     int(input("How many games should be simulated? (>0)"))
            if (dimension not in [3,5,7] or scenario not in [1, 2] or games < 0):
                valid_values = False
                print("Please let dimensions be a value of 3, 5,or 7.")
                print("Let games be a value greater than zero")
                print("Let scenario  be either one or two, depending on what scenario to simulate")
                continue
        except:
            valid_values = False
            print("You need to provide integer values as data!")
        finally:
            if(not valid_values):
                print("Try again!")

    player_one = 0
    draw = 0
    player_two = 0

    # 2. Actually playing the games:
    for i in range(games):
        winning_player = play_game(dimension, scenario)

        if(winning_player == 1):
            player_one += 1

        elif winning_player == 2:
            player_two += 1

        else:
            draw += 1

    print("Player 1 wins: %d" % player_one)
    print("Player 2 wins: %d" % player_two)
    print("Draw: %d" % draw)

    # 3. Matplot, creating plots and saving the result:
    x_coordinates  = ["Spelare 1", "Spelare 2", "Oavgjorda"]
    diagram_height = [player_one, player_two, draw]
    plot.bar(x_coordinates, diagram_height, width = 0.5)
    title = "Utfall tre-i-rad %dx%d, scenario %d"%(dimension, dimension, scenario)
    plot.title(title)
    plot.savefig("plot.pdf")

    # 4. TESTING SUITE:
    run_test_suite()
