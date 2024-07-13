from tkinter import *
from PIL import ImageTk
from tkinter import font


# Window title
signup_window = Tk()
signup_window.title('Signup Page')

# Colors
brown = "#E6D9B9"
darkbrown = "#6D4C41"
lightbrown = '#EAD7BB'
lightbrown1 = '#CAB083'

#for showing and hiding password
def hide():
    openeye.config(file='hide.png')
    passwordEntry.config(show = '*')
    eyebuttonpass.config(command=show)

def show():
    openeye.config(file='show.png')
    passwordEntry.config(show = '')
    eyebuttonpass.config(command=hide)

def hidecon():
    openeye.config(file='hide.png')
    passwordEntry.config(show = '*')
    eyebuttonconpass.config(command=showcon)

def showcon():
    openeye.config(file='show.png')
    passwordEntry.config(show = '')
    eyebuttonconpass.config(command=hide)

def login():
    signup_window.destroy()
    import login

signup_bg = ImageTk.PhotoImage(file='signup_bg.png')

bgLabel = Label(signup_window, image=signup_bg)
bgLabel.grid(row=0, column=0)

# The heading
heading = Label(signup_window, text='CREATE AN ACCOUNT', font=('RocaOne-Bl', 23),
                bg=brown, fg=darkbrown)
heading.place(x=475, y=300)

# Fields
username=Label(signup_window, text = 'Username', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
username.place(x=400, y=345)
usernameEntry=Entry( width=48,font=('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown)
usernameEntry.place(x=404, y=369 )

password=Label(signup_window, text = 'Password', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
password.place(x=400, y=400)
passwordEntry=Entry( width=48,font=('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown)
passwordEntry.place(x=404, y=424 )

confirmpassword=Label(signup_window, text = 'Confirm Password', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
confirmpassword.place(x=400, y=450)
confirmpasswordEntry=Entry( width=48,font=('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown)
confirmpasswordEntry.place(x=404, y=475 )


#Show and hide pass
closedeye = PhotoImage(file='hide.png')
openeye = PhotoImage(file = 'show.png')

eyebuttonpass=Button(signup_window, image = openeye, bd=0,bg = lightbrown,activebackground=lightbrown
                 ,cursor ='hand2', command = hide)
eyebuttonpass.place(x=844, y=425)

eyebuttonconpass=Button(signup_window, image = openeye, bd=0,bg = lightbrown,activebackground=lightbrown
                 ,cursor ='hand2', command = hidecon)
eyebuttonconpass.place(x=844, y=476)


# Signup
signup=Button(signup_window, text = 'SIGN UP',font=('Open Sans', 16,),
              fg=darkbrown, bg = lightbrown1,width = 10)
signup.place(x=580,y=530)


#GO BACK
# forget pass
goback=Button(signup_window, text = 'Go Back',bd=0,bg = lightbrown,activebackground=lightbrown
                 ,cursor ='hand2', font = ('Microsoft Yahei UI Light',11), 
                 fg= darkbrown, underline =True,command=login)
goback.place(x=800,y=600)

signup_window.mainloop()