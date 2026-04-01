import tkinter as tk

def test_my_button():
    root.title("Authorization")
    # my_text = ent_password.get()
    # set the text, pack, raise
    lbl_pwd.config(text=ent_password.get())
    lbl_pwd.pack()
    frame_auth.tkraise()

# main window
root = tk.Tk()
root.wm_geometry("300x200")
root.title("Login")

# create a frame
frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky='news')

# create label
lbl_username = tk.Label(frame_login, padx=100, text='Username:', font = "Courier")
lbl_username.pack()

# create text box
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

# another label
lbl_password = tk.Label(frame_login, text="Password:",font="Courier")
lbl_password.pack()

# another text box
ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)

# a button
btn_login = tk.Button(frame_login, text='Login', command=test_my_button)
btn_login.pack(pady=20)

# another frame
frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky='news')

# a label
lbl_pwd = tk.Label(frame_auth, padx=100, font = "Courier")


# bring the login frame to the front
frame_login.tkraise()
root.mainloop()