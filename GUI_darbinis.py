from tkinter import *
from tkinter import simpledialog
import os


def get_message():
	print(phone_number.get())
	print(msg_box.get("1.0", "end-1c"))
	msg_box.delete("1.0", "end-1c")
	phone_number.delete(0, END)


def clear():
	msg_box.delete("1.0", "end-1c")
	phone_number.delete(0, END)


def clear_hint_message_box(event):
	msg_box.delete("1.0", "end-1c")


def clear_hint_phone_box(event):
	phone_number.delete(0, END)


def check():
	dirName = r"C:\SMS_Sender"  # Create target directory & all intermediate directories if don't exists

	if not os.path.exists(dirName):
		os.makedirs(dirName)
		print("Directory ", dirName, " Created ")
	else:
		print("Directory ", dirName, " already exists")


def user_crediantials():
	username_info = username.get()
	password_info = password.get()

	dirName = r"C:\SMS_Sender"  # Create target directory & all intermediate directories if don't exists

	if not os.path.exists(dirName):
		os.makedirs(dirName)
		print("Directory ", dirName, " Created ")
	else:
		pass

	with open(r"C:\SMS_Sender\credentials.txt", "w") as f:
		f.write(username_info+"\n")
		f.write(password_info)

	username_entry.delete(0, END)
	password_entry.delete(0, END)

	Label(login_screen, text="Login Successful", fg="green", font=("calibri", 12)).pack()


def login():
	global username, password, username_entry, password_entry, login_screen
	login_screen = Toplevel(root)
	login_screen.title("Login information")
	login_screen.geometry("270x210")

	username = StringVar()
	password = StringVar()

	Label(login_screen, text="").pack()
	Label(login_screen, text="Username *").pack()
	username_entry = Entry(login_screen, textvariable=username)
	username_entry.pack()

	Label(login_screen, text="Password *").pack()
	password_entry = Entry(login_screen, textvariable=password, show='*')
	password_entry.pack()
	Label(login_screen, text="").pack()
	Button(login_screen, text="Login", width=30, height=3, command=user_crediantials).pack()


def add_contact():

	name_info = name.get()
	phone_info = phone.get()

	contact_list.insert(END, name_info+" - "+phone_info)

	with open(r"C:\SMS_Sender\contacts.txt", "a") as f:
		f.write(name_info+" - "+phone_info+"\n")

	contact_name_entry.delete(0, END)
	contact_phone_entry.delete(0, END)


def get_contacts():
	with open(r"C:\SMS_Sender\contacts.txt", "r") as f:
		for line in f:
			contact_list.insert(END, line)


def contacts():

	global name, phone, contact_name_entry, contact_phone_entry, contact_list
	contact_screen = Toplevel(root)
	contact_screen.title("Contacts")
	contact_screen.geometry("350x250")

	name = StringVar()
	phone = StringVar()

	Label(contact_screen, text="Double click to add contact to message sender.").pack()

	contact_list = Listbox(contact_screen, width=30, height=15, selectmode=SINGLE)
	contact_list.pack(side=LEFT)

	Label(contact_screen, text="Name").pack()
	contact_name_entry = Entry(contact_screen, textvariable=name)
	contact_name_entry.pack()
	Label(contact_screen, text="Phone number").pack()
	contact_phone_entry = Entry(contact_screen, textvariable=phone)
	contact_phone_entry.pack()
	Label(contact_screen, text="").pack()

	add_contact_button = Button(contact_screen, text="Add New", width=10, height=1, command=add_contact)
	add_contact_button.pack()

	delete_contact_button = Button(contact_screen, text="Delete", width=10, height=1, command=lambda contact_list=contact_list: contact_list.delete(ANCHOR))
	delete_contact_button.pack()

	get_contacts()



def main_screen():
	global root, msg_box, phone_number, send_button, clear_button

	root = Tk()
	root.title("Talkmore SMS sender")

	msg_box = Text(width=30, height=10, wrap=WORD, padx=5, pady=5)
	msg_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
	msg_box.insert(INSERT, "Your message goes here...")
	msg_box.bind("<Button-1>", clear_hint_message_box)

	phone_number = Entry(bd=1, width=12, font=21)
	phone_number.grid(row=2, column=0, padx=10, pady=5 )
	phone_number.insert(INSERT, "Phone number...")
	phone_number.bind("<Button-1>", clear_hint_phone_box)

	send_button = Button(text="Send SMS", bg="#a1d078", padx=15, pady=5, command=lambda: get_message())
	send_button.grid(row=2, column=1)

	clear_button = Button(text="Clear", bg="#a1d078", padx=27, pady=5, command=lambda: clear())
	clear_button.grid(row=3, column=1)

	empty_line = Label(text="")
	empty_line.grid(row=4, column=1)

	login_button = Button(text="Login", bg="#a1d078", padx=25, pady=5, command=login)
	login_button.grid(row=5, column=0)

	contacts_button = Button(text="Contacts", bg="#a1d078", padx=17, pady=5, command=contacts)
	contacts_button.grid(row=5, column=1)

	root.configure(background="#f7f7f7")
	root.geometry("270x340")
	root.resizable(width=False, height=False)

	check()
	root.mainloop()


main_screen()