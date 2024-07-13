import tkinter as tk
import mysql.connector
from mysql.connector import Error
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import subprocess

def average():

    def disp_prob1():
        try:
            mysqldb = mysql.connector.connect( host="localhost", user="root", password="Gelai 100618", database="hotelrsrv")

            # Retrieve data from the table
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT CONCAT(fname, '- ', contact) AS 'Name - Contact' FROM guest WHERE guestID <10;")
            rows = mycursor.fetchall()

            # Create a Treeview widget
            tree = ttk.Treeview(content_frame)
            tree["columns"] = ("NameContact")
            tree.heading("NameContact", text="Name - Contact")

            tree.column("#0", width=0, stretch=tk.NO)

            # Insert retrieved data into the Treeview
            for row in rows:
                tree.insert("", tk.END, values=row)


            # Place the Treeview inside the content frame
            tree.place(x=860, y=250)
            
                
        except Error as e:
                messagebox.showerror("MySQL Error", str(e))
                
        finally:
                if mysqldb.is_connected():
                    mysqldb.close()
                    mysqldb.close()
        
    def disp_prob2():

        # Connect to the MySQL database
        try:
            mysqldb = mysql.connector.connect(host="localhost",user="root",password="Gelai 100618",database="hotelrsrv")

            # Retrieve data from the table
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT guestID, total_amount FROM payment Order by total_amount DESC;")
            rows = mycursor.fetchall()

            # Define the columns
            tree = ttk.Treeview(content_frame)
            tree["columns"] = ("Guest ID", "Total Amount")
            tree.column("#0", width=0, stretch=tk.YES)

            # Set the column headings
            tree.heading("Guest ID", text="Guest ID")
            tree.heading("Total Amount", text="Total Amount")


            # Insert the fetched rows into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Place the Treeview inside the content frame
            tree.place(x=765, y=610)
            
        except Error as e:
            messagebox.showerror("MySQL Error", str(e))
            
        finally:
            if mysqldb.is_connected():
                mycursor.close()
                mysqldb.close()

    def disp_prob3():

        # Connect to the MySQL database
        try:
            mysqldb = mysql.connector.connect(host="localhost",user="root",password="Gelai 100618",database="hotelrsrv")

            # Retrieve data from the table
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT reservation_id, datediff(CURDATE(), checkin_date)  AS 'Elapsed Days ' FROM reservation_tb ORDER BY 2 DESC;")
            rows = mycursor.fetchall()

            # Define the columns
            tree = ttk.Treeview(content_frame)
            tree["columns"] = ("Reservation ID", "Elapsed Days")
            tree.column("#0", width=0, stretch=tk.YES)

            # Set the column headings
            tree.heading("Reservation ID", text="Reservation ID")
            tree.heading("Elapsed Days", text="Elapsed Days")


            # Insert the fetched rows into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Place the Treeview inside the content frame
            tree.place(x=765, y=920)
            
        except Error as e:
            messagebox.showerror("MySQL Error", str(e))
            
        finally:
            if mysqldb.is_connected():
                mycursor.close()
                mysqldb.close()

    def disp_prob4():
        # Connect to the MySQL database
        try:
            mysqldb = mysql.connector.connect(host="localhost",user="root",password="Gelai 100618",database="hotelrsrv")

            # Retrieve data from the table
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT payment_type, SUM(total_amount) AS 'Total Payment' FROM payment GROUP BY payment_type;")
            rows = mycursor.fetchall()

            # Define the columns
            tree = ttk.Treeview(content_frame)
            tree["columns"] = ("Payment Type", "Total Payment")
            tree.column("#0", width=0, stretch=tk.YES)

            # Set the column headings
            tree.heading("Payment Type", text="Payment Type")
            tree.heading("Total Payment", text="Total Payment")


            # Insert the fetched rows into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Place the Treeview inside the content frame
            tree.place(x=765, y=1270)
            
        except Error as e:
            messagebox.showerror("MySQL Error", str(e))
            
        finally:
            if mysqldb.is_connected():
                mycursor.close()
                mysqldb.close()

    def disp_prob5():

        # Connect to the MySQL database
        try:
            mysqldb = mysql.connector.connect(host="localhost",user="root",password="Gelai 100618",database="hotelrsrv")

            # Retrieve data from the table
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT r_type AS 'Room Type', COUNT(*) AS 'Total Reservations' FROM room_tb GROUP BY r_type ORDER BY 'Total Reservations' ASC;")
            rows = mycursor.fetchall()

            # Define the columns
            tree = ttk.Treeview(content_frame)
            tree["columns"] = ("Room Type", "Total Reservations")
            tree.column("#0", width=0, stretch=tk.YES)

            # Set the column headings
            tree.heading("Room Type", text="Room Type")
            tree.heading("Total Reservations", text="Total Reservations")


            # Insert the fetched rows into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Place the Treeview inside the content frame
            tree.place(x=765, y=1580)
            
        except Error as e:
            messagebox.showerror("MySQL Error", str(e))
            
        finally:
            if mysqldb.is_connected():
                mycursor.close()
                mysqldb.close()

    def go_back():
        window.destroy()
        subprocess.Popen(["python", "sql_window.py"])  

    #Colors
    bluegreen = "#447E8C"
    darkbrown = "#6D4C41"
    orange = "#FDC2B4"
    blue = "#C8DCF4"

    # Create a window
    window = tk.Tk()
    window.title('Average Problems')
    window.geometry('1280x720')
    window.geometry("+100+50")
    window.resizable(False,False)
    
    #Canvas
    canvas =tk.Canvas(window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    # Create a Scrollbar widget
    scrollbar = tk.Scrollbar(window, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Configure the Canvas to use the Scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    # Create a Frame inside the Canvas for the content
    content_frame = tk.Frame(canvas) 
    
    # Load the background image
    background_image = Image.open("ave_bg.png")  # Replace "background_image.png" with your actual image file path
    background_photo = ImageTk.PhotoImage(background_image)
    
    # Create a Label widget to display the background image
    background_label = tk.Label(content_frame, image=background_photo)
    
    background_label.pack()
    
    # Add the content frame to the Canvas
    canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

    button1 = tk.Button(content_frame,text = 'Display', fg = bluegreen, bd = 0,bg = orange, activebackground = orange, cursor = 'hand2', font = ('Julius Sans One', 20, 'bold'),command = disp_prob1 )
    button1.place (x = 220, y = 440)
    
    button2 = tk.Button(content_frame,text = 'Display', fg = bluegreen, bd = 0,bg = orange, activebackground = orange, cursor = 'hand2', font = ('Julius Sans One', 20, 'bold'), command= disp_prob2 )
    button2.place (x = 220, y = 778)

    button3 = tk.Button(content_frame,text = 'Display', fg = bluegreen, bd = 0,bg = orange, activebackground = orange, cursor = 'hand2', font = ('Julius Sans One', 20, 'bold'), command=disp_prob3 )
    button3.place (x = 220, y = 1109)

    button4 = tk.Button(content_frame,text = 'Display', fg = bluegreen, bd = 0,bg = orange, activebackground = orange, cursor = 'hand2', font = ('Julius Sans One', 20, 'bold'), command=disp_prob4 )
    button4.place (x = 220, y = 1435)

    button5 = tk.Button(content_frame,text = 'Display', fg = bluegreen, bd = 0,bg = orange, activebackground = orange, cursor = 'hand2', font = ('Julius Sans One', 20, 'bold'), command=disp_prob5 )
    button5.place (x = 220, y = 1788)

    back = tk.Button(content_frame,text = 'Go Back', fg = darkbrown, bd = 0,bg = blue, activebackground = blue, cursor = 'hand2', font = ('Julius Sans One', 18, 'bold'), command=go_back )
    back.place (x = 1130, y = 40)
    
    window.mainloop()

average()

    
