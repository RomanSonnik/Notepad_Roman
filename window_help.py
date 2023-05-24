import tkinter as help
import locale

language = locale.getdefaultlocale()
if 'ru_RU' in language:
    from russian import *
elif 'lv_LV' in language:
    from latvian import *
else:
    from english import *

window_help = help.Tk()
window_help.title(help_button)
min_window_help_width = 500
min_window_help_height = 300
window_help.iconbitmap('icon.ico')
window_help['bg'] = '#ffffff'
window_help.resizable(False, False)

# get the screen dimension
screen_width = window_help.winfo_screenwidth()
screen_height = window_help.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - min_window_help_width / 2)
center_y = int(screen_height / 2 - min_window_help_height / 2)

# set the position of the window_help to the center of the screen
window_help.geometry(f'{min_window_help_width}x{min_window_help_height}+{center_x}+{center_y}')
window_help.minsize(min_window_help_width, min_window_help_height)

text = help.Text(height=25)
text.pack()
text.insert('1.0', help_text)
text["state"] = "disabled"

help.mainloop()
