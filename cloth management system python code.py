import mysql.connector as sql
import pandas as pd
mydb=sql.connect(host='localhost',password='root',user='root',database='cloth',auth_plugin="mysql_native_password")
cursor=mydb.cursor()
def registercust():
    while True: 
             print("*"*70)
             print("Enter 1- Insert customer details")
             print("Enter 2- Show customer details")
             print("Enter 3- Deletion of customer record")
             print("Enter 4- Update customer details")
             print("Enter 5- To see all records")
             print("Enter 6- Return to main menu")
             print("*"*70) 
             y=int(input("enter your choice: "))
             if y==1:
                 l=[]
                 print("*"*70) 
                 custid=input("Enter customer id no: ")
                 l.append(custid)
                 date=input("Enter date: ")
                 l.append(date)
                 custname=input("Enter name: ")
                 l.append(custname)
                 add=input("Enter address: ")
                 l.append(add)
                 phno=input("Enter phone no.: ")
                 l.append(phno)
                 amt=input("Enter bill amount: ")
                 l.append(amt)
                 print("Record has been saved in customer table!!!")
                 cust=(l)
                 sql="insert into customer(idno,date,cust_name,address,phno,amount) values(%s,%s,%s,%s,%s,%s);" 
                 cursor.execute(sql,cust)
                 mydb.commit()
             elif y==2:
                
                print("*"*70) 
                cid=input("Enter customer id: ") 
                qry="select * from customer where idno='%s'"%(cid)
                df=pd.read_sql(qry,mydb)
                print(df)
             elif y==3:
                print("*"*70) 
                cid=input("enter customer id: ") 
                sql="delete from customer where idno='%s'"%(cid)
                cursor.execute(sql) 
                print("Data deleted successfully!!!")
             elif y==4:
                 print("*"*70)
                 cid=input("enter customer id: ")
                 nm=input("enter correct name : ")
                 a=input("enter correct address: ")
                 p=input("enter correct phno: ")
                 amu=input("enter correct amount: ")
                 sql="update customer set cust_name='%s',address='%s',phno='%s' ,amount='%s' where idno='%s'"%(nm,a,p,amu,cid)
                 cursor.execute(sql) 
                 print("Data updated successfully!!!!")
             elif y==5: 
                 print("*"*70)
                 qry="select * from customer;" 
                 df=pd.read_sql(qry,mydb)
                 print(df)
             elif y==6:
                return
             else:
                 print("invalid choice please try again...")
def types():
    print("*"*70)
    qry="select * from types;" 

    df=pd.read_sql(qry,mydb)
    print(df)
    print("*"*70)   

def rate():
    print("*"*50)
    total = 0
    prices = {"mens kurta": 900, 
              "womens kurta": 1200, 
              "mens shirt": 600, 
              "t-shirt": 300, 
              "top": 200, 
              "mens jeans": 700, 
              "womens jeans": 1000}
    custid=input("enter customer id:")
    noofitems = int(input("Enter total Number of items:"))
    if (noofitems < 51):
        listofitems = {}
        for x in range(noofitems):
            print("Item", end=" ")
            print(x+1)
            item = str(input("Enter item name: "))
            priceofitem = prices.get(item)
            quantity = int(input("Enter quantity:"))
            total = total + (priceofitem * quantity)
        print("Total bill amount:- ", end="")
        print(total)
        sql="update customer set amount='%s' where idno='%s'"%(total,custid)
        cursor.execute(sql)
        print("*"*50)
        return None 

                  


print('='*70) 
print("##@@@WELCOME TO HARSHAL CLOTH COLLECTION @@@##")    
print('='*70)     
while True: 
 print("1:Enter customer data ") 
 print("2:View clothes")
 print("3:Calculating bill ")
 print("4:Exit ")         
 print("*"*70)           
 userinput=int(input("Please select an above option:"))
 if(userinput==1):
    registercust()
 elif(userinput==2):
    types()
 elif(userinput==3):
    rate()
 elif(userinput==4):
    print("THANKS!!! FOR VISITING...")
    quit()
 else:
    print("Enter correct choice!!!!")
