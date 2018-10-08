# Matt Andrzejczuk 2018

class ink:
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TEAL = '\033[96m'
    BLACK = '\033[97m'
    GRAY = '\033[90m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

    @classmethod
    def print_blue(cls, log, _e):
        print(cls.lightblue, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_darkblue(cls, log, _e):
        print(cls.blue, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_red(cls, log, _e):
        print(cls.red, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_lightred(cls, log, _e):
        print(cls.lightred, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_orange(cls, log, _e):
        print(cls.orange, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_green(cls, log, _e):
        print(cls.lightgreen, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_pink(cls, log, _e):
        print(cls.pink, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_yellow(cls, log, _e):
        print(cls.yellow, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_cyan(cls, log, _e):
        print(cls.cyan, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_purple(cls, log, _e):
        print(cls.purple, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_lightcyan(cls, log, _e):
        print(cls.lightcyan, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
    @classmethod
    def print_gray(cls, log, _e):
        print(cls.GRAY, end="")
        print(log, end=_e)
        print(cls.ENDC, end="")
