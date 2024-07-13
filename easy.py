import tkinter as tk
import mysql.connector
from mysql.connector import Error
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import subprocess

def easy():  
    def create_connection():
        global connection
        try:
            connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Gelai 100618",
            database="hotelrsrv"
            )
        except Error as e:
            messagebox.showerror("MySQL Error", str(e))
    
    def display1_table():
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute("SELECT RoomNumber, R_type, R_references FROM room_tb WHERE R_type = 'Standard' AND R_references = 'Single'")
                rows = cursor.fetchall()

                table_frame = tk.Frame(canvas)
                table_frame.pack()

                if rows:
                    column_names = [desc[0] for desc in cursor.description]
                
                    tree = ttk.Treeview(table_frame, columns=column_names, show="headings")
                    for column_name in column_names:
                        tree.heading(column_name, text=column_name)

                    for row in rows:
                        tree.insert("", "end", values=row)

                    tree.pack(fill="both", expand=True)

                    canvas.create_window(635, 290, anchor=tk.NW, window=table_frame,height= 200,)

        except Error as e:
            messagebox.showerror("MySQL Error", str(e))

    def display2_table():
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute("SELECT guestID, fname, address FROM guest WHERE address LIKE '%Manila%' AND fname LIKE 'J%'")
                rows = cursor.fetchall()

                table_frame = tk.Frame(canvas)
                table_frame.pack()

                if rows:
                    column_names = [desc[0] for desc in cursor.description]
                
                    tree = ttk.Treeview(table_frame, columns=column_names, show="headings")
                    for column_name in column_names:
                        tree.heading(column_name, text=column_name)

                    for row in rows:
                        tree.insert("", "end", values=row)

                    tree.pack(fill="both", expand=True)

                    canvas.create_window(635, 600, anchor=tk.NW, window=table_frame)

        except Error as e:
            messagebox.showerror("MySQL Error", str(e))


    def display3_table():
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute("SELECT reservation_id, guest_num FROM reservation_tb WHERE night_num > 7")
                rows = cursor.fetchall()

                table_frame = tk.Frame(canvas)
                table_frame.pack()

                if rows:
                    column_names = [desc[0] for desc in cursor.description]
                    
                    tree = ttk.Treeview(table_frame, columns=column_names, show="headings")
                    for column_name in column_names:
                        tree.heading(column_name, text=column_name)

                    for row in rows:
                        tree.insert("", "end", values=row)

                    tree.pack(fill="both", expand=True)

                    canvas.create_window(635, 934, anchor=tk.NW, window=table_frame)

        except Error as e:
            messagebox.showerror("MySQL Error", str(e))

    def display4_table():
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute("SELECT reservation_id, checkin_date, checkout_date FROM reservation_tb WHERE MONTH(checkin_date) = 6 AND checkout_date BETWEEN '2023-07-15' AND '2023-07-31'")
                rows = cursor.fetchall()

                table_frame = tk.Frame(canvas)
                table_frame.pack()

                if rows:
                    column_names = [desc[0] for desc in cursor.description]
                    
                    tree = ttk.Treeview(table_frame, columns=column_names, show="headings")
                    for column_name in column_names:
                        tree.heading(column_name, text=column_name)

                    for row in rows:
                        tree.insert("", "end", values=row)

                    tree.pack(fill="both", expand=True)

                    canvas.create_window(635, 1255, anchor=tk.NW, window=table_frame)

        except Error as e:
            messagebox.showerror("MySQL Error", str(e))

    def display5_table():
        try:
            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute("SELECT guestID, RoomNum, total_amount FROM payment WHERE total_amount > 5000")
                rows = cursor.fetchall()

                table_frame = tk.Frame(canvas)
                table_frame.pack()

                if rows:
                    column_names = [desc[0] for desc in cursor.description]
                    
                    tree = ttk.Treeview(table_frame, columns=column_names, show="headings")
                    for column_name in column_names:
                        tree.heading(column_name, text=column_name)

                    for row in rows:
                        tree.insert("", "end", values=row)

                    tree.pack(fill="both", expand=True)

                    canvas.create_window(635, 1595, anchor=tk.NW, window=table_frame)

        except Error as e:
            messagebox.showerror("MySQL Error", str(e))

    def back():
        easywindow.destroy()
        subprocess.Popen(["python", "sql_window.py"])


    global canvas
    easywindow = tk.Tk()
    easywindow.geometry("1280x720")
    easywindow.geometry("+100+50")

    canvas = tk.Canvas(easywindow, width=1280, height=720, highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(canvas)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=canvas.yview)

    bg_image = Image.open("easybg.png")
    bg_image = bg_image.resize((1280, 2000), Image.ANTIALIAS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

    display1_button = tk.Button(
        canvas,
        text="DISPLAY", font=('Microsoft Yahei UI Light', 15, 'bold'),
        bg="#FDC2B4",
        highlightthickness=0,
        bd=0,
        command=display1_table
    )
    display2_button = tk.Button(
        canvas,
        text="DISPLAY", font=('Microsoft Yahei UI Light', 15, 'bold'),
        bg="#FDC2B4",
        highlightthickness=0,
        bd=0,
        command=display2_table
    )
    display3_button = tk.Button(
        canvas,
        text="DISPLAY", font=('Microsoft Yahei UI Light', 15, 'bold'),
        bg="#FDC2B4",
        highlightthickness=0,
        bd=0,
        command=display3_table
    )
    display4_button = tk.Button(
        canvas,
        text="DISPLAY", font=('Microsoft Yahei UI Light', 15, 'bold'),
        bg="#FDC2B4",
        highlightthickness=0,
        bd=0,
        command=display4_table
    )
    display5_button = tk.Button(
        canvas,
        text="DISPLAY", font=('Microsoft Yahei UI Light', 15, 'bold'),
        bg="#FDC2B4",
        highlightthickness=0,
        bd=0,
        command=display5_table
    )
    goback_button = tk.Button(
        canvas,
        text="GO BACK", font=('Microsoft Yahei UI Light', 15, 'bold'),
        bg="#C8DCF4",
        highlightthickness=0,
        bd=0,
        command =back
    )
    # Place the button within the canvas
    canvas.create_window(238, 470, anchor=tk.NW, window=display1_button)
    canvas.create_window(238, 790, anchor=tk.NW, window=display2_button)
    canvas.create_window(238, 1125, anchor=tk.NW, window=display3_button)
    canvas.create_window(238, 1450, anchor=tk.NW, window=display4_button)
    canvas.create_window(238, 1785, anchor=tk.NW, window=display5_button)
    canvas.create_window(1135, 40, anchor=tk.NW, window=goback_button)

    canvas.config(scrollregion=canvas.bbox("all"))

    create_connection()
    easywindow.mainloop()

easy()
