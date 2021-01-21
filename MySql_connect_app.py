from  tkinter import *
from tkinter import ttk
import  tkinter as tk
from tkinter import messagebox
import pymysql.cursors
import random

class MemmberConnect:


    def __init__(self,root):
        self.root = root
        blank_space = ""  #this varibale is used posistion

        self.root.title =(202*blank_space+"MySQ; Connector")
        self.root.geometry("1360x700+0+0")
        self.scroll_y=ttk.Scrollbar(self.root)




        self.MemID =StringVar()
        self.FistName =StringVar()
        self.Surname =StringVar()
        self.Address =StringVar()
        self.POBOX =StringVar
        self.Gender=StringVar()
        self.Mtype =StringVar()
        self.Mobile=StringVar()
        self.Email = StringVar()
        self.Search = StringVar()
        self.MemIDBar=StringVar()
        #===============================================================================================

        MainFrame = tk.Frame(self.root,bd=10,width=1350,height=700,relief=RIDGE,bg="cadetblue")
        MainFrame.grid()

        TitleFrames = tk.Frame(MainFrame,bd=7,width=1320,height=100,bg="cadetblue",relief=RIDGE)
        TitleFrames.grid(row=0,column=0)

        TitleFrame = tk.Frame(TitleFrames, bd=7, width=1320, height=100, bg="cadetblue", relief=RIDGE)
        TitleFrame.grid(row=0, column=0)

        ButtonFrame = tk.Frame(MainFrame,bd=7,width=1340,height=50,bg="cadetblue",relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)

        SearchFrame = tk.Frame(MainFrame, bd=5, width=1340, height=50, relief=RIDGE)
        SearchFrame.grid(row=2, column=0)

        MidFrame = tk.Frame(MainFrame, bd=5, width=1340, height=500, relief=RIDGE)
        MidFrame.grid(row=3, column=0)

        LeftFrame = tk.Frame(MidFrame, bd=5, width=1340, height=400,padx=2,  relief=RIDGE)
        LeftFrame.pack(side=LEFT,padx=5,pady=0)

        InnerLeftFrame = tk.Frame(LeftFrame, bd=5, width=1340, height=180, padx=4,pady=4, relief=RIDGE)
        InnerLeftFrame.pack(side=TOP, padx=10, pady=0)

        #===============================================================================================
        self.lblTitle =tk.Label(TitleFrames,font=("Arial",40,"bold"),text="MySql Connection",bd=7,bg="cadetblue")
        self.lblTitle.grid(row=0,column=0,padx=422)
        #==========================================================================================================

        #MemID StringVar
        self.lblmemberID = tk.Label(InnerLeftFrame, font=("Arial", 12, "bold"), text="Member ID", bd=7, anchor="w",
                                 justify=LEFT)
        self.lblmemberID.grid(row=0, column=0,sticky=W,padx=5)

        self.txtmemberID = tk.Entry(InnerLeftFrame,font=("Arial",12,"bold"),bd=5,width=35,justify="left",
                                 textvariable=self.MemID)
        self.txtmemberID.grid(row=0,column=1)


        #FirstName StringVar
        self.lblFirstName = tk.Label(InnerLeftFrame,font=("Arial",12,"bold"),text="FirstName",bd=7,anchor="w",
                                  justify="left")
        self.lblFirstName.grid(row=1,column=0,sticky=W,padx=5)
        self.txtFirstName  =Entry(InnerLeftFrame,font=("Arial",12,"bold"),bd=5,width=35,justify="left",
                                  textvariable=self.FistName)
        self.txtFirstName.grid(row=1,column=1)

        #Surname   StringVar
        self.lblSurname = tk.Label(InnerLeftFrame,font=("Arial", 12, "bold"),text="Surname",bd=7,justify=LEFT)
        self.lblSurname.grid(row=2,column=0,sticky=W,padx=5)
        self.txtsurname = tk.Entry(InnerLeftFrame,font=("Arial", 12, "bold"),bd=5,width=35,justify="left",
                                textvariable=self.Surname)
        self.txtsurname.grid(row=2,column=1)


        #Adress
        self.lblAddress = tk.Label(InnerLeftFrame, font=("Arial", 12, "bold"), text="Address", bd=7, justify=LEFT)
        self.lblAddress.grid(row=0, column=2)
        self.txtAddress = Entry(InnerLeftFrame, font=("Arial", 12, "bold"), bd=5, width=35, justify="left",
                                textvariable=self.Address)
        self.txtAddress.grid(row=0, column=3)

        # POBOX StringVar
        self.lblPoBox = tk.Label(InnerLeftFrame, font=("Arial", 12, "bold"), text="PO Box", bd=7)
        self.lblPoBox.grid(row=0, column=4, sticky=W, padx=5)
        self.txtPOBox = tk,Entry(InnerLeftFrame, font=("Arial", 12, "bold"), bd=5, width=35, justify="left",
                              textvariable=self.POBOX)
        self.txtPOBox.grid(row=0, column=5)


        #Gender StringVar
        self.lblGender = tk.Label(InnerLeftFrame, font=("Arial", 12, "bold"), text="Gender", bd=5)
        self.lblGender.grid(row=1, column=2,sticky=W,padx=5)
        self.cboGender = ttk.Combobox(InnerLeftFrame, font=("Arial", 12, "bold"),  width=33, state="readonly",
                                      textvariable=self.Gender)
        self.cboGender["values"] = ("","Female","Male")
        self.cboGender.current(0)
        self.cboGender.grid(row=1, column=3)




        #Email StringVar
        self.lblEmail= tk.Label(InnerLeftFrame, font=("Arial", 12, "bold"), text="Email", bd=7)
        self.lblEmail.grid(row=1, column=4,sticky=W,padx=5)
        self.txtemail= tk.Entry(InnerLeftFrame, font=("Arial", 12, "bold"), bd=5, width=35, justify="left",
                                textvariable=self.Email)
        self.txtemail.grid(row=1, column=5)

        #Mobile StringVar
        self.lblMobile = tk.Label(InnerLeftFrame, font=("Arial", 12, "bold"), text="Mobile", bd=7)
        self.lblMobile.grid(row=2, column=2,sticky=W,padx=5)
        self.txtMobile = tk.Entry(InnerLeftFrame, font=("Arial", 12, "bold"), bd=5, width=35, justify="left",
                                textvariable=self.Mobile)
        self.txtMobile.grid(row=2, column=3,sticky=W)




        self.lblAddress = tk.Label(InnerLeftFrame,font=("Arial", 12, "bold"),text="Type",bd=7)
        self.lblAddress.grid(row=2,column=4,sticky=W,padx=5)
        # Type StringVar
        self.cboType = ttk.Combobox(InnerLeftFrame, width=33,font=("Arial", 12, "bold"),state="readonly",
                                    textvariable=self.Mtype)
        self.cboType["values"] = ("User Category","Employee Category","Visitor Category")
        self.cboType.current(0)
        self.cboType.grid(row=2, column=5)



    #============================================================FUNCTION for the buttons===================================

        def addNew(self):

            if self.MemID.get() != "" and txtFirstName.get() != "" and self.Surname.get() != "":
                pass
            else:
                tk.messagebox.showerror("Error,Check Input", "Enter correct members details")
                sqlCon = pymysql.connect(host="localhost",
                                                 user="root",
                                                 password="",
                                                 database="members",
                                                 cursorclass=pymysql.cursors.DictCursor)
                cursors = sqlCon.cursor()
                a=self.MemID.get(),
                b=self.FistName.get(),
                c=self.Surname.get(),
                d=self.Address.get(),
                e=self.POBOX.get(self),
                f=self.Gender.get(),
                g=self.Mtype.get(),
                h=self.Mobile.get(),
                i=self.Email.get(),
                j=Search.get(),
                k=self.MemIDBar.get()

                cursors.execute("INSERT INTO members values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", [
                    a,
                    b,
                    c,
                    d,
                    e,
                    f,
                    g,
                    h,
                    i,
                    j,
                    k


                ])

                sqlCon.commit()
                ShowRecord()
                sqlCon.close()
                messagebox.showinfo("Data Entry Form", "Record Entered successfully")

        #=================================================================Search==============================

        scroll_y =ttk.Scrollbar(LeftFrame,orient="vertical")
        # scrollbar =ttk.ScrollBar(self.root)
        # self.scroll_y=ttk.ScrollBar(LeftFrame,orient="VERTICAL")

        self.member_record = ttk.Treeview(LeftFrame,height=12,columns=("memid","firstname","surname","address","pobox","gender","mobile","email","mtype"),yscrollcommand=scroll_y.set)

        # self.scroll_y.grid(side=RIGHT,fill=Y,padx=5,pady=0)
        self.scroll_y.grid(sticky=E,row=3,column=0,padx=5,pady=0)

        self.member_record.heading("memid",text="MemberID")
        self.member_record.heading("firstname",text="FirstName")
        self.member_record.heading("surname",text="Surname")
        self.member_record.heading("address",text="Address")
        self.member_record.heading("pobox",text="Gender")
        self.member_record.heading("gender",text="Mobile")
        self.member_record.heading("mobile",text="PO BOX")
        self.member_record.heading("email",text="Email")
        self.member_record.heading("mtype",text="Type")

        self.member_record["show"] = "headings"

        self.member_record.column("memid",width=70)
        self.member_record.column("firstname",width=90)
        self.member_record.column("surname",width=70)
        self.member_record.column("address",width=70)
        self.member_record.column("pobox",width=70)
        self.member_record.column("gender",width=70)
        self.member_record.column("mobile",width=70)
        self.member_record.column("email",width=70)
        self.member_record.column("mtype",width=70)


        self.member_record.pack(fill=BOTH,expand=1)
        self.member_record.bind("<ButtonRelease-1>")#,MembersInfo)
        # ShowRecord()  #method to be used


        #=================================================================Search==============================




        self.lblBarCode = tk.Label(SearchFrame,font=("Arial", 12, "bold"),text="BarCode")
        self.lblBarCode.grid(row=0,column=0,sticky=W,padx=4)
        self.txtBarCode =tk.Entry(SearchFrame,font=("CCode39",13),width=26,justify="center",textvariable=self.MemIDBar)
        self.txtBarCode.grid(row=0,column=1,padx=39)
        self.txtSearchFrame=tk.Entry(SearchFrame,font=("Arial", 21, "bold"),width=33,justify="right",textvariable=self.Search)
        self.txtSearchFrame.grid(row=0,column=2)
        self.btnSearch = tk.Button(SearchFrame,font=("Arial", 16, "bold"),padx=29,width=9,height=1,text="Search",bg="cadetblue",fg="black",pady=1)
        self.btnSearch.grid(row=0,column=3,padx=1)



        #=============================================================Buttons==================================



        self.btnAddNew = tk.Button(ButtonFrame,pady=1,bd=4,fg="black",command=addNew(self),font=("Arial", 16, "bold"),
                                padx=28,width=12,height=1,text="Add New User",
                                bg="cadetblue")
        self.btnAddNew.grid(row=0,column=0,padx=2)

        self.btnShowRecord = tk.Button(ButtonFrame, pady=1, bd=4, fg="black", font=("Arial", 16, "bold"), padx=29, width=12,
                                height=1, text="Show Records",
                                bg="cadetblue",command="")
        self.btnShowRecord.grid(row=0, column=1, padx=1)


        self.btnUpDate = tk.Button(ButtonFrame, pady=1, bd=4, fg="black", font=("Arial", 16, "bold"), padx=29, width=11,
                                height=1, text="Update",
                                bg="cadetblue")
        self.btnUpDate.grid(row=0, column=2, padx=2)


        self.btnDelete = tk.Button(ButtonFrame, pady=1, bd=4, fg="black", font=("Arial", 16, "bold"), padx=29, width=12,
                                height=1, text="Delete",
                                bg="cadetblue")
        self.btnDelete.grid(row=0, column=3, padx=1)

        self.btnReset = tk.Button(ButtonFrame, pady=1, bd=4, fg="black", font=("Arial", 16, "bold"), padx=29, width=11,
                                height=1, text="Reset",
                                bg="cadetblue")
        self.btnReset.grid(row=0, column=4, padx=2)

        self.btnExit = tk.Button(ButtonFrame, pady=1, bd=4, fg="black", font=("Arial", 16, "bold"), padx=29, width=11,
                               height=1, text="Exit",
                               bg="cadetblue")
        self.btnReset.grid(row=0, column=5, padx=2)

        #===============================================================================================



        #===============================================================================================


if __name__ == '__main__':
    root = Tk()
    application = MemmberConnect(root)
    root.mainloop()



