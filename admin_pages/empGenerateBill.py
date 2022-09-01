import json
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import database
from tkinter.ttk import Combobox

import random
class EmpBill:
    def __init__(self):
        self.root=Toplevel()
        self.root.title("bill slip")
        self.root.geometry('1166x718')
        self.root.state('zoomed')
        self.bg_color='#34495E'

    #======================variable=================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.item=StringVar()
        self.Rate=IntVar()
        self.quantity=IntVar()
        self.bill_no=StringVar()
        self.x=random.randint(1000,9999)
        self.bill_no.set(str(self.x))

        global l
        l=[]
        self.bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        #=========================Functions================================

    def additm(self, i):
        bookName = list(globals()[f"self.bookDrop{i}"].get().split())
        bookName = bookName[1]

        quantity = globals()[f"self.quantEntry{i}"].get()
        cost = globals()[f"self.costEntry{i}"].get()

        # self.textarea.insert((10.0+float(len(l)-1)), f"{self.item.get()}\t\t{self.quantity.get()}\t\t{self.m}\n")
        self.textarea.insert((10.0+float(len(l)-1)), f'{bookName}\t\t{quantity}\t\t{cost}\n')
        # self.n=self.Rate.get()
        # self.m=self.quantity.get()*self.n
        # l.append(self.m)
        # if self.item.get()!='':
        #     self.textarea.insert((10.0+float(len(l)-1)), f"{self.item.get()}\t\t{self.quantity.get()}\t\t{self.m}\n")
        # else:
        #     messagebox.showerror('Error','Please enter item')


    def gbill(self):
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("Error", "Customer detail are must")
        else:
            textAreaText = self.textarea.get(10.0,(10.0+float(len(l))))
            self.welcome()
            total = [int(globals()[f"self.costEntry{i}"].get()) for i in range(self.i)]
            for i in range(self.i):
                self.additm(i)
            self.textarea.insert(END, textAreaText)
            self.textarea.insert(END, f"\n======================================")
            self.textarea.insert(END, f"\nTotal Paybill Amount :\t\t      {sum(total)}")
            self.textarea.insert(END, f"\n\n======================================")
            # self.save_bill()
            data = (
                self.c_name.get(),
                self.c_phone.get(),
                sum(total),
                json.dumps((self.id[0], self.id[1]))
            )
            res = database.createOrder(data)
            if res:
                for i in range(self.i):
                    bookName = list(globals()[f"self.bookDrop{i}"].get().split())
                    bookId = bookName[0]
                    quantity = globals()[f"self.quantEntry{i}"].get()

                    data = (
                        res,
                        bookId,
                        quantity
                    )
                    print(data)
                    res1 = database.createOrderDetails(data)
                    if res1:
                        messagebox.showinfo('Success', 'Order created successfully.')
                    else:
                        messagebox.showerror('Error', 'something went wrong.')
            else:
                messagebox.showerror('Error', 'something went wrong.')



    def clear(self):
        self.c_name.set('')
        self.c_phone.set('')
        self.item.set('')
        self.Rate.set(0)
        self.quantity.set(0)
        self.welcome()
        
    def exit(self):
        self.op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if self.op > 0:
            self.root.destroy()
    def save_bill(self):
        op=messagebox.askyesno("Save bill","Do you want t o save the Bill?")
        if op>0:
            bill_details=self.textarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(bill_details)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no, :{self.bill_no.get()} Saved Successfully")
        else:
            return
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t  Welcome To Book Shop")
        self.textarea.insert(END,f"\n\nBill Number:\t\t{self.bill_no.get()}")
        self.textarea.insert(END,f"\nCustomer Name:\t\t{self.c_name.get()}")
        self.textarea.insert(END,f"\nPhone Number:\t\t{self.c_phone.get()}")
        self.textarea.insert(END,f"\n\n======================================")
        self.textarea.insert(END,"\nBook\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n======================================\n")
        self.textarea.configure(font='arial 15 bold')


    def billing(self, id):

        self.id = id

        F0=LabelFrame(self.root,bd=10,relief=GROOVE,bg=self.bg_color)
        F0.place(x=0,y=0,relwidth=1)
        
        cname_lbl=Label(F0,text='GENERATE BILL',font=('times new romon',25,'bold'),bg=self.bg_color,fg='white').grid(row=0,column=0,padx=530,pady=5)

        #=================Product Frames=================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text='CUSTOMER DETAILS',font=('times new romon',15,'bold'),fg='gold',bg=self.bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text='CUSTOMER NAME',font=('times new romon',18,'bold'),bg=self.bg_color,fg='white').grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name, bg="#ADD8E6", font='arial 15 bold',relief=SUNKEN,bd=7).grid(row=0,column=1,padx=10,pady=5)

        cphone_lbl=Label(F1,text='PHONE NO. ',font=('times new romon',18,'bold'),bg=self.bg_color,fg='white').grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,font='arial 15 bold',bg="#ADD8E6",textvariable=self.c_phone,relief=SUNKEN,bd=7).grid(row=0,column=3,padx=10,pady=5)

        self.F2 = LabelFrame(self.root, text='BOOK DETAILS', font=('times new romon', 18, 'bold'), fg='gold',bg=self.bg_color)
        self.F2.place(x=20, y=180,width=800,height=500)

        category_lable= Label(self.F2, text='CATEGORY', font=('times new romon',18, 'bold'), bg=self.bg_color, fg='white').place(x=10,y=19)
        
        
 
        book_lable= Label(self.F2, text='BOOKS', font=('times new romon',18, 'bold'), bg=self.bg_color, fg='white').place(x=210,y=19)
        
        
        
        quantity_lable= Label(self.F2, text='QUANTITY', font=('times new romon',18, 'bold'), bg=self.bg_color, fg='white').place(x=390,y=19)
        
        
        cost_lable= Label(self.F2, text='COST', font=('times new romon',18, 'bold'), bg=self.bg_color, fg='white').place(x=560,y=19)

        

        # itm_txt = Entry(self.F2, width=20,textvariable=self.item, bg="#ADD8E6",font='arial 15 bold', relief=SUNKEN, bd=7).grid(row=0, column=1, padx=10,pady=20)

        # rate= Label(self.F2, text='BOOK PRICE    ', font=('times new romon',18, 'bold'), bg=self.bg_color, fg='white').place(x=30,y=50)
        
        
        # rate_txt = Entry(self.F2, width=20,textvariable=self.Rate, bg="#ADD8E6",font='arial 15 bold', relief=SUNKEN, bd=7).place(x=10,y=10)
        # n= Label(self.F2, text='BOOK STOCK   ', font=('times new romon',18, 'bold'), bg=self.bg_color, fg='white').place(x=60,y=10)
        # n_txt = Entry(self.F2, width=20,textvariable=self.quantity, bg="#ADD8E6",font='arial 15 bold', relief=SUNKEN, bd=7).place(x=60,y=10)
        
        
        self.add_button = Button(self.F2, text="ADD", bg="BLUE", fg="white", 
                                    font=("yu gothic ui", 12, "bold") , height= 1, width=4, command=self.addLabels)
        self.add_button.place(x=700, y=0)
        
        
        


        #========================Bill area================
        F3=Frame(self.root,relief=GROOVE,bd=10)
        F3.place(x=850,y=180,width=500,height=500)

        self.ill_title=Label(F3,text='Bill Area',bg="#ADD8E6",font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
        self.scrol_y=Scrollbar(F3,orient=VERTICAL)
        self.textarea=Text(F3,yscrollcommand=self.scrol_y)
        self.scrol_y.pack(side=RIGHT,fill=Y)
        self.scrol_y.config(command=self.textarea.yview)
        self.textarea.pack()
        self.welcome()
        #=========================Buttons======================
        # btn1=Button(self.F2,text='Add item',font='arial 15 bold',command=self.additm,padx=5,pady=10,bg='blue',fg='white' , width=15)
        # btn1.grid(row=3,column=0,padx=10,pady=30)
        btn2=Button(self.F2,text='Generate Bill',font='arial 15 bold',padx=5,pady=10,bg='blue',fg='white' ,width=15, command=self.gbill)
        btn2.grid(row=3,column=1,padx=10,pady=30)
        # btn3=Button(self.F2,text='Clear',font='arial 15 bold',padx=5,pady=10,command=self.clear,bg='blue',fg='white' ,width=15)
        # btn3.grid(row=4,column=0,padx=10,pady=30)
        # btn4=Button(self.F2,text='Exit',font='arial 15 bold',padx=5,pady=10,command=exit,bg='blue',fg='white' ,width=15)
        # btn4.grid(row=4,column=1,padx=10,pady=30)

        self.x = 10
        self.y = 90

        self.i = 0

        self.root.mainloop()

    def addLabels(self):
        # category_lable_txt = StringVar()
        self.options= database.allCategories()
        globals()[f"self.catDrop{self.i}"] = Combobox(self.F2, values= self.options)
        globals()[f"self.catDrop{self.i}"].place(x=self.x, y=self.y , height=34, width= 146)

        globals()[f"self.catDrop{self.i}"].bind("<<ComboboxSelected>>", lambda e, x = self.i: self.getBooks(e, x))  

        globals()[f"self.bookOptions{self.i}"]= []
        globals()[f"self.bookDrop{self.i}"] = Combobox(self.F2,  values= self.options, state=DISABLED)
        globals()[f"self.bookDrop{self.i}"].place(x=self.x + 200, y=self.y , height=34, width= 146)  

        globals()[f"self.quantEntry{self.i}"] = Entry(self.F2, width=5, bg="#ADD8E6",font='arial 15 bold', bd=7, validate="focusout", validatecommand= lambda y = self.i: self.generatePrice(y) )
        globals()[f"self.quantEntry{self.i}"].place(x=self.x + 410,y=self.y)

        globals()[f"self.costEntry{self.i}"] = Entry(self.F2, width=5, bg="#ADD8E6",font='arial 15 bold', bd=7, state = 'readonly')
        globals()[f"self.costEntry{self.i}"].place(x=self.x + 550,y=self.y)

        self.delete_button = Image.open('images\\delete.png')
        photo = ImageTk.PhotoImage(self.delete_button)
        globals()[f"self.delBtn{self.i}"]= Button(self.F2, image=photo, bg='#040405', command = lambda j = self.i : self.getIndex(j))
        globals()[f"self.delBtn{self.i}"].image = photo
        globals()[f"self.delBtn{self.i}"].place(x=self.x + 690, y=self.y)

        print(globals()[f"self.bookDrop{self.i}"], globals()[f"self.costEntry{self.i}"])


        self.y += 50
        self.i += 1

    def getIndex(self, j):
        self.i -= 1
        print(j)
        globals()[f"self.catDrop{j}"].destroy()
        globals()[f"self.bookDrop{j}"].destroy() 
        globals()[f"self.quantEntry{j}"].destroy()
        globals()[f"self.costEntry{j}"].destroy()
        globals()[f"self.delBtn{j}"].destroy()

    
    def getBooks(self, e, x):
        print(x)
        a = list(globals()[f"self.catDrop{x}"].get().split())
        res = database.getCatBook(a[0])
        print(res)
        if res:
            globals()[f"self.bookDrop{x}"].config(state = 'normal')
            globals()[f"self.bookOptions{x}"] = res
            globals()[f"self.bookDrop{x}"].config(values=globals()[f"self.bookOptions{x}"])
            globals()[f"self.bookDrop{x}"].bind("<<ComboboxSelected>>", lambda e, y = x: self.getBookPrice(e, y))
        else:
            messagebox.showerror('Alert', 'something went wrong.')
    

    def getBookPrice(self, e, y):
        print(y)
        a = list(globals()[f"self.bookDrop{y}"].get().split())
        print(a)
        res = database.getBookPrices(a[0])
        if res:
            globals()[f"self.bookPrice{y}"] = res[0]
            print(globals()[f"self.bookPrice{y}"])
        else:
            messagebox.showerror('Alert', 'something went wrong')

    
    def generatePrice(self, y):
        print(y)
        globals()[f"self.costEntry{y}"].config(state = 'normal')
        price = int(globals()[f"self.bookPrice{y}"]) * int(globals()[f"self.quantEntry{y}"].get())
        globals()[f"self.costEntry{y}"].insert(0, price)
        globals()[f"self.costEntry{y}"].config(state = 'readonly')

        
if __name__ == '__main__':
    obj=EmpBill()
    obj.billing()