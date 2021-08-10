import time
from typing import Any


class AnsiColors():
    '''
    Small AnsiColors color class to pick a color scheme for a built in unix type shell output
    The class uses the 256 color range using non-RGB style of color code

    Example: \33[38;5;31] = 'The color Red'
    '''

    def __init__(self, background_code, style_code, color_code) -> None:
        self.background_code = background_code
        self.style_code = style_code
        self.color_code = color_code

    def background_color(self) -> str:
        return f'\33[{self.background_code}m'

    def style_text(self) -> str:
        return f'\33[{self.style_code}m'

    def color_text(self) -> str:
        return f'\33[38;5;{self.color_code}m'
    
    def clear_color_scheme(self) -> str:
        return f'\33[0m'


class ProgressBar():
    '''
    Progress bar class that allows you to not just print a progress bar but choose
    the symbols printed and the colors used to print the bar
    '''

    def __init__(self, list_content: list[Any], complete_symbol: str = '#', uncomplete_symbol: str = '.', countdown_length: int = 100) -> None:
        self.complete_symbol = complete_symbol
        self.uncomplete_symbole = uncomplete_symbol
        self.list_content = list_content
        self.countdown_length = countdown_length


    def progress_bar(self) -> None:
        percent_complete: float = 0.0
        countdown_row: int = 100

        # progress bar color under 32%
        red: AnsiColors = AnsiColors(0,0,197)
        red_fg_color: str = red.color_text()
        reset_color_red: str = red.clear_color_scheme()

        # progress bar color above 33% and below 66%
        yellow: AnsiColors = AnsiColors(0,0,220)
        yellow_fg_color: str = yellow.color_text()
        reset_color_yellow: str = yellow.clear_color_scheme()

        # progress bar color above 66%
        green: AnsiColors = AnsiColors(0,0,48)
        green_fg_color: str = green.color_text()
        reset_color_green: str = green.clear_color_scheme()

        while countdown_row > 0:
            for _ in range(len(self.list_content) + 1):
                time.sleep(0.1)

                # basic algorithm for creating the base
                # percentage from the length of the list
                percentage_conversion: float = 100.0 / len(self.list_content)

                # building the progress bar visusal output
                prog_bar: str = "{percentage_complete:.2f}% [{hash_marks}{dot_marks}]".format(
                    percentage_complete=percent_complete,
                    hash_marks=self.complete_symbol * round(percent_complete),
                    dot_marks=self.uncomplete_symbole  * (self.countdown_length - round(percent_complete)))

                # write output to the same line and flush the buffer
                if percent_complete <= 32.00:
                    print(f'{red_fg_color}{prog_bar}{reset_color_red}', end='\r')
                elif percent_complete >= 33.00 and percent_complete <= 66.00:
                    print(f'{yellow_fg_color}{prog_bar}{reset_color_yellow}', end='\r')
                else:
                    print(f'{green_fg_color}{prog_bar}{reset_color_green}', end='\r')

                # increase the percent complete as each iteration occurs
                percent_complete += percentage_conversion

                # decrease the unfinsihed portion of the progress bar
                countdown_row -= percent_complete

        print('\ndone')
