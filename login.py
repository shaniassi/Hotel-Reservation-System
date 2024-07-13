from tkinter import *
from PIL import ImageTk
from tkinter import font

# for deleting text when field is clicked
def clear_default(event):
    # Function to clear the default text when the Entry widget is clicked
    if username.get() == 'Username':
        username.delete(0, END)

def clear_defaultpass(event):
    # Function to clear the default text when the Entry widget is clicked
    if password.get() == 'Password':
        password.delete(0, END)

#for showing and hiding password
def hide():
    openeye.config(file='hide.png')
    password.config(show = '*')
    eyebutton.config(command=show)

def show():
    openeye.config(file='show.png')
    password.config(show = '')
    eyebutton.config(command=hide)

def open_signup():
    root.destroy()
    import signup

# Window title
root = Tk()
root.title('Login Page')

# Colors
brown = "#E6D9B9"
darkbrown = "#6D4C41"
lightbrown = '#EAD7BB'
lightbrown1 = '#CAB083'

# Load the image using ImageTk.PhotoImage
login_bg = ImageTk.PhotoImage(file='login_bg.png')

bgLabel = Label(root, image=login_bg)
bgLabel.grid(row=0, column=0)

# The heading
heading = Label(root, text='USER LOGIN', font=('RocaOne-Bl', 23),
                bg=brown, fg=darkbrown)
heading.place(x=550, y=300)

# Username Field
username_text = 'Username'

username = Entry(root, width=40, font=('Microsoft Yahei UI Light', 14), fg=darkbrown)
username.place(x=420, y=360)
username.insert(0, username_text)
username.bind("<Button-1>", clear_default)

# Password Field
pass_text = 'Password'

password = Entry(root, width=40, font=('Microsoft Yahei UI Light', 14), fg=darkbrown)
password.place(x=420, y=400)
password.insert(0, pass_text)
password.bind("<Button-1>", clear_defaultpass)

#Show and hide pass
closedeye = PhotoImage(file='hide.png')
openeye = PhotoImage(file = 'show.png')

eyebutton=Button(root, image = openeye, bd=0,bg = 'white',activebackground='white'
                 ,cursor ='hand2', command = hide)
eyebutton.place(x=830,y=402)

# forget pass
forgetbutton=Button(root, text = 'Forgot Password?',bd=0,bg = lightbrown,activebackground=lightbrown
                 ,cursor ='hand2', font = ('Microsoft Yahei UI Light',11), 
                 fg= darkbrown)
forgetbutton.place(x=740,y=430)

# Login
login=Button(root, text = 'LOGIN',font=('Open Sans', 16,),
              fg=darkbrown, bg = lightbrown1,width = 10)
login.place(x=580,y=465)

# bottom buttons
adminbutton=Button(root, text = 'Admin',bd=0,bg = lightbrown,activebackground=lightbrown
                 ,cursor ='hand2', font = ('Microsoft Yahei UI Light',11), 
                 fg= darkbrown)
adminbutton.place(x=468,y=620)

signupbutton=Button(root, text = 'Sign Up',bd=0,bg = lightbrown,activebackground=lightbrown
                 ,cursor ='hand2', font = ('Microsoft Yahei UI Light',11), 
                 fg= darkbrown,command=open_signup)
signupbutton.place(x=620,y=620)

guestbutton=Button(root, text = 'Guest',bd=0,bg = lightbrown,activebackground=lightbrown
                 ,cursor ='hand2', font = ('Microsoft Yahei UI Light',11), 
                 fg= darkbrown)
guestbutton.place(x=765,y=620)


root.mainloop()


