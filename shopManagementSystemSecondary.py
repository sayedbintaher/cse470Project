from tkinter import *
import sqlite3
from PIL import Image,ImageTk
import tkinter.messagebox
import datetime
import math
import os
import random 

conn = sqlite3.connect("F:\cse470Project\Database\store.db")
c =conn.cursor()

results = c.execute("SELECT Max(productID) FROM inventory")
for r in results:
	id=r[0]


#=================================================================these components are needed while billing the customers===========================================================#
#date
date = datetime.datetime.now().date()

#temporary lists like sessions
product_list = []
product_price = []
product_quantity = []
product_id = []

#list for labels
labels_list = []		
#------------------------------------------------------------------------------Menu in order to select the options------------------------------------------------------------------------#
class secondWindow:
	def __init__(self, root,*args,**kwargs):
		#root.withdraw()
		a=root
		self.master = root
		self.master.title("Shop Management System")
		self.master.geometry("1920x1080")
		self.master.state('zoomed')
		self.master.configure(bg="#5e8cad")
		frame_heading=Frame(self.master,bg="steelblue",highlightbackground="#bdbdbd",highlightthickness="5")
		frame_heading.place(x=500,y=10,height=150,width=800)

		name_heading=Label(frame_heading,text="Cyberpunk Super Store",font=('Century Gothic',50,'bold'),bg="steelblue",fg="white")
		name_heading.place(x=30,y=15)

		frame_login=Frame(self.master,bg="steelblue",highlightbackground="#bdbdbd",highlightthickness="5")
		frame_login.place(x=650,y=250,height=440,width=500)

		addProductdb_btn=Button(frame_login,text="Add Products to the database",width=40,height=2,fg="white",bg="red",font=("Goudy old style",16),command=lambda:self.addProductsToDbW(root))
		addProductdb_btn.place(x=20, y=30)

		updateProductdb_btn=Button(frame_login,text="Update Products in the database",width=40,height=2,fg="white",bg="red",font=("Goudy old style",16),command=lambda:self.updateProductDbW(root))
		updateProductdb_btn.place(x=20, y=130)

		seeProductdb_btn=Button(frame_login,text="See Products in the database",width=40,height=2,fg="white",bg="red",font=("Goudy old style",16),command=lambda:self.databaseInfoW(root))
		seeProductdb_btn.place(x=20, y=230)

		sellProduct_btn=Button(frame_login,text="Sell Products to the customer",width=40,height=2,fg="white",bg="red",font=("Goudy old style",16),command=lambda:self.customer_bill(root))
		sellProduct_btn.place(x=20, y=330)

		exit_btn=Button(self.master, text="Exit",fg="#f1f1f1",bg="red",font=("Century Gothic",30),command=root.destroy)
		exit_btn.place(x=850,y=900,width=100,height=55)

	def addProductsToDbW(self,root):
		self.newWindow = Toplevel(self.master)
		self.app = addProductsToDbW(self.newWindow)

	def updateProductDbW(self,root):
		self.newWindow = Toplevel(self.master)
		self.app = updateProductDbW(self.newWindow)

	def databaseInfoW(self,root):
		self.newWindow = Toplevel(self.master)
		self.app = databaseInfoW(self.newWindow)

	def customer_bill(self,root):
		self.newWindow = Toplevel(self.master)
		self.app = customer_bill(self.newWindow)
	
def menuWindow():
	root= Tk()
	obj =secondWindow(root)
	root.mainloop()

#============================================================================Adding Product To the database Class========================================================================#
class addProductsToDbW:

	def __init__(self, master, *args, **kwargs):

		self.master= master
		self.master.title("Add Products to database")
		self.master.geometry("1920x1080")
		self.master.state('zoomed')
		self.heading= Label(master,text="Add Products In The Inventory", font=('Century Gothic',40,'bold'),bg='#5e8cad',fg='white')
		self.heading.place(x=400, y=0)
		self.master.configure(bg="#5e8cad")

		#self.bg=ImageTk.PhotoImage(file="image.jpg")
		#self.bg_image=Label(self.master,image=self.bg).place(x=0,y=0,relwidth=1, relheight=1)

  
		#labels and entries for the window
		self.name_1 =Label (master, text="Enter product name",font=('arial 18 bold'),bg='#5e8cad',fg='white')
		self.name_1.place(x=0, y=70)

		self.stock_1 =Label (master, text="Enter stock",font=('arial 18 bold'),bg='#5e8cad', fg='white')
		self.stock_1.place(x=0, y=120)
		
		
		self.costPrice_1 =Label (master, text="Enter Cost Price",font=('arial 18 bold'),bg='#5e8cad', fg='white')
		self.costPrice_1.place(x=0, y=170)

		
		self.sellingPrice_1 =Label (master, text="Enter Selling Price",font=('arial 18 bold'),bg='#5e8cad', fg='white')
		self.sellingPrice_1.place(x=0, y=220)

		
		self.vendor_1 =Label (master, text="Enter Vendor's Name",font=('arial 18 bold'),bg='#5e8cad', fg='white')
		self.vendor_1.place(x=0, y=270)

		
		self.vendorPhoneNo_1 =Label (master, text="Enter Vendor's Phone no",font=('arial 18 bold'),bg='#5e8cad', fg='white')
		self.vendorPhoneNo_1.place(x=0, y=320)

		self.id_1=Label (master, text="Enter ID",font=('arial 18 bold'),bg='#5e8cad', fg='white')
		self.id_1.place(x=0, y=370)

		#entries for the labels
		self.name_e= Entry(master, width=25, font='arial 18 bold')
		self.name_e.place(x=380, y=70)

		self.stock_e= Entry(master, width=25, font='arial 18 bold')
		self.stock_e.place(x=380, y=120)

		self.costPrice_e= Entry(master, width=25, font='arial 18 bold')
		self.costPrice_e.place(x=380, y=170)

		self.sellingPrice_e= Entry(master, width=25, font='arial 18 bold')
		self.sellingPrice_e.place(x=380, y=220)

		self.vendor_e= Entry(master, width=25, font='arial 18 bold')
		self.vendor_e.place(x=380, y=270)

		self.vendorPhoneNo_e=Entry(master, width=25, font='arial 18 bold')
		self.vendorPhoneNo_e.place(x=380, y=320)

		self.id_e=Entry(master, width=25, font=('arial 18 bold'))
		self.id_e.place(x=380, y=370)

		#button to add the database 
		self.btn_add= Button(master, text="Add To Database", width=25, height=2, bg='steelblue', fg='white', command=lambda:self.get_items(master))
		self.btn_add.place(x=520, y=420)


		#clear button
		self.btn_clear= Button(master, text="Clear all fields", width=18, height=2, bg="lightgreen", fg="white",command=self.clear_all)
		self.btn_clear.place(x=380, y=420)

		#back button
		self.back_clear= Button(master, text="Back", font=("Goudy Old Style",16,"bold"),width=8, height=1, bg="steelblue", fg="white",command=master.destroy)
		self.back_clear.place(x=10, y=8)

	def clear_all(self):
		self.name_e.delete(0, END)
		self.stock_e.delete(0,END)
		self.costPrice_e.delete(0,END)
		self.sellingPrice_e.delete(0,END)
		self.vendor_e.delete(0,END)
		self.vendorPhoneNo_e.delete(0,END)
		self.id_e.delete(0,END)

	def get_items(self,master):
		#get from entries
		self.name = self.name_e.get()
		self.stock = self.stock_e.get()
		self.costPrice = self.costPrice_e.get()
		self.sellingPrice = self.sellingPrice_e.get()
		self.vendor = self.vendor_e.get()
		self.vendorPhoneNo = self.vendorPhoneNo_e.get()

		#dynamic entries
		self.totalCostPrice = float(self.costPrice) * float(self.stock)
		self.totalSellingPrice = float(self.sellingPrice)* float(self.stock)
		self.assumed_profit= float(self.totalSellingPrice - self.totalCostPrice)
		if self.name == '' or self.stock =='' or self.costPrice == '' or self.sellingPrice == '':
			tkinter.messagebox.showerror("Error", "Please fill all the entries")
		else:
			sql = "INSERT INTO inventory (name, stock, costPrice, sellingPrice, totalCostPrice, totalSellingPrice, vendor, vendorPhoneNo) VALUES (?,?,?,?,?,?,?,?)"
			c.execute(sql,(self.name, self.stock,self.costPrice,self.sellingPrice,self.totalCostPrice,self.totalSellingPrice,self.vendor,self.vendorPhoneNo))
			conn.commit()
			tkinter.messagebox.showinfo("Success","Successfully added to the database")

		master.destroy()

#======================================================================Updating Product in Database=======================================================================#

class updateProductDbW:
	def __init__(self, master, *args, **kwargs):

		self.master= master
		self.master.title("Add Products to database")
		self.master.geometry("1920x1080")
		self.master.state('zoomed')
		self.master.configure(bg="#5e8cad")

		self.heading= Label(master,text="Update Products In Inventory", font=("Century Gothic", 40, "bold"),bg="#5e8cad",fg='white')
		self.heading.place(x=550, y=0)


		#Label and entry for the id 
		self.id_1e =Label(master, text="Enter ID", font=("Goudy old style", 18, "bold"),bg="#5e8cad",fg='white')
		self.id_1e.place(x=0, y=70)

		self.id_1eb= Entry(master, font=("Goudy old style", 18, "bold"), width=15)
		self.id_1eb.place(x=380, y=70)

		self.btn_search =Button(master, text="Search",font=("Goudy old style", 14, "bold"),width=10, height=1, bg="orange", command=self.search)
		self.btn_search.place(x=585, y=67)

  
		#labels and entries for the window
		self.name_1 =Label (master, text="Enter product name",font=("Goudy old style", 18, "bold"),bg="#5e8cad", fg='white')
		self.name_1.place(x=0, y=120)

		self.stock_1 =Label (master, text="Enter stock",font=("Goudy old style", 18, "bold"), bg="#5e8cad",fg='white')
		self.stock_1.place(x=0, y=170)
		
		
		self.costPrice_1 =Label (master, text="Enter Cost Price",font=("Goudy old style", 18, "bold"), bg="#5e8cad",fg='white')
		self.costPrice_1.place(x=0, y=220)

		
		self.sellingPrice_1 =Label (master, text="Enter Selling Price",font=("Goudy old style", 18, "bold"), bg="#5e8cad",fg='white')
		self.sellingPrice_1.place(x=0, y=270)

		self.totalCostPrice_1 =Label (master, text="Enter Total Cost Price",font=("Goudy old style", 18, "bold"), bg="#5e8cad",fg='white')
		self.totalCostPrice_1.place(x=0, y=320)

		self.totalSellingPrice_1 =Label (master, text="Enter Total Selling Price",font=("Goudy old style", 18, "bold"),bg="#5e8cad", fg='white')
		self.totalSellingPrice_1.place(x=0, y=370)

		
		self.vendor_1 =Label (master, text="Enter Vendor's Name",font=("Goudy old style", 18, "bold"),bg="#5e8cad", fg='white')
		self.vendor_1.place(x=0, y=420)

		
		self.vendorPhoneNo_1 =Label (master, text="Enter Vendor's Phone no",font=("Goudy old style", 18, "bold"), bg="#5e8cad",fg='white')
		self.vendorPhoneNo_1.place(x=0, y=470)


		#entries for the labels
		self.name_e= Entry(master, width=25, font=("Goudy old style", 18, "bold"))
		self.name_e.place(x=380, y=120)

		self.stock_e= Entry(master, width=25,font=("Goudy old style", 18, "bold"))
		self.stock_e.place(x=380, y=170)

		self.costPrice_e= Entry(master, width=25,font=("Goudy old style", 18, "bold"))
		self.costPrice_e.place(x=380, y=220)

		self.sellingPrice_e= Entry(master, width=25,font=("Goudy old style", 18, "bold"))
		self.sellingPrice_e.place(x=380, y=270)

		self.totalCostPrice_e= Entry(master, width=25,font=("Goudy old style", 18, "bold"))
		self.totalCostPrice_e.place(x=380, y=320)

		self.totalSellingPrice_e= Entry(master, width=25,font=("Goudy old style", 18, "bold"))
		self.totalSellingPrice_e.place(x=380, y=370)

		self.vendor_e= Entry(master, width=25,font=("Goudy old style", 18, "bold"))
		self.vendor_e.place(x=380, y=420)

		self.vendorPhoneNo_e=Entry(master, width=25,font=("Goudy old style", 18, "bold"))
		self.vendorPhoneNo_e.place(x=380, y=470)

		#button to add the database 
		self.btn_add= Button(master, text="Update Database",font=("Goudy old style", 12, "bold"), width=20, height=2, bg='steelblue', fg='black', command=lambda:self.update(master))
		self.btn_add.place(x=497, y=520)

		#back button
		self.back_clear= Button(master, text="Back", font=("Goudy Old Style",16,"bold"),width=8, height=1, bg="steelblue", fg="white",command=master.destroy)
		self.back_clear.place(x=10, y=8)

	def search(self, *args, **kwargs):
		sql="SELECT * FROM inventory WHERE productID=?"
		result= c.execute(sql, str(self.id_1eb.get()))
		for r in result:
			self.n1= r[1] #name
			self.n2= r[2] #stock
			self.n3= r[3] #costPrice
			self.n4= r[4] #sellingPrice
			self.n5= r[5] #totalCostPrice
			self.n6= r[6] #totalSellingPrice
			self.n8= r[7] #vendor
			self.n9= r[8] #vendorPhoneNo
		conn.commit()

		#insert into the entries to update
		self.name_e.delete(0, END)
		self.name_e.insert(0,str(self.n1))

		self.stock_e.delete(0, END)
		self.stock_e.insert(0,str(self.n2))

		self.costPrice_e.delete(0, END)
		self.costPrice_e.insert(0,str(self.n3))

		self.sellingPrice_e.delete(0, END)
		self.sellingPrice_e.insert(0,str(self.n4))

		self.vendor_e.delete(0, END)
		self.vendor_e.insert(0,str(self.n8))

		self.vendorPhoneNo_e.delete(0, END)
		self.vendorPhoneNo_e.insert(0,self.n9)

		self.totalCostPrice_e.delete(0,END)
		self.totalCostPrice_e.insert(0, str(self.n5))

		self.totalSellingPrice_e.delete(0,END)
		self.totalSellingPrice_e.insert(0, str(self.n6))


	def update(self, master,*args, **kwargs):
		#get all the updated values
		self.u1 = self.name_e.get()
		self.u2 = self.stock_e.get()
		self.u3 = self.costPrice_e.get()
		self.u4 = self.sellingPrice_e.get()
		self.u5 = self.totalCostPrice_e.get()
		self.u6 = self.totalSellingPrice_e.get()
		#self.u1 = self.name_e.get()
		self.u7 = self.vendor_e.get()
		self.u8 = self.vendorPhoneNo_e.get()

		query = "UPDATE inventory SET name=?, stock=?, costPrice=?, sellingPrice=?, totalCostPrice=?, totalSellingPrice=?, vendor=?, vendorPhoneNo=? WHERE productID=?"
		c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8, self.id_1eb.get()))
		conn.commit()
		tkinter.messagebox.showinfo("Success", "Update database successfully")
		master.destroy()

#=======================================================Class for customer billings======================================================================================#
class customer_bill:
	def __init__(self,master,*args, **kwargs):
		self.master=master
		self.master.title("Billing the customers")
		self.master.geometry("1920x1080")
		self.master.state('zoomed')

		#frames
		self.left=Frame(master,width=1200,height=1080,bg="#9073b5",highlightbackground="#bdbdbd",highlightthickness="5")
		self.left.pack(side=LEFT)

		self.right=Frame(master,width=720,height=1080,bg="#5e8cad",highlightbackground="#bdbdbd",highlightthickness="5")
		self.right.pack(side=RIGHT)

		#self.bg=ImageTk.PhotoImage(file="frame.jpg")
		#self.bg_image=Label(self.right,image=self.bg).place(x=0,y=0)

		#components
		self.heading = Label(self.left, text="Cyberpunk Super Store", font=("Century Gothic",40,"bold"), bg="#9073b5")
		self.heading.place(x=400,y=0)

		#back button
		self.back_clear= Button(self.left, text="Back", font=("Goudy Old Style",20,"bold"),width=10, height=1, bg="steelblue", fg="white",command=master.destroy)
		self.back_clear.place(x=10, y=5)

		self.date_l = Label(self.right, text="Today's Date: "+str(date), font=("Goudy Old Style",20,"bold"), bg="#5e8cad", fg="white")
		self.date_l.place(x=5,y=10)

		#table invoice
		self.tproduct=Label(self.right, text="Products", font=("Goudy Old Style",25,"bold"),bg="#5e8cad", fg="white")
		self.tproduct.place(x=100, y=90)

		self.tquantity=Label(self.right, text="Quantity", font=("Goudy Old Style",25,"bold"),bg="#5e8cad",fg="white")
		self.tquantity.place(x=300, y=90)

		self.tamount=Label(self.right, text="Amount", font=("Goudy Old Style",25,"bold"), bg="#5e8cad",fg="white")
		self.tamount.place(x=500, y=90)

		#enter stuff
		self.enterid = Label(self.left, text="Enter Product's ID", font=("Goudy Old Style",25,"bold"), bg="#9073b5")
		self.enterid.place(x=0, y=80)

		self.enteride = Entry(self.left, width=27, font=("Goudy Old Style",25,"bold"), bg="lightblue")
		self.enteride.place(x=270, y=80)
		self.enteride.focus()

		#button
		self.search_btn = Button(self.left, text="Search",font=("Goudy Old Style",25,"bold"),width=8,height=1, bg="#174978",command=lambda:self.ajax(master))
		self.search_btn.place(x=570, y=130)


		#fill it later by the function ajax
		self.productname = Label(self.left, text="",font=("Goudy Old Style",25,"bold"), bg="#9073b5", fg="blue")
		self.productname.place(x=0, y=250)

		self.pprice = Label(self.left, text="",font=("Goudy Old Style",25,"bold"), bg="#9073b5", fg="blue")
		self.pprice.place(x=0, y=290)

		#total label
		self.total_l= Label(self.right, text="Total", font=("Goudy Old Style",25,"bold"), bg="#5e8cad",fg="white")
		self.total_l.place(x=100,y=900)

		


	def ajax(self, master,*args, **kwargs):
		self.get_id = self.enteride.get()
		#get the products info with that id and fill it in the labels above
		query = "SELECT * FROM inventory where productID=?" 
		result = c.execute(query,(self.get_id, ))
		for self.r in result:
			self.get_id=self.r[0]
			self.get_name =self.r[1]
			self.get_stock = self.r[2]
			self.get_price =self.r[4]
		self.productname.configure(text="Product's Name: "+str(self.get_name))
		self.pprice.configure(text="Price: BDT "+str(self.get_price))

		#create the quantity and the discount label 
		self.quantity_l = Label(self.left, text="Enter Quantity ", font=("Goudy Old Style",25,"bold"), bg="#9073b5")
		self.quantity_l.place(x=0, y=370)

		self.quantity_e = Entry(self.left,width = 27,font=("Goudy Old Style",25,"bold"), bg="lightblue")
		self.quantity_e.place(x=270, y=370)
		self.quantity_e.focus()

		#discout
		self.discount_l = Label(self.left, text="Enter Discount", font=("Goudy Old Style",25,"bold"), bg="#9073b5")
		self.discount_l.place(x=0, y=420)


		self.discount_e = Entry(self.left,width =27, font=("Goudy Old Style",25,"bold"), bg="lightblue")
		self.discount_e.place(x=270, y=420)
		self.discount_e.insert(END, 0)

		#add to cart button
		self.addToCart_btn = Button(self.left, text="Add To Cart",font=("Goudy Old Style",21,"bold"),width=12,height=1, bg="#174978", command=self.addToCart)
		self.addToCart_btn.place(x=529, y=470)

		#generate bill and change
		self.change_l = Label(self.left, text="Given amount", font=("Goudy Old Style",25,"bold"), bg="#9073b5")
		self.change_l.place(x=0, y=550)

		self.change_e = Entry(self.left,width =27, font=("Goudy Old Style",25,"bold"), bg="lightblue")
		self.change_e.place(x=270, y=550)

		#button change
		self.change_btn = Button(self.left, text="Calculate Change",font=("Goudy Old Style",20,"bold"),width=13,height=1, bg="#174978",command=self.change_func)
		self.change_btn.place(x=529, y=600)

		#generate bill button
		self.bill_btn = Button(self.left, text="Generate Bill",font=("Goudy Old Style",22,"bold"),width=46,height=1, bg="#174978",fg="black",command=lambda:self.generateBill(master))
		self.bill_btn.place(x=0, y=850)

	
		

	def addToCart(self, *args, **kwargs):
		self.quantity_value = int (self.quantity_e.get())
		if self.quantity_value>int(self.get_stock):
			tkinter.messagebox.showinfo("Error", "Not that many products in the inventory")
		else:
			self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))
			product_list.append(self.get_name)
			product_price.append(self.final_price)
			product_quantity.append(self.quantity_value)
			product_id.append(self.get_id)

			self.x_index=0
			self.y_index=140
			self.counter=0
			for self.p in product_list:
				self.tempname=Label(self.right, text=str(product_list[self.counter]), font=("Goudy Old Style",25,"bold"), bg="#5e8cad", fg="white")
				self.tempname.place(x=100, y=self.y_index)
				labels_list.append(self.tempname)

				self.tempqt=Label(self.right, text=str(product_quantity[self.counter]), font=("Goudy Old Style",25,"bold"), bg="#5e8cad", fg="white")
				self.tempqt.place(x=310, y=self.y_index)
				labels_list.append(self.tempqt)

				self.tempprice=Label(self.right, text=str(product_price[self.counter]), font=("Goudy Old Style",25,"bold"), bg="#5e8cad", fg="white")
				self.tempprice.place(x=510, y=self.y_index)
				labels_list.append(self.tempprice)

				self.y_index += 40
				self.counter += 1

				#total configure
				self.total_l.configure(text="Total: BDT "+ str(sum(product_price)))

				#delete
				self.quantity_l.place_forget()
				self.quantity_e.place_forget()
				self.discount_l.place_forget()
				self.discount_e.place_forget()
				self.productname.configure(text="")
				self.pprice.configure(text="")
				self.addToCart_btn.destroy()

				#autofocus to the enter id
				self.enteride.focus()
				self.enteride.delete(0, END)


	def change_func(self, *args, **kwargs):
		self.amount_given = float(self.change_e.get())
		self.our_total = float(sum(product_price))

		self.to_give = self.amount_given - self.our_total

		self.c_amount = Label(self.left, text="Change: BDT "+str(self.to_give), font=("Goudy Old Style",25,"bold"),bg="#9073b5",fg='black')
		self.c_amount.place(x=0, y=600)
	


	def generateBill(self, master,*args, **kwargs):
		#create the bill before updating to the database 
		invoiceNo = random.randrange(5000,10000)
		directory="F:/cse470Project/invoice/"+str(date) + "/"
		if not os.path.exists(directory):
			os.makedirs(directory)

		#templates for the bill
		company ="\t\t\t\tCyberpunk Company Pvt. Ltd.\n"
		address ="\t\t\t\tChittagong, Bangladesh\n"
		phone ="\t\t\t\t\t01849250564\n"
		sample="\t\t\t\t\tInvoice No:"+str(invoiceNo) + "\n"
		dt="\t\t\t\t\t"+ str(date)

		table_header="\n\n\t\t\t---------------------------------------\n\t\t\tSn.\tProduct\t\tQty\t\tAmount\n\t\t\t---------------------------------------"
		final = company + address + phone + sample + dt + "\n" + table_header

		#open a file to write it to
		file_name = str(directory) + str(invoiceNo) + ".rtf"
		f = open(file_name, 'w')
		f.write(final)
		#fill details 
		r=1
		i=0
		for t in product_list:
			f.write("\n\t\t\t"+ str(r) + "\t" + str(product_list[i]+"		")[:10]+"\t\t"+ str(product_quantity[i])+"\t\t"+ str(product_price[i]))
			i += 1
			r += 1
		f.write("\n\n\t\t\tTotal: BDT " + str(sum(product_price)))
		f.write("\n\t\t\tThanks for visiting")
		os.startfile(file_name, "print")
		f.close() 

		#decrease the stock 
		self.x=0
		initial = "SELECT * FROM inventory WHERE productID=?"
		result = c.execute(initial, (product_id[self.x], ))
		#decrease the stock 
		for i in product_list:
			for r in result:
				self.old_stock = r[2]
			self.new_stock = int(self.get_stock) - int(product_quantity[self.x])

			#updating the stock 
			sql="UPDATE inventory SET stock=? WHERE productID=?"
			c.execute(sql, (self.new_stock, product_id[self.x]))
			conn.commit()
			
			#insert into the transaction
			sql2 ="INSERT INTO transactions (name, quantity,amount, date,invoice_no) VALUES (?, ?, ?, ?, ?)"
			c.execute(sql2, (product_list[self.x], product_quantity[self.x], product_price[self.x], date, invoiceNo))
			conn.commit()
			
			self.x +=1
		for a in labels_list:
			a.destroy()
		del(product_list[:])
		del(product_id[:])
		del(product_quantity[:])
		del(product_price[:])

		self.total_l.configure(text="")
		self.c_amount.configure(text="")
		self.change_e.delete(0, END)
		self.enteride.focus()
		tkinter.messagebox.showinfo("Success", "Done everything smoothly")
		master.destroy()

#==============================================================================================
class databaseInfoW:
	def __init__(self,master,*args, **kwargs):
		self.master=master
		self.master.title("Billing the customers")
		self.master.geometry("1920x1080")
		self.master.state('zoomed')
		self.master.configure(bg='#5e8cad')
		self.lab =Label (master, text="Products Available In Store",font=("Century Gothic",40,"bold"),bg='#5e8cad',fg='white')
		self.lab.place(x=600, y=5)
		frame_data=Frame(self.master,bg="#f1f1f1",highlightbackground="#bdbdbd",highlightthickness="5")
		frame_data.place(x=400,y=100)
		self.tablabel=Label(master, text=" ProductID    Name          Stock           CostPrice     SellingPrice  TCostPrice   TSellPrice     Vendor         V.Phone",font=("Century Gothic",16,"bold"),bg='#5e8cad',fg="white").place(x=397,y=67)
		back_btn=Button(master, text="Back",font=("Century Gothic",20,"bold"),bg='#5e8cad',fg="white",command=master.destroy).place(x=10,y=10)

		c.execute("SELECT * FROM inventory")
		i=0
		for count in c:
			for j in range(len(count)):
				e = Entry(frame_data, width=10, font=("Century Gothic",16,"bold"),bg="#fff9ad",fg="black")
				e.grid(row=i, column=j)
				e.insert(END, count[j])
			i=i+1
		conn.commit()






