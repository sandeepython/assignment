
from fastapi import FastAPI
from tkinter import *
import sqlite3


app = FastAPI()



root = Tk()
root.title("Assignment")


root.geometry('400x500')

# Information List
datas = []


class Longitude:
    pass


class Latitude:
    pass


class Distance:
    pass


def add():
    global datas
    datas.append([Latitude.get(), Longitude.get(), Distance.get(1.0, "end-1c")])
    update_book()


def view():
    Latitude.set(datas[int(select.curselection()[0])][0])
    Longitude.set(datas[int(select.curselection()[0])][1])
    Distance.delete(1.0, "end")
    Distance.insert(1.0, datas[int(select.curselection()[0])][2])


def delete():
    Latitude.set('')
    Longitude.set('')
    Distance.delete(1.0, "end")

def update_book():
    select.delete(0, END)
    for Li, Lo, D in datas:
        select.insert(END, Li,Lo,D)

Latitude = DoubleVar()
Longitude = DoubleVar()

frame = Frame()
frame.pack(pady=10)

frame1 = Frame()
frame1.pack()

frame2 = Frame()
frame2.pack(pady=10)

Label(frame, text='Latitude', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable=Latitude, width=50).pack()

Label(frame1, text='Longitude', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable=Longitude, width=50).pack()

Label(frame2, text='Distance', font='arial 12 bold').pack(side=LEFT)
Distance = Text(frame2, width=37, height=1)
Distance.pack()

Button(root, text="Create/update", font="arial 12 bold", command=add).place(x=100, y=210)
Button(root, text="view", font="arial 12 bold", command=view).place(x=100, y=310)
Button(root, text="Delete", font="arial 12 bold", command=delete).place(x=100, y=390)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200, y=260)

import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('adress.db')

cursor_obj = connection_obj.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS adress")


table = """ CREATE TABLE ADRESS (
          Latitude FLOAT(255) NOT NULL,
          Longitude FLOAT(25) NOT NULL,
          Distance INTIGER
        ); """

cursor_obj.execute(table)

print("Table is Ready")

connection_obj.close()
root.mainloop()


