import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import random 
import mysql.connector
from tkcalendar import DateEntry 
import subprocess 


class BookingSystem:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1280x720")
        self.window.title("The Shorline Hotel")
        self.window.geometry("+100+50")
        self.window.resizable(False,False)

        bg_image = Image.open("bg.png")
        bg_image = bg_image.resize((1270, 2400), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.canvas = tk.Canvas(self.window, width=1280, height=720, highlightthickness=0)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.canvas)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.canvas.yview)

        self.content_frame = tk.Frame(self.canvas, bg="white")

        self.content_frame.update_idletasks()
        self.canvas.create_window((0, 0), window=self.content_frame, anchor=tk.NW)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)

        button = tk.Button(
        self.canvas,
        text="BOOK NOW!", font=('Casual', 20),
        bg="#E3EDF5",height=0, width=12,
        highlightthickness=0, command=self.open_booking_form
        )
        goback = tk.Button(
        self.canvas,
        text="<<<", font=('Casual', 10, 'bold'),
        bg="#E3EDF5",height=0, width=4,
        highlightthickness=0, command= self.main
        )
        self.canvas.create_window(1038, 30, anchor=tk.NW, window=button)
        self.canvas.create_window(5, 2, anchor=tk.NW, window=goback)
        
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  

        self.window.mainloop()

    def main(self):
        self.window.destroy()
        subprocess.call(["python", "main_hotelrsv.py"])

    def open_booking_form(self):
        self.booking_window = tk.Toplevel()
        self.booking_window.geometry("1280x720")
        self.booking_window.geometry("+100+50")
        self.booking_window.resizable(False,False)

        bg_image = Image.open("bookbg.png") # palitan nalang directory
        bg_image = bg_image.resize((1280, 720), Image.ANTIALIAS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        canvas = tk.Canvas(self.booking_window, width=1280, height=720, highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)

        global r2
        global r3
        global r4
        
        Label(self.booking_window, text = "Room Type", font= ('Microsoft Yahei UI Light', 15,'bold' ), bg= '#EAD7BB').place(x=400, y=250)
        Label(self.booking_window, text = "Room Reference", font= ('Microsoft Yahei UI Light', 15,'bold' ), bg= '#EAD7BB').place(x=400, y=300)

        self.r2 = ttk.Combobox(self.booking_window, values=["Standard", "Deluxe", "Suite"])
        self.r2.place(x=580, y=260)

        self.r3 = ttk.Combobox(self.booking_window, values=["Single", "Double", "Triple", "Quadruple"])
        self.r3.place(x=580, y=310)

        Button(self.booking_window, text="Reserve", font=('Microsoft Yahei UI Light', 15, 'bold'), bg='#EAD7BB',
               command=self.book, height=1, width=7).place(x=800, y=420)
        
        Button(self.booking_window, text="Go Back", font=('Microsoft Yahei UI Light', 15, 'bold'),
               bg='#EAD7BB', command=self.booking_window.destroy, height=1, width=16).place(x=540, y=575)

        self.booking_window.mainloop()
        
    def book(self):
        R_type = self.r2.get()
        R_references = self.r3.get()
        R_status = "Reserved"

        room_type_mapping = {
            "Standard": "ST",
            "Deluxe": "DL",
            "Suite": "SU"
        }

        room_reference_mapping = {
            "Single": "S",
            "Double": "D",
            "Triple": "T",
            "Quadruple": "Q"
        }

        room_type_code = room_type_mapping.get(R_type, "")
        room_reference_code = room_reference_mapping.get(R_references, "")

        if not room_type_code or not room_reference_code:
            messagebox.showerror("Error", "Invalid room type or room reference")
            return

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="Gelai 100618", database="hotelrsrv")
        mycursor = mysqldb.cursor()

        try:
            # Get the room rate based on room type and reference
            room_rate = self.get_room_rate(R_type.lower(), R_references.lower())
            self.room_rate = int(room_rate) ## para makuha ko room rate na di tinatawag function

            if room_rate is None: 
                messagebox.showerror("Error", "Invalid room type or room reference")
                self.booking_window.destroy()
                return

            # Get the latest room number with the same room type and reference
            mycursor.execute(
                "SELECT RoomNumber FROM room_tb WHERE R_type = %s AND R_references = %s ORDER BY RoomNumber DESC LIMIT 1",
                (R_type, R_references)
            )
            result = mycursor.fetchone()

            if result:
                latest_room_number = result[0]
                increment = int(latest_room_number[3:]) + 1  # Extract the numeric part and increment
            else:
                increment = 1

            room_number = f"{room_type_code}{room_reference_code}{increment}"
            self.roomnum = room_number

            # Insert data into the table
            sql = "INSERT INTO room_tb (RoomNumber, R_type, R_references, R_status, R_rates) VALUES (%s, %s, %s, %s, %s)"
            val = (room_number, R_type, R_references, R_status, room_rate)
            mycursor.execute(sql, val)
            mysqldb.commit()

            result = messagebox.showinfo("Information", f"Room Number: {room_number},\nRoom Rate: {room_rate}\nTo process, provide the necessary reservation details...")
            if result == "ok":
                self.show_rn_guestinfo_window()#pass sa na sa reservation info

        except mysql.connector.IntegrityError as e:
            if e.errno == 1062:
                messagebox.showerror("We try sorry to say...", "There are no available rooms for you at the moment. \nThey are all reserved..\nPlease try booking different Room type and reference")
                self.booking_window.destroy()
            else:
                messagebox.showerror("Error", "An error occurred while processing your request.")
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

        

    def get_room_rate(self, room_type, room_reference): #para makuha yung rates nya base sa room type and room ref
        room_rates = {
        "standard": {
            "single": 950,
            "double": 1300,
            "triple": 1650,
            "quadruple": 2200
         },
        "deluxe": {
            "single": 1950,
            "double": 2300,
            "triple": 2650,
            "quadruple": 3200
         },
        "suite": {
            "single": 2950,
            "double": 3300,
            "triple": 3650,
            "quadruple": 4200
         }
        }
        
        room_type = room_type.lower()
        room_reference = room_reference.lower()
        if room_type in room_rates and room_reference in room_rates[room_type]:
            return room_rates[room_type][room_reference]   
        
    def generate_reservation_id(self):
        reservation_id = str(random.randint(10000, 99999))

        # Check if the generated ID already exists in the table
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="Gelai 100618", database="hotelrsrv")
        mycursor = mysqldb.cursor()

        try:
            # Check if the reservation ID already exists in the table
            mycursor.execute("SELECT reservation_id FROM reservation_tb WHERE reservation_id = %s", (reservation_id,))
            result = mycursor.fetchone()
            if result:
            # If the generated ID already exists, recursively call the function to generate a new ID
                return self.generate_reservation_id()
            # Close the database connection
            mycursor.close()
            mysqldb.close()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
        # Return the unique reservation ID
        return reservation_id
    def show_rn_guestinfo_window(self):
        self.window.withdraw()
        self.booking_window.destroy()
        reservation_id = self.generate_reservation_id()
        roominfo_window = tk.Toplevel()
        roominfo_window.geometry("1280x720")
        roominfo_window.title("Reservation Information")
        roominfo_window.geometry("+100+50")
        roominfo_window.resizable(False,False)
    
        # Load the background image
        self.bg_image = Image.open("guestbg.png")  # Replace "background.png" with your actual image file path
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a Canvas widget
        self.canvas = tk.Canvas(roominfo_window, width=1280, height=720)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Add the background image to the Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo)
        # Create and pack the reservation ID label
        reservation_id_label = tk.Label(roominfo_window, text=f"Reservation ID: {reservation_id}", font=("Microsoft Yahei UI Light", 30,'bold'),
                                        bg= '#C5BEAC')
        reservation_id_label.place(x=460, y=60)

        Label(roominfo_window, text = "Guest Number", font= ('Microsoft Yahei UI Light', 15,'bold' ), bg= '#EAD7BB').place(x=400, y=250)
        guest_number_entry = tk.Entry(roominfo_window)
        guest_number_entry.place(x=600, y=260)

        Label(roominfo_window, text = "Number of Night(s)", font= ('Microsoft Yahei UI Light', 15,'bold' ), bg= '#EAD7BB').place(x=400, y=300)
        number_of_nights_entry = tk.Spinbox(roominfo_window, from_=1, to=30)
        number_of_nights_entry.place(x=600, y=310)

        Label(roominfo_window, text = "Check-in Date:", font= ('Microsoft Yahei UI Light', 15,'bold' ), bg= '#EAD7BB').place(x=400, y=350)
        checkin_date_entry = DateEntry(roominfo_window, date_pattern="yyyy-mm-dd")
        checkin_date_entry.place(x=600, y= 360)

        Label(roominfo_window, text = "Check-out Date:", font= ('Microsoft Yahei UI Light', 15,'bold' ), bg= '#EAD7BB').place(x=400, y=400)
        checkout_date_entry = DateEntry(roominfo_window, date_pattern="yyyy-mm-dd")
        checkout_date_entry.place(x=600, y=410)


        Button(roominfo_window, text="Proceed", font=('Microsoft Yahei UI Light', 15, 'bold'), bg='#EAD7BB',
               command=lambda: self.proceed_to_payment(reservation_id,guest_number_entry.get(), number_of_nights_entry.get(), 
                                                       checkin_date_entry.get(), checkout_date_entry.get()), height=1, width=7).place(x=800, y=420)
        
        roominfo_window.mainloop()

    def proceed_to_payment(self, reservation_id, guest_number, number_of_nights, checkin_date, checkout_date): #para lang mastore yung data sa rsrv info
        
        # Store the reservation details in the reservation table
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="Gelai 100618", database="hotelrsrv")
        mycursor = mysqldb.cursor()

        try:
        # Insert data into the reservation table
            sql = "INSERT INTO reservation_tb (reservation_id, guest_num, night_num, checkin_date, checkout_date) VALUES (%s, %s, %s, %s, %s)"
            val = (reservation_id, guest_number, number_of_nights, checkin_date, checkout_date)
            mycursor.execute(sql, val)
            mysqldb.commit()

        # Close the database connection
            mycursor.close()
            mysqldb.close()

        # Open the payment window
            self.open_payment_window(reservation_id,number_of_nights)

        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()

    def open_payment_window(self, reservation_id,number_of_nights): # dito nalang yung payment
        def rsrvbutton():
            ## Storing in db
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="Gelai 100618", database="hotelrsrv")
            mycursor = mysqldb.cursor()

            comp_name = nameEntry.get()
            comp_contact = contactEntry.get()
            print(comp_name,comp_contact, '= name and contact')
            MOP = paymenttype.get()

            try:
                sql = "SELECT guestID FROM guest WHERE fname = %s AND contact = %s"
                val =(comp_name,comp_contact)
                mycursor.execute(sql,val)
                result = mycursor.fetchone()
                print('guest ID found')
                
                if result is not None:
                    sql = "INSERT INTO payment (guestID, reservationID, roomnum, total_amount, payment_type) VALUES (%s, %s, %s, %s, %s)"
                    val =(result[0],reservation_id,self.roomnum,total_amount,paymenttype.get())
                    mycursor.execute(sql, val)
                    mysqldb.commit()
                    subprocess.Popen(["python", "myspace.py"])
                    messagebox.showinfo('Success','Reservation has been saved.')   
                else:
                    subprocess.Popen(["python", "myspace.py"])
                    messagebox.showerror('Error','You already have a reservation')
                
            except Exception as e:
                print('except ran')
                print(e)
                mysqldb.rollback()
                mysqldb.close

        total_amount = self.room_rate * int(number_of_nights)
        print (self.room_rate, "roomrate")
        print (number_of_nights,'nights')
        print(total_amount, "= total amnt")
        # Colors
        brown = "#E6D9B9"
        darkbrown = "#6D4C41"
        lightbrown = '#EAD7BB'
        lightbrown1 = '#CAB083'

        payment_window = tk.Toplevel()
        payment_window.geometry("1280x720")
        payment_window.geometry("+100+50")
        payment_window.title("Payment")
        payment_window.resizable(False,False)

        # Load the background image
        payment_image = Image.open('bookbg.png')
        paymentbg_image = payment_image.resize((1280, 720), Image.ANTIALIAS)
        paymentbg_photo = ImageTk.PhotoImage(paymentbg_image)

        # Create a Canvas widget
        canvas = tk.Canvas(payment_window, width=1280, height=720, highlightthickness=0)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add the background image to the Canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=paymentbg_photo)

        # entry fields
        name=Label(payment_window, text = 'Registered Name', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
        name.place(x=400, y=250)
        nameEntry=Entry( payment_window,font=('Microsoft Yahei UI Light', 12,'bold'),bg = 'white')
        nameEntry.place(x=580, y=250 )

        contact=Label(payment_window, text = 'Registered Contact', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
        contact.place(x=400, y=300)
        contactEntry=Entry( payment_window,font=('Microsoft Yahei UI Light', 12,'bold'),bg = 'white')
        contactEntry.place(x=580, y=300 )

        roomnum=Label(payment_window, text = 'Room Number', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
        roomnum.place(x=400, y=350)
        roomnumEntry=Entry( payment_window,font=('Microsoft Yahei UI Light', 12,'bold'),bg = 'white')
        roomnumEntry.place(x=580, y=350 )

        amnt=Label(payment_window, text = 'Total Amount', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
        amnt.place(x=400, y=400)
        amntDisp=Label( payment_window,text = ("Php " + str(total_amount)), font=('Microsoft Yahei UI Light', 12,'bold'),bg = 'white')
        amntDisp.place(x=580, y=400 )

        paymentlabel=Label(payment_window, text = 'Payment Type', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
        paymentlabel.place(x=400, y=450)
        paymenttype = ttk.Combobox(payment_window, values=["Cash", "Debit", "Credit", "eWallet"])
        paymenttype.place(x=580, y=450)    

        Button(payment_window, text="Reserve", font=('Microsoft Yahei UI Light', 12, 'bold'), bg='#EAD7BB',
               command=rsrvbutton, height=1, width=7).place(x=820, y=440)
        Button(payment_window, text="Go Back", font=('Microsoft Yahei UI Light', 15, 'bold'),
               bg='#EAD7BB', command=payment_window.destroy, height=1, width=16).place(x=540, y=575)
        


        payment_window.mainloop()

    def run(self):
        self.window.mainloop()

booking_system = BookingSystem()
booking_system.run()

