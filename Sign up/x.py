from datetime import datetime
from tkinter import *
from tkinter import messagebox
def calculate_age(born):
    today = datetime.now( )
    bornDate =datetime.strptime(born, '%d/%m/%Y')
    return today.year - bornDate.year - ((today.month, today.day) < (bornDate.month, bornDate.day))
def get():
    title = titleVar.get()
    first_name = first_name_enter.get()
    second_name = second_name_enter.get()
    address = address_enter.get()
    post = post_enter.get()
    day = dayVar.get()
    month = monthVar.get()
    year = yearVar.get()
    dob = (str(day))+"/"+(str(month))+"/"+(str(year))
    age = str(calculate_age(dob))
    print("Title: "+title+
          "\nFirst Name: "+first_name+
          "\nSecond Name: "+second_name+
          "\nAddress: "+address+
          "\nPost Code: "+post+
          "\nDOB: "+dob+
          "\nAge: "+age)
    messagebox.showinfo("Information","Entry has been recorded")

def start():
    window = Tk()
    window.title("Sign Up")
    window.config(bg="#84fc80")
    frame = Frame(window)
    frame.config(bg="blue")
    frame.grid(padx=20,pady=20,column=0,row=0)

    headers=Label(frame,text = "Enter your details below")
    headers.config(bg="white",font=("Arial Bold",26))
    headers.grid(column=0,row=0,columnspan=5,padx=10,pady=10,sticky="ew")

    header = Label(frame,text="Enter title")
    header.config(bg="#b6bac1", font=("Arial Bold",))
    header.grid(column=0,row=1,columnspan=2,padx=10,pady=10,sticky="ew")

    titleVar = StringVar(frame)
    titleVar.set("Title")
    title = OptionMenu(frame, titleVar, "Mr","Mrs","Dr","Miss")
    title.config(bg="#b6bac1", font=("Arial Bold",12))
    title.grid(column=2,row=1,columnspan=1,padx=10,pady=10,sticky="ew")

    headers=Label(frame,text = "Enter your 1st Name")
    headers.config(bg="#b6bac1",font=("Arial Bold",14))
    headers.grid(column=0,row=2,columnspan=2,padx=10,pady=10,sticky="ew")

    first_name_enter = Entry(frame)
    first_name_enter.config(bg="white",font = ("Arial Bold",18),width=24, justify="left")
    first_name_enter.grid(column=2,row=2,columnspan=3,padx=10,pady=10)

    headers=Label(frame,text = "Enter your 2nd Name")
    headers.config(bg="#b6bac1",font=("Arial Bold",14))
    headers.grid(column=0,row=3,columnspan=2,padx=10,pady=10,sticky="ew")

    second_name_enter = Entry(frame)
    second_name_enter.config(bg="white",font = ("Arial Bold",18),width=24, justify="left")
    second_name_enter.grid(column=2,row=3,columnspan=3,padx=10,pady=10)

    headers=Label(frame,text = "Address line 1")
    headers.config(bg="#b6bac1",font=("Arial Bold",14))
    headers.grid(column=0,row=4,columnspan=2,padx=10,pady=10,sticky="ew")

    address_enter = Entry(frame)
    address_enter.config(bg="white",font = ("Arial Bold",18),width=24, justify="left")
    address_enter.grid(column=2,row=4,columnspan=3,padx=10,pady=10)

    headers=Label(frame,text = "Post Code")
    headers.config(bg="#b6bac1",font=("Arial Bold",14))
    headers.grid(column=0,row=5,columnspan=2,padx=10,pady=10,sticky="ew")

    post_enter = Entry(frame)
    post_enter.config(bg="white",font = ("Arial Bold",18),width=24, justify="left")
    post_enter.grid(column=2,row=5,columnspan=3,padx=10,pady=10)

    headers=Label(frame,text = "DOB")
    headers.config(bg="#b6bac1",font=("Arial Bold",14))
    headers.grid(column=0,row=6,columnspan=2,padx=10,pady=10,sticky="ew")

    dayVar = StringVar(frame)
    dayVar.set("Day")
    day = OptionMenu(frame, dayVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
    day.config(bg="#b6bac1", font=("Arial Bold",12))
    day.grid(column=2,row=6,columnspan=1,padx=10,pady=10,sticky="ew")

    monthVar = StringVar(frame)
    monthVar.set("Month")
    month = OptionMenu(frame, monthVar, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')
    month.config(bg="#b6bac1", font=("Arial Bold",12))
    month.grid(column=3,row=6,columnspan=1,padx=10,pady=10,sticky="ew")

    yearVar = StringVar(frame)
    yearVar.set("Year")
    year = OptionMenu(frame, yearVar, '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018')
    year.config(bg="#b6bac1", font=("Arial Bold",12))
    year.grid(column=4,row=6,columnspan=1,padx=10,pady=10,sticky="ew")

    button = Button(frame,command=get,text="Press to submit")
    button.config(bg="#4fa04d",font=("Arial Bold",18),)
    button.grid(column=0,row=7,columnspan=5,padx=20,pady=20)

    window.mainloop()
start()
