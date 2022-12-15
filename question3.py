import pandas
import sqlite3
import pandas as pd

con = sqlite3.connect("PIWorks.db")
cursor=con.cursor()

#Table1
cursor.execute("CREATE TABLE IF NOT EXISTS salary (Employee_ID INT,First_Name TEXT,Last_Name TEXT,City TEXT,State TEXT)")
con.commit()
cursor.execute("Insert into salary Values(10330,'John','John','NY','NY'),(10449,'Sarah','Lebat','Melbourne','Bourke'),(11012,'Jon','Dallas','NY','NY'),(11013,'Gheorghe','Honey','NY','NY'),(11014,'Anton','Savar','NY','NY')")
con.commit()

columns_employee=["Employee ID","FirstName","LastName","City","State"]
employee_table=pd.DataFrame(columns=columns_employee)

cursor.execute("Select * From salary")
liste1=cursor.fetchall()
employee_table=pd.DataFrame(liste1, columns=columns_employee)

#Table2
cursor.execute("CREATE TABLE IF NOT EXISTS tablo (Employee_ID INT,Salary_Date INT,Month_ID INT,Value INT)")
con.commit()   
cursor.execute("Insert into tablo Values(10330,'June',6,128),(10330,'July',7,158),(10330,'August',8,133),(10330,'September',9,120),(10330,'October',10,188),(10330,'November',11,160),(10330,'December',12,105),(10449,'September',9,150),(10449,'October',10,158),(10449,'November',11,160),(10449,'December',12,180)")
con.commit()

cursor.execute("Select * From tablo")
liste2=cursor.fetchall()

columns_payments=["Employee ID", "Salary Date", "Month ID", "Value"]
payments_table=pd.DataFrame(columns=columns_payments)
payments_table=pd.DataFrame(liste2, columns=columns_payments)


#Query any employee's salary information.       
def search_employee_salary(): 
    name=input("Name: ")
    lastname=input("Last Name: ")
    eid=""
    for i in employee_table.index:
        if employee_table.iloc[i,1]==name:
            if employee_table.iloc[i,2]==lastname:
                eid=employee_table.iloc[i,0]
    if eid=="":
        print("There is no one with this name.")
    else:
        value=0
        for j in payments_table.index:
            if payments_table.iloc[j,0]==eid:
                value=value + payments_table.iloc[j,3]
        if value==0:
            print("There is no information about the salary.")
        else:
            print("Salary of employee=",value)        

#Employees with the initial J.
def j_letter_employees():
    emp_list=[]
    for i in employee_table.index:
        if employee_table.iloc[i,1][0]=="J":
            emp_list.append(employee_table.iloc[i,1]+" "+employee_table.iloc[i,2])
    if emp_list==[]:
        print("There is no one with this initial.")
    else:
        print(emp_list)

#Employee list by initials.
def first_letter(firstletter):
    emp_list=[]
    for i in employee_table.index:
        if employee_table.iloc[i,1][0]==firstletter:
            emp_list.append(employee_table.iloc[i,1]+" "+employee_table.iloc[i,2])
    if emp_list==[]:
        print("There is no one with this initial.")
    else:
        print(emp_list)
