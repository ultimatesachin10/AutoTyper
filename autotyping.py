from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pynput.keyboard import Controller
import time

keyword = Controller()


def get_details():
    get_message = message.get()
    get_runt = rt.get()
    get_spt = st.get()
    if get_message == "" or get_runt == "" or get_spt == "":
        messagebox.showerror("Alert", "All Fields Are Required To Fill")
    else:
        a = int(float(get_runt))
        sec = a
        b = float(get_spt)
        sp = b
        messagebox.showinfo("Confirmation", "Your Auto Typing Is Set")
        time.sleep(sec)
        for i in message.get():
            keyword.type(i)
            time.sleep(sp)


def exiting():
    t.destroy()


t = Tk()
t.title('Auto Typer')
image = Image.open("autobg.jpg")
t.geometry("503x300")
timage = ImageTk.PhotoImage(image)
t.iconbitmap(r"autoicon.ico")


image_label = Label(t, image=timage).grid()

message_label = Label(t, text="Paste Your Text", bd=0, font=("poppins", 12))
message_label.place(x=12, y=135)

message = Entry(t, width="25", border=3, font=("poppins", 18))
message.place(x=135, height=35, y=130)


rt_label = Label(t, text="Set Start In Second", bd=0, font=("poppins", 12))
rt_label.place(x=12, y=185)

rt = Spinbox(t, from_=0, to=20, width="5", border=3, font=("poppins", 18))
rt.place(x=165, y=180)


st_label = Label(t, text="Set Speed ", bd=0, font=("poppins", 12))
st_label.place(x=290, y=185)

st = Spinbox(t, from_=0.1, to=1.0, increment=0.1, width="5", border=3, font=("poppins", 18))
st.place(x=390, y=180)


button = Button(t, text="Start Typing", font=("poppins", 10, "bold"), fg="#ffffff", bg="#2193b0", width=20,
                relief="raised", command=get_details)
button.place(x=70, y=250)


button1 = Button(t, text="EXIT", font=("poppins", 10, "bold"), fg="#ffffff", bg="#2193b0", width=20,
                 relief="raised", command=exiting)
button1.place(x=280, y=250)


info = Label(t, text="Created By Ultimate Sachin", bg="white", font=("poppins", 7))
info.place(x=5, y=280)

version = Label(t, text="Beta Version 1.0", bg="white", font=("poppins", 7))
version.place(x=425, y=5)

t.resizable(0, 0)
t.mainloop()
