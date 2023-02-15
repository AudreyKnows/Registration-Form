



from  tkinter import *
root = Tk()

def getvals():
  print("Submission Accepted")
  


root.mainloop()
root.geometry(“500x300”)

#heading
Label(root, text=“ Python Registration Form ”, font=“ar 15 bold”).grid(row=0, column=3)

# field name
name = Label(root, text=“Name”)

phone = Label(root, text=“Phone”)

email = Label(root, text=“E-mail”)

birthday = Label(root, text=“Birthday”)

gender = Label(root, text=“Gender”)

instagram = Label(root, text=“Instagram”)

linkedin = Label(root, text=“LinkedIn”)

# packing fields 
name.grid(row=1, column=2)

phone.grid(row=2, column=2)

email.grid(row=3, column=2)

birthday.grid(row=4, column=2)

gender.grid(row=5, column=2)

instagram.grid(row=6, column=2)

linkedin.grid(row=7, column=2)

# variable for storing data
namevalue = StringVar

phonevalue = StringVar

emailvalue = StringVar

birthdayvalue = StringVar

gendervalue = StringVar

instagramvalue = StringVar

linkedinvalue = StringVar

checkvalue =IntVar

# creating entry field 
nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
emailentry = Entry(root, textvariable =emailvalue)
birthdayentry = Entry(root, textvariable =birthdayvalue
genderentry = Entry(root, textvariable =gendervalue

# packing entry fields
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
Emailentry.grid(row=3, column=3)
birthdayentry.grid(row=4, column=3)
gender entry.grid(row=5, column=3)
Instagramentey.grid(row=6, column=3)
linkedinentry.grid(row=6, column=3)

# creating checkbox
checkbtn = checkbutton(text=“Remember me?”,  variable = checkvalue)
checkbtn.grid(row=6, column= 3)

# submit button
button(text=“Submit”, command=getvals).grid(row=7, column=3)






