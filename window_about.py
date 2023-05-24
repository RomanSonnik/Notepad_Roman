import tkinter as about
import locale

language = locale.getdefaultlocale()
if 'ru_RU' in language:
    from russian import *
elif 'lv_LV' in language:
    from latvian import *
else:
    from english import *

window_about = about.Tk()
window_about.title(about_button)
min_window_about_width = 500
min_window_about_height = 300
window_about.iconbitmap('./icon.ico')
window_about['bg'] = '#ffffff'
window_about.resizable(False, False)

# get the screen dimension
screen_width = window_about.winfo_screenwidth()
screen_height = window_about.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - min_window_about_width / 2)
center_y = int(screen_height / 2 - min_window_about_height / 2)

# set the position of the window_about to the center of the screen
window_about.geometry(f'{min_window_about_width}x{min_window_about_height}+{center_x}+{center_y}')
window_about.minsize(min_window_about_width, min_window_about_height)

text = about.Text(height=9)
text.pack()
text.insert('1.0', about_text)
text["state"] = "disabled"

about.mainloop()
