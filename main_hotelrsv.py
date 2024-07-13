from tkinter import *
from PIL import Image, ImageTk
import subprocess



class HotelReservation:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("The Shorline Hotel")
        self.root.geometry("+100+50")
        
        # ========== LOGO ==========
        self.image = Image.open(r"C:\Users\glaiz\Desktop\Assessments (2nd sem)\IM\Hotelrsrv\Hotel Room Reservation - Copy\hotellogo.png")
        
        # Convert the image to an icon (.ico) format
        icon = ImageTk.PhotoImage(self.image)
        self.root.iconphoto(True, icon)

        # ========== CANVAS ==========
        canvas = Canvas(self.root)
        canvas = Canvas(self.root, scrollregion=(0, 0, 2000, 3084))
        canvas.pack(expand=True, fill='both')
        
        vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
        
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        canvas.configure(yscrollcommand=vsb.set)
        canvas.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        
        # ========== BUTTONS WITH FUNCTIONS ==========
        def my_space():
            self.root.destroy()
            subprocess.Popen(["python", "myspace.py"])
            
        def sign_up_clicked():
            root.destroy()
            subprocess.Popen(["python", "current_final.py"])
            
        def about_clicked():
            x1 = 0
            y1 = 2800
            x2 = 2000
            y2 = 3530
        
            canvas.xview_moveto(x1 / 1280)
            canvas.yview_moveto(y1 / 3084)
        
        def contact_clicked():
            x1 = 0
            y1 = 3500
            x2 = 2000
            y2 = 3690
            
            canvas.xview_moveto(x1 / 1280)
            canvas.yview_moveto(y1 / 3084)
        
        def booknow_clicked():
            root.destroy()
            subprocess.Popen(["python", "finalbook.py"])
        

        

        
        # ========== BUTTONS ==========
        cust_btn1 = Button(canvas, text="MY SPACE", font=("Julius Sans One", 22, "bold"), bg="#DBE9F6", fg="#6D4C41", relief=FLAT, cursor ='hand2',command=my_space)
        cust_btn2 = Button(canvas, text="ROOMS", font=("Julius Sans One", 22, "bold"), bg="#DCEAF5", fg="#6D4C41", relief=FLAT,command=booknow_clicked)
        cust_btn3 = Button(canvas, text="ABOUT", font=("Julius Sans One", 22, "bold"), bg="#E0ECF6", fg="#6D4C41", relief=FLAT,cursor ='hand2', command=about_clicked)
        cust_btn4 = Button(canvas, text="CONTACT", font=("Julius Sans One", 22, "bold"), bg="#E0ECF6", fg="#6D4C41", relief=FLAT,cursor ='hand2', command=contact_clicked)
        cust_btn5 = Button(canvas, text="SIGN UP", font=("Julius Sans One", 19, "bold"), bg="#F8F7F2", fg="#6D4C41", relief=FLAT, cursor ='hand2',command=sign_up_clicked)
        cust_btn6 = Button(canvas, text="BOOK NOW", font=("Julius Sans One", 15, "bold"), bg="#FFEBE6", fg="#6D4C41", relief=FLAT, cursor ='hand2',command = booknow_clicked)
        cust_btn7 = Button(canvas, text="SEE ALL ROOMS", font=("Julius Sans One", 18, "bold"), bg="#F8F7F2", fg="#447E8C", relief=FLAT,cursor ='hand2',command = booknow_clicked)
        
        canvas.create_window(420, 50, anchor="nw", window=cust_btn1)
        canvas.create_window(600, 50, anchor="nw", window=cust_btn2)
        canvas.create_window(745, 50, anchor="nw", window=cust_btn3)
        canvas.create_window(880, 50, anchor="nw", window=cust_btn4)
        canvas.create_window(1095, 54, anchor="nw", window=cust_btn5)
        canvas.create_window(1033, 1060, anchor="nw", window=cust_btn6)
        canvas.create_window(190, 1658, anchor="nw", window=cust_btn7)
        
        # ========== SCROLL BAR ==========
        scrollbar = Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)

        # Load the image
        image1 = Image.open(r"C:\Users\glaiz\Desktop\Assessments (2nd sem)\IM\Hotelrsrv\Hotel Room Reservation - Copy\Desktop - 3.png")  # Replace "path_to_image_file.jpg" with the actual path of your image file
        
        # Resize the image to fit the canvas
        image1 = image1.resize((1280, 3084), Image.Resampling.LANCZOS)

        # Create a Tkinter-compatible image object
        self.tk_image = ImageTk.PhotoImage(image1)

        # Display the image on the canvas
        canvas.create_image(0, 0, anchor=NW, image=self.tk_image)
         

if __name__ == "__main__":
    root = Tk()
    obj = HotelReservation(root)
    root.mainloop()
