import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 400, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('Copperplate Gothic Bold',30 ))
canvas1.create_window(250,100, window=label1)
def getJPG ():
    global im1
    
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
    
browseButton_JPG = tk.Button(text=" Import  JPG File ", command=getJPG, bg='black', fg='white', font=('Times New Roman', 16, 'bold '))
canvas1.create_window(240, 180, window=browseButton_JPG)

def convertToPNG ():
    global im1
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)

saveAsButton_PNG = tk.Button(text='Convert  JPG --> PNG', command=convertToPNG, bg='black', fg='white', font=('Times New Roman', 16, 'bold '))
canvas1.create_window(240, 240, window=saveAsButton_PNG)

root.mainloop()
