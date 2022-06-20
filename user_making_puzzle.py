import pygame
from solver import *
import copy


class Grid:
    # Static attribute - Represents an Empty Board
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Constructor
    def __init__(self, width, height):
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(9)] for i in range(9)]
        self.width = width
        self.height = height
        self.puzzle = None
        self.selected = None

    # Updates the puzzle each time user inputs value in a cell
    def update_puzzle(self):
        self.puzzle = [[self.cubes[i][j].value for j in range(9)] for i in range(9)]

    # Assigns value to the cell in the grid and updates the puzzle
    def place_value(self, val):
        row, col = self.selected
        self.cubes[row][col].value = val
        self.update_puzzle()

        # Checks if the value entered is valid according to Rules of Sudoku
        # if the value is not valid we set it back to 0 in our puzzle and update it
        if valid(self.puzzle, val, (row, col)):
            return True
        else:
            self.cubes[row][col].value = 0
            self.cubes[row][col].temp = 0
            self.update_puzzle()
            return False

    # Assigns temporary value to the cell
    def assign_temp(self, val):
        row, col = self.selected
        self.cubes[row][col].temp = val

    # Draws the grid on the screen
    def draw(self, win):
        # Draw Grid Lines
        cell_width = self.width / 9
        for i in range(10):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0, 0, 0), (0, i * cell_width), (self.width, i * cell_width), thick)
            pygame.draw.line(win, (0, 0, 0), (i * cell_width, 0), (i * cell_width, self.height), thick)

        # Draw Cubes
        for i in range(9):
            for j in range(9):
                self.cubes[i][j].draw(win)

    # sets the 'selected' attribute of class Grid to the row and column of the selected box from the grid
    def select(self, row, col):
        # Reset all other
        for i in range(9):
            for j in range(9):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    # Clears the value from the selected box
    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].temp = 0

    # Takes the coordinates of mouse as parameter
    # Returns the corresponding row and column of the selected box in the grid
    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            cell_x = pos[0] // gap
            cell_y = pos[1] // gap
            return int(cell_y), int(cell_x)
        else:
            return None


# Class for each box of the grid
class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    # Displays the value of temp/permanent variable on screen
    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        cell_size = self.width / 9
        x = self.col * cell_size
        y = self.row * cell_size

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            # Placing the temporary value at the top left corner of the cell
            win.blit(text, (x + 5, y + 5))
        elif self.value != 0:
            text = fnt.render(str(self.value), 1, (255, 0, 0), (255, 255, 255))
            # Placing the permanent value in the middle of the cell
            win.blit(text, (x + (cell_size / 2 - text.get_width() / 2), y + (cell_size / 2 - text.get_height() / 2)))
        # If we select a cell then self.selected is initialised to the position of the cell
        # Draws a red coloured rectangle around the cell
        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, cell_size, cell_size), 3)


def redraw_window(win, board, strikes):
    # Background colour of the board
    win.fill((116, 232, 220))
    fnt = pygame.font.SysFont("comicsans", 40)
    # Draw Strikes
    text = fnt.render("X " * strikes, 1, (255, 0, 0))
    win.blit(text, (80, 570))
    # Solve button
    display = pygame.font.Font(None, 40).render('SOLVE', True, (0, 0, 100), (255, 255, 255))
    display_rect = display.get_rect()
    display_rect.center = (270, 580)
    win.blit(display, display_rect)
    # Draw the board
    board.draw(win)


# Draws the final solved puzzle on the screen
def draw_final(win, board, temp_board):
    basicfont = pygame.font.Font(None, 40)

    for i in range(9):
        for j in range(9):
            x = j * 60
            y = i * 60
            # Displays already filled values in red colour
            if temp_board[i][j] != 0:
                display = basicfont.render(str(board[i][j]), 1, (255, 0, 0), (255, 255, 255))
                display_rect = display.get_rect()
                display_rect.center = (x + 30, y + 30)
                win.blit(display, display_rect)
            # Displays newly filled values in black colour
            else:
                display = basicfont.render(str(board[i][j]), 1, (0, 0, 0), (255, 255, 255))
                display_rect = display.get_rect()
                display_rect.center = (x + 30, y + 30)
                win.blit(display, display_rect)
    # Displays the message "YOUR PUZZLE IS SOLVED" in place of solve button on screen
    display = pygame.font.Font(None, 45).render("YOUR PUZZLE IS SOLVED", 1, (0, 255, 0), (255, 255, 255))
    display_rect = display.get_rect()
    display_rect.center = 265, 580
    win.blit(display, display_rect)


def main(win):
    # Displays the image of back button on screen
    arrow = pygame.image.load('left_arrow.png')
    pygame.display.set_caption("Sudoku")
    # creates two instances of class Grid
    board = Grid(540, 540)
    temp_board = Grid(540, 540)
    key = None
    is_valid_sudoku = None
    run = True
    strikes = 0
    # No. of times solve button is pressed
    pressed_solve = 0
    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # If we click on back button we return to the main menu screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 0 < pos[0] < 100 and 560 < pos[1] < 700:
                    win.fill((255,255,255))
                    return
            # Until solve button is pressed
            if pressed_solve == 0:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        key = 1
                    if event.key == pygame.K_2:
                        key = 2
                    if event.key == pygame.K_3:
                        key = 3
                    if event.key == pygame.K_4:
                        key = 4
                    if event.key == pygame.K_5:
                        key = 5
                    if event.key == pygame.K_6:
                        key = 6
                    if event.key == pygame.K_7:
                        key = 7
                    if event.key == pygame.K_8:
                        key = 8
                    if event.key == pygame.K_9:
                        key = 9
                    # Clears the value (if it is temp) in the selected box when backspace key is pressed
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                        key = None
                    # Makes the temp value permanent when we press enter
                    if event.key == pygame.K_RETURN:
                        i, j = board.selected
                        if board.cubes[i][j].temp != 0:

                        # If we give an invalid number as input then a cross mark appears
                        # cross mark remains on screen until we give a valid value as input

                            if board.place_value(board.cubes[i][j].temp):
                                if strikes > 0:
                                    strikes -= 1
                            else:
                                if strikes == 0:
                                    strikes += 1
                                else:
                                    strikes = 1
                            key = None

                if event.type == pygame.MOUSEBUTTONDOWN:

                    pos = pygame.mouse.get_pos()
                    # When solve button is clicked
                    if 200 < pos[0] < 400 and 560 < pos[1] < 700 and board.puzzle != None:
                        # Creating a copy of the puzzle just before solving it
                        temp_board.puzzle = copy.deepcopy(board.puzzle)
                        is_valid_sudoku = solve(board.puzzle)
                        pressed_solve += 1

                    clicked = board.click(pos)
                    if clicked:
                        board.select(clicked[0], clicked[1])
                        key = None

        if board.selected and key != None:
            board.assign_temp(key)
        # Redraws the grid until solve button is pressed
        if pressed_solve == 0:
            redraw_window(win, board, strikes)

        elif pressed_solve > 0:
            # displays solved sudoku puzzle if the given puzzle is solvable else gives an error message
            if is_valid_sudoku:
                draw_final(win, board.puzzle, temp_board.puzzle)
                strikes = 0
            else:
                win.fill((255, 255, 255))
                display = pygame.font.Font(None, 60).render("INVALID SUDOKU PUZZLE", 1, (100, 100, 100))
                display_rect = display.get_rect()
                display_rect.center = 270, 280
                win.blit(display, display_rect)

        win.blit(arrow, (0, 560))
        pygame.display.update()


