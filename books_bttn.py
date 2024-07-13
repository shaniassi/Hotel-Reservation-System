import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import subprocess


def books():
    def go_back():
        view_window.destroy()
        subprocess.Popen(["python", "dashboard.py"]) 

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Gelai 100618", database="hotelrsrv")
    mycursor = mysqldb.cursor()

    mycursor.execute("SELECT * FROM room_tb")
    result = mycursor.fetchall()

    view_window = tk.Tk()
    view_window.title("Room Information")
    view_window.geometry("1280x720")
    view_window.geometry("+100+50")

    bg_image = Image.open("bookdata.png")
    bg_image = bg_image.resize((1280, 720), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(view_window, width=1280, height=720, highlightthickness=0)
    canvas.pack()

    canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

    table_frame = tk.Frame(canvas, bg="#CAB083")
    table_frame.place(relx=0.52, rely=0.5, anchor=tk.CENTER)
        
    title_label = Label(table_frame, text="ROOM TABLE", font=("Palatino", 20, "bold"), bg="#CAB083")
    title_label.pack(pady=0)

    table = ttk.Treeview(table_frame, column=("Room Number", "Room Type", "Room Reference", "Room Status", "Room Rate"),height=20)
    table.pack()

    table.column("#0", width=0, stretch=tk.NO)
    table.column("Room Number", width=150)
    table.column("Room Type", width=150)
    table.column("Room Reference", width=150)
    table.column("Room Status", width=150)
    table.column("Room Rate", width=150)

    table["columns"] = ("Room Number", "Room Type", "Room Reference", "Room Status", "Room Rate")
        
    table.heading("Room Number", text="Room Number")
    table.heading("Room Type", text="Room Type")
    table.heading("Room Reference", text="Room Reference")
    table.heading("Room Status", text="Room Status")
    table.heading("Room Rate", text="Room Rate")
    
        # Add the results to the table
    for row in result:
        table.insert('', 'end', values=row)

    go_back_button = Button(view_window, text="GO BACK", font=('Microsoft Yahei UI Light', 15, 'bold'),bg="#CAB083",highlightthickness=0,
        bd=0, command=go_back)
    go_back_button.place(x=600, y=615) 

    view_window.mainloop()
 
books()