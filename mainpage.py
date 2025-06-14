#print('helloworld')
#hhhhhhhh = int(input('hello')

import tkinter as tk
window=tk.Tk()
window.title("**** TRAVELS")
window.geometry("1024x640")
label = tk.Label(window, text="Choose the user", font=("Arial", 14))
label.pack()
def click():
    label.config(text="Welcome!")
bt1=tk.Button(window,text="Admin",command=click)
bt1.pack()
bt2=tk.Button(window,text="customer",command=click)
bt2.pack()
window.mainloop()

