
    
    def addNew(self):

        if MemID.get() != "" and txtFirstName.get() != "" and Surname.get() != "":
            pass
        else:
            messagebox.showerror("Error,Check Input","Enter correct members details")
            sqlCon =pymysql.cursors.connect(host="localhost",
                                                  user="root",
                                                  password="",
                                                  database="members")
            cursors=  sqlCon.cursors()

            cursors.execute("INSERT INTO members values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                MemID.get(),
                FistName.get(),
                Surname.get(),
                Address.get(),
                POBOX.get(),
                Gender.get(),
                Mtype.get(),
                Mobile.get(),
                Email.get(),
                Search.get(),
                MemIDBar.get()

            ))

            sqlCon.commit()
            ShowRecord()
            sqlCon.close()
            messagebox.showinfo("Data Entry Form","Record Entered successfully")

    def ShowRecord(self):
        sqlCon = pymysql.cursors.connect(host="localhost",
                                     user="root",
                                     password="",
                                     database="members")
        cursors = sqlCon.cursors()
        cursors.execute("SELECT* FROM members")
        results = cursors.fetchall()
        if len(results) !=0:
            self.member_record.delete(*self.member_record.get_children())
            for row in results:
                self.member_record.insert("",END,values=row)
                sqlCon.commit()

        sqlCon.close()



    def MembersInfo(self):


        viewInfo = self.member_record.focus()
        learnerData = self.member_record.item(viewInfo)
        row=learnerData["values"]

        MemID.set(row[0])
        FistName.set(row[1])
        Surname.set(row[2]),
        Address.set(row[3])
        POBOX.set(row[4])
        Gender.set(row[5])
        Mobile.set(row[6])
        Email.set(row[7])
        Mtype.set(row[8])

        # Search.set(row[0])
        # MemIDBar.get()

        def update(self):
            sqlCon = pymysql.cursors.connect(host="localhost",
                                             user="root",
                                             password="",
                                             database="members")
            cursors = sqlCon.cursors()
            cursors.execute("UPDATE members SET firstname=%s,surname=%s,address=%s,pobox=%s,gender=%s,mobile=%s,email=%s,mtype=%s WHERE memid=%s",(
                FistName.get(),
                Surname.get(),
                Address.get(),
                POBOX.get(),
                Gender.get(),
                Mobile.get(),
                Email.get(),
                Mtype.get(),
                MemID.get(),

            ))

            sqlCon.commit()
            ShowRecord()
            sqlCon.close()
            messagebox.showinfo("Data Entry Form","Record Entered successfully")

    def ShowRecord(self):
        sqlCon = pymysql.cursors.connect(host="localhost",
                                     user="root",
                                     password="",
                                     database="members")
        cursors = sqlCon.cursors()
        cursors.execute("SELECT* FROM members")
        results = cursors.fetchall()
        if len(results) !=0:
            self.member_record.delete(*self.member_record.get_children())
            for row in results:
                self.member_record.insert("",END,values=row)
                sqlCon.commit()

        sqlCon.close()



    def MembersInfo(self):


        viewInfo = self.member_record.focus()
        learnerData = self.member_record.item(viewInfo)
        row=learnerData["values"]

        MemID.set(row[0])
        FistName.set(row[1])
        Surname.set(row[2]),
        Address.set(row[3])
        POBOX.set(row[4])
        Gender.set(row[5])
        Mobile.set(row[6])
        Email.set(row[7])
        Mtype.set(row[8])

        # Search.set(row[0])
        # MemIDBar.get()

        def update(self):
            sqlCon = pymysql.cursors.connect(host="localhost",
                                             user="root",
                                             password="",
                                             database="members")
            cursors = sqlCon.cursors()
            cursors.execute("UPDATE members SET firstname=%s,surname=%s,address=%s,pobox=%s,gender=%s,mobile=%s,email=%s,mtype=%s WHERE memid=%s",(
                FistName.get(),
                Surname.get(),
                Address.get(),
                POBOX.get(),
                Gender.get(),
                Mobile.get(),
                Email.get(),
                Mtype.get(),
                MemID.get(),

            ))
