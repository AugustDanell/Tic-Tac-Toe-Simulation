import random
import matplotlib.pyplot as plot

def run_all_tests():
    '''
        run_all_tests
        Run all tests is running tests on the check_board_3D function specifically. We look through all 13 cases that can
        match in the matrices down below. To understand it exactly each indvidual list is like a stack where the players
        can place their markers on top of each other. We look through all cases where there is such a match below as well
        as make sure that when there is no match, false ought to be returned by the checking function.
    '''

    # TESTING SUITE
    # 1. Test extreme cases, roofs and floors (Z = dim-1 and Z = 0):
    FLOOR_HORISONTAL = [[[2], [],  [2]],
                        [[1], [1], [1]],
                        [[2], [],  []]]

    ROOF_HORISONTAL =  [[[2], [],  [2]],
                        [[0,0,1], [0,0,1], [0,0,1]],
                        [[2], [],  []]]

    FLOOR_VERTICAL =   [[[2], [1], [2]],
                        [[],  [1], []],
                        [[2], [1], []]]

    ROOF_VERTICAL =    [[[2],  [1,2,1], [2]],
                        [[],  [2,1,1], []],
                        [[2], [2,1,1], []]]

    FLOOR_LDIAGONAL =  [[[1], [],  []],
                        [[2], [1], [2]],
                        [[],  [],  [1]]]

    ROOF_LDIAGONAL =   [[[0,0,1], [],  []],
                        [[2], [0,0,1], [2]],
                        [[],  [],  [0,0,1]]]

    FLOOR_RDIAGONAL =  [[[2], [],  [1]],
                        [[2], [1], [2]],
                        [[1], [],  []]]

    ROOF_RDIAGONAL =  [[[2], [],  [0,0,1]],
                        [[2], [0,0,1], [2]],
                        [[0,0,1], [],  []]]

    VERTICAL =        [[[2], [1,1],  [1]],
                       [[], [2,1],    [2]],
                       [[], [2,1,2],  []]]

    HORISONTAL =      [[[2], [2], [1]],
                       [[2,1], [2, 1], [2,1]],
                       [[], [2], []]]

    # 2. Test Inclinational cases:
    VERTICAL_BOT_TOP_INCLINATION = [[[2],[2,2,1],[1]],
                                    [[], [2,1],  [2]],
                                    [[], [1],    []]]

    VERTICAL_TOP_BOT_INCLINATION = [[[2],[1],     [1]],
                                    [[], [2,1],   [2]],
                                    [[], [2,1,1], []]]

    HORISONTAL_LEFT_RIGHT_INCLINATION = [[[2],[1],    [1]],
                                         [[2], [1,2], [1,1,2]],
                                         [[], [2],    []]]

    HORISONTAL_RIGHT_LEFT_INCLINATION = [[[2], [1], [1]],
                                         [[1,1,2], [1, 2], [2]],
                                         [[],   [2], []]]

    RDIAGONAL_BOT_TOP_INCLINATION = [[[2],[],      [2,2,1]],
                                     [[], [2,1],    [2]],
                                     [[1], [],  []]]

    RDIAGONAL_TOP_BOT_INCLINATION = [[[],[],      [1]],
                                     [[], [2,1],    [2]],
                                     [[2,2,1], [],  []]]

    LDIAGONAL_BOT_TOP_INCLINATION = [[[2,2,1], [], []],
                                     [[], [2, 1], [2]],
                                     [[], [], [1]]]

    LDIAGONAL_TOP_BOT_INCLINATION = [[[1], [], []],
                                     [[], [2, 1], [2]],
                                     [[], [], [2, 2, 1]]]

    # 3. Z-check
    Z =                             [[[1], [], []],
                                     [[], [1,1,1], []],
                                     [[], [], []]]

    # 4. Test cases that ought to return false:
    F1 =                            [[[1], [], []],
                                     [[], [1], []],
                                     [[], [], []]]

    F2 =                            [[[1], [1], []],
                                     [[1], [1,2,1], []],
                                     [[], [], []]]

    F3 =                            [[[1], [2], []],
                                     [[], [1,2,2], []],
                                     [[], [1,2,1], []]]

    F4 =                            [[[1], [1,2,1], []],
                                     [[], [1,2,2], []],
                                     [[], [2], []]]

    F5 =                            [[[1], [1,2,1], [2,1]],
                                     [[], [1,2,2], []],
                                     [[1,2], [2], []]]

    assert check_board_3D(ROOF_HORISONTAL,  3)[0]
    assert check_board_3D(FLOOR_HORISONTAL, 3)[0]
    assert check_board_3D(FLOOR_VERTICAL,   3)[0]
    assert check_board_3D(ROOF_VERTICAL,    3)[0]
    assert check_board_3D(FLOOR_RDIAGONAL,  3)[0]
    assert check_board_3D(ROOF_RDIAGONAL,   3)[0]
    assert check_board_3D(FLOOR_LDIAGONAL,  3)[0]
    assert check_board_3D(ROOF_LDIAGONAL,   3)[0]
    assert check_board_3D(VERTICAL,         3)[0]
    assert check_board_3D(HORISONTAL,       3)[0]

    assert check_board_3D(VERTICAL_BOT_TOP_INCLINATION, 3)[0]
    assert check_board_3D(VERTICAL_TOP_BOT_INCLINATION, 3)[0]
    assert check_board_3D(HORISONTAL_LEFT_RIGHT_INCLINATION, 3)[0]
    assert check_board_3D(HORISONTAL_RIGHT_LEFT_INCLINATION, 3)[0]
    assert check_board_3D(RDIAGONAL_BOT_TOP_INCLINATION, 3)[0]
    assert check_board_3D(RDIAGONAL_TOP_BOT_INCLINATION, 3)[0]
    assert check_board_3D(LDIAGONAL_TOP_BOT_INCLINATION, 3)[0]
    assert check_board_3D(LDIAGONAL_BOT_TOP_INCLINATION, 3)[0]

    assert check_board_3D(Z, 3)[0]

    assert not check_board_3D(F1,3)[0]
    assert not check_board_3D(F2,3)[0]
    assert not check_board_3D(F3,3)[0]
    assert not check_board_3D(F4,3)[0]
    assert not check_board_3D(F5, 3)[0]
    print("All tests passed!")

def get_center_coordinates(dimension):
    '''
        get_center_coordinates (Identical to basic.get_center_coordinates)
        This function takes in the dimension d that spans the dxd board. Given d we can calculate the center of the board as
        a function to be used in scenario 2 etc. If d is odd we get the exact center point, (see test case 5.1).
        We can reuse this from the basic.py, simply put it is like we are in a birds point of view and we drop down our marker
        in the center point, the only differance is that the center point now can stack in the z-axis since it is in 3D. This
        does not affect where the center point is however.
    '''

    center_point = (dimension-1)//2
    return center_point

def get_remaining_coordinates_3D(board, dimension):
    '''
        get_remaining_coordinates_3D
        This function is very similar to its 2D counterpart in basic.py, however, this function look at all the board elements
        which are lists and not elements themselves now, and the function returns those that do not have 5 elements in them.
        This is because in the 3D version we can put up to 5 pieces in one (x,y) coordinate and have them stack via the z-axis,
        and as long as a coordinate (i,j) is not fully stacked with dimension = 5 elements we return them as valid coordinates.
    '''

    ok_coordinates = []
    for i in range(dimension):
        for j in range(dimension):
            if(not len(board[i][j]) == dimension):
                ok_coordinates.append([i,j])

    return ok_coordinates


def check_three_in_row_3D(x,y,z,board,dimension):
    '''
        check_three_in_row_3d
        Much like its 2D counterpart check_three_in_row_3D aims to solve the problem which is to take in a point (x,y,z) and
        see if that point forms a centerpoint for a three in row. A center point can now have 13 matches, as all previous matches
        can have an upward or downward slope, or inclination, moreover we can also find a match in the z-axis:
    '''


    # 1: As in 2D, we return false on corners:
    if(x in [0,dimension-1] and y in [0, dimension-1] and z in [0, dimension-1]):
        return False, 0

    # 2: We set the player marker to be what the point is, returning false if it does not exist within the list:
    player = 0
    if(len(board[x][y]) -1 < z):
        return False, 0
    else:
        player = board[x][y][z]

    # 3.1: As in 2D, setting up some check marks but here we also account for the Z-axis:
    vertical_check   = x > 0 and x < dimension - 1
    horizontal_check = y > 0 and y < dimension - 1
    Z_check =          z > 0 and z < dimension - 1

    # 3.2 - Non-inclinational Checks, that is, looking at cases where Z is the same for all points:
    # 3.2.1 - Direct Vertical Check:
    if(vertical_check and len(board[x-1][y])-1 >= z and len(board[x+1][y])-1 >= z):
        if (board[x - 1][y][z] == player and board[x + 1][y][z] == player):
            return True, player

    # 3.2.2 - Direct Horisontal Check:
    if(horizontal_check and len(board[x][y-1])-1 >= z and len(board[x][y+1]) -1 >= z):
        if (board[x][y - 1][z] == player and board[x][y + 1][z] == player):
            return True, player


    # Diagonal Checks have to fulfill both vertical and horisontal out of bounds:
    if(vertical_check and horizontal_check):

        # 3.2.3 - Direct Left Diagonal Check:
        if(len(board[x-1][y-1]) -1 >= z and len(board[x+1][y+1])-1 >= z):
            if (board[x - 1][y - 1][z] == player and board[x + 1][y + 1][z] == player):
                return True, player


        # 3.2.4 - Direct Right Diagonal Check:
        if(len(board[x-1][y+1]) -1 >= z and len(board[x+1][y-1])-1 >= z):
            if (board[x - 1][y + 1][z] == player and board[x + 1][y - 1][z] == player):
                return True, player

    # 3.3 - Checking all the inclinational cases:
    if(Z_check):
        if(vertical_check):
            # 3.3.1.1 - Vertical Top_To_Bot:
            if(len(board[x-1][y])-1 >= z-1 and len(board[x+1][y])-1 >= z+1):
                if(board[x-1][y][z-1] == player and board[x+1][y][z+1] == player):
                    return True, player

            # 3.3.1.2 - Vertical Bot_To_Top inclination:
            if(len(board[x-1][y])-1 >= z+1 and len(board[x+1][y])-1 >= z-1):
                if(board[x - 1][y][z+1] == player and board[x + 1][y][z-1] == player):
                    return True, player

        if(horizontal_check):
            # 3.3.2.1 - Horisontal LEFT_TO_RIGHT
            if(len(board[x][y-1])-1 >= z-1 and len(board[x][y+1])-1 >= z+1):
                if(board[x][y-1][z-1] == player and board[x][y+1][z+1] == player):
                    return True, player

            # 3.3.2.2 - Horisontal RIGHT_TO_LEFT
            if(len(board[x][y-1])-1 >= z+1 and len(board[x][y+1])-1 >= z-1):
                if(board[x][y-1][z+1] == player and board[x][y+1][z-1] == player):
                    return True, player


        if (vertical_check and horizontal_check):
            # 3.3.3.1 - Right Diagonal BOT_TO_TOP
            if(len(board[x+1][y-1])-1 >= z-1 and len(board[x-1][y+1])-1 >= z+1):
                if(board[x+1][y-1][z-1] == player and board[x-1][y+1][z+1] == player):
                    return True, player

            # 3.3.3.2 - Right Diagonal TOP_TO_BOT
            if(len(board[x+1][y-1])-1 >= z+1 and len(board[x-1][y+1])-1 >= z-1):
                if(board[x+1][y-1][z+1] == player and board[x-1][y+1][z-1] == player):
                    return True, player

            # 3.3.4.1 - Left Diagonal BOT_TO_TOP
            if(len(board[x-1][y-1])-1 >= z+1 and len(board[x+1][y+1])-1 >= z-1):
                if(board[x-1][y-1][z+1] == player and board[x+1][y+1][z-1] == player):
                    return True, player

            # 3.3.4.2 - Left Diagonal BOT_TO_TOP
            if(len(board[x-1][y-1])-1 >= z-1 and len(board[x+1][y+1])-1 >= z+1):
                if(board[x-1][y-1][z-1] == player and board[x+1][y+1][z+1] == player):
                    return True, player

        # 3.4 Look at the direct z-axis:
        if(board[x][y][z-1] == player and len(board[x][y]) -1 >= z +1 and board[x][y][z+1] == player):
            return True, player

    # 4.0
    return False, 0

def check_board_3D(board, dimension):
    '''
        check_board_3D
        Very similar to the 2D version. We iterate through the entire board in all dimensions, if there is a matching three
        in a row the player of which it belongs to is returned (see check_three_in_row_3D()).
    '''

    for x in range(dimension):
        for y in range(dimension):
            for z in range(dimension):
                has_won, player = check_three_in_row_3D(x,y, z, board, dimension)
                if(has_won):
                    return has_won, player

    return False, 0


def play_game_3D(scenario):
    '''
        play_game_3D()
        play_game()_3D is the main body of the game itself, if one so will. It is a function that simulates a game playing
        until either all spots have been exhausted or one of the players, player one and player two respectively, have
        won. The differance between the 2D version is that the space is in 3D space, dropping down the markers down the
        z-axis, and as such
    '''

    # 1: We start with initiating a DxD board and a counter, where each cell will be a list:
    dimension = 5
    board = [[[] for j in range(dimension)] for i in range(dimension)]
    player_turn = 1

    # 2: If scenario two is played, player one will start the game with appending their marker onto the center point:
    if scenario == 2:
        center_point = get_center_coordinates(dimension)
        board[center_point][center_point].append(1)
        player_turn = 2

    # 3: Iterate until either a draw or a winner has been found upon which the game will exit:
    while (True):

        # 3.1: Start each iteration with declaring which spots are left:
        available_spots = get_remaining_coordinates_3D(board, dimension)
        number_of_spots = len(available_spots)
        if(number_of_spots == 0):
            break

        # 3.2: Randomize placements on remaining spots:
        index = random.randint(0, number_of_spots -1)
        x, y = available_spots[index]
        board[x][y].append(player_turn)

        # 3.3: If there is a winner, return that winner.
        has_won, winning_player = check_board_3D(board, dimension)
        if (has_won):
            return winning_player

        # 3.4: If not, alternate turn instead.
        player_turn = (player_turn % 2) + 1

    # 4.0:
    return 0

if __name__ == '__main__':
    # 0. Testing phase: Set this to be false to run the simulation, else it proceeds to unit testing directly.
    only_test = False

    if(not only_test):
        # 1. Validating user data.
        valid_values = False
        while(not valid_values):
            valid_values = True
            try:
                dimension = 5
                scenario =  int(input("Which scenario do you want to play? (1/2)"))
                games =     int(input("How many games should be simulated? (>0)"))
                if (scenario not in [1, 2] or games < 0):
                    valid_values = False
                    print("Let games be a value greater than zero")
                    print("Let scenario be either one or two, depending on what scenario to simulate")
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

        # 2: Playing the game, keeping score of who wins what match.
        for i in range(games):
            winning_player = play_game_3D(scenario)

            if (winning_player == 1):
                player_one += 1

            elif winning_player == 2:
                player_two += 1

            else:
                draw += 1

        print("Player 1 wins: %d" % player_one)
        print("Player 2 wins: %d" % player_two)
        print("Draw: %d" % draw)

        # 3. Matplot, creating plots and saving the result:
        x_coordinates = ["Spelare 1", "Spelare 2", "Oavgjorda"]
        diagram_height = [player_one, player_two, draw]
        plot.bar(x_coordinates, diagram_height, width=0.5)
        title = "Utfall 3D-tre-i-rad %dx%d, scenario %d" % (dimension, dimension, scenario)
        plot.title(title)
        plot.savefig("plot.pdf")

    # 4. Run the Testing Suite
    run_all_tests()
