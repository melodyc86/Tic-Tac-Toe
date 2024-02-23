import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (255, 0, 0)
CROSS_COLOR = (0, 0, 255)
FPS = 30

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
clock = pygame.time.Clock()

# Game variables
board = [['', '', ''], ['', '', ''], ['', '', '']]
player_turn = 'X'
game_over = False

# Functions
def draw_grid():
    # Draw horizontal lines
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * HEIGHT/3), (WIDTH, i * HEIGHT/3), LINE_WIDTH)
    # Draw vertical lines
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (i * WIDTH/3, 0), (i * WIDTH/3, HEIGHT), LINE_WIDTH)

def draw_symbols():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * WIDTH/3, row * HEIGHT/3), ((col + 1) * WIDTH/3, (row + 1) * HEIGHT/3), LINE_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, ((col + 1) * WIDTH/3, row * HEIGHT/3), (col * WIDTH/3, (row + 1) * HEIGHT/3), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * WIDTH/3 + WIDTH/6), int(row * HEIGHT/3 + HEIGHT/6)), int(WIDTH/6 - LINE_WIDTH))

def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def is_board_full():
    for row in board:
        if '' in row:
            return False
    return True

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = int(mouseY // (HEIGHT / 3))
            clicked_col = int(mouseX // (WIDTH / 3))
            #left off here
            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = player_turn
                player_turn = 'O' if player_turn == 'X' else 'X'
                
                winner = check_winner()
                
                if winner:
                    #print(f'Player {winner} wins!')
                    game_over = True
                elif is_board_full():
                    #print('It\'s a draw!')
                    game_over = True
                    
    screen.fill(WHITE)
    draw_grid()
    draw_symbols()

    # Display winner or draw text
    if game_over:
        font = pygame.font.Font(None, 36)
        # find winner name
        winner= check_winner()
        #get winner/tie text
        if winner: 
            text = font.render(f'Player {winner} wins!', True, LINE_COLOR)
        elif is_board_full():
            text = font.render('It\'s a draw!', True, LINE_COLOR)
      
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, text_rect)
        

    pygame.display.flip()
    clock.tick(FPS)
