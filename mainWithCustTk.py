import customtkinter as tk
import mysql.connector as sql

mycon=sql.connect(host='localhost',user='root',passwd='1864',database='juno')
mycur=mycon.cursor()
      
tk.set_default_color_theme('green')
master=tk.CTk()
master.title('Travel Agency')
master.geometry('500x500')

def admin():
    clear_frame()
    MainPage=tk.CTkLabel(master,text='Admin Login',height=50,font=('Times New Roman',50))
    MainPage.pack(pady=0)
    user=tk.CTkLabel(master,text='Username',height=20,font=('Times New Roman',35))
    user.pack(pady=10)
    usrname=tk.CTkEntry(master,placeholder_text='Enter username',corner_radius=15,
                        height=35,width=200)
    usrname.pack(pady=10)
    passwr=tk.CTkLabel(master,text='Password',height=20,font=('Times New Roman',35))
    passwr.pack(pady=10)
    password=tk.CTkEntry(master,placeholder_text='Enter password',corner_radius=15,
                        height=35,width=200)
    password.pack(pady=10)
    submit=tk.CTkButton(master,text='Submit')
    submit.pack(pady=30)
    back=tk.CTkButton(master,text='Back',command=LoginScreen)
    back.pack(pady=30)

def user():
    clear_frame()
    MainPage=tk.CTkLabel(master,text='User LOgin')
    MainPage.pack(pady=30)
    back=tk.CTkButton(master,text='Back',command=LoginScreen)
    back.pack(pady=30)


def clear_frame():
        for widget in master.winfo_children():
            widget.destroy()

def MainScreen():
    clear_frame()
    heading=tk.CTkLabel(master, text='The Travel Agency',height=30,font=('Times New Roman',50))
    heading.pack(pady=20)

    chooseUsr=tk.CTkLabel(master, text='Choose the user',height=25,font=('Times New Roman',25))
    chooseUsr.pack(pady=20)

    adminBtn=tk.CTkButton(master,text='Admin',text_color=('black'),
                    corner_radius=20,height=40,command=admin,
                    width=170,font=('Helvetica', 20))
    adminBtn.pack(pady=20)

    userBtn=tk.CTkButton(master,text='Customer',height=40,width=170,command=user,
                    text_color=('black'),corner_radius=20,
                    font=('Monotone',20))
    userBtn.pack(pady=1)

    tst=tk.CTkLabel(master,text='')
    tst.pack(pady=20)

MainScreen()


master.mainloop()

