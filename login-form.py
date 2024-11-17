from tkinter import *


base = Tk()
lblFont = ('Arial bold', 25)
textFont = ('Rockwell', 25)
btnFont = ('Arial Bold', 20)
baseBG = '#8e75e4'
base2BG = '#e2725b'

base.geometry('800x500')
base.title('Sign-In Form')
base.configure(bg=baseBG)

def reset_method():
    getUserText = userText.get()
    getPassText = passText.get()

    userText.delete(0, len(getUserText))
    passText.delete(0, len(getPassText))
    userText.focus()
        

def signUp_method():
    def reset_method2():
        firstNameText.delete(0, len(getFirstNameText))
        lastNameText.delete(0, len(getLastNameText))
        emailText.delete(0, len(getEmailText))
        passwordText.delete(0, len(getPasswordText))
        cnfPassText.delete(0, len(getCnfPassText))
        firstNameText.focus()

    base.destroy()
    base2 = Tk()
    base2.geometry('800x550')
    base2.title('New User Sign-up form')
    base2.configure(bg=base2BG)

    # Lables
    firstNameLbl = Label(base2, text='First Name', font=lblFont, bg=base2BG)
    lastNameLbl = Label(base2, text='Last Name', font=lblFont, bg=base2BG)
    emailLbl = Label(base2, text='Email', font=lblFont, bg=base2BG)
    passwordLbl = Label(base2, text='Password', font=lblFont, bg=base2BG)
    cnfPassLbl = Label(base2, text='Confirm Password', font=lblFont, bg=base2BG)

    # TextBoxes
    firstNameText = Entry(base2, width=15, bg=base2BG, font=textFont, border=1, relief='solid')
    lastNameText = Entry(base2, width=15, bg=base2BG, font=textFont, border=1, relief='solid')
    emailText = Entry(base2, width=15, bg=base2BG, font=textFont, border=1, relief='solid')
    passwordText = Entry(base2, width=15, bg=base2BG, font=textFont, border=1, relief='solid')
    cnfPassText = Entry(base2, width=15, bg=base2BG, font=textFont, border=1, relief='solid')

    # Getting Text
    getFirstNameText = firstNameText.get()
    getLastNameText = lastNameText.get()
    getEmailText = emailText.get()
    getPasswordText = passwordText.get()
    getCnfPassText = cnfPassText.get()

    signUpBtn = Button(base2, text='SIGN-UP', font=btnFont, border=5, relief='groove', bg=base2BG)
    resetBtn2 = Button(base2, text='RESET', font=btnFont, border=5, relief='groove', bg=base2BG, command=reset_method2)

    firstNameLbl.grid(row=0, column=0, padx=(50, 0), pady=(50, 10))
    lastNameLbl.grid(row=1, column=0, padx=(50, 0), pady=(20, 10))
    emailLbl.grid(row=2, column=0, padx=(50, 0), pady=(20, 10))
    passwordLbl.grid(row=3, column=0, padx=(50, 0), pady=(20, 10))
    cnfPassLbl.grid(row=4, column=0, padx=(50, 0), pady=(20, 10))

    firstNameText.grid(row=0, column=1, padx=(100, 0), pady=(50, 0))
    lastNameText.grid(row=1, column=1, padx=(100, 0), pady=(15, 0))
    emailText.grid(row=2, column=1, padx=(100, 0), pady=(15, 0))
    passwordText.grid(row=3, column=1, padx=(100, 0), pady=(15, 0))
    cnfPassText.grid(row=4, column=1, padx=(100, 0), pady=(15, 0))

    signUpBtn.grid(row=5, column=0, padx=(130, 0), pady=(50, 0))
    resetBtn2.grid(row=5, column=1, padx=(80, 0), pady=(50, 0))

    base2.mainloop()
    

userLbl = Label(base, text='Enter User ID', font=lblFont, bg=baseBG)
passLbl = Label(base, text='Enter Password', font=lblFont, bg=baseBG)
userText = Entry(base, width=15, bg=baseBG, font=textFont, border=1, relief='solid')
passText = Entry(base, width=15, bg=baseBG, font=textFont, show='*', border=1, relief='solid')

userLbl.place(x=70, y=70)
passLbl.place(x=70, y=140)
userText.place(x=370, y=70)
passText.place(x=370, y=140)

newUserLbl = Label(base, text='New User?', font=lblFont, bg=baseBG)
hereLbl = Label(base, text='Here', font=lblFont, bg=baseBG)

newUserLbl.place(x=80, y=350)
hereLbl.place(x=390, y=350)

signInBtn = Button(base, text='SIGN-IN', font=btnFont, border=3, relief='groove', bg=baseBG)
resetBtn = Button(base, text='RESET', font=btnFont, border=3, relief='groove', bg=baseBG, command=reset_method)

signInBtn.place(x=120, y=260)
resetBtn.place(x=450, y=260)


signUpBtn = Button(base, text='SIGN-UP', font=('Arial Bold', 22), underline=2, relief='flat', width=7, command=signUp_method, bg=baseBG)
signUpBtn.place(x=250, y=345)


base.mainloop()