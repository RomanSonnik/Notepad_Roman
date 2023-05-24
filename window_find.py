import tkinter as find
import locale

language = locale.getdefaultlocale()
if 'ru_RU' in language:
    from russian import *
elif 'lv_LV' in language:
    from latvian import *
else:
    from english import *

window_find = find.Tk()
window_find.title(find_text)
min_window_find_width = 300
min_window_find_height = 100
window_find.iconbitmap('./assets/icon.ico')
window_find['bg'] = '#ffffff'
window_find.resizable(False, False)

# get the screen dimension
screen_width = window_find.winfo_screenwidth()
screen_height = window_find.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - min_window_find_width / 2)
center_y = int(screen_height / 2 - min_window_find_height / 2)

# set the position of the window_find to the center of the screen
window_find.geometry(f'{min_window_find_width}x{min_window_find_height}+{center_x}+{center_y}')
window_find.minsize(min_window_find_width, min_window_find_height)

text = find.Text(height=25)
text.pack()
text.insert('1.0', '')
text["state"] = "disabled"

find.mainloop()
