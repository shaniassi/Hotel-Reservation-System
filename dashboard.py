from tkinter import *
from PIL import Image, ImageTk
import subprocess

class admin_dashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("Administrator")
        self.root.resizable(False, False)
        self.root.geometry("+100+50")
        
        # ========== CANVAS ==========
        canvas = Canvas(self.root)
        canvas = Canvas(self.root, scrollregion=(0, 0, 2000, 3740))
        canvas.pack(expand=True, fill='both')
        
        # Image
        image = Image.open(r"C:\Users\glaiz\Desktop\Assessments (2nd sem)\IM\Final Proj\dashboard_bg.png")
        image1 = image.resize((1280, 720), Image.ANTIALIAS)
        self.tk_iamge = ImageTk.PhotoImage(image1)
        canvas.create_image(0, 0, anchor=NW, image=self.tk_iamge)
        
        # ========== BUTTONS FUNCTIONS ==========
        def bookings_button():
            root.destroy()
            subprocess.Popen(["python", "total_bookings.py"])
            
        def room_button():
            root.destroy()
            subprocess.Popen(["python", "books_bttn.py"])
            
        def sql_button():
            root.destroy()
            subprocess.Popen(["python", "sql_window.py"])
        
        def logOut_button():
            root.destroy()
            subprocess.Popen(["python", "current_final.py"]) 
            # will go to main window
        
        # ========== BUTTONS ==========
        btn1 = Button(canvas, text="SHOW", font=("Julius Sans One", 12, "bold"), bg="#AEEBE7", fg="#447E8C", relief=FLAT, cursor="hand2", width=7, height=1, command=bookings_button)
        btn2 = Button(canvas, text="SHOW", font=("Julius Sans One", 12, "bold"), bg="#B9EDCC", fg="#447E8C", relief=FLAT, cursor="hand2", width=7, height=1, command=room_button)
        btn3 = Button(canvas, text="SHOW", font=("Julius Sans One", 12, "bold"), bg="#F2DCD6", fg="#447E8C", relief=FLAT, cursor="hand2", width=7, height=1, command=sql_button)
        btn4 = Button(canvas, text="LOG OUT", font=("Julius Sans One", 18, "bold"), bg="#DBE9F6", fg="#6D4C41", relief=FLAT, cursor="hand2", command=logOut_button)

        canvas.create_window(82, 442, anchor="nw", window=btn1)
        canvas.create_window(500, 442, anchor="nw", window=btn2)
        canvas.create_window(910, 442, anchor="nw", window=btn3)
        canvas.create_window(1140, 30, anchor="nw", window=btn4)
        

if __name__ == "__main__":
    root = Tk()
    obj = admin_dashboard(root)
    root.mainloop()
    

