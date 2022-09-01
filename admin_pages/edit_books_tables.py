
from tkinter import *
from tkinter.ttk import Treeview
# from .database import editbook
import edit_books_tables
import database
import book_tables
from tkinter import messagebox
import book_edit
class EditBooksTables():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('BOOKS DETAILS')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2 )
        self.height=int((self.fullheight-500)/2)

        s = "1000x500+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def EditBOOKS(self):
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="1000", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I'), selectmode="extended")

        self.tr.heading('#0',text="ID")
        self.tr.column('#0',minwidth=0,width=25,stretch=NO)

        self.tr.heading('#1',text="BOOK NAME")
        self.tr.column('#1',minwidth=0,width=200 ,stretch=NO)

        self.tr.heading('#3', text="AUTHOR")
        self.tr.column('#3', minwidth=0, width=170, stretch=NO)
        
        self.tr.heading('#2', text="CATEGORY")
        self.tr.column('#2', minwidth=0, width=170, stretch=NO)

        self.tr.heading('#4', text="PRICE")
        self.tr.column('#4', minwidth=0, width=90, stretch=NO)
        
        self.tr.heading('#6', text="STOCK")
        self.tr.column('#6', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#5', text="RACKNO./COLUMN")
        self.tr.column('#5', minwidth=0, width=130, stretch=NO)
        
        self.tr.heading('#7', text="Edit")
        self.tr.column('#7', minwidth=0, width=60, stretch=NO)

        self.tr.heading('#8', text="Delete")
        self.tr.column('#8', minwidth=0, width=60, stretch=NO)
        self.tr.place(x=0,y=0,width="1000",height="500")

    

        j = 0
        # print("manage",database.allBooks)
        for i in database.allBooks():
            self.tr.insert('', 0, text=i[0], values=(i[1],i[2],i[3],i[4],i[5],i[6],'Edit','Delete'))          

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
        if col == '#8':
            a = messagebox.askyesno('Alert', 'Do you really want to delete it?')
            if a:
                res = database.deletebook(id)
                if res:
                    messagebox.showinfo('Success', 'student deleted successfully.')
                    self.root.destroy()
                    obj = EditBooksTables()
                    obj.EditBOOKS()                    
                else:
                    messagebox.showerror('Alert', 'Somethng went wrong.')

        if col == '#7':
            obj= book_edit.page(id)



        

if __name__ == '__main__':
    obj = EditBooksTables()
    obj.EditBOOKS()