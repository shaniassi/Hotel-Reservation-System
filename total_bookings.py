import tkinter as tk
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
import mysql.connector
import subprocess

global canvas

new_window = tk.Tk()
new_window.geometry("1280x720")
new_window.geometry("+100+50")
new_window.resizable(False, False)
new_window.title("SQL Difficult Problems")

canvas = tk.Canvas(new_window, width=3500, height=720, highlightthickness=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

bg_image = Image.open(r"C:\Users\glaiz\Desktop\Assessments (2nd sem)\IM\Final Proj\bookings page4.png")
bg_image = bg_image.resize((1280, 720), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)
canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

def back_button():
    new_window.destroy()
    subprocess.Popen(["python", "dashboard.py"])

back_btn = tk.Button(canvas, text="GO BACK", font=("Julius Sans One", 17, "bold"), bg="#DCE9F6", fg="#6D4C41", relief=tk.FLAT, cursor="hand2", width=8, height=1, command=back_button)
canvas.create_window(1140, 30, anchor="nw", window=back_btn)

connect = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gelai 100618",
        database="hotelrsrv")

conn = connect.cursor()
conn.execute("SELECT guest.guestid, guest.fname, guest.address, guest.contact, reservation_tb.reservation_id , reservation_tb.guest_num , reservation_tb.night_num, reservation_tb.checkin_date, reservation_tb.checkout_date, room_tb.roomnumber, room_tb.r_references, room_tb.r_type, room_tb.r_status, payment.total_amount, payment.payment_type FROM guest, reservation_tb, room_tb, payment WHERE payment.guestid = guest.guestid AND payment.reservationid = reservation_tb.reservation_id AND payment.roomnum = room_tb.roomnumber")
    
tree=ttk.Treeview(canvas)  
tree['show']='headings'   

s = ttk.Style(canvas)
s.theme_use("clam")

s.configure('.', font=('Julius Sans One', 11))
s.configure("Treeview.Heading", foreground='#6D4C41', font=('Julius Sans One', 11, "bold"))

# define number of columns
tree["columns"] = ["guest_id", "fname", "address", "contactinfo", "reservation_id" , "total_num_guests" , "total_num_stay", "check_in_date", "check_out_date", "room_num", "room_ref", "room_type", "room_status", "total_amount", "payment_type"]

# assign width, minwich and anchor to the respective columns
tree.column("guest_id", width=80, minwidth=50, anchor=tk.CENTER)
tree.column("fname", width=200, minwidth=100, anchor=tk.CENTER)
tree.column("address", width=500, minwidth=80, anchor=tk.CENTER)
tree.column("contactinfo", width=150, minwidth=70, anchor=tk.CENTER)
tree.column("reservation_id", width=100, minwidth=50, anchor=tk.CENTER)
tree.column("total_num_guests", width=60, minwidth=50, anchor=tk.CENTER)
tree.column("total_num_stay", width=150, minwidth=50, anchor=tk.CENTER)
tree.column("check_in_date", width=115, minwidth=50, anchor=tk.CENTER)
tree.column("check_out_date", width=120, minwidth=50, anchor=tk.CENTER)
tree.column("room_num", width=115, minwidth=50, anchor=tk.CENTER)
tree.column("room_ref", width=130, minwidth=50, anchor=tk.CENTER)
tree.column("room_type", width=100, minwidth=50, anchor=tk.CENTER)
tree.column("room_status", width=100, minwidth=50, anchor=tk.CENTER)
tree.column("total_amount", width=110, minwidth=50, anchor=tk.CENTER)
tree.column("payment_type", width=120, minwidth=50, anchor=tk.CENTER)
   
      
#assgin the heading names to the respective columns
tree.heading("guest_id", text="Guest ID", anchor=tk.CENTER)
tree.heading("fname", text="Full Name", anchor=tk.CENTER)
tree.heading("address", text="Address", anchor=tk.CENTER)
tree.heading("contactinfo", text="Contact Information", anchor=tk.CENTER)
tree.heading("reservation_id", text="Reservation ID", anchor=tk.CENTER)
tree.heading("total_num_guests", text="Guests", anchor=tk.CENTER)
tree.heading("total_num_stay", text="Number of Stay", anchor=tk.CENTER)
tree.heading("check_in_date", text="Check-in Date", anchor=tk.CENTER)
tree.heading("check_out_date", text="Check-out Date", anchor=tk.CENTER)
tree.heading("room_num", text="Room Number", anchor=tk.CENTER)
tree.heading("room_ref", text="Room Reference", anchor=tk.CENTER)
tree.heading("room_type", text="Room Type", anchor=tk.CENTER)
tree.heading("room_status", text="Room Status", anchor=tk.CENTER)
tree.heading("total_amount", text="Total Amount", anchor=tk.CENTER)
tree.heading("payment_type", text="Payment Type", anchor=tk.CENTER)
    
i=0 
for row in conn:
    #print(row)
    tree.insert('', i, text='', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14]))
    i = i+1

hsb = ttk.Scrollbar(canvas, orient="horizontal", command=tree.xview)
tree.configure(xscrollcommand=hsb.set)
hsb.pack(fill=X, side=BOTTOM)

table_frame = tk.Frame(canvas)
table_frame.place(x=3, y=213, anchor=tk.NW)
tree.place(in_=table_frame, rely=1.0, bordermode="inside", width=1490)
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=220)
new_window.mainloop()
