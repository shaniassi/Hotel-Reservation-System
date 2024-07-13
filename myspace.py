from tkinter import ttk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import font
from tkinter import messagebox
import mysql.connector
import subprocess
import sys

global brown,darkbrown,lightbrown,lightbrown1
# Colors
brown = "#E6D9B9"
darkbrown = "#6D4C41"
lightbrown = '#EAD7BB'
lightbrown1 = '#CAB083'
lightblue = '#E1EDF6'
pink = '#FDC2B4'
bluegreen = '#447E8C'

def when_logged():
   
    def go_back():
        view_window.destroy()
        subprocess.Popen(["python", "main_hotelrsv.py"]) 
    def logout():
        sql_delete = ("DELETE FROM temp_user_pass WHERE username = %s AND pass = %s")
        val = (username, password)
        mycursor.execute(sql_delete, val)
        mysqldb.commit()
        subprocess.Popen(["python", "current_final.py"])
        view_window.destroy()
    def quit():
        root_windows = [w for w in sys.root_windows() if w.state() == "normal"]
        for root_window in root_windows:
            root_window.destroy()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="Gelai 100618", database="hotelrsrv")
    mycursor = mysqldb.cursor()

    sql = ("SELECT username,pass FROM temp_user_pass")
    mycursor.execute(sql)
    result = mycursor.fetchall()
    
    if not result:
        messagebox.showinfo('Error','Please login first.')
    if result:
        global username,password
        username = result[0][0]
        password = result[0][1]

        sql= ("SELECT fname,contact,reservation_tb.reservation_id, roomnum,guest_num,night_num,checkin_date,checkout_date, total_amount FROM guest,reservation_tb,payment WHERE guest.guestID = payment.guestID AND payment.reservationID = reservation_tb.reservation_id AND guest.username = %s  AND password = %s")
        val =(username,password)
        mycursor.execute(sql,val)
        result = mycursor.fetchall()

        view_window = Tk()
        view_window.title("User Information")
        view_window.geometry("1280x720")
        view_window.geometry("+100+50")

        bg_image = Image.open("bookdata.png")
        bg_image = bg_image.resize((1280, 720), Image.ANTIALIAS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Set the background image as the background of the main window
        background_label = Label(view_window, image=bg_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
            # The heading
        heading = Label(view_window, text='MY RESERVATION', font=('RocaOne-Bl', 23),
                        bg=lightblue, fg=bluegreen)
        heading.place(x=480, y=100)
            
        # Create a Treeview widget
        tree = ttk.Treeview(view_window)
        tree["columns"] = ("fname", "contact", "reservation_id","roomnum", "guest_num", "night_num", "checkin_date", "checkout_date", "total_amount")
        tree.column("#0", width=25, stretch=YES)
        tree["columns"] = ("fname", "contact", "reservation_id","roomnum", "guest_num", "night_num", "checkin_date", "checkout_date", "total_amount")
        tree.column("#0", width=25, stretch=NO)
        tree.column("fname", width=150, stretch=YES)
        tree.column("contact", width=150, stretch=YES)
        tree.column("reservation_id", width=100, stretch=YES)
        tree.column("roomnum", width=100, stretch=YES)
        tree.column("guest_num", width=100, stretch=YES)
        tree.column("night_num", width=100, stretch=YES)
        tree.column("checkin_date", width=150, stretch=YES)
        tree.column("checkout_date", width=150, stretch=YES)
        tree.column("total_amount", width=100, stretch=YES)
        tree.pack()
        tree.place(x=90, y=200)

        tree.heading("#0", text="")
        tree.heading("fname", text="Full Name")
        tree.heading("contact", text="Contact Number")
        tree.heading("reservation_id", text="Reservation ID")
        tree.heading("roomnum", text="Room Number")
        tree.heading("guest_num", text="Total Guest")
        tree.heading("night_num", text="Total Nights")
        tree.heading("checkin_date", text="Check-in Date")
        tree.heading("checkout_date", text="Check-out Date")
        tree.heading("total_amount", text="Total Amount")

        for row in result:
            tree.insert("", "end", values=row)

        ## Buttons
      #  cancel=Button(view_window, text = 'Quit',font=('Open Sans', 16,),
       #         fg=bluegreen, bg = pink,cursor ='hand2',width = 15,command=quit)
       # cancel.place(x=565,y=450)
        out=Button(view_window, text = 'Log Out',font=('Open Sans', 16,),
                fg=bluegreen, bg = pink,cursor ='hand2',width = 15, command=logout)
        out.place(x=765,y=450)
        back=Button(view_window, text = 'Go Back',font=('Open Sans', 16,),
                fg=bluegreen, bg = pink,cursor ='hand2',width = 15, command=go_back)
        back.place(x=965,y=450)



        view_window.mainloop()



    
       
when_logged()

    
 