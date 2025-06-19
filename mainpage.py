import customtkinter as tk
import mysql.connector as sql

mycon=sql.connect(host='localhost',user='root',passwd='1864',database='ait')
mycur=mycon.cursor()
      
tk.set_default_color_theme('green')
master=tk.CTk()
master.title('Travel Agency')
master.geometry('700x600')

admin_credentials = {
    'ajmal': 'ajmal',
    's': 's',
    'anirudh': 'anirudh'
}

def checkID():
    global ids
    mycur.execute('select ID from packages')
    s=mycur.fetchall() 
    ids=[]
    for i in range(0,len(s)):
        ids.append(s[i][0])

def adminPanel():
    clear_frame()
    def view_edit_pack():
        clear_frame()
        def removePackage():
            checkID()
            if int(removeID.get()) in ids:
                mycur.execute('delete from packages where ID=(%s)',(int(removeID.get()),))
                mycon.commit()
                view_edit_pack() 
                tk.CTkLabel(master,text='Package successfully deleted!').pack()       
            else:               
                view_edit_pack() 
                tk.CTkLabel(master,text='The ID entered has not been made yet!').pack()
        def insertPackage():
            checkID()
            if int(id.get()) in ids:
                view_edit_pack() 
                tk.CTkLabel(master,text='ID is already selected, please try again!').pack()             
            else:          
                mycur.execute('insert into packages (ID, Package_name,date,price) values (%s,%s,%s,%s)',(int(id.get()),name.get(),date.get(),int(price.get())))
                mycon.commit()
                view_edit_pack()
                tk.CTkLabel(master,text='Package successfully entered!').pack()        
        main_frame=tk.CTkFrame(master,width=400,height=300)
        main_frame.pack()
        tk.CTkLabel(main_frame, text='Add Packages',font=('Impact',20)).pack()
        id=tk.CTkEntry(main_frame,placeholder_text='Enter ID')
        id.pack()
        name=tk.CTkEntry(main_frame,placeholder_text='Enter name of Package')
        name.pack()
        price=tk.CTkEntry(main_frame,placeholder_text='Price')
        price.pack()
        date=tk.CTkEntry(main_frame,placeholder_text='Enter date (YYYY-MM-DD)')
        date.pack()
        submit=tk.CTkButton(main_frame,text='Submit',command=insertPackage,width=100)
        submit.pack()
        remove_frame=tk.CTkFrame(master,width=400,height=300)
        remove_frame.pack()
        tk.CTkLabel(remove_frame, text='Remove Packages',font=('Impact',20)).pack()
        removeID=tk.CTkEntry(remove_frame,placeholder_text='Enter the ID of package')
        removeID.pack()
        submit=tk.CTkButton(remove_frame,text='Submit',command=removePackage,width=100)
        submit.pack()
        back=tk.CTkButton(master, text='Back',command=adminPanel,text_color=('black'))
        back.pack(pady=55)
    def view_edit_book():
        clear_frame()


        back=tk.CTkButton(master, text='Back',command=adminPanel,text_color=('black'))
        back.pack(pady=55)
    def view_cust():
        clear_frame()


        back=tk.CTkButton(master, text='Back',command=adminPanel,text_color=('black'))
        back.pack(pady=55)
    tk.CTkLabel(master, text='Admin',font=('Courier New',35)).pack(pady=20)
    tk.CTkButton(master,text='View/Edit Packages',font=('Times New Roman',20),command=view_edit_pack,text_color=('black'),width=150,height=40).pack(pady=10)
    tk.CTkButton(master,text='View/Edit Bookings',font=('Times New Roman',20),command=view_edit_book,text_color=('black'),width=150,height=40).pack(pady=10)
    tk.CTkButton(master,text='View customer details',font=('Times New Roman',20),command=view_cust,text_color=('black'),width=150,height=40).pack(pady=10)
    
    back=tk.CTkButton(master, text='Back',command=LoginScreen,text_color=('black'))
    back.pack(pady=55)
    
    


def adminLogin():
    clear_frame()
    tk.CTkLabel(master,text='Admin Login',height=50,font=('Times New Roman',50)).pack(pady=0)
    tk.CTkLabel(master,text='Username',height=20,font=('Times New Roman',25)).pack(pady=5)
    username=tk.CTkEntry(master,placeholder_text='Enter username',corner_radius=15,
                        height=35,width=200)
    username.pack(pady=10)
    tk.CTkLabel(master,text='Password',height=20,font=('Times New Roman',25)).pack(pady=5)
    password=tk.CTkEntry(master,placeholder_text='Enter password',corner_radius=15,
                        height=35,width=200,show='*')
    password.pack(pady=10)
    submit = tk.CTkButton(master, text='Submit',text_color=('black'),command=lambda: verify_admin(username.get(),password.get()))
    submit.pack(pady=10)
    back=tk.CTkButton(master,text_color=('black'),text='Back',command=LoginScreen).pack(pady=10)

# Admin verification function
def verify_admin(username,password):
    if username in admin_credentials and admin_credentials[username] == password:
        tk.CTkLabel(master,text=f"Login Success, Welcome, {username}!").pack()
        adminPanel()
    else:
        adminLogin()
        tk.CTkLabel(master,text="Login Failed. Invalid username or password! Try Again!").pack()
        

def user():
    clear_frame()
    tk.CTkLabel(master,text='Customer Page',height=50,font=('Times New Roman',50)).pack(pady=0)
    tk.CTkButton(master,text='Back',text_color=('black'),command=LoginScreen).pack(pady=30)

def clear_frame():
        for widget in master.winfo_children():
            widget.destroy()

def LoginScreen():
    clear_frame()
    tk.CTkLabel(master, text='The Travel Agency',height=30,font=('Times New Roman',50)).pack(pady=20)

    tk.CTkLabel(master, text='Choose the user',height=25,font=('Times New Roman',25)).pack(pady=20)

    tk.CTkButton(master,text='Admin',text_color=('black'),
                    corner_radius=20,height=40,command=adminLogin,
                    width=170,font=('Helvetica', 20)).pack(pady=20)

    tk.CTkButton(master,text='Customer',height=40,width=170,command=user,
                    text_color=('black'),corner_radius=20,
                    font=('Monotone',20)).pack(pady=20)

    tst=tk.CTkLabel(master,text='').pack(pady=20)

LoginScreen()
master.mainloop()
