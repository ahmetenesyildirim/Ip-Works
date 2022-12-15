from tkinter import *

user_entry = Tk()
canvas= Canvas(user_entry, height=450, width=700)
canvas.pack()

frame_ust=Frame(user_entry, bg="#e2e2e2")
frame_ust.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

new_user_ticket= Label(frame_ust, bg="#e2e2e2", text="New User", font="Verdana 13")
new_user_ticket.pack(padx=10, pady=10, side=LEFT)

#Username
frame_username=Frame(user_entry)
frame_username.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.1)
#-------------------
username= Label(frame_username, text="Username:", font="Verdana 10")
username.pack(padx=10, pady=10, side=LEFT)
#-------------------
frame_username_input=Entry(user_entry, bg="#ffffff")
frame_username_input.place(relx=0.27, rely=0.2, relwidth=0.68, relheight=0.07)

#Display Name
frame_display=Frame(user_entry)
frame_display.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.1)
#-------------------
display_name= Label(frame_display, text="Display Name:", font="Verdana 10")
display_name.pack(padx=10, pady=10, side=LEFT)
#-------------------
frame_display_input=Entry(user_entry, bg="#ffffff")
frame_display_input.place(relx=0.27, rely=0.3, relwidth=0.68, relheight=0.07)

#Phone
frame_phone=Frame(user_entry)
frame_phone.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.1)
#-------------------
phone= Label(frame_phone, text="Phone:", font="Verdana 10")
phone.pack(padx=10, pady=10, side=LEFT)
#-------------------
frame_phone_input=Entry(user_entry, bg="#ffffff")
frame_phone_input.place(relx=0.27, rely=0.4, relwidth=0.68, relheight=0.07)

#email
frame_email=Frame(user_entry)
frame_email.place(relx=0.05, rely=0.5, relwidth=0.9, relheight=0.1)
#-------------------
email= Label(frame_email, text="Email:", font="Verdana 10")
email.pack(padx=10, pady=10, side=LEFT)
#-------------------
frame_email_input=Entry(user_entry, bg="#ffffff")
frame_email_input.place(relx=0.27, rely=0.5, relwidth=0.68, relheight=0.07)

#User Roles
frame_userrole=Frame(user_entry)
frame_userrole.place(relx=0.05, rely=0.6, relwidth=0.9, relheight=0.1)
#-------------------
userrole= Label(frame_userrole, text="User Roles:", font="Verdana 10")
userrole.pack(padx=10, pady=10, side=LEFT)
#-------------------
frame_userrole_input=Entry(user_entry, bg="#ffffff")
frame_userrole_input.place(relx=0.27, rely=0.6, relwidth=0.68, relheight=0.07)


#Save User
def clicked():
    print("tıklanıldı")

frame_saveuser=Frame(user_entry, bg="#6fc7e8")
frame_saveuser.place(relx=0.8, rely=0.072, relwidth=0.13, relheight=0.06)

button1 = Button(user_entry)
button1=Label(frame_saveuser, text="Save User",bg="#6fc7e8", fg="white", font="Verdana 10 bold")
button1.config(text="Save User", bg="#6fc7e8", fg="black", command=clicked)
button1.place(relx=0.9, rely=0.1, relwidth=0.68, relheight=0.07)
button1.pack()


user_entry.mainloop() 