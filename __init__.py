from constants import WELCOME_STRING, BOARD_HEIGHT, BOARD_WIDTH, ViewSymbols
from bcolors import BColors
from random import choice, randint

EMPTY = '='
SONAR = 's'
TREASURE = 't'


def get_random_chests(count, width, height):
    chests = []
    for i in range(count):
        chests.append([randint(0, height - 1), randint(0, width - 1)])

    return chests


def create_board(width, height, chests):
    board = []
    for i in range(height):
        board.append([EMPTY] * width)

    for chest in chests:
        x = chest[1]
        y = chest[0]
        board[y] = [TREASURE if v == x else EMPTY for v in range(width)]

    print(board)
    return board


def draw_board(board):
    wave_symbols = [ViewSymbols.WAVE_BOTTOM, ViewSymbols.WAVE_TOP]

    def draw_symbol(symbol):
        if symbol == EMPTY:
            return choice(wave_symbols)
        elif symbol == TREASURE:
            return ViewSymbols.TREASURE

        return ViewSymbols.SONAR

    height = len(board)
    width = len(board[0])

    prefix = '    '
    header = f'{BColors.BOLD}{prefix} ' + ''.join(
        [f'{int(v / 10)}' if v % 10 == 0 else ' ' for v in range(1, width)]) + f'{BColors.ENDC}'
    rows = prefix + ''.join(list(''.join(['0123456789'] * (width % 10)))[:width])
    top_border = prefix + ''.join(['‾'] * width)
    bottom_border = prefix + ''.join(['_'] * width)

    print(header)
    print(rows)
    print(f'{BColors.OKBLUE}{top_border}{BColors.ENDC}')

    for row in range(0, height):
        print(
            '{b}{first_index}{end}{blue} |{line}|{end} {b}{last_index}{end}'.format(
                first_index=f' {row}' if row < 10 else row,
                last_index=row,
                b=BColors.BOLD,
                end=BColors.ENDC,
                blue=BColors.OKBLUE,
                line=''.join([
                    draw_symbol(board[row][v]) for v in range(width)
                ])
            )
        )

    print(f'{BColors.OKBLUE}{bottom_border}{BColors.ENDC}')
    print(rows)
    print(header)


def draw_them_all(board):
    print(WELCOME_STRING)
    draw_board(board)


def main():
    chests = get_random_chests(3, BOARD_WIDTH, BOARD_HEIGHT)
    board = create_board(BOARD_WIDTH, BOARD_HEIGHT, chests)
    draw_them_all(board)


main()
