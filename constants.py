from bcolors import BColors


class ViewSymbols:
    WAVE_BOTTOM = '~'
    WAVE_TOP = '`'
    TREASURE = '💎',
    SONAR = '🚩️'


BOARD_WIDTH = 59
BOARD_HEIGHT = 14

WELCOME_STRING = '''
    =================================
    🐋 Welcome to {b}{green}the {un}Sonar game!{end} 🚤
    =================================
'''.format(
    end=BColors.ENDC,
    b=BColors.BOLD,
    un=BColors.UNDERLINE,
    green=BColors.OKGREEN,
)
