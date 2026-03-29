import tkinter as tk
window=tk.Tk()
window.title("**** TRAVELS")
window.geometry("1024x640")
label = tk.Label(window, text="Choose the user", font=("Arial", 14))
label.pack()
def show_main_menu():
    for widget in window.winfo_children():
        widget.destroy()
    label = tk.Label(window, text="Choose the user", font=("Arial", 14))
    label.pack()
    bt1=tk.Button(window,text="Admin",command=admin_screen)
    bt1.pack()
    bt2=tk.Button(window,text="customer",comman=customer_screen)
    bt2.pack()
def admin_screen():
    for widget in window.winfo_children():
        widget.destroy()
    tk.Label(window, text="Admin Login", font=("Arial", 16)).pack()
    tk.Label(window, text="Username").pack()
    tk.Entry(window).pack()
    tk.Label(window, text="Password").pack()
    tk.Entry(window, show='*').pack()
    tk.Button(window, text="Back", command=show_main_menu).pack()
def customer_screen():
     for widget in window.winfo_children():
        widget.destroy()
     tk.Button(window, text="Back", command=show_main_menu).pack()
bt1=tk.Button(window,text="Admin",command=admin_screen)
bt1.pack()
bt2=tk.Button(window,text="customer",command=customer_screen)
bt2.pack()
window.mainloop()
