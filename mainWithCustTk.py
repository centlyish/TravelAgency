import customtkinter as tk
import mysql.connector as sql

#mycon=sql.connect(host='',user='frienduser',passwd='1864',database='juno')
#mycur=mycon.cursor()
      
tk.set_default_color_theme('green')
master=tk.CTk()
master.title('Travel Agency')
master.geometry('500x500')

admin_credentials = {
    'ajmal': 'ajmal',
    'sridev': 'sridev',
    'anirudh': 'anirudh'
}

def adminPanel():
     clear_frame()
     lb1=tk.CTkLabel(master, text='admin').pack()
     back=tk.CTkButton(master, text='Back',command=LoginScreen).pack(pady=10)
     #make the admin panel!!


def adminLogin():
    clear_frame()
    MainPage=tk.CTkLabel(master,text='Admin Login',height=50,font=('Times New Roman',50)).pack(pady=0)
    user=tk.CTkLabel(master,text='Username',height=20,font=('Times New Roman',25)).pack(pady=5)
    username=tk.CTkEntry(master,placeholder_text='Enter username',corner_radius=15,
                        height=35,width=200)
    username.pack(pady=10)
    passwr=tk.CTkLabel(master,text='Password',height=20,font=('Times New Roman',25)).pack(pady=5)
    password=tk.CTkEntry(master,placeholder_text='Enter password',corner_radius=15,
                        height=35,width=200,show='*')
    password.pack(pady=10)
    submit = tk.CTkButton(master, text='Submit',command=lambda: verify_admin(username.get(),password.get()))
    submit.pack(pady=10)
    back=tk.CTkButton(master,text='Back',command=LoginScreen).pack(pady=10)

# Admin verification function
def verify_admin(username,password):
    if username in admin_credentials and admin_credentials[username] == password:
        lb1=tk.CTkLabel(master,text=f"Login Success, Welcome, {username}!").pack()
        adminPanel()
        # You can redirect to the admin panel here
    else:
        adminLogin()
        lb1=tk.CTkLabel(master,text="Login Failed. Invalid username or password! Try Again!").pack()
        

def user():
    clear_frame()
    MainPage=tk.CTkLabel(master,text='Customer Page',height=50,font=('Times New Roman',50)).pack(pady=0)
    back=tk.CTkButton(master,text='Back',command=LoginScreen).pack(pady=30)

def clear_frame():
        for widget in master.winfo_children():
            widget.destroy()

def LoginScreen():
    clear_frame()
    heading=tk.CTkLabel(master, text='The Travel Agency',height=30,font=('Times New Roman',50)).pack(pady=20)

    chooseUsr=tk.CTkLabel(master, text='Choose the user',height=25,font=('Times New Roman',25)).pack(pady=20)

    adminBtn=tk.CTkButton(master,text='Admin',text_color=('black'),
                    corner_radius=20,height=40,command=adminLogin,
                    width=170,font=('Helvetica', 20)).pack(pady=20)

    userBtn=tk.CTkButton(master,text='Customer',height=40,width=170,command=user,
                    text_color=('black'),corner_radius=20,
                    font=('Monotone',20)).pack(pady=20)

    tst=tk.CTkLabel(master,text='').pack(pady=20)

LoginScreen()
master.mainloop()
