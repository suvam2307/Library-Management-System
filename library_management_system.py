from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
print("Hello world")




class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("LibraryMangementSystem")
        self.root.geometry("1550x800+0+0")
        
        self.member_var=StringVar()
        self.prn_no_var=StringVar()
        self.title_var=StringVar()
        self.first_name_var=StringVar()
        self.last_name_var=StringVar()
        self.mobile_var=StringVar()
        self.address_var=StringVar()
        self.book_var=StringVar()
        self.book_id_var=StringVar()
        self.book_title_var=StringVar()
        self.auther_var=StringVar()
        self.date_borrowed_var=StringVar()
        self.date_due_var=StringVar()
        self.days_on_book=StringVar()
        self.late_return_var=StringVar()
        self.date_over_due_var=StringVar()
        self.final_price_var=StringVar()
        
        
        lbtitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",border=20,relief=RIDGE,font=("times new roman",30,"bold"),padx=2,pady=4)
        lbtitle.pack(side=TOP,fill=X)
        
        frame1=Frame(self.root,border=12,bg="powder blue",relief=RIDGE,padx=20)
        frame1.place(x=0,y=90,width=1530,height=400)
        #***********************************Data frame left * **********************************************
        Datalabelleft=LabelFrame(frame1,text="Library Membership Information",bg="powder blue",fg="green",border=10,relief=RIDGE,font=("times new roman",10,"bold"))
        Datalabelleft.place(x=0,y=2,width=830,height=360)
        
        lblMember=Label(Datalabelleft,text="Member Type",bg="powder blue",font=("times new roamn",12,"bold"),padx=2,pady=6,)
        lblMember.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(Datalabelleft,font=("times new roamn",12,"bold"),width=27,state="readonly",textvariable=self.member_var)
        comMember["value"]=("Admin staf","Student","Lecture")
        comMember.grid(row=0,column=1)
        
        lblPRN=Label(Datalabelleft,text="PRN number",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblPRN.grid(row=1,column=0,sticky=W)
        textPRN=Entry(Datalabelleft,font=("arial",12,"bold"),width=32,textvariable=self.prn_no_var)
        textPRN.grid(row=1,column=1)
        
        lblTitle=Label(Datalabelleft,text="ID number",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblTitle.grid(row=2,column=0,sticky=W)
        textTitle=Entry(Datalabelleft,font=("arial",12,"bold"),width=32,textvariable=self.title_var)
        textTitle.grid(row=2,column=1)
        
        lblFirstName=Label(Datalabelleft,text="First Name",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblFirstName.grid(row=3,column=0,sticky=W)
        textFirstName=Entry(Datalabelleft,font=("arial",12,"bold"),width=32,textvariable=self.first_name_var)
        textFirstName.grid(row=3,column=1)
        
        lblLastName=Label(Datalabelleft,text="Last Name",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblLastName.grid(row=4,column=0,sticky=W)
        textLastName=Entry(Datalabelleft,font=("arial",12,"bold"),width=32,textvariable=self.last_name_var)
        textLastName.grid(row=4,column=1)
        
        lblAddress=Label(Datalabelleft,text="Adress",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=5,column=0,sticky=W)
        textAdress=Entry(Datalabelleft,font=("arial",12,"bold"),width=32,textvariable=self.address_var)
        textAdress.grid(row=5,column=1)
        
        lblMobile=Label(Datalabelleft,text="Mobile No",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=6,column=0,sticky=W)
        textMobile=Entry(Datalabelleft,font=("arial",12,"bold"),width=32,textvariable=self.mobile_var)
        textMobile.grid(row=6,column=1)
        
        lblBookId=Label(Datalabelleft,text="BookId",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookId.grid(row=7,column=0,sticky=W)
        textBookId=Entry(Datalabelleft,font=("arial",12,"bold"),width=32,textvariable=self.book_id_var)
        textBookId.grid(row=7,column=1)
        
        lblBookTitle=Label(Datalabelleft,text="Book Title",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblBookTitle.grid(row=8,column=0,sticky=W)
        textBookTitle=Entry(Datalabelleft,font=("arial",12,"bold"),width=32,textvariable=self.book_title_var)
        textBookTitle.grid(row=8,column=1)
        
        lblAuther=Label(Datalabelleft,text="Auther Name",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblAuther.grid(row=0,column=2,sticky=W)
        textAuther=Entry(Datalabelleft,font=("arial",12,"bold"),width=29,textvariable=self.auther_var)
        textAuther.grid(row=0,column=3)
        
        lblDateBorrowed=Label(Datalabelleft,text="Borrowed Date",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateBorrowed.grid(row=1,column=2,sticky=W)
        textDateBorrowed=Entry(Datalabelleft,font=("arial",12,"bold"),width=29,textvariable=self.date_borrowed_var)
        textDateBorrowed.grid(row=1,column=3)
        
        lblDateDue=Label(Datalabelleft,text="Due Date",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateDue.grid(row=2,column=2,sticky=W)
        texDateDue=Entry(Datalabelleft,font=("arial",12,"bold"),width=29,textvariable=self.date_due_var)
        texDateDue.grid(row=2,column=3)
        
        lblDaysOnBook=Label(Datalabelleft,text="Days On Book",bg="powder blue",font=('arial',12,"bold"),padx=2,pady=6)
        lblDaysOnBook.grid(row=3,column=2,sticky=W)
        textDaysOnBook=Entry(Datalabelleft,font=("arial",12,"bold"),width=29,textvariable=self.days_on_book)
        textDaysOnBook.grid(row=3,column=3)
        
        lblLateFine=Label(Datalabelleft,text="Late Return Fine",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblLateFine.grid(row=4,column=2,sticky=W)
        textLateFine=Entry(Datalabelleft,font=("arial",12,"bold"),width=29,textvariable=self.late_return_var)
        textLateFine.grid(row=4,column=3)
        
        lblDateOverDue=Label(Datalabelleft,text="Date Over Due",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblDateOverDue.grid(row=5,column=2,sticky=W)
        textDateOverDue=Entry(Datalabelleft,font=("arial",12,"bold"),width=29,textvariable=self.date_over_due_var)
        textDateOverDue.grid(row=5,column=3)
        
        lblActualPrice=Label(Datalabelleft,text="Actual Price",bg="powder blue",font=("arial",12,"bold"),padx=2,pady=6)
        lblActualPrice.grid(row=6,column=2,sticky=W)
        textActualPrice=Entry(Datalabelleft,font=("arial",12,"bold"),width=29,textvariable=self.final_price_var)
        textActualPrice.grid(row=6,column=3)
        
        #**************************************DataFrameRight********************************************************    
        Datalabelright=LabelFrame(frame1,text="Book Details",bg="powder blue",fg="green",border=10,relief=RIDGE,font=("times new roman",10,"bold"))
        Datalabelright.place(x=830,y=2,width=500,height=360)
        
        self.textBox=Text(Datalabelright,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.textBox.grid(row=0,column=2)
        #Creating the scrollbar
        listScroll=Scrollbar(Datalabelright)
        listScroll.grid(row=0,column=1,sticky="ns")
        book_List=["In Search of Lost Time","Ulysses","Don Quixote","The Great Gatsby","Moby Dick","War and Peace","Hamlet","The Odyssey","Lolita","Crime and Punishment","Nineteen Eighty Four",'Great Expectations',"The Grapes of Wrath","To Kill a Mockingbird","The Trial","The Red and the Black","Gulliver's Travels","Jane Eyre","The Aeneid"]
        def select_book(event=""):
            print("executing the select_book")
            indeces=listBox.curselection()
            index=indeces[0]
            print(index)
            selected_book=str(listBox.get(index))
            print(selected_book)
            if selected_book == "In Search of Lost Time":
                print("I am inside the if statement")
                self.book_id_var.set(123)
                self.book_title_var.set("Novel")
                self.auther_var.set("Marcel Proust")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Ulysses":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
                
            if selected_book == "Don Quixote":
                print("I am inside the if statement")
                self.book_id_var.set(125)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            
            if selected_book == "The Great Gatsby":
                print("I am inside the if statement")
                self.book_id_var.set(120)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Moby Dick":
                print("I am inside the if statement")
                self.book_id_var.set(127)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "War and Peace":
                print("I am inside the if statement")
                self.book_id_var.set(137)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Hamlet":
                print("I am inside the if statement")
                self.book_id_var.set(169)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "The Odyssey":
                print("I am inside the if statement")
                self.book_id_var.set(194)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Lolita":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Crime and Punishment":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Nineteen Eighty Four":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Great Expectations":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "The Grapes of Wrath":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "To Kill a Mockingbird":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Ulysses":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Ulysses":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Ulysses":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Ulysses":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            if selected_book == "Ulysses":
                print("I am inside the if statement")
                self.book_id_var.set(124)
                self.book_title_var.set("Novel")
                self.auther_var.set("James Joyce")
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=30) # To set the difference of due date as 1 month
                d3 = d1 + d2 # Finding the final due date 
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.days_on_book.set(30)
                self.late_return_var.set(50)
                self.date_over_due_var.set("No")
                self.final_price_var.set("Rs.589")
            
            
                

# Assuming you have defined the StringVar variables like this:
# self.book_id_var = StringVar()
# self.book_title_var = StringVar()
# self.auther_var = StringVar()
# self.date_borrowed_var = StringVar()
# self.date_due_var = StringVar()
# self.days_on_book = StringVar()
# self.late_return_var = StringVar()
# self.date_over_due_var = StringVar()
# self.final_price_var = StringVar()

        listBox = Listbox(Datalabelright, font=("arial", 12, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", select_book)
        listBox.grid(row=0, column=0, padx=4)
        listScroll.config(command=listBox.yview)

        for item in book_List:
            listBox.insert(END, item)

        
       
        
                
            
        
        # ************************************button frame *****************************************************
        ButtonFrame=Frame(self.root,border=12,bg="powder blue",relief=RIDGE,padx=5)
        ButtonFrame.place(x=0,y=480,width=1530,height=60)
        
        btnAddData=Button(ButtonFrame,bg="green",fg="white",font=("arial",12,"bold"),width=23,text="addData",command=self.add_data)
        btnAddData.grid(row=0,column=0)
        
        showData=Button(ButtonFrame,bg="green",fg="white",font=("arial",12,"bold"),width=23,text="showData",command=self.show_data)
        showData.grid(row=0,column=1)
        
        btnDeleteData=Button(ButtonFrame,bg="green",fg="white",font=("arial",12,"bold"),width=23,text="delete",command=self.delete)
        btnDeleteData.grid(row=0,column=2)
        
        
        
        btnUpdate=Button(ButtonFrame,bg="green",fg="white",font=("arial",12,"bold"),width=23,text="update",command=self.update)
        btnUpdate.grid(row=0,column=3)
        
        btnReset=Button(ButtonFrame,bg="green",fg="white",font=("arial",12,"bold"),width=23,text="Reset",command=self.reset)
        btnReset.grid(row=0,column=4)
        
        btnExit=Button(ButtonFrame,bg="green",fg="white",font=("arial",12,"bold"),width=23,text="Exit",command=self.isExit)
        btnExit.grid(row=0,column=5)
        
        
        
        
        # ***********************************information frame ************************************************
        InfoFrame=Frame(self.root,border=12,bg="powder blue",relief=RIDGE,padx=5)
        InfoFrame.place(x=0,y=530,width=1530,height=400)
        
        TableFrame=Frame(InfoFrame,border=5,bg="powder blue",relief=RIDGE,padx=3)
        TableFrame.place(x=0,y=2,width=1330,height=100)
        
        xscroll=ttk.Scrollbar(TableFrame,orient="horizontal")
        yscroll=ttk.Scrollbar(TableFrame,orient="vertical")
        
        self.library_table=ttk.Treeview(InfoFrame,columns=("membertype","prnno","title","firstName","lastName","address","mobile","bookid","booktitle","auther","dateborrowed","datedue","dues","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN No")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstName",text="firstName")
        self.library_table.heading("lastName",text="lastName")
        self.library_table.heading("address",text="Address")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book Id")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrow")
        self.library_table.heading("datedue",text="Due Date")
        self.library_table.heading("dues",text="Dues")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Dues")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill="both",expand=1)
        
        self.library_table.column("membertype",width=60)
        self.library_table.column("prnno",width=60)
        self.library_table.column("title",width=60)
        self.library_table.column("firstName",width=60)
        self.library_table.column("lastName",width=60)
        self.library_table.column("address",width=60)
        self.library_table.column("mobile",width=60)
        self.library_table.column("bookid",width=60)
        self.library_table.column("booktitle",width=60)
        self.library_table.column("dateborrowed",width=60)
        self.library_table.column("datedue",width=60)
        self.library_table.column("dues",width=60)
        self.library_table.column("latereturnfine",width=60)
        self.library_table.column("dateoverdue",width=60)
        self.library_table.column("finalprice",width=60)
        self.library_table.column('auther',width=50)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease>",self.get_cursor)
        
    def add_data(self):
        conn=mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="test"
        )
        my_cur=conn.cursor()
        query = "INSERT INTO test.library  VALUES (%s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(self.member_var.get(),
                self.prn_no_var.get(),
                self.title_var.get(),
                self.first_name_var.get(),
                self.last_name_var.get(),
                self.address_var.get(),
                self.mobile_var.get(),
                self.book_id_var.get(),
                self.book_title_var.get(),
                self.auther_var.get(),
                self.date_borrowed_var.get(),
                self.date_due_var.get(),
                self.days_on_book.get(),
                self.late_return_var.get(),
                self.date_over_due_var.get(),
                self.final_price_var.get()
                )
        my_cur.execute(query,values)
        conn.commit()
        print("Data inserted successfully")
        self.fetch_data()
        conn.close()
        messagebox.showinfo(title="success", message="The member is succesfully added")
        #Creating a message box after we succesfully add the insert  a row.
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="test")
        
        mycur=conn.cursor()
        mycur.execute("update library set membertype=%s,title=%s,firstName=%s,lastName=%s,address=%s,mobile=%s,bookid=%s,booktitle=%s,auther=%s,dateborrowed=%s,datedue=%s,dues=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where prnno=%s",
                      (self.member_var.get(),
                      self.title_var.get(),
                      self.first_name_var.get(),
                      self.last_name_var.get(),
                      self.address_var.get(),
                      self.mobile_var.get(),
                      self.book_id_var.get(),
                      self.book_title_var.get(),
                      self.auther_var.get(),
                      self.date_borrowed_var.get(),
                      self.date_due_var.get(),
                      self.days_on_book.get(),
                      self.late_return_var.get(),
                      self.date_over_due_var.get(),
                      self.final_price_var.get(),
                      self.prn_no_var.get())
                    )
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("sucess","Your data is sucessfuly updated")
        
        
    def fetch_data(self):
        conn=mysql.connector.connect(
            host="localhost",
            username="root",
            password="root",
            database="test"
        )
        
        my_cur=conn.cursor()
        my_cur.execute("select * from library")
        
        rows=my_cur.fetchall()
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children()) #To delete previous existing data fromm the table
            
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        print("Inside the get_cursor")
        cursor_row=self.library_table.focus()
        print(cursor_row)
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0]),
        self.prn_no_var.set(row[1]),
        self.title_var.set(row[2]),
        self.first_name_var.set(row[3]),
        self.last_name_var.set(row[4]),
        self.address_var.set(row[5]),
        self.mobile_var.set(row[6]),
        self.book_id_var.set(row[7]),
        self.book_title_var.set(row[8]),
        self.auther_var.set(row[9]),
        self.date_borrowed_var.set(row[10]),
        self.date_due_var.set(row[11]),
        self.days_on_book.set(row[12]),
        self.late_return_var.set(row[13]),
        self.date_over_due_var.set(row[14]),
        self.final_price_var.set(row[15])
        
    def show_data(self):
        self.textBox.insert(END,"Member Type \t\t"+self.member_var.get()+"\n")
        self.textBox.insert(END,"PRN NO \t\t"+self.prn_no_var.get()+"\n")
        self.textBox.insert(END,"ID No \t\t"+self.title_var.get()+"\n")
        self.textBox.insert(END,"First Name \t\t"+self.first_name_var.get()+"\n")
        self.textBox.insert(END,"Last Name \t\t"+self.last_name_var.get()+"\n")
        self.textBox.insert(END,"Adress \t\t"+self.address_var.get()+"\n")
        self.textBox.insert(END,"Mobile No \t\t"+self.address_var.get()+"\n")
        self.textBox.insert(END,"Book id \t\t"+self.book_id_var.get()+"\n")
        self.textBox.insert(END,"Book Title \t\t"+self.book_id_var.get()+"\n")
        self.textBox.insert(END,"Auther Name \t\t"+self.auther_var.get()+"\n")
        self.textBox.insert(END,"Date borrowed \t\t"+self.date_borrowed_var.get()+"\n")
        self.textBox.insert(END,"Date due \t\t"+self.date_due_var.get()+"\n")
        self.textBox.insert(END,"Days on book \t\t"+self.days_on_book.get()+"\n")
        self.textBox.insert(END,"late fine \t\t"+self.late_return_var.get()+"\n")
        self.textBox.insert(END,"due over date  \t\t"+self.date_over_due_var.get()+"\n")
        self.textBox.insert(END,"Final price\t\t"+self.final_price_var.get()+"\n")
       
       
    def reset(self):
        print("Inside the reset")        
        self.member_var.set(""),
        self.prn_no_var.set(""),
        self.title_var.set(""),
        self.first_name_var.set(""),
        self.last_name_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.book_id_var.set(""),
        self.book_title_var.set(""),
        self.auther_var.set(""),
        self.date_borrowed_var.set(""),
        self.date_due_var.set(""),
        self.days_on_book.set(""),
        self.late_return_var.set(""),
        self.date_over_due_var.set(""),
        self.final_price_var.set("")
        
        
    def isExit(self):
        iexit=messagebox.askyesno("Library management system","Do you want to exit?")
        
        if iexit>0:
            self.root.destroy()
        return
    
    def delete(self):
        if self.prn_no_var=="" or self.title_var=="":
            messagebox.showerror("Error","choose  a  vald human")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="test")
            my_cur=conn.cursor()
            query="delete from library where prnno=%s"
            value=(self.prn_no_var.get(),)
            my_cur.execute(query,value)
            conn.commit()
            self.fetch_data()
            self.fetch_data()
            self.reset()
            my_cur.close()
            messagebox.showinfo("dELETE","The member is sucessfully deleted")
    
            
        
        

if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
