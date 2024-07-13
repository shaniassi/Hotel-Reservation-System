import tkinter as tk
import mysql.connector
from mysql.connector import Error
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import subprocess

def difficult():
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
                    
            def prob1():
                try:
                    if connection.is_connected():
                        cursor = connection.cursor()

                        cursor.execute("SELECT room_tb.r_references, count(*) as TotalGuests FROM reservation_tb, room_tb, payment WHERE (reservation_tb.checkin_date BETWEEN '2023-01-01' AND curdate()) AND payment.reservationid = reservation_tb.reservation_id AND payment.roomnum = room_tb.roomnumber GROUP BY room_tb.r_references")
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

                        canvas.create_window(691, 254, anchor=tk.NW, window=table_frame, height= 315, width=560)

                except Error as e:
                    messagebox.showerror("MySQL Error", str(e))
                    
            def prob2():
                try:
                    if connection.is_connected():
                        cursor = connection.cursor()

                        cursor.execute("SELECT room_tb.r_references AS RoomReference, room_tb.r_type AS RoomType, count(*) as Reservation_Count FROM room_tb, reservation_tb, payment WHERE payment.payment_type NOT IN ('eWallet') AND payment.reservationid = reservation_tb.reservation_id AND payment.roomnum = room_tb.roomnumber GROUP BY room_tb.r_references, room_tb.r_type ORDER BY Reservation_Count DESC;")
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

                        canvas.create_window(691, 625, anchor=tk.NW, window=table_frame, height= 315, width=560)

                except Error as e:
                    messagebox.showerror("MySQL Error", str(e))
                    
            def prob3():
                try:
                    if connection.is_connected():
                        cursor = connection.cursor()

                        cursor.execute("SELECT guest.guestid, room_tb.r_references, room_tb.r_type, datediff(reservation_tb.checkout_date, reservation_tb.checkin_date) AS Total_Stay FROM guest, room_tb, payment, reservation_tb WHERE payment.total_amount >= 15000 AND payment.roomnum = room_tb.roomnumber AND payment.guestid = guest.guestid AND payment.reservationid = reservation_tb.reservation_id GROUP BY guest.guestid, room_tb.r_references, room_tb.r_type, night_num HAVING night_num >= 20;")
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

                        canvas.create_window(500, 1007, anchor=tk.NW, window=table_frame, height= 315, width=750)

                except Error as e:
                    messagebox.showerror("MySQL Error", str(e))
                    
            def prob4():
                try:
                    if connection.is_connected():
                        cursor = connection.cursor()

                        cursor.execute(" SELECT room_tb.r_references AS RoomReference, room_tb.r_type AS RoomType, sum(payment.total_amount) as Revenue FROM room_tb, payment WHERE payment.roomnum = room_tb.roomnumber  GROUP BY room_tb.r_references, room_tb.r_type HAVING sum(payment.total_amount) >= 10000 ORDER BY 3;")
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

                        canvas.create_window(690, 1385, anchor=tk.NW, window=table_frame, height= 315, width=560)

                except Error as e:
                    messagebox.showerror("MySQL Error", str(e))
                    
            def prob5():
                try:
                    if connection.is_connected():
                        cursor = connection.cursor()

                        cursor.execute("SELECT room_tb.r_references, room_tb.r_type, ROUND(AVG(guest.age), 2) AS average_age, ROUND(AVG(reservation_tb.night_num), 2) AS TotalStay, ROUND(avg(payment.total_amount), 2) as TotalAmount FROM room_tb, guest, reservation_tb, payment WHERE payment.roomnum = room_tb.roomnumber AND payment.guestid = guest.guestid AND payment.reservationid = reservation_tb.reservation_id GROUP BY room_tb.r_references, room_tb.r_type;")
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

                        canvas.create_window(313, 1853, anchor=tk.NW, window=table_frame, height= 315, width=950)

                except Error as e:
                    messagebox.showerror("MySQL Error", str(e))
        
        
            global canvas 
            new_window = tk.Tk()
            new_window.geometry("1280x720")
            new_window.resizable(False, False)
            new_window.title("SQL Difficult Problems")
            new_window.geometry("+100+50")
            
            canvas = tk.Canvas(new_window, width=1280, height=720, highlightthickness=0)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            scrollbar = tk.Scrollbar(canvas)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            canvas.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=canvas.yview)
            
            bg_image = Image.open(r"C:\Users\glaiz\Desktop\Assessments (2nd sem)\IM\Final Proj\sql codes difficult page5.png")
            bg_image = bg_image.resize((1280, 2225), Image.ANTIALIAS)
            bg_photo = ImageTk.PhotoImage(bg_image)
            canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)
            
            def back_button():
                new_window.destroy()
                subprocess.Popen(["python", "sql_window.py"])
        
            # ========== BUTTONS ==========
            btn1 = tk.Button(canvas, text="DISPLAY", font=("Julius Sans One", 17, "bold"), bg="#FDC2B4", fg="#447E8C", relief=tk.FLAT, cursor="hand2", width=7, height=1, command=prob1)
            btn2 = tk.Button(canvas, text="DISPLAY", font=("Julius Sans One", 17, "bold"), bg="#FDC2B4", fg="#447E8C", relief=tk.FLAT, cursor="hand2", width=7, height=1, command=prob2)
            btn3 = tk.Button(canvas, text="DISPLAY", font=("Julius Sans One", 17, "bold"), bg="#FDC2B4", fg="#447E8C", relief=tk.FLAT, cursor="hand2", width=7, height=1, command=prob3)
            btn4 = tk.Button(canvas, text="DISPLAY", font=("Julius Sans One", 17, "bold"), bg="#FDC2B4", fg="#447E8C", relief=tk.FLAT, cursor="hand2", width=7, height=1, command=prob4)
            btn5 = tk.Button(canvas, text="DISPLAY", font=("Julius Sans One", 17, "bold"), bg="#FDC2B4", fg="#447E8C", relief=tk.FLAT, cursor="hand2", width=7, height=1, command=prob5)
            back_btn = tk.Button(canvas, text="GO BACK", font=("Julius Sans One", 17, "bold"), bg="#C6DBF4", fg="#6D4C41", relief=tk.FLAT, cursor="hand2", width=8, height=1, command=back_button)
            
            canvas.create_window(317, 522, anchor="nw", window=btn1)
            canvas.create_window(317, 893, anchor="nw", window=btn2)
            canvas.create_window(317, 1273, anchor="nw", window=btn3)
            canvas.create_window(317, 1653, anchor="nw", window=btn4)
            canvas.create_window(135, 2130, anchor="nw", window=btn5)
            canvas.create_window(1135, 36, anchor="nw", window=back_btn)
            
            canvas.config(scrollregion=canvas.bbox("all"))

            create_connection()
            new_window.mainloop()
            
difficult()