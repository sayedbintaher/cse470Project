from tkinter import *
from shopManagementSystemSecondary import *
from PIL import Image,ImageTk
from tkinter import messagebox
class login:
	def __init__(self,root,*args,**kwargs):
		r=root
		self.root=root
		self.root.title("Login System")
		self.root.geometry("1920x1080+0+0")
		self.root.state('zoomed')
		#---------Background Image------------#
		self.bg=ImageTk.PhotoImage(file="image.jpg")
		self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1, relheight=1)

		#---------Login Frame-----------------#
		Frame_login=Frame(self.root,bg="#f1f1f1",highlightbackground="#bdbdbd",highlightthickness="5")
		Frame_login.place(x=650,y=250,height=340,width=500)

		title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="red",bg="#f1f1f1").place(x=90,y=30)
		desc=Label(Frame_login,text="Accountant Employee Login",font=("Goudy old style",15,"bold"),fg="red",bg="#f1f1f1").place(x=90,y=100)
		#----------Username-------------------#
		lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="red",bg="#f1f1f1").place(x=90,y=140)
		self.txt_user=Entry(Frame_login,font=("century gothic",15),bg="lightgray")
		self.txt_user.place(x=90,y=170,width=350,height=35)
		#----------Password-------------------#
		lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="red",bg="#f1f1f1").place(x=90,y=210)
		self.txt_pass=Entry(Frame_login,font=("century gothic",15),bg="lightgray",show='*')
		self.txt_pass.place(x=90,y=240,width=350,height=35)
		#----------Login Submission button----#
		login_btn=Button(self.root,text="Login",fg="#f1f1f1",bg="red",font=("Goudy old style",20),command=lambda:[self.login(root)])
		login_btn.place(x=845,y=565,width=180,height=40)
		login_btn.bind('<Return>',login)

	def login(self,root):
		if self.txt_user.get()=="Sayed" or self.txt_pass.get()=="12345":
			navChange(root)
		elif self.txt_user.get()=="" or self.txt_pass.get()=="":
			tkinter.messagebox.showerror("Error","All fields needed to be filled up")
		else:
			tkinter.messagebox.showerror("Login Failed","Incorrect Username or Password")
			self.txt_user.delete(0, END)
			self.txt_user.focus()
			self.txt_pass.delete(0, END)
			self.txt_user.focus()


def navChange(root,*args,**kwargs):
	root.destroy()
	menuWindow()

def mainWindow():
	root= Tk()
	obj =login(root)
	root.mainloop()


mainWindow()