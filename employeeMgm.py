from os import system
import re
# import mysql connector
import mysql.connector

# making mysql db connections
con = mysql.connector.connect(
    host = " localhost ",
    user = "aa",
    password = "Qwerty@123",
    database = " employee "
)
mycursor = con.cursor() #allows row-by-row processing of the result sets
mycursor.execute('''CREATE TABLE IF NOT EXISTS empdata (
                            Id INT(11) PRIMARY KEY,
                            Name VARCHAR(1800),
                            Email_Id TEXT(1800),
                            Phone_no BIGINT(11),
                            Address TEXT(1000),
                            Post TEXT(1000),
                            Salary BIGINT(20))''')


# make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
# for validating Phone number
Pattern = re.compile("(0|91)?[7-9][0-9]{9}")

# Function to Add_Employee
def Add_Employ():
    print("{:>60}".format("-->> Add Employee Record <<--\n"))
    Id = input("Enter Employee Id:")
    # checking if Employee Id is Exist or # NOTE:
    if (check_employee(Id) == True):
        print("Employee ID Already Exists\sTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Name = input("Enter Employee Name: ")
    # checking if Employee Name is Exist or Not
    if (check_employee_name(Name) == True):
        print("Employee Name Already Exists\nTry Again..")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Email_Id = input("Enter Employee Email ID: ")
    if (re.fullmatch(regex, Email_Id)):
        print("Valid Email")
    else:
        print("Invalid Email")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Phone_no = input("Enter Employee Phone No.: ")
    if (Pattern.match(Phone_no)):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")
        press = input("Press Any Key To Continue..")
        Add_Employ()
    Address = input("Enter Employee Address: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")
    data = (Id, Name, Email_Id, Phone_no, Address, Post, Salary)
    # Inserting Employee Details in
    # the Employee (empdata) Table
    sql = 'INSERT INTO empdata VALUES(%s,%s,%s,%s,%s,%s,%s)'
    c = con.cursor()

    # Executing the sql Query
    c.execute(sql, data)

    # Commit() method to make changes in the table
    con.commit()
    print("Successfully Added Employee Record")
    press = input("Press Any Key To Continue..")
    menu()


# Function To Check if Employee With
# given Name Exists or not
def check_employee_name(employee_name):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'SELECT * FROM empdata WHERE Name=%s'

    # making the cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_name,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


# Function To Check if Employee With
# given Id Exists or not
def check_employee(employee_id):
    # query to select all Rows from
    # employee(empdata) table
    sql = 'SELECT * FROM empdata WHERE Id=%s'

    # making the cursor buffered to make
    # rowcount method work properly
    c = con.cursor(buffered=True)
    data = (employee_id,)

    # Execute the sql query
    c.execute(sql, data)

    # rowcount method to find number
    # of rows with given values
    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


def Display_Employ():
    print("{:>60}".format("--> Display Employee Record <--\n"))
    # query to select all rows from the Employee (empdata) table
    sql = 'SELECT * FROM empdata'
    c = con.cursor()

    # Executing the sql query
    c.execute(sql)

    # Fetching all details of all the Employees
    r = c.fetchall()
    for i in r:
        print("Employee Id: ", i[0])
        print("Employee Name: ", i[1])
        print("Empoyee Email Id: ", i[2])
        print("Employee Phone No.: ", i[3])
        print("Employee Address: ", i[4])
        print("Employee Post: ", i[5])
        print("Employee Salary: ", i[6])
        print("\n")
    press = input("Press Any Key To Continue..")
    menu()


def Update_Employ():
    print("{:>60}".format("--> Update Employee Record <<--\n"))
    Id = input("Enter Employee ID: ")
    # checking if Employee Id is Exist or Not
    if (check_employee(Id) == False):
        print("Employee Record Not Exist\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Email_Id = input("Enter Employee Email ID: ")
        if (re.fullmatch(regex, Email_Id)):
            print("Valid Email")
        else:
            print("Invalid Email")
            press = input("Press Any Key To Continue..")
            Update_Employ()
        Phone_no = input("Enter Employee Phone No.: ")
        if (Pattern.match(Phone_no)):
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number")
            press = input("Press Any Key To Continue..")
            Update_Employ()
        Address = input("Enter Employee Address: ")
        # Updating Employee details in empdata table
        sql = 'UPDATE empdata SET Email_Id = %s, Phone_no = %s, Address = %s WHERE Id = %s'
        data = (Email_Id, Phone_no, Address, Id)
        c = con.cursor()

        # Executing the sql query
        c.execute(sql, data)

        # commit() method to make changes in the table
        con.commit()
        print("Updated Employee Record")
        press = input("Press Any Key To Continue..")
        menu()


# Function to Promote Employee
def Promote_Employ():
    print("{:>60}".format("--> Promote Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking if Employee Id is Exist or Not
    if (check_employee(Id) == False):
        print("Employee Record Not exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        Amount = int(input("Enter Increase Salary: "))
        # query to fetch salary of Employee with given data
        sql = 'SELECT Salary FROM empdata WHERE Id=%s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        # fetching salary of Employee with given Id
        r = c.fetchone()
        t = r[0]+Amount

        #query to update salary of Employee with given Id
        sql = 'UPDATE empdata SET Salary = %s WHERE Id = %s'
        d = (t, Id)

        # executing the sql query
        c.execute(sql, d)

        # commit() method to make changes in the table
        con.commit()
        print("Employee Promoted")
        press = input("Press Any Key To Continue..")
        menu()


# Function to Remove Employee
def Remove_Employ():
    print("{:>60}".format("--> Remove Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking if Employee Id is Exist or Not
    if (check_employee(Id) == False):
        print("Employee Record Not Exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        # query to delete Employee from empdata table
        sql = 'DELETE FROM empdata where Id = %s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        # commit() method to make changes in the empdata table
        con.commit()
        print("Employee Removed")
        press = input("Press Any Key To Continue..")
        menu()


# Function to Search Employee
def Search_Employ():
    print("{:>60}".format("-->> Search Employee Record <<--\n"))
    Id = input("Enter Employee Id: ")
    # checking if Employee Id is Exist or Not
    if (check_employee(Id) == False):
        print("Employee Record Not Exists\nTry Again")
        press = input("Press Any Key To Continue..")
        menu()
    else:
        # query to search Employee from empdata table
        sql = 'SELECT * FROM empdata WHERE Id = %s'
        data = (Id,)
        c = con.cursor()

        # executing the sql query
        c.execute(sql, data)

        # fetching all details of all the employee
        r = c.fetchall()
        for i in r:
            print("Employee Id: ", i[0])
            print("Employee Name: ", i[1])
            print("Employee Email Id: ", i[2])
            print("Employee Phone No.: ", i[3])
            print("Employee Address: ", i[4])
            print("Employee Post: ", i[5])
            print("Employee Salary: ", i[6])
            print("\n")
        press = input("Press Any Key To Continue..")
        menu()


# Menu function to display the menu
def menu():
    system("cls")
    print("{:>60}".format("************************************"))
    print("{:>60}".format("-->> Employee Management System <<--"))
    print("{:>60}".format("************************************"))
    print("1. Add Employee")
    print("2. Display Employee Record")
    print("3. Update Employee Record")
    print("4. Promote Employee Record")
    print("5. Remove Employee Record")
    print("6. Search Employee Record")
    print("7. Exit\n")
    print("{:>60}".format("-->> Choice Options: [1/2/3/4/5/6/7] <<--"))

    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        system("cls")
        Add_Employ()
    elif ch == 2:
        system("cls")
        Display_Employ()
    elif ch == 3:
        system("cls")
        Update_Employ()
    elif ch == 4:
        system("cls")
        Promote_Employ()
    elif ch == 5:
        system("cls")
        Remove_Employ()
    elif ch == 6:
        system("cls")
        Search_Employ()
    elif ch == 7:
        system("cls")
        print("{:>60}".format("Have A Nice Day: "))
        exit(0)
    else:
        print("Invalid Choice!")
        press = input("Press Any Key To Continue..")
        menu()


# Calling the menu function
menu()
