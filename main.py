from tkinter import *
from datetime import datetime
from tkinter import messagebox

temp = 1800
after_id = ""


def report():
    global temp, after_id
    after_id = root.after(1000, report)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.configure(text=str(f_temp))
    temp -= 1
    if temp == -1:
        end_pm()
        messagebox.showinfo(message="Всё!!! можешь расслабиться")
        relax()


tmp = 300
aft = ''


def relax():
    global tmp, aft
    aft = root.after(1000, relax)
    w_temp = datetime.fromtimestamp(tmp).strftime("%M:%S")
    label1.configure(text=str(w_temp))
    tmp -= 1
    if tmp == -1:
        root.after_cancel(aft)
        messagebox.showinfo(message="Работай!!!")
        res_pm()


def start_pm():
    btn1.grid_forget()
    btn2.grid(row=1, column=0, sticky="ew")
    btn3.grid(row=1, column=1, sticky="ew")
    report()


def end_pm():
    btn1.grid(row=1, column=0, sticky="ew")
    btn3.grid(row=1, column=1, sticky="ew")
    root.after_cancel(after_id)


def res_pm():
    global temp
    temp = 1800
    label1.configure(text="30:00")
    btn2.grid_forget()
    btn3.grid_forget()
    end_pm()
    btn1.grid(row=1, column=0)


root = Tk()

root.title("Обратный отсчет")

label1 = Label(root, width=5, font=("Ubuntu", 100), text="30:00")
label1.grid(row=0, columnspan=2)

btn1 = Button(text="START", font=("Ubuntu", 30), command=start_pm)
btn2 = Button(text="STOP", font=("Ubuntu", 30), command=end_pm)
btn3 = Button(text="RESET", font=("Ubuntu", 30), command=res_pm)

btn1.grid(row=1, columnspan=2, sticky="ew")

root.mainloop()
