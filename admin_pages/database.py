# pip install mysql
# pip install mysql.connector

from datetime import date
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="book_shop"    
)

cursor = con.cursor()


def editCat(data):
    try:
        cursor.execute('UPDATE categories SET Categories = %s WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False

def getEarnings():
    try:
        cursor.execute('SELECT SUM(totalCost) FROM orders')
        return cursor.fetchall()[0][0]
    except:
        return 0

def totalRacks():
    try:
        cursor.execute('SELECT * FROM addracks')
        return cursor.fetchall()
    except:
        return []

def totalBooks():
    try:
        cursor.execute('SELECT * FROM addbooks')
        return cursor.fetchall()
    except:
        return []

def totalEmp():
    try:
        cursor.execute('SELECT * FROM addemployee')
        return cursor.fetchall()
    except:
        return []

def adminLogin(data):
    
    # print(data)
    try:
        cursor.execute('SELECT * FROM adminlogin WHERE username = %s and password = %s', data)
        return cursor.fetchall()
    except:
        return False
    
def employeeLogin(data):
    
    # print(data)
    try:
        cursor.execute('SELECT * FROM addemployee WHERE username = %s and password = %s', data)
        return cursor.fetchone()
    except:
        return False
        

def AddEmployee(data):
    try:
        cursor.execute('INSERT INTO addemployee (Name,Email,PhoneNo,UserName,Password) VALUES(%s,%s,%s,%s,%s)', data)
        con.commit()
        return True
    except:
        return False
    
def AddCategory(data):
    try:
        cursor.execute('INSERT INTO categories (Categories) VALUES(%s)', data)
        con.commit()
        return True
    except:
        return False

def AddBooks(data):
    try:
        cursor.execute('INSERT INTO addbooks (BookName,BookCategory,BookAuthor,BookPrice,RackNoColumn,Stock) VALUES(%s,%s,%s,%s,%s,%s)', data)
        con.commit()
        return True
    except:
        return False
    
def AddRacks(data):
    try:
        cursor.execute('INSERT INTO addracks (RackName,NoOfRows,TotalCapacity,CapacityPerRow) VALUES(%s,%s,%s,%s)', data)
        con.commit()
        return True
    except:
        return False

def Addorders(data):
    try:
        cursor.execute('INSERT INTO orderid (CustomerName,CustomerPhoneNo,BookName,BookAuthor,price,Stock) VALUES(%s,%s,%s,%s,%s,%s)', data)
        con.commit()
        return True
    except:
        return False

def allEmployees():
    try:
        cursor.execute('SELECT * FROM addemployee')
        return cursor.fetchall()
    except:
        return False

def allCategories():
    try:
        cursor.execute('SELECT * FROM categories')
        return cursor.fetchall()
    except:
        return False
    
def allracks():
    try:
        cursor.execute('SELECT * FROM addracks')
        return cursor.fetchall()
    except:
        return False
    
    
def allorders():
    try:
        cursor.execute('SELECT * FROM orders')
        return cursor.fetchall()
    except:
        return False
    
    
def allBooks():
    # cursor.execute('SELECT * FROM addbooks')
    
    try:
        cursor.execute('SELECT addbooks.id, addbooks.BookName, categories.Categories, addbooks.BookAuthor, addbooks.BookPrice, addracks.RackName, addbooks.Stock FROM addbooks LEFT JOIN categories ON addbooks.BookCategory = categories.id LEFT JOIN addracks ON addbooks.RackNoColumn = addracks.id')
        return cursor.fetchall()
    except:
        return False
    
    
    
    
def editbook(data):
    try:
        cursor.execute('UPDATE addbooks SET BookName = %s, BookCategory = %s, BookAuthor = %s , BookPrice =%s,RackNoColumn=%s, 	Stock=%s  WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False
    
    
    
def editOrder(data):
    try:
        cursor.execute('UPDATE orderid SET CustomerName = %s, CustomerPhoneNo = %s, BookName = %s , 	BookAuthor =%s,	price=%s,Stock=%s  WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False
    
    
def editEmployee(data):
    try:
        cursor.execute('UPDATE addemployee SET Name = %s, 	Email = %s, PhoneNo = %s , UserName =%s,Password=%s   WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False
    
    
def editrack(data):
    try:
        cursor.execute('UPDATE addracks SET RackName = %s, 	NoOfRows = %s, TotalCapacity = %s , CapacityPerRow	 =%s  WHERE id = %s', data)
        con.commit()
        return True
    except:
        return False
    
    
    
    
# def deletebook(id):
#     try:
#         cursor.execute('DELETE FROM students WHERE id = %s', id)
#         con.commit()
#         return True
#     except:
#         return False
    
def deleteemployee(id):
    try:
        cursor.execute('DELETE FROM addemployee WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False
    
    
def deleteOrder(id):
    try:
        cursor.execute('DELETE FROM orderid WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False
    
    
def deletebook(id):
    # cursor.execute('DELETE FROM addbook WHERE id = %s', id)
    
    try:
        cursor.execute('DELETE FROM addbooks WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False
    
def deleterack(id):
    # cursor.execute('DELETE FROM addbook WHERE id = %s', id)
    
    try:
        cursor.execute('DELETE FROM addracks WHERE id = %s', id)
        con.commit()
        return True
    except:
        return False

def singleCategory(id):
    try:
        cursor.execute('SELECT * FROM categories WHERE id = %s', id)
        return cursor.fetchone()
    except:
        return False
    
def singlebook(id):
    print(id)
    # cursor.execute('SELECT * FROM addbooks WHERE id = %s', id)
    try:
        cursor.execute('SELECT * FROM addbooks WHERE id = %s', id)
        return cursor.fetchone()
    except:
        return False
    
    
def singleOrder(id):
    print(id)
    # cursor.execute('SELECT * FROM addbooks WHERE id = %s', id)
    try:
        cursor.execute('SELECT * FROM orderid WHERE id = %s', id)
        return cursor.fetchone()
    except:
        return False
    
def singleEmployee(id):
    print(id)
    # cursor.execute('SELECT * FROM addbooks WHERE id = %s', id)
    try:
        cursor.execute('SELECT * FROM addemployee WHERE id = %s', id)
        return cursor.fetchone()
    except:
        return False
    
def singleRack(id):
    print(id)
    # cursor.execute('SELECT * FROM addbooks WHERE id = %s', id)
    try:
        cursor.execute('SELECT * FROM addracks WHERE id = %s', id)
        return cursor.fetchone()
    except:
        return False
    
def singlerack():
    try:
        cursor.execute('SELECT id,RackName FROM addracks')
        return cursor.fetchall()
    except:
        return False
def order():
    try:
        cursor.execute('SELECT BookName FROM addbooks')
        return cursor.fetchall()
    except:
        return False


def getCatBook(catId):
    try:
        cursor.execute('SELECT id, BookName FROM addbooks WHERE BookCategory = %s', (catId, ))
        return cursor.fetchall()
    except:
        return False

def getBookPrices(bookId):
    try:
        cursor.execute('SELECT BookPrice FROM addbooks WHERE id = %s', (bookId, ))
        return cursor.fetchone()
    except:
        return False


def createOrder(data):
    try:
        cursor.execute('INSERT INTO orders (customerName, customerPhone, totalCost, addedBy) VALUES (%s, %s, %s, %s)', data)
        con.commit()
        return cursor.lastrowid
    except:
        return False

def createOrderDetails(data):
    try:
        cursor.execute('INSERT INTO orderdetails (orderId, bookId, quantity) VALUES (%s, %s, %s)', data)
        con.commit()
        return True
    except:
        return False


def allOrders():
    try:
        cursor.execute('SELECT * FROM orders')
        return cursor.fetchall()

    except:
        return False

def orderDetail(orderId):
    print(orderId)
    try:
        cursor.execute('SELECT orderdetails.id, addbooks.BookName, addbooks.BookPrice, orderdetails.quantity FROM orderdetails LEFT JOIN addbooks ON orderdetails.bookId = addbooks.id WHERE orderdetails.orderId = %s', orderId)
        return cursor.fetchall()
    except:
        return False