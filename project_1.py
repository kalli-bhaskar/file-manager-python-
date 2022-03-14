from tkinter import *
import shutil
import os
import easygui as gui
from tkinter import filedialog
from tkinter import messagebox as mb


def open_window():
    read = gui.fileopenbox()
    return read


def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File Not Found!")


def copy_file():
    source1 = open_window()
    destination1 = filedialog.askdirectory()
    shutil.copy(source1, destination1)
    mb.showinfo('confirmation', "File Copied")


def del_file():
    delete_file = open_window()
    if os.path.exists(delete_file):
        os.remove(delete_file)
    else:
        mb.showinfo('confirmation', "File not Found")


def move_file():
    mov_file = open_window()
    destination = filedialog.askdirectory()
    if mov_file == destination:
        mb.showinfo('confirmation', "source and destination are same")
    else:
        shutil.move(mov_file, destination)
        mb.showinfo('confirmation', "file moved successfully")


def rename():
    file_name = open_window()
    path1 = os.path.dirname(file_name)
    extension = os.path.splitext(file_name)[1]
    print("Enter a new name")
    new_name = input()
    path = os.path.join(path1, new_name+extension)
    print(path)
    os.rename(file_name, path)
    mb.showinfo('confirmation', "File Renamed")


def list_file():
    folder_list = filedialog.askdirectory()
    sort_list = sorted(os.listdir(folder_list))
    i = 0
    print("Files in ", folder_list, " folder are")
    while i < len(sort_list):
        print(sort_list[i]+'\n')
        i += 1


root = Tk()
canv = Canvas(root, width=500, height=500, bg='grey')
