from tkinter import *
root = Tk()
root.geometry("600x500")

def getvals():
    print("Accepted")

# Heading
Label(root, text="First Python Registration Form", font="ar 16 bold").grid(row=0, column=3)

# Field Name
name = Label(root, text="Name")
phoneno = Label(root, text="Phone no")
dateofbirth = Label(root, text="Date of Birth")
gender = Label(root, text="Gender")
age = Label(root, text="Age")
paymentmode = Label(root, text="Payment Mode")

# Packing Field
name.grid(row=1, column=2)
phoneno.grid(row=2, column=2)
dateofbirth.grid(row=3, column=2)
gender.grid(row=4, column=2)
age.grid(row=5, column=2)
paymentmode.grid(row=6, column=2)

#Variable for Storing data
namevalue = StringVar
phonenovalue = StringVar
dateofbirthvalue = StringVar
gendervalue = StringVar
agevalue = StringVar
paymentmode = StringVar
checkvalue = IntVar

# Creating entry field
nameentry = Entry(root, textvariable=namevalue)
phonenoentry = Entry(root, textvariable=phonenovalue)
dateofbirthentry = Entry(root, textvariable=dateofbirthvalue)
genderentry = Entry(root, textvariable=gendervalue)
ageentry = Entry(root, textvariable=agevalue)
paymentmodeentry = Entry(root, textvariable=paymentmode)

# Packing entry field
nameentry.grid(row=1, column=3)
phonenoentry.grid(row=2, column=3)
dateofbirthentry.grid(row=3, column=3)
genderentry.grid(row=4, column=3)
ageentry.grid(row=5, column=3)
paymentmodeentry.grid(row=6, column=3)

# Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=7, column= 3)

#submit button
Button(text="Submit", command=getvals).grid(row=8, column=3)

root.mainloop()