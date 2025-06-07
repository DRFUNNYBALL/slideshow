from tkinter import *
from PIL import ImageTk, Image

def forward(image_number):
    global image_label
    global button_forward
    global button_back

    image_label.grid_forget()
    image_label = Label(image=image_list[image_number-1])

    button_back = Button(root, text='<--', command=lambda: back(image_number-1))

    if image_number == len(image_list):
        button_forward = Button(root, text='-->', state=DISABLED)
    else:
        button_forward = Button(root, text='-->', command=lambda: forward(image_number+1))
    
    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
    global image_label
    global button_forward
    global button_back

    image_label.grid_forget()
    image_label = Label(image=image_list[image_number-1])

    button_forward = Button(root, text='-->', command=lambda: back(image_number+1))

    if image_number == 1:
        button_back = Button(root, text='<--', state=DISABLED)
    else:
        button_back = Button(root, text='<--', command=lambda: back(image_number-1))
    
    image_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

root = Tk()
root.title('Slideshow')

image1 = ImageTk.PhotoImage(Image.open("D:\VSCODE\python\image\8efad7b53c142eee1bea125db3993866.jpg"))
image2 = ImageTk.PhotoImage(Image.open("D:\VSCODE\python\image\Lujiralun Apex Legends Video Game Poster Vintage Metal Tin Sign Metal Plaque Decor 12x8 inches.jpg"))
image_list = [image1, image2]

image_label = Label(image=image1)
image_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text='<--', state=DISABLED)
button_exit = Button(root, text='Exit', command=root.quit)
button_forward = Button(root, text='-->', command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()