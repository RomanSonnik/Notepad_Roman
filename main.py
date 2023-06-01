# import all components
import locale
import tkinter as notepad
import keyboard
import pyautogui
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

# get and set language
language = locale.getdefaultlocale()
if 'ru_RU' in language:
    from russian import *
    print("Language: Russian")
elif 'lv_LV' in language:
    from latvian import *
    print("Language: Latvian")
else:
    from english import *
    print("Language: English")

# main settings
window = notepad.Tk()
window.title('Notepad')
min_window_width = 1000
min_window_height = 600
#window.iconbitmap('icon.ico')

# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - min_window_width / 2)
center_y = int(screen_height / 2 - min_window_height / 2)

# set the position of the window to the center of the screen
window.geometry(f'{min_window_width}x{min_window_height}+{center_x}+{center_y}')
window.minsize(min_window_width, min_window_height)

# set text preferences
window.columnconfigure(5, weight=1)
window.rowconfigure(2, weight=1)
text = ScrolledText(window, width=1000, height=480)
text.grid(row=2, column=1, columnspan=5, sticky="W")


# about function
def about():
    notepad.messagebox.showinfo(title=about_button, message=about_text)


def help():
    notepad.messagebox.showinfo(title=help_button, message=help_text)


def notepad_exit():
    answer = messagebox.askokcancel(exit_title, exit_text)
    if answer:
        window.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title=open_file_title, filetypes=((file_types, '*.txt'), (all_files, '*.*')))
    if file_path:
        text.delete('1.0', END)
        text.insert('1.0', open(file_path, encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=((file_types, '*.txt'), (all_files, '*.*')))
    file_path = file_path + '.txt'
    f = open(file_path, 'w', encoding='utf-8')
    text_save = text.get('1.0', END)
    f.write(text_save)
    f.close()


# hotkeys
keyboard.add_hotkey('Ctrl + s', lambda: save_file())
keyboard.add_hotkey('Ctrl + o', lambda: open_file())
keyboard.add_hotkey('Ctrl + h', lambda: help())

main_menu = Menu(window)

# file menu
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label=open_text, command=lambda: open_file())
file_menu.add_command(label=save, command=lambda: save_file())
file_menu.add_separator()
file_menu.add_command(label=close, command=lambda: notepad_exit())
window.config(menu=file_menu)

# edit menu
edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label=cut, command=lambda: pyautogui.hotkey('ctrl', 'x'))
edit_menu.add_command(label=copy, command=lambda: pyautogui.hotkey('ctrl', 'c'))
edit_menu.add_command(label=paste, command=lambda: pyautogui.hotkey('ctrl', 'v'))
edit_menu.add_separator()
edit_menu.add_command(label=select_all, command=lambda: pyautogui.hotkey('ctrl', 'a'))

# help menu
help_menu = Menu(main_menu, tearoff=0)
help_menu.add_command(label=help_button, command=lambda: help())
help_menu.add_command(label=about_button, command=lambda: about())

main_menu.add_cascade(label=file, menu=file_menu)
main_menu.add_cascade(label=edit, menu=edit_menu)
main_menu.add_cascade(label=about_button, menu=help_menu)

window.config(menu=main_menu)


window.mainloop()
