from tkinter import *
from tkinter import messagebox
import sqlite3

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
        getFirstNameText = firstNameText.get()
        getLastNameText = lastNameText.get()
        getEmailText = emailText.get()
        getPasswordText = passwordText.get()
        getCnfPassText = cnfPassText.get()

        firstNameText.delete(0, len(getFirstNameText))
        lastNameText.delete(0, len(getLastNameText))
        emailText.delete(0, len(getEmailText))
        passwordText.delete(0, len(getPasswordText))
        cnfPassText.delete(0, len(getCnfPassText))
        firstNameText.focus()

    def store_data():
        getFirstNameText = firstNameText.get()
        getLastNameText = lastNameText.get()
        getEmailText = emailText.get()
        getPasswordText = passwordText.get()
        getCnfPassText = cnfPassText.get()

        if getPasswordText != getCnfPassText:
            messagebox.showerror(message='Password incorrect')
        else:
            q = "insert into signup_details values('{0}','{1}','{2}','{3}')".format(getFirstNameText, getLastNameText, getEmailText, getPasswordText)
            con = sqlite3.connect('sign-in-form.db')
            con.execute(q)
            con.commit()
            con.close()

            messagebox.showinfo(message='Data Saved Succesfully...')
            base2.destroy()

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
    passwordText = Entry(base2, width=15, bg=base2BG, font=textFont, border=1, relief='solid', show='*')
    cnfPassText = Entry(base2, width=15, bg=base2BG, font=textFont, border=1, relief='solid', show='*')


    signUpBtn2 = Button(base2, text='SIGN-UP', font=btnFont, border=5, relief='groove', bg=base2BG, command=store_data)
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

    signUpBtn2.grid(row=5, column=0, padx=(130, 0), pady=(50, 0))
    resetBtn2.grid(row=5, column=1, padx=(80, 0), pady=(50, 0))

    base2.mainloop()

def signIn_method():
    getUserText = userText.get()
    getPassText = passText.get()
    
    q = "select * from signup_details where userID=" + getUserText
    con = sqlite3.connect('sign-in-form.db')
    cur = con.cursor()
    cur.execute(q)
    data = cur.fetchone()
    cur.close()
    con.close()

    if data:
        if data[4] != getPassText:
            messagebox.showerror(message='INCORRECT PASSWORD')
        else: 
            messagebox.showinfo(message='LOGIN SUCCESFUL')
            base.destroy()
            base3 = Tk()
            base3.geometry('800x500')
            base3.title('User Info')
            base3.configure(bg='#a155b9')

            fullNameLbl = Label(base3, text='Name:- ' + data[1] + ' ' + data[2], font=lblFont, bg='#a155b9')
            infoEmailLbl = Label(base3, text='Email:- ' + data[3], font=lblFont, bg='#a155b9')

            fullNameLbl.grid(row=0, column=0, padx=(100, 0), pady=(80, 10))
            infoEmailLbl.grid(row=1, column=0, padx=(100, 0), pady=(80, 10))

            base3.mainloop()
    else:
        messagebox.showerror(message='NO USER FOUND')


userLbl = Label(base, text='Enter User ID', font=lblFont, bg=baseBG)
passLbl = Label(base, text='Enter Password', font=lblFont, bg=baseBG)
userText = Entry(base, width=15, bg=baseBG, font=textFont, border=1, relief='solid')
passText = Entry(base, width=15, bg=baseBG, font=textFont, show='*', border=1, relief='solid')

signInBtn = Button(base, text='SIGN-IN', font=btnFont, border=3, relief='groove', bg=baseBG, command=signIn_method)
resetBtn = Button(base, text='RESET', font=btnFont, border=3, relief='groove', bg=baseBG, command=reset_method)

newUserLbl = Label(base, text='New User?', font=('Arial', 20), bg=baseBG)
signUpBtn = Button(base, text='SIGN-UP', font=('Arial', 20), underline=2, relief='flat', command=signUp_method, bg=baseBG)
hereLbl = Label(base, text='Here', font=('Arial', 20), bg=baseBG)

userLbl.grid(row=0, column=0, padx=(80, 0), pady=(50, 10))
passLbl.grid(row=1, column=0, padx=(80, 0), pady=(50, 10))
userText.grid(row=0, column=1, padx=(80, 0), pady=(50, 10))
passText.grid(row=1, column=1, padx=(80, 0), pady=(50, 10))

signInBtn.grid(row=2, column=0, padx=(110, 0), pady=(70, 10))
resetBtn.grid(row=2, column=1, padx=(40, 0), pady=(70, 10))

newUserLbl.grid(row=3, column=0, padx=(150, 10), pady=(50, 10))
signUpBtn.place(x=300, y=388)
hereLbl.place(x=432, y=396)

base.mainloop()