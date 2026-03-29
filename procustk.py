import customtkinter as tk
import mysql.connector as sql
from tkinter import messagebox
from datetime import datetime

# Database connection
mycon = sql.connect(host='localhost', user='ajmal', passwd='mintajmal', database='abc')
mycur = mycon.cursor()

tk.set_appearance_mode("dark")
tk.set_default_color_theme('green')

master = tk.CTk()
master.title('Travel Agency')
master.geometry('800x900')

admin_credentials = {'ajmal': 'a', 'sreedev': 's', 'anirudh': 'an'}

def clear_frame():
    for widget in master.winfo_children():
        widget.destroy()

# ---------------- ADMIN PANEL ----------------

def admin_panel():
    clear_frame()
    heading = tk.CTkLabel(master, text='Admin Panel', font=('Times New Roman', 40))
    heading.pack(pady=20)

    tk.CTkButton(master, text='Add Package', command=add_package).pack(pady=10)
    tk.CTkButton(master, text='View/Edit/Delete Packages', command=manage_packages).pack(pady=10)
    tk.CTkButton(master, text='View Bookings', command=view_bookings).pack(pady=10)
    tk.CTkButton(master, text='Reset Database', command=confirm_reset_database).pack(pady=20)
    tk.CTkButton(master, text='Logout', command=LoginScreen).pack(pady=20)

def confirm_reset_database():
    confirm = messagebox.askyesno("Confirm Reset", "Are you sure you want to reset all bookings and customers? This action cannot be undone.")
    if confirm:
        reset_database()

def reset_database():
    try:
        mycur.execute("DELETE FROM bookings")
        mycur.execute("DELETE FROM customers")
        mycon.commit()
        messagebox.showinfo("Success", "Bookings and Customers reset successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- PACKAGE MANAGEMENT ----------------

def add_package():
    clear_frame()
    heading = tk.CTkLabel(master, text='Add Package', font=('Times New Roman', 40))
    heading.pack(pady=20)

    pkg_name_entry = tk.CTkEntry(master, placeholder_text='Enter Package Name', width=300)
    pkg_name_entry.pack(pady=5)

    price_entry = tk.CTkEntry(master, placeholder_text='Enter Price', width=300)
    price_entry.pack(pady=5)

    date_entry = tk.CTkEntry(master, placeholder_text='Enter Date (YYYY-MM-DD)', width=300)
    date_entry.pack(pady=5)

    airline_entry = tk.CTkEntry(master, placeholder_text='Enter Airlines', width=300)
    airline_entry.pack(pady=5)

    def save_package():
        pkg_name = pkg_name_entry.get()
        price = price_entry.get()
        date = date_entry.get()
        airline = airline_entry.get()

        if not pkg_name or not price or not date or not airline:
            messagebox.showerror("Error", "Please fill all fields!")
            return

        try:
            price_float = float(price)
            datetime.strptime(date, '%Y-%m-%d')
            mycur.execute("INSERT INTO packages (package_name, price, date, airlines) VALUES (%s, %s, %s, %s)",
                          (pkg_name, price_float, date, airline))
            mycon.commit()
            messagebox.showinfo("Success", "Package added successfully!")
            add_package()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.CTkButton(master, text='Save Package', command=save_package).pack(pady=20)
    tk.CTkButton(master, text='Back', command=admin_panel).pack(pady=10)

def manage_packages():
    clear_frame()
    heading = tk.CTkLabel(master, text='Manage Packages', font=('Times New Roman', 40))
    heading.pack(pady=20)

    mycur.execute("SELECT * FROM packages")
    packages = mycur.fetchall()

    for pkg in packages:
        info = f"ID:{pkg[0]} | {pkg[1]} | Price: {pkg[2]} | Date: {pkg[3]} | Airline: {pkg[4]}"
        tk.CTkLabel(master, text=info).pack(pady=5)
        tk.CTkButton(master, text="Edit", command=lambda p=pkg: edit_package(p)).pack(pady=2)
        tk.CTkButton(master, text="Delete", command=lambda p=pkg[0]: delete_package(p)).pack(pady=2)

    tk.CTkButton(master, text='Back', command=admin_panel).pack(pady=20)

def edit_package(pkg):
    clear_frame()
    heading = tk.CTkLabel(master, text='Edit Package', font=('Times New Roman', 40))
    heading.pack(pady=20)

    pkg_name_entry = tk.CTkEntry(master, width=300)
    pkg_name_entry.insert(0, pkg[1])
    pkg_name_entry.pack(pady=5)

    price_entry = tk.CTkEntry(master, width=300)
    price_entry.insert(0, pkg[2])
    price_entry.pack(pady=5)

    date_entry = tk.CTkEntry(master, width=300)
    date_entry.insert(0, pkg[3])
    date_entry.pack(pady=5)

    airline_entry = tk.CTkEntry(master, width=300)
    airline_entry.insert(0, pkg[4])
    airline_entry.pack(pady=5)

    def save_changes():
        try:
            price_float = float(price_entry.get())
            datetime.strptime(date_entry.get(), '%Y-%m-%d')
            mycur.execute("UPDATE packages SET package_name=%s, price=%s, date=%s, airlines=%s WHERE id=%s",
                          (pkg_name_entry.get(), price_float, date_entry.get(), airline_entry.get(), pkg[0]))
            mycon.commit()
            messagebox.showinfo("Success", "Package updated!")
            manage_packages()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.CTkButton(master, text="Save", command=save_changes).pack(pady=10)
    tk.CTkButton(master, text='Back', command=manage_packages).pack(pady=10)

def delete_package(pkg_id):
    mycur.execute("DELETE FROM packages WHERE id=%s", (pkg_id,))
    mycon.commit()
    messagebox.showinfo("Deleted", "Package deleted!")
    manage_packages()

# ---------------- BOOKINGS VIEW ----------------

def view_bookings():
    clear_frame()
    heading = tk.CTkLabel(master, text='All Bookings', font=('Times New Roman', 40))
    heading.pack(pady=20)

    mycur.execute("""
        SELECT b.id, c.name, p.package_name, b.booking_date 
        FROM bookings b 
        JOIN customers c ON b.customer_id = c.id 
        JOIN packages p ON b.package_id = p.id""")
    bookings = mycur.fetchall()

    for book in bookings:
        info = f"BookingID:{book[0]} | Customer: {book[1]} | Package: {book[2]} | Date: {book[3]}"
        tk.CTkLabel(master, text=info).pack(pady=5)

    tk.CTkButton(master, text='Back', command=admin_panel).pack(pady=20)

# ---------------- CUSTOMER SYSTEM ----------------

def customer_login_screen():
    clear_frame()
    heading = tk.CTkLabel(master, text='Customer Login', font=('Times New Roman', 40))
    heading.pack(pady=20)

    username_entry = tk.CTkEntry(master, placeholder_text='Username', width=300)
    username_entry.pack(pady=5)

    password_entry = tk.CTkEntry(master, placeholder_text='Password', show='*', width=300)
    password_entry.pack(pady=5)

    def login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        mycur.execute("SELECT id FROM customers WHERE username=%s AND password=%s", (username, password))
        customer = mycur.fetchone()

        if customer:
            customer_panel(customer[0])
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    tk.CTkButton(master, text='Log in', command=login).pack(pady=10)
    tk.CTkButton(master, text='Register', command=customer_register_screen).pack(pady=5)
    tk.CTkButton(master, text='Back', command=LoginScreen).pack(pady=10)

def customer_register_screen():
    clear_frame()
    heading = tk.CTkLabel(master, text='Customer Register', font=('Times New Roman', 40))
    heading.pack(pady=20)

    name_entry = tk.CTkEntry(master, placeholder_text='Full Name', width=300)
    name_entry.pack(pady=5)

    email_entry = tk.CTkEntry(master, placeholder_text='Email', width=300)
    email_entry.pack(pady=5)

    phone_entry = tk.CTkEntry(master, placeholder_text='Phone', width=300)
    phone_entry.pack(pady=5)

    username_entry = tk.CTkEntry(master, placeholder_text='Username', width=300)
    username_entry.pack(pady=5)

    password_entry = tk.CTkEntry(master, placeholder_text='Password', show='*', width=300)
    password_entry.pack(pady=5)

    def register():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        try:
            mycur.execute("INSERT INTO customers (name, email, phone, username, password) VALUES (%s, %s, %s, %s, %s)",
                          (name, email, phone, username, password))
            mycon.commit()
            messagebox.showinfo("Success", "Registered Successfully!")
            customer_login_screen()
        except sql.errors.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.CTkButton(master, text='Register', command=register).pack(pady=10)
    tk.CTkButton(master, text='Back', command=customer_login_screen).pack(pady=10)

def customer_panel(customer_id):
    clear_frame()
    heading = tk.CTkLabel(master, text='Customer Panel', font=('Times New Roman', 40))
    heading.pack(pady=20)

    mycur.execute("SELECT id, package_name FROM packages")
    packages = mycur.fetchall()
    package_dict = {f"{pkg[1]} (ID:{pkg[0]})": pkg[0] for pkg in packages}
    package_options = list(package_dict.keys())
    selected_package = tk.StringVar()
    if package_options:
        selected_package.set(package_options[0])
    tk.CTkOptionMenu(master, variable=selected_package, values=package_options).pack(pady=5)

    def book():
        package_id = package_dict[selected_package.get()]
        today = datetime.today().strftime('%Y-%m-%d')
        mycur.execute("INSERT INTO bookings (customer_id, package_id, booking_date) VALUES (%s, %s, %s)",
                      (customer_id, package_id, today))
        mycon.commit()
        messagebox.showinfo("Success", "Booking successful!")
        customer_panel(customer_id)

    tk.CTkButton(master, text='Book Package', command=book).pack(pady=20)
    tk.CTkButton(master, text='View My Bookings', command=lambda: my_bookings(customer_id)).pack(pady=5)
    tk.CTkButton(master, text='Logout', command=LoginScreen).pack(pady=10)

def my_bookings(customer_id):
    clear_frame()
    heading = tk.CTkLabel(master, text='My Bookings', font=('Times New Roman', 40))
    heading.pack(pady=20)

    mycur.execute("""
        SELECT b.id, p.package_name, b.booking_date 
        FROM bookings b 
        JOIN packages p ON b.package_id = p.id 
        WHERE b.customer_id = %s""", (customer_id,))
    bookings = mycur.fetchall()

    for book in bookings:
        info = f"BookingID:{book[0]} | Package: {book[1]} | Date: {book[2]}"
        tk.CTkLabel(master, text=info).pack(pady=5)
        tk.CTkButton(master, text="Delete", command=lambda b_id=book[0]: delete_my_booking(b_id, customer_id)).pack(pady=2)

    tk.CTkButton(master, text='Back', command=lambda: customer_panel(customer_id)).pack(pady=20)

def delete_my_booking(booking_id, customer_id):
    mycur.execute("DELETE FROM bookings WHERE id=%s", (booking_id,))
    mycon.commit()
    messagebox.showinfo("Deleted", "Booking deleted!")
    my_bookings(customer_id)

# ---------------- ADMIN LOGIN ----------------

def verify_admin(username, password):
    if username in admin_credentials and admin_credentials[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        admin_panel()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")

def admin():
    clear_frame()
    heading = tk.CTkLabel(master, text='Admin Login', font=('Times New Roman', 50))
    heading.pack(pady=20)

    username_entry = tk.CTkEntry(master, placeholder_text='Enter username', width=200)
    username_entry.pack(pady=10)

    password_entry = tk.CTkEntry(master, placeholder_text='Enter password', show="*", width=200)
    password_entry.pack(pady=10)

    tk.CTkButton(master, text='Log in', command=lambda: verify_admin(username_entry.get(), password_entry.get())).pack(pady=10)
    tk.CTkButton(master, text='Back', command=LoginScreen).pack(pady=10)

# ---------------- MAIN LOGIN SCREEN ----------------

def LoginScreen():
    clear_frame()
    heading = tk.CTkLabel(master, text='The Travel Agency', font=('Times New Roman', 50))
    heading.pack(pady=20)

    tk.CTkLabel(master, text='Choose the user', font=('Times New Roman', 25)).pack(pady=20)

    tk.CTkButton(master, text='Admin', command=admin, width=170, font=('Helvetica', 20)).pack(pady=20)
    tk.CTkButton(master, text='Customer', command=customer_login_screen, width=170, font=('Monotone', 20)).pack(pady=20)

LoginScreen()
master.mainloop()

