
from tkinter import *
from tkinter import messagebox , messagebox
from tkinter.ttk import Treeview
import mysql.connector
import database
import edit_categories
class viewcategory():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('CATEGORIES DETAILS')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-800)/2 )
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def category(self):
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I'), selectmode="extended")

        self.tr.heading('#0',text="ID")
        self.tr.column('#0',minwidth=0,width=125,stretch=NO)

        self.tr.heading('#1',text="CATEGORIES")
        self.tr.column('#1',minwidth=0,width=460 ,stretch=NO)

        self.tr.heading('#2', text="Edit")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Delete")
        self.tr.column('#3', minwidth=0, width=80, stretch=NO)


        self.tr.place(x=0,y=0,width="800",height="500")
        
        j = 0
        print("manage",database.allCategories)
        for i in database.allCategories():
            self.tr.insert('', 0, text=i[0], values=(i[1],'Edit','Delete'))          
        
      
        self.tr.bind('<Double-Button-1>', self.actions)
        res = database.allCategories()
  


        self.root.mainloop()
        
    def actions(self,e):
        #get the values of the selected row
        tt=self.tr.focus()

        #get the column Id
        col= self.tr.identify_column(e.x)
        print(col)
        print(self.tr.item(tt))

        id=(
            self.tr.item(tt).get('text'),
        )

        print(id, col)
        if col == '#3':
            a = messagebox.askyesno('Alert', 'Do you really want to delete it?')
            if a:
                res = database.deletebook(id)
                if res:
                    messagebox.showinfo('Success', 'student deleted successfully.')
                    self.root.destroy()
                    obj = viewcategory()
                    obj.category()                    
                else:
                    messagebox.showerror('Alert', 'Somethng went wrong.')

        if col == '#2':
            obj= edit_categories.page(id)


if __name__ == '__main__':
    obj = viewcategory()
    obj.category()