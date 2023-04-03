import pygame
import sys
import random

class Tic_Toe():
    def __init__(self, x_o, easy_hard, first_second):
        self.grid = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [
            0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [
                0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [
                    0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
        # a list of list of list of int
        # pos_location is a list (row) of list (column) of int (idx)
        self.position_x = [[(28, 104), (104, 180), (180, 256)], [
            (256, 335), (335, 412), (412, 490)], [(490, 566), (556, 644), (644, 719)]]
        self.position_y = [[(32, 107), (107, 187), (187, 262)], [
            (262, 337), (337, 416), (416, 493)], [(493, 570), (570, 647), (647, 723)]]
        assert x_o == 'x' or x_o == 'o', 'you must enter from one of \'x\' or \'o\'.'
        assert easy_hard == 'easy' or easy_hard == 'medium' or easy_hard == 'hard', 'you must enter either \'easy\' or \'hard\'.'
        assert first_second == 'first' or first_second == 'second', 'you must enter either \'first\' or \'second\'.'
        self.x_o = x_o
        self.easy_hard = easy_hard
        self.first_second = first_second

    def chess(self):
        screen = pygame.display.set_mode([750, 750])
        pygame.display.set_caption('双倍的井字棋双倍的快乐')
        background = [255, 255, 255]
        screen.fill(background)
        back_pic = pygame.image.load(
            'C:\\Users\\Duality\\Desktop\\井字棋\\背景.png')
        back_rect = back_pic.get_rect()
        back_rect.center = (375, 375)
        screen.blit(back_pic, (back_rect.x, back_rect.y))
        pygame.display.flip()

        check_filled = [False for i in range(9)]
        big_center = [(142, 147), (373, 147), (604.5, 147), (142, 377.5),
                      (373, 377.5), (604.5, 377.5), (142, 608), (373, 608), (604.5, 608)]
        next_box = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        if self.first_second == 'second':
            self.grid[4][1][1] = 'new_o'
            next_box = [4]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        position = event.pos
                        background = [255, 255, 255]
                        screen.fill(background)
                        back_pic = pygame.image.load(
                            'C:\\Users\\Duality\\Desktop\\井字棋\\背景.png')
                        back_rect = back_pic.get_rect()
                        back_rect.center = (375, 375)
                        screen.blit(back_pic, (back_rect.x, back_rect.y))
                        pygame.display.flip()

                        for ran in range(len(self.position_x)):
                            if self.position_x[ran][0][0] < position[0] < self.position_x[ran][2][1]:
                                x_coor = ran
                                for length in range(len(self.position_y)):
                                    if self.position_y[length][0][0] < position[1] < self.position_y[length][2][1]:
                                        y_coor = length
                                        if ran//3 != ran/3:
                                            square_x_idx = [
                                                ran//3+ran % 3, ran//3+ran % 3+3, ran//3+ran % 3+6]
                                        elif ran//3 == ran/3:
                                            square_x_idx = [
                                                ran//3, ran//3+3, ran//3+6]
                                        if y_coor == 0:
                                            pos_location = square_x_idx[0]
                                        elif y_coor == 1:
                                            pos_location = square_x_idx[1]
                                        elif y_coor == 2:
                                            pos_location = square_x_idx[2]

                        x_change = False
                        if check_filled[pos_location] == False:
                            if pos_location == 0 or pos_location == 3 or pos_location == 6:
                                x_loc = 0
                            elif pos_location == 1 or pos_location == 4 or pos_location == 7:
                                x_loc = 1
                            else:
                                x_loc = 2
                            for row in self.position_x[x_loc]:
                                # row is a tuple
                                if row[0] < position[0] < row[1]:
                                    x_coor = (row[0]+row[1])/2
                                    if pos_location == 0 or pos_location == 1 or pos_location == 2:
                                        y_loc = 0
                                    elif pos_location == 3 or pos_location == 4 or pos_location == 5:
                                        y_loc = 1
                                    elif pos_location == 6 or pos_location == 7 or pos_location == 8:
                                        y_loc = 2

                            # assume 'x' is the player and 'o' is the computer
                            ########################################
                            for col in range(len(self.position_x[x_loc])):
                                if self.position_x[x_loc][col][0] < position[0] < self.position_x[x_loc][col][1]:
                                    x_idx = col
                            for row in range(len(self.position_y[y_loc])):
                                if self.position_y[y_loc][row][0] < position[1] < self.position_y[y_loc][row][1]:
                                    y_idx = row
                            # changes x
                            print(next_box)
                            if self.grid[pos_location][y_idx][x_idx] == 0 and (pos_location in next_box or (check_filled[next_box[0]] == True or check_filled[next_box[0]] == 'a')):
                                self.grid[pos_location][y_idx][x_idx] = 'x'
                                x_change = True

                        ###########################################

                        for box_idx in range(len(self.grid)):
                            for row_idx in range(len(self.grid[box_idx])):
                                for item_idx in range(len(self.grid[box_idx][row_idx])):
                                    if x_change and self.grid[box_idx][row_idx][item_idx] == 'new_o':
                                        self.grid[box_idx][row_idx][item_idx] = 'o'

                        ################
                        # horizontal
                        for box in range(len(self.grid)):
                            for row in self.grid[box]:
                                if row[0] == 'x' and row[0] == row[1] and row[1] == row[2]:
                                    check_filled[box] = True
                                    if self.x_o == 'x':
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                    else:
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                elif (row[0] == 'o' or row[0] == 'new_o') and (row[1] == 'o' or row[1] == 'new_o') and (row[2] == 'o' or row[2] == 'new_o'):
                                    check_filled[box] = 'a'
                                    if self.x_o == 'x':
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                    else:
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()

                        # slant 1
                        for box in range(len(self.grid)):
                            if self.grid[box][0][0] == 'x' and self.grid[box][0][0] == self.grid[box][1][1] and self.grid[box][1][1] == self.grid[box][2][2]:
                                check_filled[box] = True
                                if self.x_o == 'x':
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                                else:
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                            elif (self.grid[box][0][0] == 'o' or self.grid[box][0][0] == 'new_o') and (self.grid[box][1][1] == 'o' or self.grid[box][1][1] == 'new_o') and (self.grid[box][2][2] == 'o' or self.grid[box][2][2] == 'new_o'):
                                check_filled[box] = 'a'
                                if self.x_o == 'x':
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                                else:
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                        # slant 2
                        for box in range(len(self.grid)):
                            if self.grid[box][0][2] == 'x' and self.grid[box][0][2] == self.grid[box][1][1] and self.grid[box][1][1] == self.grid[box][2][0]:
                                check_filled[box] = True
                                if self.x_o == 'x':
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                                else:
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                            elif (self.grid[box][0][2] == 'o' or self.grid[box][0][2] == 'new_o') and (self.grid[box][1][1] == 'o' or self.grid[box][1][1] == 'new_o') and (self.grid[box][2][0] == 'o' or self.grid[box][2][0] == 'new_o'):
                                check_filled[box] = 'a'
                                if self.x_o == 'x':
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                                else:
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                        # straight
                        for box in range(len(self.grid)):
                            for column in range(3):
                                if self.grid[box][0][column] == 'x' and self.grid[box][0][column] == self.grid[box][1][column] and self.grid[box][1][column] == self.grid[box][2][column]:
                                    check_filled[box] = True
                                    if self.x_o == 'x':
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                    else:
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                elif (self.grid[box][0][column] == 'o' or self.grid[box][0][column] == 'new_o') and (self.grid[box][1][column] == 'o' or self.grid[box][1][column] == 'new_o') and (self.grid[box][2][column] == 'o' or self.grid[box][2][column] == 'new_o'):
                                    check_filled[box] = 'a'
                                    if self.x_o == 'x':
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                    else:
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()

                        #####
                        if (y_idx, x_idx) == (0, 0):
                            box_idx = 0
                        elif (y_idx, x_idx) == (0, 1):
                            box_idx = 1
                        elif (y_idx, x_idx) == (0, 2):
                            box_idx = 2
                        elif (y_idx, x_idx) == (1, 0):
                            box_idx = 3
                        elif (y_idx, x_idx) == (1, 1):
                            box_idx = 4
                        elif (y_idx, x_idx) == (1, 2):
                            box_idx = 5
                        elif (y_idx, x_idx) == (2, 0):
                            box_idx = 6
                        elif (y_idx, x_idx) == (2, 1):
                            box_idx = 7
                        elif (y_idx, x_idx) == (2, 2):
                            box_idx = 8
                        if self.easy_hard == 'easy':
                            if x_change and check_filled[box_idx] == False:
                                x = random.randint(0, 2)
                                y = random.randint(0, 2)
                                while self.grid[box_idx][x][y] == 'x' or self.grid[box_idx][x][y] == 'o' or self.grid[box_idx][x][y] == 'new_o':
                                    x = random.randint(0, 2)
                                    y = random.randint(0, 2)
                                self.grid[box_idx][x][y] = 'new_o'
                                if (x, y) == (0, 0):
                                    next_box = [0]
                                elif (x, y) == (0, 1):
                                    next_box = [1]
                                elif (x, y) == (0, 2):
                                    next_box = [2]
                                elif (x, y) == (1, 0):
                                    next_box = [3]
                                elif (x, y) == (1, 1):
                                    next_box = [4]
                                elif (x, y) == (1, 2):
                                    next_box = [5]
                                elif (x, y) == (2, 0):
                                    next_box = [6]
                                elif (x, y) == (2, 1):
                                    next_box = [7]
                                elif (x, y) == (2, 2):
                                    next_box = [8]
                            elif (check_filled[box_idx] == True or check_filled[box_idx] == 'a') and x_change:
                                x = random.randint(0, 2)
                                y = random.randint(0, 2)
                                new_box_idx = random.randint(0, 8)
                                while self.grid[new_box_idx][x][y] == 'x' or self.grid[new_box_idx][x][y] == 'o' or self.grid[new_box_idx][x][y] == 'new_o' or check_filled[new_box_idx] == True or check_filled[new_box_idx] == 'a':
                                    x = random.randint(0, 2)
                                    y = random.randint(0, 2)
                                    new_box_idx = random.randint(0, 8)
                                self.grid[new_box_idx][x][y] = 'new_o'
                                if (y, x) == (0, 0):
                                    next_box = [0]
                                elif (y, x) == (0, 1):
                                    next_box = [1]
                                elif (y, x) == (0, 2):
                                    next_box = [2]
                                elif (y, x) == (1, 0):
                                    next_box = [3]
                                elif (y, x) == (1, 1):
                                    next_box = [4]
                                elif (y, x) == (1, 2):
                                    next_box = [5]
                                elif (y, x) == (2, 0):
                                    next_box = [6]
                                elif (y, x) == (2, 1):
                                    next_box = [7]
                                elif (y, x) == (2, 2):
                                    next_box = [8]
                            count = 0
                            for box in self.grid:
                                print(count, box)
                                count += 1

                        # medium
                        elif self.easy_hard == 'medium':
                            def find_next_box(x,y):
                                if (x, y) == (0, 0):
                                    next_box = 0
                                elif (x, y) == (0, 1):
                                    next_box = 1
                                elif (x, y) == (0, 2):
                                    next_box = 2
                                elif (x, y) == (1, 0):
                                    next_box = 3
                                elif (x, y) == (1, 1):
                                    next_box = 4
                                elif (x, y) == (1, 2):
                                    next_box = 5
                                elif (x, y) == (2, 0):
                                    next_box = 6
                                elif (x, y) == (2, 1):
                                    next_box = 7
                                elif (x, y) == (2, 2):
                                    next_box = 8
                                return(next_box)
                            print('box idx:', box_idx)
                            print('filled or not:',check_filled[box_idx])
                            # the box is not filled
                            if x_change and check_filled[box_idx] == False:
                                print('box_idx is not filled')
                                x = -1
                                y = -1
                                # list the pairs of x, y that are possible for the computer to fill
                                available_grids = []
                                for row in range(len(self.grid[box_idx])):
                                    for item in range(len(self.grid[box_idx][row])):
                                        if self.grid[box_idx][row][item] == 0:
                                            available_grids.append((row, item))  #y, x
                                # if there is no x and y value that can be connected
                                if x == -1 or y == -1:
                                    # give a random value to x and y
                                    x = available_grids[0][1]
                                    y = available_grids[0][0]
                                # if horizontal or vertical or slant cross of a box is possible, fill
                                computer_fill_line = False
                                # horizontal
                                for row in range(len(self.grid[box_idx])):
                                    if (self.grid[box_idx][row][0] == 'o' and self.grid[box_idx][row][1] == 'o') or (self.grid[box_idx][row][0] == 'new_o' and self.grid[box][row][1] == 'o') or (self.grid[box_idx][row][0] == 'o' and self.grid[box_idx][row][1] == 'new_o'):
                                        y = row
                                        x = 2
                                        computer_fill_line = True
                                        if self.grid[box_idx][y][x] != 0:
                                            y = -1
                                            x = -1
                                            computer_fill_line = False
                                        print('row:',computer_fill_line)
                                    if computer_fill_line == False:
                                        if (self.grid[box_idx][row][0] == 'o' and self.grid[box_idx][row][2] == 'o') or (self.grid[box_idx][row][0] == 'new_o' and self.grid[box_idx][row][2] == 'o') or (self.grid[box_idx][row][0] == 'o' and self.grid[box_idx][row][2] == 'new_o'):
                                            y = row
                                            x = 1
                                            computer_fill_line = True
                                            if self.grid[box_idx][y][x] != 0:
                                                y = -1
                                                x = -1
                                                computer_fill_line = False
                                            print('row:',computer_fill_line)
                                    if computer_fill_line == False:
                                        if (self.grid[box_idx][row][1] == 'o' and self.grid[box_idx][row][2] == 'o') or (self.grid[box_idx][row][1] == 'new_o' and self.grid[box_idx][row][2] == 'o') or (self.grid[box_idx][row][1] == 'o' and self.grid[box_idx][row][2] == 'new_o'):
                                            y = row
                                            x = 0
                                            computer_fill_line = True
                                            if self.grid[box_idx][y][x] != 0:
                                                y = -1
                                                x = -1
                                                computer_fill_line = False
                                            print('row:',computer_fill_line)
                                # slant 1
                                if computer_fill_line == False:
                                    if (self.grid[box_idx][0][0] == 'o' and self.grid[box_idx][1][1] == 'o') or (self.grid[box_idx][0][0] == 'new_o' and self.grid[box_idx][1][1] == 'o') or (self.grid[box_idx][0][0] == 'o' and self.grid[box_idx][1][1] == 'new_o'):
                                        y = 2
                                        x = 2
                                        computer_fill_line = True
                                        if self.grid[box_idx][y][x] != 0:
                                            y = -1
                                            x = -1
                                            computer_fill_line = False
                                        print('slant1:',computer_fill_line)
                                if computer_fill_line == False:
                                    if (self.grid[box_idx][1][1] == 'o' or self.grid[box_idx][2][2] == 'o') and (self.grid[box_idx][1][1] == 'o' or self.grid[box_idx][2][2] == 'new_o') and (self.grid[box_idx][1][1] == 'new_o' or self.grid[box_idx][2][2] == 'o'):
                                        y = 0
                                        x = 0
                                        computer_fill_line = True
                                        if self.grid[box_idx][y][x] != 0:
                                            y = -1
                                            x = -1
                                            computer_fill_line = False
                                        print('slant1:',computer_fill_line)
                                if computer_fill_line == False:
                                    if (self.grid[box_idx][0][0] == 'o' or self.grid[box_idx][2][2] == 'o') and (self.grid[box_idx][0][0] == 'o' or self.grid[box_idx][2][2] == 'new_o') and (self.grid[box_idx][0][0] == 'new_o' or self.grid[box_idx][2][2] == 'o'):
                                        y = 1
                                        x = 1
                                        computer_fill_line = True
                                        if self.grid[box_idx][y][x] != 0:
                                            y = -1
                                            x = -1
                                            computer_fill_line = False
                                        print('slant1:',computer_fill_line)
                                # slant 2
                                if computer_fill_line == False:
                                    if (self.grid[box_idx][0][2] == 'o' and self.grid[box_idx][1][1] == 'o') or (self.grid[box_idx][0][2] == 'new_o' and self.grid[box_idx][1][1] == 'o') or (self.grid[box_idx][0][2] == 'o' and self.grid[box_idx][1][1] == 'new_o'):
                                        y = 2
                                        x = 0
                                        computer_fill_line = True
                                        if self.grid[box_idx][y][x] != 0:
                                            y = -1
                                            x = -1
                                            computer_fill_line = False
                                        print('slant2:',computer_fill_line)
                                if computer_fill_line == False:
                                    if (self.grid[box_idx][1][1] == 'o' or self.grid[box_idx][2][0] == 'o') and (self.grid[box_idx][1][1] == 'o' or self.grid[box_idx][2][0] == 'new_o') and (self.grid[box_idx][1][1] == 'new_o' or self.grid[box_idx][2][0] == 'o'):
                                        y = 0
                                        x = 2
                                        computer_fill_line = True
                                        if self.grid[box_idx][y][x] != 0:
                                            y = -1
                                            x = -1
                                            computer_fill_line = False
                                        print('slant2:',computer_fill_line)
                                if computer_fill_line == False:
                                    if (self.grid[box_idx][0][2] == 'o' or self.grid[box_idx][2][0] == 'o') and (self.grid[box_idx][0][2] == 'o' or self.grid[box_idx][2][0] == 'new_o') and (self.grid[box_idx][0][2] == 'new_o' or self.grid[box_idx][2][0] == 'o'):
                                        y = 1
                                        x = 1
                                        computer_fill_line = True
                                        if self.grid[box_idx][y][x] != 0:
                                            y = -1
                                            x = -1
                                            computer_fill_line = False
                                        print('slant2:',computer_fill_line)
                                # straight
                                for column in range(3):
                                    if computer_fill_line == False:
                                        if (self.grid[box_idx][0][column] == 'o' and self.grid[box_idx][1][column] == 'o') or (self.grid[box_idx][0][column] == 'new_o' and self.grid[box_idx][1][column] == 'o') or (self.grid[box_idx][0][column] == 'o' and self.grid[box_idx][1][column] == 'new_o'):
                                            x = column
                                            y = 2
                                            computer_fill_line = True
                                            if self.grid[box_idx][y][x] != 0:
                                                y = -1
                                                x = -1
                                                computer_fill_line = False
                                            print('straight:',computer_fill_line)
                                    if computer_fill_line == False:
                                        if (self.grid[box_idx][0][column] == 'o' and self.grid[box_idx][2][column] == 'o') or (self.grid[box_idx][0][column] == 'new_o' and self.grid[box_idx][2][column] == 'o') or (self.grid[box_idx][0][column] == 'o' and self.grid[box_idx][2][column] == 'new_o'):
                                            x = column
                                            y = 1
                                            computer_fill_line = True
                                            if self.grid[box_idx][y][x] != 0:
                                                y = -1
                                                x = -1
                                                computer_fill_line = False
                                            print('straight:',computer_fill_line)
                                    if computer_fill_line == False:
                                        if (self.grid[box_idx][1][column] == 'o' and self.grid[box_idx][2][column] == 'o') or (self.grid[box_idx][1][column] == 'new_o' and self.grid[box_idx][2][column] == 'o') or (self.grid[box_idx][1][column] == 'o' and self.grid[box_idx][2][column] == 'new_o'):
                                            x = column
                                            y = 0
                                            computer_fill_line = True
                                            if self.grid[box_idx][y][x] != 0:
                                                y = -1
                                                x = -1
                                                computer_fill_line = False
                                            print('straight:',computer_fill_line)
                                print('computer_fill_line:',computer_fill_line)
                                # if horizontal or vertical or slant cross of a box for the user is possible, fill
                                computer_block_user = False
                                # bug in the boolean: if the other grid is filled, then skip the situation
                                if computer_fill_line == False:
                                    # horizontal
                                    for row in range(len(self.grid[box_idx])):
                                        if self.grid[box_idx][row][0] == 'x' and self.grid[box_idx][row][1] == 'x' and self.grid[box_idx][row][2] == 0:
                                            y = row
                                            x = 2
                                            computer_block_user = True
                                            next_box = find_next_box(x,y)
                                            if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                y = -1
                                                x = -1
                                                computer_block_user = False
                                        elif self.grid[box_idx][row][0] == 'x' and self.grid[box_idx][row][2] == 'x' and self.grid[box_idx][row][1] == 0:
                                            y = row
                                            x = 1
                                            computer_block_user = True
                                            next_box = find_next_box(x,y)
                                            if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                y = -1
                                                x = -1
                                                computer_block_user = False
                                        elif self.grid[box_idx][row][1] == 'x' and self.grid[box_idx][row][2] == 'x' and self.grid[box_idx][row][0] == 0:
                                            y = row
                                            x = 0
                                            computer_block_user = True
                                            next_box = find_next_box(x,y)
                                            if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                y = -1
                                                x = -1
                                                computer_block_user = False
                                    # slant 1
                                    if self.grid[box_idx][0][0] == 'x' and self.grid[box_idx][1][1] == 'x' and self.grid[box_idx][2][2] == 0:
                                        y = 2
                                        x = 2
                                        computer_block_user = True
                                        next_box = find_next_box(x,y)
                                        if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                            y = -1
                                            x = -1
                                            computer_block_user = False
                                    elif self.grid[box_idx][1][1] == 'x' and self.grid[box_idx][2][2] == 'x' and self.grid[box_idx][0][0] == 0:
                                        y = 0
                                        x = 0
                                        computer_block_user = True
                                        next_box = find_next_box(x,y)
                                        if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                            y = -1
                                            x = -1
                                            computer_block_user = False
                                    elif self.grid[box_idx][0][0] == 'x' and self.grid[box_idx][2][2] == 'x' and self.grid[box_idx][1][1] == 0:
                                        y = 1
                                        x = 1
                                        computer_block_user = True
                                        next_box = find_next_box(x,y)
                                        if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                            y = -1
                                            x = -1
                                            computer_block_user = False
                                    # slant 2
                                    if self.grid[box_idx][0][2] == 'x' and self.grid[box_idx][1][1] == 'x' and self.grid[box_idx][2][0] == 0:
                                        y = 2
                                        x = 0
                                        computer_block_user = True
                                        next_box = find_next_box(x,y)
                                        if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                            y = -1
                                            x = -1
                                            computer_block_user = False
                                    elif self.grid[box_idx][1][1] == 'x' and self.grid[box_idx][2][0] == 'x' and self.grid[box_idx][0][2] == 0:
                                        y = 0
                                        x = 2
                                        computer_block_user = True
                                        next_box = find_next_box(x,y)
                                        if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                            y = -1
                                            x = -1
                                            computer_block_user = False
                                    elif self.grid[box_idx][0][2] == 'x' and self.grid[box_idx][2][0] == 'x' and self.grid[box_idx][1][1] == 0:
                                        y = 1
                                        x = 1
                                        computer_block_user = True
                                        next_box = find_next_box(x,y)
                                        if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                            y = -1
                                            x = -1
                                            computer_block_user = False
                                    # straight
                                    for column in range(3):
                                        if self.grid[box_idx][0][column] == 'x' and self.grid[box_idx][1][column] == 'x' and self.grid[box_idx][2][column] == 0:
                                            x = column
                                            y = 2
                                            computer_block_user = True
                                            next_box = find_next_box(x,y)
                                            if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                y = -1
                                                x = -1
                                                computer_block_user = False
                                        elif self.grid[box_idx][0][column] == 'x' and self.grid[box_idx][2][column] == 'x' and self.grid[box_idx][1][column] == 0:
                                            x = column
                                            y = 1
                                            computer_block_user = True
                                            next_box = find_next_box(x,y)
                                            if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                y = -1
                                                x = -1
                                                computer_block_user = False
                                        elif self.grid[box_idx][1][column] == 'x' and self.grid[box_idx][2][column] == 'x' and self.grid[box_idx][0][column] == 0:
                                            x = column
                                            y = 0
                                            computer_block_user = True
                                            next_box = find_next_box(x,y)
                                            if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                y = -1
                                                x = -1
                                                computer_block_user = False
                                if x == -1 or y == -1:
                                    y = available_grids[0][0]
                                    x = available_grids[0][1]
                                print('computer_bock_user:',computer_block_user)
                                print('current y_x:',y,x)
                                if (y, x) == (0, 0):
                                    next_box = [0]
                                elif (y, x) == (0, 1):
                                    next_box = [1]
                                elif (y, x) == (0, 2):
                                    next_box = [2]
                                elif (y, x) == (1, 0):
                                    next_box = [3]
                                elif (y, x) == (1, 1):
                                    next_box = [4]
                                elif (y, x) == (1, 2):
                                    next_box = [5]
                                elif (y, x) == (2, 0):
                                    next_box = [6]
                                elif (y, x) == (2, 1):
                                    next_box = [7]
                                elif (y, x) == (2, 2):
                                    next_box = [8]
                                # if the user can fill directly, assign the computer to another position in the given box
                                user_can_fill = False
                                # horizontal
                                for row in range(3):
                                    print(self.grid[next_box[0]][row][0])
                                    print(self.grid[next_box[0]][row][1])
                                    print(self.grid[next_box[0]][row][2])
                                    if self.grid[next_box[0]][row][0] == 'x' and self.grid[next_box[0]][row][1] == 'x' and self.grid[next_box[0]][row][2] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                    elif self.grid[next_box[0]][row][0] == 'x' and self.grid[next_box[0]][row][2] == 'x' and self.grid[next_box[0]][row][1] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                    elif self.grid[next_box[0]][row][1] == 'x' and self.grid[next_box[0]][row][2] == 'x' and self.grid[next_box[0]][row][0] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                # slant 1
                                if self.grid[next_box[0]][0][0] == 'x' and self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][2] == 0 and check_filled[next_box[0]] == False:
                                    user_can_fill = True
                                elif self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][2] == 'x' and self.grid[next_box[0]][0][0] == 0 and check_filled[next_box[0]] == False:
                                    user_can_fill = True
                                elif self.grid[next_box[0]][0][0] == 'x' and self.grid[next_box[0]][2][2] == 'x' and self.grid[next_box[0]][1][1] == 0 and check_filled[next_box[0]] == False:
                                    user_can_fill = True
                                # slant 2
                                if self.grid[next_box[0]][0][2] == 'x' and self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][0] == 0 and check_filled[next_box[0]] == False:
                                    user_can_fill = True
                                elif self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][0] == 'x' and self.grid[next_box[0]][0][2] == 0 and check_filled[next_box[0]] == False:
                                    user_can_fill = True
                                elif self.grid[next_box[0]][0][2] == 'x' and self.grid[next_box[0]][2][0] == 'x' and self.grid[next_box[0]][1][1] == 0 and check_filled[next_box[0]] == False:
                                    user_can_fill = True
                                # straight
                                for column in range(3):
                                    if self.grid[next_box[0]][0][column] == 'x' and self.grid[next_box[0]][1][column] == 'x' and self.grid[next_box[0]][2][column] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                    elif self.grid[next_box[0]][0][column] == 'x' and self.grid[next_box[0]][2][column] == 'x' and self.grid[next_box[0]][1][column] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                    elif self.grid[next_box[0]][1][column] == 'x' and self.grid[next_box[0]][2][column] == 'x' and self.grid[next_box[0]][0][column] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                print('user_can_fill(1):',user_can_fill)
                                print('check_user_can_fill:',self.grid[next_box[0]])
                                if (user_can_fill or check_filled[next_box[0]] != False) and not computer_fill_line:
                                    for pair in available_grids:
                                        temp_y = pair[0]
                                        temp_x = pair[1]
                                        if (temp_y, temp_x) == (0, 0):
                                            next_box = [0]
                                        elif (temp_y, temp_x) == (0, 1):
                                            next_box = [1]
                                        elif (temp_y, temp_x) == (0, 2):
                                            next_box = [2]
                                        elif (temp_y, temp_x) == (1, 0):
                                            next_box = [3]
                                        elif (temp_y, temp_x) == (1, 1):
                                            next_box = [4]
                                        elif (temp_y, temp_x) == (1, 2):
                                            next_box = [5]
                                        elif (temp_y, temp_x) == (2, 0):
                                            next_box = [6]
                                        elif (temp_y, temp_x) == (2, 1):
                                            next_box = [7]
                                        elif (temp_y, temp_x) == (2, 2):
                                            next_box = [8]
                                        user_can_fill = False
                                        # horizontal
                                        for row in range(3):
                                            if self.grid[next_box[0]][row][0] == 'x' and self.grid[next_box[0]][row][1] == 'x' and self.grid[next_box[0]][row][2] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                            elif self.grid[next_box[0]][row][0] == 'x' and self.grid[next_box[0]][row][2] == 'x' and self.grid[next_box[0]][row][1] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                            elif self.grid[next_box[0]][row][1] == 'x' and self.grid[next_box[0]][row][2] == 'x' and self.grid[next_box[0]][row][0] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                        # slant 1
                                        if self.grid[next_box[0]][0][0] == 'x' and self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][2] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                        elif self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][2] == 'x' and self.grid[next_box[0]][0][0] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                        elif self.grid[next_box[0]][0][0] == 'x' and self.grid[next_box[0]][2][2] == 'x' and self.grid[next_box[0]][1][1] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                        # slant 2
                                        if self.grid[next_box[0]][0][2] == 'x' and self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][0] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                        elif self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][0] == 'x' and self.grid[next_box[0]][0][2] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                        elif self.grid[next_box[0]][0][2] == 'x' and self.grid[next_box[0]][2][0] == 'x' and self.grid[next_box[0]][1][1] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                        # straight
                                        for column in range(3):
                                            if self.grid[next_box[0]][0][column] == 'x' and self.grid[next_box[0]][1][column] == 'x' and self.grid[next_box[0]][2][column] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                            elif self.grid[next_box[0]][0][column] == 'x' and self.grid[next_box[0]][2][column] == 'x' and self.grid[next_box[0]][1][column] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                            elif self.grid[next_box[0]][1][column] == 'x' and self.grid[next_box[0]][2][column] == 'x' and self.grid[next_box[0]][0][column] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                        print('in user_can_fill loop; pair =',pair)
                                        print('user_can_fill:',user_can_fill)
                                        if user_can_fill == False and check_filled[next_box[0]] == False:
                                            print('in user_fill_line, check_filled[next_box[0]]:',check_filled[next_box[0]])
                                            x = temp_x
                                            y = temp_y
                                            break
                                if x == -1 or y == -1:
                                    y = available_grids[0][0]
                                    x = available_grids[0][1]
                                # fill self.grid[box_idx][y][x] with 'new_o'
                                self.grid[box_idx][y][x] = 'new_o'
                                # next_box is the box that tha user is supposed to go to after the computer has made this step
                                if (y, x) == (0, 0):
                                    next_box = [0]
                                elif (y, x) == (0, 1):
                                    next_box = [1]
                                elif (y, x) == (0, 2):
                                    next_box = [2]
                                elif (y, x) == (1, 0):
                                    next_box = [3]
                                elif (y, x) == (1, 1):
                                    next_box = [4]
                                elif (y, x) == (1, 2):
                                    next_box = [5]
                                elif (y, x) == (2, 0):
                                    next_box = [6]
                                elif (y, x) == (2, 1):
                                    next_box = [7]
                                elif (y, x) == (2, 2):
                                    next_box = [8]

                            # in the following senario, the box the computer is supposed to go to is filled
                            elif check_filled[box_idx] != False and x_change:
                                print('box_idx is filled')
                                x = -1
                                y = -1
                                new_box_idx = -1

                                available_box_grid = []
                                for box in range(len(self.grid)):
                                    if check_filled[box] == False:
                                        for row in range(len(self.grid[box])):
                                            for item in range(len(self.grid[box][row])):
                                                if self.grid[box][row][item] == 0:
                                                    available_box_grid.append((box, row, item)) #box_idx, y, x
                                print(available_box_grid)
                                # possibly no x and y values can be connected or (user) blocked
                                if x == -1 or y == -1 or new_box_idx == -1: # no box_grid can be filled or can block the user's way
                                    # if there is no place to fill, then select randomly first
                                    new_box_idx = available_box_grid[0][0]
                                    x = available_box_grid[0][1]
                                    y = available_box_grid[0][2]

                                # second priority
                                # check if any other box can be filled (since the computer can go random now)
                                computer_fill_line = False
                                for box_idx in range(len(self.grid)):
                                    if check_filled[box_idx] == False:
                                        # horizontal
                                        for row in range(len(self.grid[box_idx])):
                                            if (self.grid[box_idx][row][0] == 'o' and self.grid[box_idx][row][1] == 'o') or (self.grid[box_idx][row][0] == 'new_o' and self.grid[box][row][1] == 'o') or (self.grid[box_idx][row][0] == 'o' and self.grid[box_idx][row][1] == 'new_o'):
                                                new_box_idx = box_idx
                                                y = row
                                                x = 2
                                                computer_fill_line = True
                                                if self.grid[new_box_idx][y][x] != 0:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_fill_line = False
                                                print('row:',computer_fill_line)
                                            if computer_fill_line == False:
                                                if (self.grid[box_idx][row][0] == 'o' and self.grid[box_idx][row][2] == 'o') or (self.grid[box_idx][row][0] == 'new_o' and self.grid[box_idx][row][2] == 'o') or (self.grid[box_idx][row][0] == 'o' and self.grid[box_idx][row][2] == 'new_o'):
                                                    new_box_idx = box_idx
                                                    y = row
                                                    x = 1
                                                    computer_fill_line = True
                                                    if self.grid[new_box_idx][y][x] != 0:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_fill_line = False
                                                    print('row:',computer_fill_line)
                                            if computer_fill_line == False:
                                                if (self.grid[box_idx][row][1] == 'o' and self.grid[box_idx][row][2] == 'o') or (self.grid[box_idx][row][1] == 'new_o' and self.grid[box_idx][row][2] == 'o') or (self.grid[box_idx][row][1] == 'o' and self.grid[box_idx][row][2] == 'new_o'):
                                                    new_box_idx = box_idx
                                                    y = row
                                                    x = 0
                                                    computer_fill_line = True
                                                    if self.grid[new_box_idx][y][x] != 0:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_fill_line = False
                                                    print('row:',computer_fill_line)
                                        # slant 1
                                        if computer_fill_line == False:
                                            if (self.grid[box_idx][0][0] == 'o' and self.grid[box_idx][1][1] == 'o') or (self.grid[box_idx][0][0] == 'new_o' and self.grid[box_idx][1][1] == 'o') or (self.grid[box_idx][0][0] == 'o' and self.grid[box_idx][1][1] == 'new_o'):
                                                new_box_idx = box_idx
                                                y = 2
                                                x = 2
                                                computer_fill_line = True
                                                if self.grid[new_box_idx][y][x] != 0:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_fill_line = False
                                                print('slant1:',computer_fill_line)
                                        if computer_fill_line == False:
                                            if (self.grid[box_idx][1][1] == 'o' or self.grid[box_idx][2][2] == 'o') and (self.grid[box_idx][1][1] == 'o' or self.grid[box_idx][2][2] == 'new_o') and (self.grid[box_idx][1][1] == 'new_o' or self.grid[box_idx][2][2] == 'o'):
                                                new_box_idx = box_idx
                                                y = 0
                                                x = 0
                                                computer_fill_line = True
                                                if self.grid[new_box_idx][y][x] != 0:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_fill_line = False
                                                print('slant1:',computer_fill_line)
                                        if computer_fill_line == False:
                                            if (self.grid[box_idx][0][0] == 'o' or self.grid[box_idx][2][2] == 'o') and (self.grid[box_idx][0][0] == 'o' or self.grid[box_idx][2][2] == 'new_o') and (self.grid[box_idx][0][0] == 'new_o' or self.grid[box_idx][2][2] == 'o'):
                                                new_box_idx = box_idx
                                                y = 1
                                                x = 1
                                                computer_fill_line = True
                                                if self.grid[new_box_idx][y][x] != 0:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_fill_line = False
                                                print('slant1:',computer_fill_line)
                                        # slant 2
                                        if computer_fill_line == False:
                                            if (self.grid[box_idx][0][2] == 'o' and self.grid[box_idx][1][1] == 'o') or (self.grid[box_idx][0][2] == 'new_o' and self.grid[box_idx][1][1] == 'o') or (self.grid[box_idx][0][2] == 'o' and self.grid[box_idx][1][1] == 'new_o'):  
                                                new_box_idx = box_idx
                                                y = 2
                                                x = 0
                                                computer_fill_line = True
                                                if self.grid[new_box_idx][y][x] != 0:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_fill_line = False
                                                print('slant2:',computer_fill_line)
                                        if computer_fill_line == False:
                                            if (self.grid[box_idx][1][1] == 'o' or self.grid[box_idx][2][0] == 'o') and (self.grid[box_idx][1][1] == 'o' or self.grid[box_idx][2][0] == 'new_o') and (self.grid[box_idx][1][1] == 'new_o' or self.grid[box_idx][2][0] == 'o'):
                                                new_box_idx = box_idx
                                                y = 0
                                                x = 2
                                                computer_fill_line = True
                                                if self.grid[new_box_idx][y][x] != 0:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_fill_line = False
                                                print('slant2:',computer_fill_line)
                                        if computer_fill_line == False:
                                            if (self.grid[box_idx][0][2] == 'o' or self.grid[box_idx][2][0] == 'o') and (self.grid[box_idx][0][2] == 'o' or self.grid[box_idx][2][0] == 'new_o') and (self.grid[box_idx][0][2] == 'new_o' or self.grid[box_idx][2][0] == 'o'):
                                                new_box_idx = box_idx
                                                y = 1
                                                x = 1
                                                computer_fill_line = True
                                                if self.grid[new_box_idx][y][x] != 0:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_fill_line = False
                                                print('slant2:',computer_fill_line)
                                        # straight
                                        for column in range(3):
                                            if computer_fill_line == False:
                                                if (self.grid[box_idx][0][column] == 'o' and self.grid[box_idx][1][column] == 'o') or (self.grid[box_idx][0][column] == 'new_o' and self.grid[box_idx][1][column] == 'o') or (self.grid[box_idx][0][column] == 'o' and self.grid[box_idx][1][column] == 'new_o'):
                                                    new_box_idx = box_idx
                                                    x = column
                                                    y = 2
                                                    computer_fill_line = True
                                                    if self.grid[new_box_idx][y][x] != 0:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_fill_line = False
                                                    print('straight:',computer_fill_line)
                                            if computer_fill_line == False:
                                                if (self.grid[box_idx][0][column] == 'o' and self.grid[box_idx][2][column] == 'o') or (self.grid[box_idx][0][column] == 'new_o' and self.grid[box_idx][2][column] == 'o') or (self.grid[box_idx][0][column] == 'o' and self.grid[box_idx][2][column] == 'new_o'):
                                                    new_box_idx = box_idx
                                                    x = column
                                                    y = 1
                                                    computer_fill_line = True
                                                    if self.grid[new_box_idx][y][x] != 0:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_fill_line = False
                                                    print('straight:',computer_fill_line)
                                            if computer_fill_line == False:
                                                if (self.grid[box_idx][1][column] == 'o' and self.grid[box_idx][2][column] == 'o') or (self.grid[box_idx][1][column] == 'new_o' and self.grid[box_idx][2][column] == 'o') or (self.grid[box_idx][1][column] == 'o' and self.grid[box_idx][2][column] == 'new_o'):
                                                    new_box_idx = box_idx
                                                    x = column
                                                    y = 0
                                                    computer_fill_line = True
                                                    if self.grid[new_box_idx][y][x] != 0:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_fill_line = False
                                                    print('straight:',computer_fill_line)
                                print(self.grid[new_box_idx])
                                # check if the computer can fill boxes that can block the user's way
                                # third priority
                                if computer_fill_line == False:
                                    for box_idx in range(len(self.grid)):
                                        if check_filled[box_idx] == False:
                                            # horizontal
                                            for row in range(len(self.grid[box_idx])):
                                                if self.grid[box_idx][row][0] == 'x' and self.grid[box_idx][row][1] == 'x' and self.grid[box_idx][row][2] == 0:
                                                    new_box_idx = box_idx
                                                    y = row
                                                    x = 2
                                                    computer_block_user = True
                                                    next_box = find_next_box(x,y)
                                                    if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_block_user = False
                                                elif self.grid[box_idx][row][0] == 'x' and self.grid[box_idx][row][2] == 'x' and self.grid[box_idx][row][1] == 0:
                                                    new_box_idx = box_idx
                                                    y = row
                                                    x = 1
                                                    computer_block_user = True
                                                    next_box = find_next_box(x,y)
                                                    if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_block_user = False
                                                elif self.grid[box_idx][row][1] == 'x' and self.grid[box_idx][row][2] == 'x' and self.grid[box_idx][row][0] == 0:
                                                    new_box_idx = box_idx
                                                    y = row
                                                    x = 0
                                                    computer_block_user = True
                                                    next_box = find_next_box(x,y)
                                                    if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_block_user = False
                                            # slant 1
                                            if self.grid[box_idx][0][0] == 'x' and self.grid[box_idx][1][1] == 'x' and self.grid[box_idx][2][2] == 0:
                                                new_box_idx = box_idx
                                                y = 2
                                                x = 2
                                                computer_block_user = True
                                                next_box = find_next_box(x,y)
                                                if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_block_user = False
                                            elif self.grid[box_idx][1][1] == 'x' and self.grid[box_idx][2][2] == 'x' and self.grid[box_idx][0][0] == 0:
                                                new_box_idx = box_idx
                                                y = 0
                                                x = 0
                                                computer_block_user = True
                                                next_box = find_next_box(x,y)
                                                if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_block_user = False
                                            elif self.grid[box_idx][0][0] == 'x' and self.grid[box_idx][2][2] == 'x' and self.grid[box_idx][1][1] == 0:
                                                new_box_idx = box_idx
                                                y = 1
                                                x = 1
                                                computer_block_user = True
                                                next_box = find_next_box(x,y)
                                                if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_block_user = False
                                            # slant 2
                                            if self.grid[box_idx][0][2] == 'x' and self.grid[box_idx][1][1] == 'x' and self.grid[box_idx][2][0] == 0:
                                                new_box_idx = box_idx
                                                y = 2
                                                x = 0
                                                computer_block_user = True
                                                next_box = find_next_box(x,y)
                                                if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_block_user = False
                                            elif self.grid[box_idx][1][1] == 'x' and self.grid[box_idx][2][0] == 'x' and self.grid[box_idx][0][2] == 0:
                                                new_box_idx = box_idx
                                                y = 0
                                                x = 2
                                                computer_block_user = True
                                                next_box = find_next_box(x,y)
                                                if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_block_user = False
                                            elif self.grid[box_idx][0][2] == 'x' and self.grid[box_idx][2][0] == 'x' and self.grid[box_idx][1][1] == 0:
                                                new_box_idx = box_idx
                                                y = 1
                                                x = 1
                                                computer_block_user = True
                                                next_box = find_next_box(x,y)
                                                if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                    y = -1
                                                    x = -1
                                                    new_box_idx = -1
                                                    computer_block_user = False
                                            # straight
                                            for column in range(3):
                                                if self.grid[box_idx][0][column] == 'x' and self.grid[box_idx][1][column] == 'x' and self.grid[box_idx][2][column] == 0:
                                                    new_box_idx = box_idx
                                                    x = column
                                                    y = 2
                                                    computer_block_user = True
                                                    next_box = find_next_box(x,y)
                                                    if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_block_user = False
                                                elif self.grid[box_idx][0][column] == 'x' and self.grid[box_idx][2][column] == 'x' and self.grid[box_idx][1][column]:
                                                    new_box_idx = box_idx
                                                    x = column
                                                    y = 1
                                                    computer_block_user = True
                                                    next_box = find_next_box(x,y)
                                                    if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_block_user = False
                                                elif self.grid[box_idx][1][column] == 'x' and self.grid[box_idx][2][column] == 'x' and self.grid[box_idx][0][column]:
                                                    new_box_idx = box_idx
                                                    x = column
                                                    y = 0
                                                    computer_block_user = True
                                                    next_box = find_next_box(x,y)
                                                    if self.grid[box_idx][y][x] != 0 or check_filled[next_box] != False:
                                                        y = -1
                                                        x = -1
                                                        new_box_idx = -1
                                                        computer_block_user = False
                                print('computer_block_user:',computer_block_user)
                                if x == -1 or y == -1 or new_box_idx == -1:
                                    y = available_box_grid[0][0]
                                    x = available_box_grid[0][1]
                                if (y, x) == (0, 0):
                                    next_box = [0]
                                elif (y, x) == (0, 1):
                                    next_box = [1]
                                elif (y, x) == (0, 2):
                                    next_box = [2]
                                elif (y, x) == (1, 0):
                                    next_box = [3]
                                elif (y, x) == (1, 1):
                                    next_box = [4]
                                elif (y, x) == (1, 2):
                                    next_box = [5]
                                elif (y, x) == (2, 0):
                                    next_box = [6]
                                elif (y, x) == (2, 1):
                                    next_box = [7]
                                elif (y, x) == (2, 2):
                                    next_box = [8]
                                # if the user can fill directly, assign the computer to another position in the given box
                                for pair in available_box_grid:
                                    box_idx = pair[0]
                                    # horizontal
                                    for row in range(len(self.grid[box_idx])):
                                        if self.grid[next_box[0]][row][0] == 'x' and self.grid[next_box[0]][row][1] == 'x' and self.grid[next_box[0]][row][2] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                        elif self.grid[next_box[0]][row][0] == 'x' and self.grid[next_box[0]][row][2] == 'x' and self.grid[next_box[0]][row][1] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                        elif self.grid[next_box[0]][row][1] == 'x' and self.grid[next_box[0]][row][2] == 'x' and self.grid[next_box[0]][row][0] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                    # slant 1
                                    if self.grid[next_box[0]][0][0] == 'x' and self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][2] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                    elif self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][2] == 'x' and self.grid[next_box[0]][0][0] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                    elif self.grid[next_box[0]][0][0] == 'x' and self.grid[next_box[0]][2][2] == 'x' and self.grid[next_box[0]][1][1] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                    # slant 2
                                    if self.grid[next_box[0]][0][2] == 'x' and self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][0] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                    elif self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][0] == 'x' and self.grid[next_box[0]][0][2] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                    elif self.grid[next_box[0]][0][2] == 'x' and self.grid[next_box[0]][2][0] == 'x' and self.grid[next_box[0]][1][1] == 0 and check_filled[next_box[0]] == False:
                                        user_can_fill = True
                                    # straight
                                    for column in range(3):
                                        if self.grid[next_box[0]][0][column] == 'x' and self.grid[next_box[0]][1][column] == 'x' and self.grid[next_box[0]][2][column] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                        elif self.grid[next_box[0]][0][column] == 'x' and self.grid[next_box[0]][2][column] == 'x' and self.grid[next_box[0]][1][column] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                        elif self.grid[next_box[0]][1][column] == 'x' and self.grid[next_box[0]][2][column] == 'x' and self.grid[next_box[0]][0][column] == 0 and check_filled[next_box[0]] == False:
                                            user_can_fill = True
                                    print('when detecting user_can_fill: ',pair)
                                    print('user_can_fill:',user_can_fill)
                                    if (user_can_fill or check_filled[next_box[0]]) and not computer_fill_line:
                                        for pair in available_box_grid:
                                            temp_new_box_idx = pair[0]
                                            temp_y = pair[1]
                                            temp_x = pair[2]
                                            if (temp_y, temp_x) == (0, 0):
                                                next_box = [0]
                                            elif (temp_y, temp_x) == (0, 1):
                                                next_box = [1]
                                            elif (temp_y, temp_x) == (0, 2):
                                                next_box = [2]
                                            elif (temp_y, temp_x) == (1, 0):
                                                next_box = [3]
                                            elif (temp_y, temp_x) == (1, 1):
                                                next_box = [4]
                                            elif (temp_y, temp_x) == (1, 2):
                                                next_box = [5]
                                            elif (temp_y, temp_x) == (2, 0):
                                                next_box = [6]
                                            elif (temp_y, temp_x) == (2, 1):
                                                next_box = [7]
                                            elif (temp_y, temp_x) == (2, 2):
                                                next_box = [8]
                                            user_can_fill = False
                                            # horizontal
                                            for row in range(len(self.grid[box_idx])):
                                                if self.grid[next_box[0]][row][0] == 'x' and self.grid[next_box[0]][row][1] == 'x' and self.grid[next_box[0]][row][2] == 0 and check_filled[next_box[0]] == False:
                                                    user_can_fill = True
                                                elif self.grid[next_box[0]][row][0] == 'x' and self.grid[next_box[0]][row][2] == 'x' and self.grid[next_box[0]][row][1] == 0 and check_filled[next_box[0]] == False:
                                                    user_can_fill = True
                                                elif self.grid[next_box[0]][row][1] == 'x' and self.grid[next_box[0]][row][2] == 'x' and self.grid[next_box[0]][row][0] == 0 and check_filled[next_box[0]] == False:
                                                    user_can_fill = True
                                            # slant 1
                                            if self.grid[next_box[0]][0][0] == 'x' and self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][2] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                            elif self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][2] == 'x' and self.grid[next_box[0]][0][0] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                            elif self.grid[next_box[0]][0][0] == 'x' and self.grid[next_box[0]][2][2] == 'x' and self.grid[next_box[0]][1][1] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                            # slant 2
                                            if self.grid[next_box[0]][0][2] == 'x' and self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][0] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                            elif self.grid[next_box[0]][1][1] == 'x' and self.grid[next_box[0]][2][0] == 'x' and self.grid[next_box[0]][0][2] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                            elif self.grid[next_box[0]][0][2] == 'x' and self.grid[next_box[0]][2][0] == 'x' and self.grid[next_box[0]][1][1] == 0 and check_filled[next_box[0]] == False:
                                                user_can_fill = True
                                            # straight
                                            for column in range(3):
                                                if self.grid[next_box[0]][0][column] == 'x' and self.grid[next_box[0]][1][column] == 'x' and self.grid[next_box[0]][2][column] == 0 and check_filled[next_box[0]] == False:
                                                    user_can_fill = True
                                                elif self.grid[next_box[0]][0][column] == 'x' and self.grid[next_box[0]][2][column] == 'x' and self.grid[next_box[0]][1][column] == 0 and check_filled[next_box[0]] == False:
                                                    user_can_fill = True
                                                elif self.grid[next_box[0]][1][column] == 'x' and self.grid[next_box[0]][2][column] == 'x' and self.grid[next_box[0]][0][column] == 0 and check_filled[next_box[0]] == False:
                                                    user_can_fill = True
                                            if user_can_fill == False and check_filled[new_box_idx] == False:
                                                new_box_idx = temp_new_box_idx
                                                y = temp_y
                                                x = temp_x
                                                print(new_box_idx,y,x)
                                                break
                                print(new_box_idx,y,x)
                                if x == -1 or y == -1 or new_box_idx == -1:
                                    y = available_grids[0][0]
                                    x = available_grids[0][1]
                                self.grid[new_box_idx][y][x] = 'new_o'
                                if (y, x) == (0, 0):
                                    next_box = [0]
                                elif (y, x) == (0, 1):
                                    next_box = [1]
                                elif (y, x) == (0, 2):
                                    next_box = [2]
                                elif (y, x) == (1, 0):
                                    next_box = [3]
                                elif (y, x) == (1, 1):
                                    next_box = [4]
                                elif (y, x) == (1, 2):
                                    next_box = [5]
                                elif (y, x) == (2, 0):
                                    next_box = [6]
                                elif (y, x) == (2, 1):
                                    next_box = [7]
                                elif (y, x) == (2, 2):
                                    next_box = [8]

                        elif self.easy_hard == 'hard':
                            print('该功能还未开发好……')
                            X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\傻逼.png')
                            X_rect = X.get_rect()
                            X_rect.center = (
                                375, 375)
                            screen.blit(
                                X, (X_rect.x, X_rect.y))
                            pygame.display.update()

                        #######
                        # horizontal
                        for box in range(len(self.grid)):
                            for row in self.grid[box]:
                                if row[0] == 'x' and row[0] == row[1] and row[1] == row[2]:
                                    check_filled[box] = True
                                    if self.x_o == 'x':
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                    else:
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                elif (row[0] == 'o' or row[0] == 'new_o') and (row[1] == 'o' or row[1] == 'new_o') and (row[2] == 'o' or row[2] == 'new_o'):
                                    check_filled[box] = 'a'
                                    if self.x_o == 'x':
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                    else:
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()

                        # slant 1
                        for box in range(len(self.grid)):
                            if self.grid[box][0][0] == 'x' and self.grid[box][0][0] == self.grid[box][1][1] and self.grid[box][1][1] == self.grid[box][2][2]:
                                check_filled[box] = True
                                if self.x_o == 'x':
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                                else:
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                            elif (self.grid[box][0][0] == 'o' or self.grid[box][0][0] == 'new_o') and (self.grid[box][1][1] == 'o' or self.grid[box][1][1] == 'new_o') and (self.grid[box][2][2] == 'o' or self.grid[box][2][2] == 'new_o'):
                                check_filled[box] = 'a'
                                if self.x_o == 'x':
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                                else:
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                        # slant 2
                        for box in range(len(self.grid)):
                            if self.grid[box][0][2] == 'x' and self.grid[box][0][2] == self.grid[box][1][1] and self.grid[box][1][1] == self.grid[box][2][0]:
                                check_filled[box] = True
                                if self.x_o == 'x':
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                                else:
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                            elif (self.grid[box][0][2] == 'o' or self.grid[box][0][2] == 'new_o') and (self.grid[box][1][1] == 'o' or self.grid[box][1][1] == 'new_o') and (self.grid[box][2][0] == 'o' or self.grid[box][2][0] == 'new_o'):
                                check_filled[box] = 'a'
                                if self.x_o == 'x':
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                                else:
                                    X = pygame.image.load(
                                        'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                    X_rect = X.get_rect()
                                    X_rect.center = (
                                        big_center[box][0], big_center[box][1])
                                    screen.blit(
                                        X, (X_rect.x, X_rect.y))
                                    pygame.display.update()
                        # straight
                        for box in range(len(self.grid)):
                            for column in range(3):
                                if self.grid[box][0][column] == 'x' and self.grid[box][0][column] == self.grid[box][1][column] and self.grid[box][1][column] == self.grid[box][2][column]:
                                    check_filled[box] = True
                                    if self.x_o == 'x':
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                    else:
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                elif (self.grid[box][0][column] == 'o' or self.grid[box][0][column] == 'new_o') and (self.grid[box][1][column] == 'o' or self.grid[box][1][column] == 'new_o') and (self.grid[box][2][column] == 'o' or self.grid[box][2][column] == 'new_o'):
                                    check_filled[box] = 'a'
                                    if self.x_o == 'x':
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigO.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()
                                    else:
                                        X = pygame.image.load(
                                            'C:\\Users\\Duality\\Desktop\\井字棋\\BigX.png')
                                        X_rect = X.get_rect()
                                        X_rect.center = (
                                            big_center[box][0], big_center[box][1])
                                        screen.blit(
                                            X, (X_rect.x, X_rect.y))
                                        pygame.display.update()

                        ######
                        if (check_filled[0] == True and check_filled[1] == True and check_filled[2] == True) or (check_filled[3] == True and check_filled[4] == True and check_filled[5] == True) or (check_filled[6] == True and check_filled[7] == True and check_filled[8] == True) or (check_filled[0] == True and check_filled[3] == True and check_filled[6] == True) or (check_filled[1] == True and check_filled[4] == True and check_filled[7] == True) or (check_filled[2] == True and check_filled[5] == True and check_filled[8] == True) or (check_filled[0] == True and check_filled[4] == True and check_filled[8] == True) or (check_filled[2] == True and check_filled[4] == True and check_filled[6] == True):
                            print('YOU WIN!')
                            win = pygame.image.load(
                                'C:\\Users\\Duality\\Desktop\\井字棋\\WIN.png')
                            win_rect = win.get_rect()
                            win_rect.center = (
                                375, 375)
                            screen.blit(
                                win, (win_rect.x, win_rect.y))
                            pygame.display.update()
                            pygame.time.delay(3000)
                            sys.exit()

                        if (check_filled[0] == 'a' and check_filled[1] == 'a' and check_filled[2] == 'a') or (check_filled[3] == 'a' and check_filled[4] == 'a' and check_filled[5] == 'a') or (check_filled[6] == 'a' and check_filled[7] == 'a' and check_filled[8] == 'a') or (check_filled[0] == 'a' and check_filled[3] == 'a' and check_filled[6] == 'a') or (check_filled[1] == 'a' and check_filled[4] == 'a' and check_filled[7] == 'a') or (check_filled[2] == 'a' and check_filled[5] == 'a' and check_filled[8] == 'a') or (check_filled[0] == 'a' and check_filled[4] == 'a' and check_filled[8] == 'a') or (check_filled[2] == 'a' and check_filled[4] == 'a' and check_filled[6] == 'a'):
                            print('YOU LOSE!')
                            lose = pygame.image.load(
                                'C:\\Users\\Duality\\Desktop\\井字棋\\LOSE.png')
                            lose_rect = lose.get_rect()
                            lose_rect.center = (
                                375, 375)
                            screen.blit(
                                lose, (lose_rect.x, lose_rect.y))
                            pygame.display.update()
                            pygame.time.delay(3000)
                            sys.exit()

                        count = 0
                        for item in check_filled:
                            if item == 'a' or item == True:
                                count += 1
                        if count == 9:
                            print('BREAK EVEN')
                            even = pygame.image.load(
                                'C:\\Users\\Duality\\Desktop\\井字棋\\EVEN.png')
                            even_rect = even.get_rect()
                            even_rect.center = (
                                375, 375)
                            screen.blit(
                                even, (even_rect.x, even_rect.y))
                            pygame.display.update()
                            pygame.time.delay(3000)
                            sys.exit()

                        ########

            for box_idx in range(len(self.grid)):
                # x
                if box_idx == 0 or box_idx == 3 or box_idx == 6:
                    x_loc = 0
                elif box_idx == 1 or box_idx == 4 or box_idx == 7:
                    x_loc = 1
                else:
                    x_loc = 2
                # y
                if box_idx == 0 or box_idx == 1 or box_idx == 2:
                    y_loc = 0
                elif box_idx == 3 or box_idx == 4 or box_idx == 5:
                    y_loc = 1
                elif box_idx == 6 or box_idx == 7 or box_idx == 8:
                    y_loc = 2
                for row_idx in range(len(self.grid[box_idx])):
                    # row is a list of 0 or 'x'
                    for item_idx in range(len(self.grid[box_idx][row_idx])):
                        if self.grid[box_idx][row_idx][item_idx] == 'x':
                            # load image in correct center location
                            y_coor = (
                                self.position_y[y_loc][row_idx][0] + self.position_y[y_loc][row_idx][1])/2
                            x_coor = (
                                self.position_x[x_loc][item_idx][0] + self.position_x[x_loc][item_idx][1])/2
                            if self.x_o == 'x':
                                X = pygame.image.load(
                                    'C:\\Users\\Duality\\Desktop\\井字棋\\X.png')
                                X_rect = X.get_rect()
                                X_rect.center = (x_coor, y_coor)
                                screen.blit(
                                    X, (X_rect.x, X_rect.y))
                                pygame.display.update()
                            elif self.x_o == 'o':
                                O = pygame.image.load(
                                    'C:\\Users\\Duality\\Desktop\\井字棋\\O.png')
                                O_rect = O.get_rect()
                                O_rect.center = (
                                    x_coor, y_coor)
                                screen.blit(
                                    O, (O_rect.x, O_rect.y))
                                pygame.display.update()
                        if self.grid[box_idx][row_idx][item_idx] == 'o' or self.grid[box_idx][row_idx][item_idx] == 'new_o':
                            # load image in correct center location
                            y_coor = (
                                self.position_y[y_loc][row_idx][0] + self.position_y[y_loc][row_idx][1])/2
                            x_coor = (
                                self.position_x[x_loc][item_idx][0] + self.position_x[x_loc][item_idx][1])/2
                            if self.x_o == 'x':
                                X = pygame.image.load(
                                    'C:\\Users\\Duality\\Desktop\\井字棋\\O.png')
                                X_rect = X.get_rect()
                                X_rect.center = (x_coor, y_coor)
                                screen.blit(
                                    X, (X_rect.x, X_rect.y))
                                pygame.display.update()
                            elif self.x_o == 'o':
                                O = pygame.image.load(
                                    'C:\\Users\\Duality\\Desktop\\井字棋\\X.png')
                                O_rect = O.get_rect()
                                O_rect.center = (
                                    x_coor, y_coor)
                                screen.blit(
                                    O, (O_rect.x, O_rect.y))
                                pygame.display.update()
                            if self.grid[box_idx][row_idx][item_idx] == 'new_o':
                                O = pygame.image.load(
                                    'C:\\Users\\Duality\\Desktop\\井字棋\\+.png')
                                O_rect = O.get_rect()
                                O_rect.center = (
                                    x_coor, y_coor)
                                screen.blit(
                                    O, (O_rect.x, O_rect.y))
                                pygame.display.update()
                        ######


play = Tic_Toe('x', 'medium', 'first')
play.chess()