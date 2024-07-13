from tkinter import *
from PIL import Image, ImageTk
import subprocess

class main_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720")
        self.root.title("SQL Codes")
        self.root.resizable(False, False)
        self.root.geometry("+100+50")
        
        # ========== CANVAS ==========
        canvas = Canvas(self.root)
        canvas = Canvas(self.root, scrollregion=(0, 0, 2000, 3740))
        canvas.pack(expand=True, fill='both')
        
        # ========== BG IMAGE ==========
        image1 = Image.open(r"C:\Users\glaiz\Desktop\Assessments (2nd sem)\IM\Final Proj\sql codes page.png")
        image1 = image1.resize((1280, 720), Image.ANTIALIAS)
        self.tk_image = ImageTk.PhotoImage(image1)
        canvas.create_image(0, 0, anchor=NW, image=self.tk_image)
        
        # ========== BUTTONS WITH FUNCTIONS ==========
        def easy_btn():
            root.destroy()
            subprocess.Popen(["python", "easy.py"])
        
        def average_btn():
            root.destroy()
            subprocess.Popen(["python", "average.py"])
        
        def difficult_btn():
            root.destroy()
            subprocess.Popen(["python", "difficult.py"])
            
        def back_button():
            root.destroy()
            subprocess.Popen(["python", "dashboard.py"])    
                 
        # ========== BUTTONS ==========
        easy_btn = Button(canvas, text="SHOW", font=("Julius Sans One", 13, "bold"), bg="#FFEBE6", fg="#447E8C", relief=FLAT, cursor="hand2", width=7, height=1, command=easy_btn)
        avg_btn = Button(canvas, text="SHOW", font=("Julius Sans One", 13, "bold"), bg="#FFEBE6", fg="#447E8C", relief=FLAT, cursor="hand2", width=7, height=1, command=average_btn)
        dif_btn = Button(canvas, text="SHOW", font=("Julius Sans One", 13, "bold"), bg="#FFEBE6", fg="#447E8C", relief=FLAT, cursor="hand2", width=7, height=1, command=difficult_btn)
        back_btn = Button(canvas, text="GO BACK", font=("Julius Sans One", 17, "bold"), bg="#DCEAF6", fg="#6D4C41", relief=FLAT, cursor="hand2", width=8, height=1, command=back_button)
        
        canvas.create_window(108, 473, anchor="nw", window=easy_btn)
        canvas.create_window(493, 473, anchor="nw", window=avg_btn)
        canvas.create_window(878, 473, anchor="nw", window=dif_btn)
        canvas.create_window(1140, 36, anchor="nw", window=back_btn)
        
        
if __name__ == "__main__":
    root = Tk()
    obj = main_window(root)
    root.mainloop()