from tkinter import *
root = Tk()
root.geometry("500x300")
root.title("Python Registration Form")

def getvals():
    print("Submission Accepted")
    print(f"Name: {namevalue.get()}")
    print(f"Phone: {phonevalue.get()}")
    print(f"Email: {emailvalue.get()}")
    print(f"Birthday: {birthdayvalue.get()}")
    print(f"Gender: {gendervalue.get()}")
    print(f"Instagram: {instagramvalue.get()}")
    print(f"LinkedIn: {linkedinvalue.get()}")
    if checkvalue.get() == 1:
        print("Remember me checked")
    else:
        print("Remember me not checked")

# heading
Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)

# field name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
email = Label(root, text="E-mail")
birthday = Label(root, text="Birthday")
gender = Label(root, text="Gender")
instagram = Label(root, text="Instagram")
linkedin = Label(root, text="LinkedIn")

# packing fields 
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
email.grid(row=3, column=2)
birthday.grid(row=4, column=2)
gender.grid(row=5, column=2)
instagram.grid(row=6, column=2)
linkedin.grid(row=7, column=2)

# variable for storing data
namevalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()
birthdayvalue = StringVar()
gendervalue = StringVar()
instagramvalue = StringVar()
linkedinvalue = StringVar()
checkvalue = IntVar()

# creating entry field 
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
emailentry = Entry(root, textvariable=emailvalue)
birthdayentry = Entry(root, textvariable=birthdayvalue)
genderentry = Entry(root, textvariable=gendervalue)
instagramentry = Entry(root, textvariable=instagramvalue)
linkedinentry = Entry(root, textvariable=linkedinvalue)

# packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
emailentry.grid(row=3, column=3)
birthdayentry.grid(row=4, column=3)
genderentry.grid(row=5, column=3)
instagramentry.grid(row=6, column=3)
linkedinentry.grid(row=7, column=3)

# creating checkbox
checkbtn = Checkbutton(root, text="Remember me?", variable=checkvalue)
checkbtn.grid(row=8, column=3)

# submit button
Button(root, text="Submit", command=getvals).grid(row=9, column=3)

root.mainloop()
