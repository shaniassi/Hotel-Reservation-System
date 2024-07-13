from tkinter import *
from PIL import ImageTk,Image
from tkinter import font
from tkinter import messagebox
import mysql.connector
import subprocess

def main():
    # for deleting text when field is clicked
    def clear_default(event):
        # Function to clear the default text when the Entry widget is clicked
        if username.get() == 'Username':
            username.delete(0, END)

    def clear_defaultpass(event):
        # Function to clear the default text when the Entry widget is clicked
        if loginpass.get() == 'Password':
            loginpass.delete(0, END)

    #for showing and hiding password
    def hide():
        openeye.config(file='hide.png')
        loginpass.config(show = '*')
        eyebutton.config(command=show)

    def show():
        openeye.config(file='show.png')
        loginpass.config(show = '')
        eyebutton.config(command=hide)

    def open_signup():
        root.destroy()
        signup_page()

    
    def open_admin():
        root.destroy()
        admin_page()
    
    def open_guest():
        messagebox.showinfo('Loading...','Loggin in as guest...')
        root.destroy()
        subprocess.call(["python", "main_hotelrsv.py"])

    
    def open_main():
        root.destroy()
        subprocess.call(["python", "main_hotelrsv.py"])

    
    # Logging In
    def login_database():
        if username.get()=='' or loginpass.get()=='':
            messagebox.showerror('Error','All fields are required!')

        check_user = username.get()
        check_pass = loginpass.get()
        mysqldb = mysql.connector.connect(host='localhost', user='root', password='Gelai 100618', database='hotelrsrv')
        mycursor = mysqldb.cursor()

        sql = ("INSERT INTO temp_user_pass (username,pass) VALUES (%s,%s)")
        val = check_user,check_pass
        mycursor.execute(sql,val)
        mysqldb.commit()

        try:
            sql = "SELECT Username, Password FROM guest WHERE Username = %s AND Password = %s"
            val =(check_user,check_pass)
            mycursor.execute(sql,val)
            result = mycursor.fetchone()
            
            if result is not None:
                messagebox.showinfo("",'logging in...')
                sql = "SELECT guestID FROM guest WHERE Username = %s AND Password = %s"
                val =(check_user,check_pass)
                mycursor.execute(sql,val)
            
                open_main()
                
            else:
                messagebox.showinfo("",'No account found, please sign up or login as guest.')
              
        
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close
        
        return(check_user,check_pass)


    # Window settings
    root = Tk()
    root.title('Login Page')
    root.geometry("+100+50")
    root.resizable(False,False)

    logo = ImageTk.PhotoImage(file='logo.png')
    root.iconphoto(root,logo)

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

    loginpass = Entry(root, width=40, font=('Microsoft Yahei UI Light', 14), fg=darkbrown)
    loginpass.place(x=420, y=400)
    loginpass.insert(0, pass_text)
    loginpass.bind("<Button-1>", clear_defaultpass)

    #Show and hide pass
    closedeye = PhotoImage(file='hide.png')
    openeye = PhotoImage(file = 'show.png')

    eyebutton=Button(root, image = openeye, bd=0,bg = 'white',activebackground='white'
                    ,cursor ='hand2', command = hide)
    eyebutton.place(x=830,y=402)

    # Login
    login=Button(root, text = 'LOGIN',font=('Open Sans', 16,),
                fg=darkbrown, bg = lightbrown1,cursor ='hand2',width = 10,command=login_database)
    login.place(x=580,y=465)

    # bottom buttons
    adminbutton=Button(root, text = 'Admin',bd=0,bg = lightbrown,activebackground=lightbrown
                    ,cursor ='hand2', font = ('Microsoft Yahei UI Light',11), 
                    fg= darkbrown,command=open_admin)
    adminbutton.place(x=468,y=620)

    signupbutton=Button(root, text = 'Sign Up',bd=0,bg = lightbrown,activebackground=lightbrown
                    ,cursor ='hand2', font = ('Microsoft Yahei UI Light',11), 
                    fg= darkbrown,command=open_signup)
    signupbutton.place(x=620,y=620)

    guestbutton=Button(root, text = 'Guest',bd=0,bg = lightbrown,activebackground=lightbrown
                    ,cursor ='hand2', font = ('Microsoft Yahei UI Light',11), 
                    fg= darkbrown,command=open_guest)
    guestbutton.place(x=765,y=620)

    root.mainloop()


def signup_page():
    
    # Window title
    signup_window = Tk()
    signup_window.title('Signup Page')
    signup_window.geometry("+100+50")
    signup_window.resizable(False,False)

    logo = ImageTk.PhotoImage(file='logo.png')
    signup_window.iconphoto(signup_window,logo)


    # Colors
    brown = "#E6D9B9"
    darkbrown = "#6D4C41"
    lightbrown = '#EAD7BB'
    lightbrown1 = '#CAB083'

    #for showing and hiding password

    def hidecon():
        openeye.config(file='hide.png')
        passwordEntry.config(show = '*')
        passwordEntry.config(show='*')
        eyebuttonconpass.config(command=showcon)

    def showcon():
        openeye.config(file='show.png')
        passwordEntry.config(show = '')
        passwordEntry.config(show='')
        eyebuttonconpass.config(command=hidecon)

    def login():
        signup_window.destroy()

        main()

    def connect_database():
        if usernameEntry.get()=='' or passwordEntry.get()==''or ageEntry.get() == ''\
        or fnameEntry == '' or addressEntry.get() == '' or contactEntry.get() == '' \
        or ageEntry.get() == '':
            messagebox.showerror('Error','All fields are required!')
        if int(ageEntry.get())< 18:
             messagebox.showerror('Error','You must be over 18!')
        elif(int(ageEntry.get())>=18):
             

            put_fname = fnameEntry.get()
            put_user = usernameEntry.get()
            put_pass = passwordEntry.get()
            put_address = addressEntry.get()
            put_contact = contactEntry.get()
            put_age = ageEntry.get()

            mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Gelai 100618', database = 'hotelrsrv')
            mycursor = mysqldb.cursor()

            try:
                sql = "INSERT INTO guest(guestID,fname,age,username,password,address,contact) VALUES (NULL,%s,%s,%s,%s,%s,%s)"
                val = (put_fname,put_age,put_user, put_pass,put_address,put_contact)
                mycursor.execute(sql,val)
                mysqldb.commit()
                messagebox.showinfo("","Success! Please go back and login.")
            except Exception as e:
                print(e)
                mysqldb.rollback()
                mysqldb.close
        


    signup_bg = ImageTk.PhotoImage(file='signup_bg.png')

    bgLabel = Label(signup_window, image=signup_bg)
    bgLabel.grid(row=0, column=0)

    # The heading
    heading = Label(signup_window, text='CREATE AN ACCOUNT', font=('RocaOne-Bl', 23),
                    bg=brown, fg=darkbrown)
    heading.place(x=475, y=300)

    # Fields
    fname=Label(signup_window, text = 'Full Name', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
    fname.place(x=400, y=345)
    fnameEntry=Entry( width=23,font=('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown)
    fnameEntry.place(x=404, y=369 )

    age=Label(signup_window, text = 'Age', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
    age.place(x=400, y=400)
    ageEntry=Entry( width=23,font=('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown)
    ageEntry.place(x=404, y=424 )

    address=Label(signup_window, text = 'Address', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
    address.place(x=650, y=345)
    addressEntry=Entry( width=23,font=('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown)
    addressEntry.place(x=654, y=369)

    contact=Label(signup_window, text = 'Contact Num.(09xxxxxxxxx)', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
    contact.place(x=650, y=400)
    contactEntry=Entry( width=23,font=('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown)
    contactEntry.place(x=654, y=424)

    username=Label(signup_window, text = 'Username', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
    username.place(x=400, y=455)
    usernameEntry=Entry( width=48,font=('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown)
    usernameEntry.place(x=404, y=479)

    password=Label(signup_window, text = 'Password', font = ('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown,fg=darkbrown)
    password.place(x=400, y=510)
    passwordEntry=Entry( width=48,font=('Microsoft Yahei UI Light', 12,'bold'),bg = lightbrown)
    passwordEntry.place(x=404, y=534)


    #Show and hide pass
    closedeye = PhotoImage(file='hide.png')
    openeye = PhotoImage(file = 'show.png')

    eyebuttonconpass=Button(signup_window, image = openeye, bd=0,bg = lightbrown,activebackground=lightbrown
                    ,cursor ='hand2', command = hidecon)
    eyebuttonconpass.place(x=844, y=536)

    # Signup

    signup=Button(signup_window, text = 'SIGN UP',font=('Open Sans', 16,),
                fg=darkbrown, bg = lightbrown1,cursor ='hand2',width = 10,command = connect_database)
    signup.place(x=580,y=610)

    #GO BACK
    goback=Button(signup_window, text = 'Go Back',bd=0,bg = lightbrown,activebackground=lightbrown
                    ,cursor ='hand2', font = ('Microsoft Yahei UI Light',11), 
                    fg= darkbrown, underline =True,command=login)
    goback.place(x=800,y=625)

    signup_window.mainloop()


def admin_page():
    # for deleting text when field is clicked
    def clear_default(event):
        # Function to clear the default text when the Entry widget is clicked
        if username.get() == 'Username':
            username.delete(0, END)

    def clear_defaultpass(event):
        # Function to clear the default text when the Entry widget is clicked
        if loginpass.get() == 'Password':
            loginpass.delete(0, END)

    #for showing and hiding password
    def hide():
        openeye.config(file='hide.png')
        loginpass.config(show = '*')
        eyebutton.config(command=show)

    def show():
        openeye.config(file='show.png')
        loginpass.config(show = '')
        eyebutton.config(command=hide)
    
    
    def open_login():
        admin_window.destroy()
        main()

    # Window title
    admin_window = Tk()
    admin_window.title('Admin Login')
    admin_window.geometry("+100+50")
    admin_window.resizable(False,False)

    logo = ImageTk.PhotoImage(file='logo.png')
    admin_window.iconphoto(admin_window,logo)


    # Colors
    brown = "#E6D9B9"
    darkbrown = "#6D4C41"
    lightbrown = '#EAD7BB'
    lightbrown1 = '#CAB083'

    #for showing and hiding password

    def hidecon():
        openeye.config(file='hide.png')
        loginpass.config(show = '*')
        eyebutton.config(command=showcon)

    def showcon():
        openeye.config(file='show.png')
        loginpass.config(show = '')
        eyebutton.config(command=hidecon)


    def check_input():
        if username.get()=='' or loginpass.get()=='':
            messagebox.showerror('Error','All fields are required!')

        put_user = username.get()
        put_pass = loginpass.get()
        mysqldb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Gelai 100618', database = 'hotelrsrv')
        mycursor = mysqldb.cursor()

        try:
            sql = "SELECT Username, Password FROM admins WHERE Username = %s AND Password = %s"
            val =(put_user,put_pass)
            mycursor.execute(sql,val)
            result = mycursor.fetchone()
            
            if result is not None:
                messagebox.showinfo("",'Logging in as admin...')
                admin_window.destroy()
                subprocess.call(["python", "dashboard.py"])
            else:
                messagebox.showinfo("",'Account not found.')
                
    
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close

    admin_bg = ImageTk.PhotoImage(file='signup_bg.png')

    bgLabel = Label(admin_window, image=admin_bg)
    bgLabel.grid(row=0, column=0)

    # The heading
    heading = Label(admin_window, text='LOGIN AS ADMIN', font=('RocaOne-Bl', 23),
                    bg=brown, fg=darkbrown)
    heading.place(x=505, y=300)

    # Username Field
    username_text = 'Username'

    username = Entry(admin_window, width=40, font=('Microsoft Yahei UI Light', 14), fg=darkbrown)
    username.place(x=420, y=360)
    username.insert(0, username_text)
    username.bind("<Button-1>", clear_default)

    # Password Field
    pass_text = 'Password'

    loginpass = Entry(admin_window, width=40, font=('Microsoft Yahei UI Light', 14), fg=darkbrown)
    loginpass.place(x=420, y=400)
    loginpass.insert(0, pass_text)
    loginpass.bind("<Button-1>", clear_defaultpass)
    
    #Show and hide pass
    closedeye = PhotoImage(file='hide.png')
    openeye = PhotoImage(file = 'show.png')

    eyebutton=Button(admin_window, image = openeye, bd=0,bg = 'white',activebackground='white'
                    ,cursor ='hand2', command = hide)
    eyebutton.place(x=830,y=402)

    # Login
    login=Button(admin_window, text = 'LOGIN',font=('Open Sans', 16,),
                fg=darkbrown, bg = lightbrown1,cursor ='hand2',width = 10,command=check_input)
    login.place(x=580,y=465)
    #GO BACK
    goback=Button(admin_window, text = 'Go Back',bd=0,bg = lightbrown,activebackground=lightbrown
                    ,cursor ='hand2', font = ('Microsoft Yahei UI Light',11), 
                    fg= darkbrown, underline =True,command=open_login)
    goback.place(x=800,y=600)

    admin_window.mainloop()



if __name__ == "__main__":
    main()
