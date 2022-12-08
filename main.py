import tkinter as tk

root = tk.Tk()
root.title('Hello!')
root.geometry('640x480+500+200')
root.iconbitmap('img/bomb.ico')
# root.resizable(False, False)
# root.minsize(400, 300)
# root.maxsize(700, 500)
label = tk.Label(
    text='Hello World!',
    font=('Arial', 48, 'bold'),
    bg='red',
    fg='green',
    width=10,
    height=5,
)
label.pack()
root.mainloop()