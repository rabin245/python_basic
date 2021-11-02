# from tkinter import *

# # widgets = GUI elements: buttons, textboxes, labels, images
# # windows = serves as a container to hold or contain these widgets

# window = Tk() #instantiate an instance of a window
# window.geometry('420x420')
# window.title('Youtube Video GUI program')

# icon = PhotoImage(file = 'gui_logo2.png')
# window.iconphoto(True, icon)
# window.config(background='teal')

# window.mainloop() #place window on computer screen, listen for events


# Scale
# from tkinter import *


# def submit():
#     print('Temperature is', scale.get(), 'degrees C')


# window = Tk()

# hotImage = PhotoImage(file='python.png')
# hotLabel = Label(image = hotImage)
# hotLabel.pack()


# scale = Scale(window,
#               from_=100,
#               to=0,
#               length=250,
#               orient=VERTICAL,
#               font=('Consolas', 14),
#               tickinterval=10,  # adds numeric indicators for value
#               # showvalue=0, # hides the current value
#               troughcolor='#69eaff',
#               foreground='#ff1c00',
#               background='black',

#               )
# # scale.set(100)
# # sets the current value to middle of the scale
# scale.set((((scale['from']-scale['to'])/2))+scale['to'])

# scale.pack()
# coldImage = PhotoImage(file='python.png')
# coldLabel = Label(image = coldImage)
# coldLabel.pack()
# button = Button(window,
#                 text='submit',
#                 command=submit
#                 )
# button.pack()
# window.mainloop()

# listbox = a listing of selectable text items within its own container
# from tkinter import *


# def submit():
#     food = []
#     for index in listbox.curselection():
#         food.insert(index, listbox.get(index))
#     print('You ordered:')
#     for item in food:
#         print(item)

# def add():
#     listbox.insert(listbox.size(), entryBox.get())
#     listbox.config(height=listbox.size())


# def delete():
#     for index in reversed(listbox.curselection()):
#         listbox.delete(index)
#     listbox.config(height=listbox.size())


# window = Tk()

# listbox = Listbox(window,
#                   background='#f7ffde',
#                   font=('Constantia', 20),
#                   width=12,
#                   selectmode=MULTIPLE
#                   )
# listbox.pack()

# listbox.insert(1, 'pizza')
# listbox.insert(2, 'pasta')
# listbox.insert(3, 'garlic bread')
# listbox.insert(4, 'soup')
# listbox.insert(5, 'salad')

# listbox.config(height=listbox.size())

# entryBox = Entry(window,
#                  )
# entryBox.pack()


# submitButton = Button(window,
#                       text='submit',
#                       command=submit)
# submitButton.pack()

# addButton = Button(window,
#                    text='add',
#                    command=add)
# addButton.pack()

# deleteButton = Button(window,
#                       text='delete',
#                       command=delete)
# deleteButton.pack()

# window.mainloop()

# from tkinter import Button, Tk, messagebox

# def click():
#     # messagebox.showinfo(title='This is an info message box',
#                         # message = 'this is the message')

#     # messagebox.showwarning(
#     #     title='warning',
#     #     message='You have a Virus!!'
#     # )

#     # messagebox.showerror(
#     #     title='Error',
#     #     message='Something went wrong!'
#     # )

#     # if messagebox.askokcancel(
#     #     title='ask ok cancel',
#     #     message = 'Do you want to do this?'):
#     #     print('You did the thing')
#     # else:
#     #     print('You canceled the thing')

#     # if messagebox.askretrycancel(
#     #     title='ask retry cancel',
#     #     message = 'Do you want to retry the thing?'):
#     #     print('You retried the thing')
#     # else:
#     #     print('You canceled the thing')

#     # if messagebox.askyesno(
#     #     title='ask yes no',
#     #     message = 'Do you know de wae?'):
#     #     print('Da QUEEN')
#     # else:
#     #     print('Do you know de wae?')

#     # answer =messagebox.askquestion(title='ask question',
#     #                     message = 'Do you like stars?')
#     # if(answer == 'yes'):
#     #     print('stargazer')
#     # else:
#     #     print('dumb bitch')

#     answer = messagebox.askyesnocancel(title='yes no cancel',
#                             message='Are u gay?',
#                             icon = 'question')
#     if answer==True:
#         print('Why are you gay?')
#     elif answer == False:
#         print('Why are u not gay?')
#     else:
#         print('Why are u running?')

# window = Tk()

# button = Button(window,
#         command = click,
#         text = 'click me'
#         )
# button.pack()

# window.mainloop()


# from tkinter import *
# from tkinter import colorchooser # submodule


# def click():
#     # color = colorchooser.askcolor()
#     # colorHex = color[1]
#     # window.config(background=colorHex)

#     window.config(background=colorchooser.askcolor()[1])


# window = Tk()

# window.geometry('420x420')
# button = Button(text='click me', command=click)
# button.pack()

# window.mainloop()

# text widget = functions like a text area, you can enter multiple lines of text
# from tkinter import *

# def submit():
#     input = text.get('1.0', END)
#     print(input)


# window = Tk()

# text = Text(
#     window,
#     background='light yellow',
#     font=('Ink Free', 24),
#     height=8,
#     width=20,
#     padx=20,
#     pady=20,
#     foreground='purple'
# )
# text.pack()
# button = Button(window, text='submit', command=submit)
# button.pack()

# window.mainloop()

# from tkinter import *
# from tkinter import filedialog


# def openFile():
#     filepath = filedialog.askopenfilename(
#         initialdir='E:\\Python',
#         title='Open fie !!!????',
#         filetypes=(('text files', '*.txt'),
#                    ('all files', '*.*'))
#     )
#     file = open(filepath, 'r')
#     print(file.read())
#     file.close()


# window = Tk()
# button = Button(text='Open', command=openFile)
# button.pack()
# window.mainloop()


# from tkinter import *
# from tkinter import filedialog


# def saveFile():
#     file = filedialog.asksaveasfile(initialdir='E:\\Python',
#                                     defaultextension='.txt',
#                                     filetypes=[
#                                         ('Text file', '.txt'),
#                                         ('HTML file', '.html'),
#                                         ('All files', '.*')
#                                     ])
#     if file is None:
#         return
#     filetext = str(text.get('1.0', END))
#     filetext = input
#     file.write(filetext)
#     file.close()


# window = Tk()
# button = Button(text='Save', command=saveFile)
# button.pack()
# text = Text(window)
# text.pack()
# window.mainloop()


# from tkinter import *

# def openFile():
#     print('File has been opened')
# def saveFile():
#     print('File has been opened')
# def cut():
#     print('you cut some text')
# def copy():
#     print('you copied some text')
# def paste():
#     print('You paste some text')

# window = Tk()

# openImage = PhotoImage(file='python.png')
# saveImage = PhotoImage(file='python.png')
# exitImage = PhotoImage(file='python.png')


# menubar = Menu(window)
# window.config(menu = menubar)

# fileMenu = Menu(menubar, tearoff=0, font=('MV Boli', 12))
# menubar.add_cascade(label='File', menu=fileMenu)
# fileMenu.add_command(label='Open', command=openFile, image=openImage, compound='left')
# fileMenu.add_command(label='Save', command=saveFile, image=saveImage, compound='left')
# fileMenu.add_separator()
# fileMenu.add_command(label='Exit', command=quit, image=exitImage, compound='left')

# editMenu = Menu(menubar, tearoff=0, font=('MV Boli', 12))
# menubar.add_cascade(label='Edit', menu = editMenu)
# editMenu.add_command(label='Cut', command=cut)
# editMenu.add_command(label='Copy', command=copy)
# editMenu.add_command(label='Paste', command=paste)
# window.mainloop()

# # frame = a rectangular container to group and hold widgets

# from tkinter import *

# window = Tk()
# frame = Frame(window, background='purple', border=5, relief=SUNKEN)
# # frame.pack(side='bottom')
# frame.place(x=0, y=0)

# Button(frame, text = 'W', font=('Consolas', 18), width=3).pack(side = 'top')
# Button(frame, text = 'A', font=('Consolas', 18), width=3).pack(side = LEFT)
# Button(frame, text = 'S', font=('Consolas', 18), width=3).pack(side = 'left')
# Button(frame, text = 'D', font=('Consolas', 18), width=3).pack(side = 'left')

# window.mainloop()

# from tkinter import *

# def create_window():
#     # new_window = Toplevel() # Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
#     new_window = Tk()       # Tk() = new independent window
#     old_window.destroy()    # close out of old window

# old_window = Tk()

# Button(old_window, text='create new window', command = create_window).pack()

# old_window.mainloop()

# from tkinter import *
# from tkinter import ttk

# window = Tk()

# notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

# tab1 = Frame(notebook)          #new frame for tab 1
# tab2 = Frame(notebook)          #new frame for tab 2

# notebook.add(tab1, text = 'Tab 1')
# notebook.add(tab2, text = 'Tab 2')
# notebook.pack(expand=True, fill='both') #expand = expand to fill any space not otherwise used
#                                         #fill = fill space on x and y axis

# Label(tab1, text='Hello this is tab 1', width=50, height=25).place(x=-100, y=-100)
# Label(tab2, text='Hello this is tab 2 shit dawg', width=50, height=25).pack()

# window.mainloop()

# from tkinter import *

# # grid() = geometry manager that organizes widgets in a table-like structure in a parent

# window = Tk()

# titleLabel = Label(window, text="Enter your info", font=(
#     'Arial', 25)).grid(row=0, column=0, columnspan=2)

# firstNameLabel = Label(window, text='First name:', width=20,
#                        background='red').grid(row=1, column=0)
# firstNameEntry = Entry(window).grid(row=1, column=1)

# lastNameLabel = Label(window, text='Last name:',
#                       background='teal').grid(row=2, column=0)
# lastNameEntry = Entry(window).grid(row=2, column=1)

# emailLabel = Label(window, text='Email:', background='blue',
#                    width=30).grid(row=3, column=0)
# emailNameEntry = Entry(window).grid(row=3, column=1)

# submitButton = Button(window, text='submit').grid(
#     row=4, column=0, columnspan=2)

# window.mainloop()

# from tkinter import *
# from tkinter.ttk import *
# import time

# # def start():
# #     tasks = 10
# #     x = 0
# #     while x<tasks:
# #         time.sleep(1)
# #         bar['value']+=10
# #         x+=1
# #         percent.set(str(int((x/tasks)*100))+'%')
# #         text.set(str(x)+'/'+str(tasks) + ' tasks completed')
# #         window.update_idletasks()

# def start():
#     GB = 50
#     download = 0
#     speed = 2
#     while download<GB:
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download+=speed
#         percent.set(str(int((download/GB)*100))+'%')
#         text.set(str(download)+'/'+str(GB) + ' GB completed')
#         window.update_idletasks()
# window = Tk()

# percent = StringVar()
# text = StringVar()

# bar = Progressbar(window, orient='horizontal', length = 300)
# bar.pack(pady=10)

# percentLabel = Label(window, textvariable=percent).pack()
# taskLabel = Label(window, textvariable=text).pack()

# button = Button(window, text = 'download', command=start).pack()

# window.mainloop()

# # canvas = widget that is used to draw graphs, plots, images in a window

# from tkinter import *

# window = Tk()

# canvas = Canvas(window, height=500, width=500)
# # canvas.create_line(0, 0, 500, 500, fill='teal', width=5)
# # canvas.create_line(0, 500, 500, 0, fill='sky blue', width=5)
# # canvas.create_rectangle(50, 50, 250, 250, fill='teal')
# # canvas.create_polygon(250, 0, 500, 500, 0, 500, fill='yellow', outline='black', width=5)
# # points = [250, 0, 500, 500, 0, 500]
# # canvas.create_polygon(points, fill='yellow', outline='black', width=5)
# # canvas.create_arc(0,0, 500,500, fill='green', style = PIESLICE, start=270, extent=180) #style = ARC|PIESLICE|CHORD
# canvas.create_arc(0,0, 500,500, fill='red', extent= 180, width=5)
# canvas.create_arc(0,0, 500,500, fill='white',start=180, extent= 180, width=5)
# canvas.create_oval(190, 190, 310, 310, fill='white', width=5)
# canvas.pack()
# window.mainloop()


# from tkinter import *
# def doSomething(event):
#     print('You pressed the button', event.keysym)
#     label.config(text=event.keysym)

# window = Tk()

# # window.bind('<Return>', doSomething)
# # window.bind('<w>', doSomething)
# # window.bind('<a>', doSomething)
# # window.bind('<Up>', doSomething)
# # window.bind('<Down>', doSomething)
# window.bind('<Key>', doSomething)

# label = Label(window, font=('Helvetica', 70))
# label.pack()
# window.mainloop()

# from tkinter import *

# def doSomething(event):
#     print('you clicked mouse at:', event.x,',', event.y)
# window=Tk()

# # window.bind('<Button-1>', doSomething) #left click
# # window.bind('<Button-2>', doSomething) #middle click
# # window.bind('<Button-3>', doSomething) #right click
# # window.bind('<ButtonRelease>', doSomething)
# # window.bind('<Enter>', doSomething) # function call when mouse pointer enters the window
# # window.bind('<Leave>', doSomething) # leave the window
# window.bind('<Motion>', doSomething) # where the mouse pointer moves

# window.mainloop()

# from tkinter import *

# def drag_start(event):
#     widget = event.widget
#     widget.startX = event.x
#     widget.startY = event.y

# def drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x()- widget.startX + event.x
#     y = widget.winfo_y()- widget.startY + event.y
#     widget.place(x=x, y=y)

# window=Tk()

# label = Label(window, background='red', width= 10, height = 5)
# label.place(x=0,y=0)

# label2 = Label(window, background='teal', width= 10, height = 5)
# label2.place(x=100,y=100)

# label.bind('<Button-1>', drag_start)
# label.bind('<B1-Motion>', drag_motion)

# label2.bind('<Button-1>', drag_start)
# label2.bind('<B1-Motion>', drag_motion)

# window.mainloop()

# from tkinter import *


# def move_up(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()-10)

# def move_down(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y()+10)

# def move_left(event):
#     label.place(x=label.winfo_x()-10, y=label.winfo_y())

# def move_right(event):
#     label.place(x=label.winfo_x()+10, y=label.winfo_y())


# window = Tk()
# window.geometry('500x500')

# window.bind('<w>', move_up)
# window.bind('<s>', move_down)
# window.bind('<a>', move_left)
# window.bind('<d>', move_right)
# window.bind('<Up>', move_up)
# window.bind('<Down>', move_down)
# window.bind('<Left>', move_left)
# window.bind('<Right>', move_right)

# myImage = PhotoImage(file='python.png')
# label = Label(window, image=myImage, bg='black')
# label.place(x=0, y=0)


# window.mainloop()

# from tkinter import *


# def move_up(event):
#     canvas.move(myImage, 0, -10)

# def move_down(event):
#     canvas.move(myImage, 0, 10)


# def move_left(event):
#     canvas.move(myImage, -10, 0)


# def move_right(event):
#     canvas.move(myImage, 10, 0)


# window = Tk()

# window.bind('<w>', move_up)
# window.bind('<s>', move_down)
# window.bind('<a>', move_left)
# window.bind('<d>', move_right)
# window.bind('<Up>', move_up)
# window.bind('<Down>', move_down)
# window.bind('<Left>', move_left)
# window.bind('<Right>', move_right)

# canvas = Canvas(window, width=500, height=500)
# canvas.pack()

# photoimage = PhotoImage(file='python.png')
# myImage = canvas.create_image(0, 0, image=photoimage, anchor=NW)


# window.mainloop()

# import time
# from tkinter import *

# WIDTH = 600
# HEIGHT = 720
# xVelocity = 3
# yVelocity = 2


# window = Tk()

# canvas = Canvas(window, width=WIDTH, height=HEIGHT)
# canvas.pack()

# background_photo = PhotoImage(file='gui_logo2.png')
# background = canvas.create_image(0, 0, image=background_photo, anchor=NW)

# photoimage = PhotoImage(file='python.png')
# myImage = canvas.create_image(0, 0, image=photoimage, anchor=NW)


# image_width = photoimage.width()
# image_height = photoimage.height()
# while True:
#     coordinates = canvas.coords(myImage)
#     print(coordinates)
#     if(coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0):
#         xVelocity = -xVelocity
#     if(coordinates[1] >= (HEIGHT-image_height) or coordinates[1] < 0):
#         yVelocity = -yVelocity
#     canvas.move(myImage, xVelocity, yVelocity)
#     window.update()
#     time.sleep(0.01)

# window.mainloop()

# from tkinter import *
# import time
# from GUI_ball import *

# window = Tk()

# WIDTH = 500
# HEIGHT = 500

# canvas = Canvas(window, width=WIDTH, height=HEIGHT)
# canvas.pack()

# volley_ball = Ball(canvas, 0, 0, 100, 1, 1, 'white')
# tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, 'yellow')
# basket_ball = Ball(canvas, 0, 0, 125, 8, 7, 'orange')

# while True:
#     volley_ball.move()
#     tennis_ball.move()
#     basket_ball.move()
#     window.update()
#     time.sleep(0.01)

# window.mainloop()


# from tkinter import *
# from time import *


# def update():
#     time_string = strftime('%I:%M:%S %p')
#     time_label.config(text=time_string)

#     day_string = strftime('%A')
#     day_label.config(text=day_string)

#     date_string = strftime('%B %d, %Y')
#     date_label.config(text=date_string)

#     window.after(1000, update)


# window = Tk()

# time_label = Label(window, font=('Arial', 50),
#                    foreground='green', background='black')
# time_label.pack()

# day_label = Label(window, font=('Ink Free', 25))
# day_label.pack()

# date_label = Label(window, font=('Ink Free', 25))
# date_label.pack()

# update()

# window.mainloop()

# import smtplib

# sender = 'drarabin@gmail.com'
# receiver = 'late6002@gmail.com'
# # receiver = 'aayussraut.ar@gmail.com'
# password = 'koroshe#*77734'
# subject = 'Python email test'
# body = 'This email was written usnig python!!!! ^_^'

# # header
# message = f"""From: SnoopDogg{sender}
# To: RauteeeeeeeeeeeeAbababababab{receiver}
# Subject: {subject}\n
# {body}
# """

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()

# try:
#     server.login(sender, password)
#     print('Logged in....')
#     server.sendmail(sender, receiver, message)
#     print('Email has been sent!')

# except smtplib.SMTPAuthenticationError:
#     print('Unable to sign in!')

# from tkinter import *


# def button_press(num):
#     global equation_text

#     equation_text = equation_text + str(num)
#     equation_label.set(equation_text)


# def equals():
#     global equation_text

#     try:
#         total = str(eval(equation_text))

#         equation_label.set(total)
#         equation_text = total
#     except ZeroDivisionError:
#         equation_label.set('Arithmitic error')
#         equation_text = ''
#     except SyntaxError:
#         equation_label.set('Syntax error')
#         equation_text = ''


# def clear():
#     global equation_text

#     equation_label.set('')
#     equation_text = ''

#     pass


# window = Tk()
# window.title('Calculator Program')
# window.geometry('500x500')

# equation_text = ""

# equation_label = StringVar()

# label = Label(window, textvariable=equation_label, font=(
#     'consolas', 20), background='white', width=24, height=2)
# label.pack()

# frame = Frame(window)
# frame.pack()

# button1 = Button(frame, text=1, height=4, width=9,
#                  font=35, command=lambda: button_press(1))
# button1.grid(row=0, column=0)

# button2 = Button(frame, text=2, height=4, width=9,
#                  font=35, command=lambda: button_press(2))
# button2.grid(row=0, column=1)

# button3 = Button(frame, text=3, height=4, width=9,
#                  font=35, command=lambda: button_press(3))
# button3.grid(row=0, column=2)

# button4 = Button(frame, text=4, height=4, width=9,
#                  font=35, command=lambda: button_press(4))
# button4.grid(row=1, column=0)

# button5 = Button(frame, text=5, height=4, width=9,
#                  font=35, command=lambda: button_press(5))
# button5.grid(row=1, column=1)

# button6 = Button(frame, text=6, height=4, width=9,
#                  font=35, command=lambda: button_press(6))
# button6.grid(row=1, column=2)

# button7 = Button(frame, text=7, height=4, width=9,
#                  font=35, command=lambda: button_press(7))
# button7.grid(row=2, column=0)

# button8 = Button(frame, text=8, height=4, width=9,
#                  font=35, command=lambda: button_press(8))
# button8.grid(row=2, column=1)

# button9 = Button(frame, text=9, height=4, width=9,
#                  font=35, command=lambda: button_press(9))
# button9.grid(row=2, column=2)

# button0 = Button(frame, text=0, height=4, width=9,
#                  font=35, command=lambda: button_press(0))
# button0.grid(row=3, column=0)

# plus = Button(frame, text='+', height=4, width=9,
#               font=35, command=lambda: button_press('+'))
# plus.grid(row=0, column=3)

# minus = Button(frame, text='-', height=4, width=9,
#                font=35, command=lambda: button_press('-'))
# minus.grid(row=1, column=3)

# multiply = Button(frame, text='*', height=4, width=9,
#                   font=35, command=lambda: button_press('*'))
# multiply.grid(row=2, column=3)

# divide = Button(frame, text='/', height=4, width=9,
#                 font=35, command=lambda: button_press('/'))
# divide.grid(row=3, column=3)

# equal = Button(frame, text='=', height=4, width=9,
#                font=35, command=lambda: equals())
# equal.grid(row=3, column=2)

# decimal = Button(frame, text='.', height=4, width=9,
#                  font=35, command=lambda: button_press('.'))
# decimal.grid(row=3, column=1)

# clearButton = Button(window, text='clear', height=4, width=12,
#                      font=35, command=lambda: clear())
# clearButton.pack()


# window.mainloop()

