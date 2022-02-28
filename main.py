from tkinter import *
from tkinter import messagebox, filedialog
from urllib.parse import quote_plus as urlquote
import tkinter.ttk as tk
import re, horizon, sqlalchemy

global root

def draw_main_screen():
    """
    Creating Main Screen Window using tkinter
    """
    try:
        connection = horizon.connect()
        connection.close()
    except Exception as e:
        root = Tk()
        root.withdraw()
        messagebox.showerror(
            "Database Error", f"{e}"
        )
        return
    root = Tk()
    root.resizable(False, False)
    root.title("Student Management System")
    screen_width = root.winfo_screenwidth() - 100
    screen_height = root.winfo_screenheight() - 100
    root.geometry(f"{screen_width}x{screen_height}")
    space_around_horizontal = (screen_width - 1100) / 2
    space_around_vertical = (screen_height - 1000) / 2
    main_fram = Frame(root, bg="#454545", relief=RIDGE)
    main_fram.place(
        y=space_around_vertical, x=space_around_horizontal, width=1100, height=900
    )
    table_frame = Frame(main_fram, bg="#52595D")
    table_frame.place(x=50, y=140, width=1000, height=600)
    global table
    table = tk.Treeview(table_frame)
    tree = table
    table.place(x=0, y=0, width=1000, height=600)
    vertical_scrollbar = tk.Scrollbar(table_frame, orient=VERTICAL, command=table.yview)
    vertical_scrollbar.pack(side="right", fill="y")
    table.configure(yscrollcommand=vertical_scrollbar.set)
    horizontal_scrollbar = tk.Scrollbar(
        table_frame, orient=HORIZONTAL, command=table.xview
    )
    horizontal_scrollbar.pack(side="bottom", fill="x")
    """
    Creating Table 
    """
    table.configure(xscrollcommand=horizontal_scrollbar.set)
    table["columns"] = ("1", "2", "3", "4", "5", "6")
    table["show"] = "headings"
    table.heading("1", text="Student ID")
    table.heading("2", text="Name")
    table.heading("3", text="Gender")
    table.heading("4", text="Contact")
    table.heading("5", text="Date Of Birth")
    table.heading("6", text="Address")
    updateTreeView()
    footer_frame = Frame(main_fram, bg="#454545", relief=GROOVE)
    footer_frame.place(x=0, y=780, height=100, width=1100)
    button_container = Frame(footer_frame, bg="#454545", relief=GROOVE)
    button_container.place(relx=0.5, rely=0.5, anchor=CENTER)
    """
    Creating Button 
    """
    btn_search = Button(
        button_container,
        text="Search Data",
        font="none 15",
        command=lambda: search_data_window(root),
    )
    btn_search.grid(column=0, row=0, padx=50)
    btn_add = Button(
        button_container,
        text="Add Data",
        font="none 15",
        command=lambda: add_data_window(root),
    )
    btn_add.grid(column=1, row=0, padx=50)
    btn_remove = Button(
        button_container,
        text="Remove Data",
        font="none 15",
        command=lambda: remove_data_window(root),
    )
    btn_remove.grid(column=2, row=0, padx=50)
    btn_update = Button(
        button_container,
        text="Update Data",
        font="none 15",
        command=lambda: update_data_window(root),
    )
    btn_update.grid(column=3, row=0, padx=50)
    btn_upload = Button(
        button_container,
        text="Upload Data",
        font="none 15",
        command=lambda: upload_data(root),
    )
    btn_upload.grid(column=4, row=0, padx=50)
    root.mainloop()

def upload_data(root):
    """
    Uploading CSV file using pandas. Detail in horizon.py and conn.py
    """
    try:
        filename = filedialog.askopenfilename(initialdir="C:/Users/akmal/PycharmProjects/pythonProject/",
                                              title="File Manager",
                                              filetypes=(("CSV Files", "*.csv"), ("All", "*.*"))
                                              )
        df = horizon.open_csv(filename)
        print(df)
        engine_stmt = 'mysql+mysqldb://%s:%s@%s:%s/%s' % ("root", urlquote("rafie1112"), "localhost", "3306", "student")
        print(engine_stmt)
        engine = sqlalchemy.create_engine(engine_stmt)
        df.to_sql(name="students", con=engine,
                  if_exists='append', index=False, chunksize=1000)
        updateTreeView()
    except Exception as e:
        print(e)

def add_data_window(root):
    window = Toplevel(root, bg="#52595D")
    window.title("Add New Student Record")
    window.geometry("550x500")
    window.resizable(False, False)
    window.grab_set()
    frame_center = Frame(window, bg="#52595D")
    frame_center.place(relx=0.5, rely=0.5, anchor=CENTER)
    string_gender = StringVar()
    string_name = StringVar()
    string_roll = StringVar()
    string_contact = StringVar()
    string_address = StringVar()
    string_dob = StringVar()
    string_gender.set("Male")
    roll_label = Label(
        frame_center,
        text="Student ID :\t",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        justify=LEFT,
    )
    roll_label.grid(column=0, row=0, pady=10, sticky="we")
    roll_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        fg="black",
        bg="white",
        textvariable=string_roll,
    )
    roll_entry.grid(column=1, row=0, pady=10, padx=10)
    name_label = Label(
        frame_center,
        text="Name :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    name_label.grid(column=0, row=1, pady=10, sticky="w")
    name_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        fg="black",
        bg="white",
        textvariable=string_name,
    )
    name_entry.grid(column=1, row=1, pady=10, padx=10)
    contact_label = Label(
        frame_center,
        text="Contact :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    contact_label.grid(column=0, row=2, pady=10, sticky="w")
    contact_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        fg="black",
        bg="white",
        textvariable=string_contact,
    )
    contact_entry.grid(column=1, row=2, pady=10, padx=10)
    gender_label = Label(
        frame_center,
        text="Gender :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    dob_label = Label(
        frame_center,
        text="Date of Birth :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    dob_label.grid(column=0, row=4, pady=10, sticky="w")
    dob_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        fg="black",
        bg="white",
        textvariable=string_dob,
    )
    dob_entry.insert(0, "2021-08-21")
    dob_entry.grid(column=1, row=4, pady=10, padx=10)
    address_label = Label(
        frame_center,
        text="Address :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    address_label.grid(column=0, row=3, pady=10, sticky="w")
    address_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        fg="black",
        bg="white",
        textvariable=string_address,
    )
    address_entry.grid(
        column=1,
        row=3,
        pady=10,
        padx=10,
    )
    gender_label.grid(column=0, row=5, pady=10, sticky="w")
    gender_frame = Frame(frame_center, bg="mistyrose2")
    gender_frame.grid(column=1, row=5, pady=10, padx=10)
    C1 = Radiobutton(
        gender_frame,
        text="Male",
        variable=string_gender,
        value="Male",
        anchor="w",
        bg="white",
        activebackground="white",
        activeforeground="green",
        fg="black",
        font="none 15",
        padx=5,
    )
    C2 = Radiobutton(
        gender_frame,
        text="Female",
        variable=string_gender,
        value="Female",
        anchor="e",
        bg="white",
        activebackground="white",
        activeforeground="green",
        fg="black",
        font="none 15",
        padx=5,
    )
    C1.pack(side=LEFT, anchor="w", fill=X)
    C2.pack(side=RIGHT, anchor="e", fill=X)

    def addData():
        if (
            len(string_roll.get()) == 0
            or len(string_name.get()) == 0
            or len(string_contact.get()) == 0
            or len(string_address.get()) == 0
        ):
            messagebox.showerror("Error!", "All Fields are Required!", parent=window)
        else:
            if string_roll.get().isdigit() and string_contact.get().isdigit():
                if len(string_contact.get()) < 20:
                    regex = r"[0-2][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]"
                    if re.fullmatch(regex, string_dob.get()):
                        addDataToDatabase(
                            [
                                string_roll,
                                string_name,
                                string_contact,
                                string_gender,
                                string_dob,
                                string_address,
                            ]
                        )
                        messagebox.showinfo("Done", "Data Added!", parent=window)
                        string_dob.set("2021-09-04")
                        string_address.set("")
                        string_contact.set("")
                        string_gender.set("Male")
                        string_name.set("")
                        string_roll.set("")
                    else:
                        messagebox.showerror(
                            "Error", "Date Of Birth Format\nYYYY-MM-DD", parent=window
                        )

                else:
                    messagebox.showerror(
                        "Error!",
                        "Mobile Number Must Be 20 Digits Long!",
                        parent=window,
                    )
            else:
                messagebox.showerror(
                    "Error!",
                    "Contact and Roll Number Must \nBe In Digits!",
                    parent=window,
                )

    submit = Button(frame_center, text="Submit", width=10, pady=5, command=addData)
    submit.grid(columnspan=2, row=6, padx=10, pady=10)

def search_data_window(root):
    canBeRemoved = StringVar()
    canBeRemoved.set("FALSE")
    window = Toplevel(root, bg="#52595D")
    window.title("Search Student Record")
    window.grab_set()
    window.geometry("550x500")
    window.resizable(False, False)
    frame_center = Frame(window, bg="#52595D")
    frame_center.place(relx=0.5, rely=0.5, anchor=CENTER)
    string_gender = StringVar()
    string_name = StringVar()
    string_roll = StringVar()
    string_contact = StringVar()
    string_address = StringVar()
    string_dob = StringVar()
    def getStudentAndFill():
        if len(string_roll.get()) != 0:
            if string_roll.get().isdigit():
                row = horizon.getStudentRecord(string_roll.get())
            else:
                messagebox.showerror(
                    "Error!", "Please Enter Valid Roll Number!", parent=window
                )
                return
        else:
            messagebox.showerror("Error!", "Please Enter Roll Number!", parent=window)
            return
        if row != None:
            canBeRemoved.set("TRUE")
            string_name.set(row.get("NAME"))
            string_gender.set(row.get("GENDER"))
            string_contact.set(row.get("CONTACT"))
            string_dob.set(row.get("DOB"))
            string_address.set(row.get("ADDRESS"))
            print(row)
        else:
            canBeRemoved.set("FALSE")
            window.grab_release()
            messagebox.showerror(
                "No record Found",
                f"No record with roll number\n{string_roll.get()}",
                parent=window,
            )
            window.grab_set()

    roll_label = Label(
        frame_center,
        text="Student ID :\t",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        justify=LEFT,
    )
    roll_label.grid(column=0, row=0, pady=10, sticky="we")
    roll_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        fg="black",
        bg="gray51",
        textvariable=string_roll,
    )
    roll_entry.grid(column=1, row=0, pady=10, padx=10)
    find_btn = Button(
        frame_center,
        text="Find",
        width=10,
        pady=5,
        command=getStudentAndFill,
    )
    find_btn.grid(column=2, row=0, pady=10, padx=10)
    name_label = Label(
        frame_center,
        text="Name :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    name_label.grid(column=0, row=1, pady=10, sticky="w")
    name_entry = Entry(
        frame_center,
        relief=RIDGE,
        state=DISABLED,
        font="none 15",
        fg="black",
        bg="white",
        textvariable=string_name,
    )
    name_entry.grid(column=1, row=1, pady=10, padx=10)
    contact_label = Label(
        frame_center,
        text="Contact :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    contact_label.grid(column=0, row=2, pady=10, sticky="w")
    contact_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        state=DISABLED,
        fg="black",
        bg="white",
        textvariable=string_contact,
    )
    contact_entry.grid(column=1, row=2, pady=10, padx=10)
    gender_label = Label(
        frame_center,
        text="Gender :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    dob_label = Label(
        frame_center,
        text="Date of Birth :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    dob_label.grid(column=0, row=4, pady=10, sticky="w")
    dob_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        fg="black",
        state=DISABLED,
        bg="white",
        textvariable=string_dob,
    )
    dob_entry.insert(0, "2021-08-21")
    dob_entry.grid(column=1, row=4, pady=10, padx=10)
    address_label = Label(
        frame_center,
        text="Address :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    address_label.grid(column=0, row=3, pady=10, sticky="w")
    address_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        state=DISABLED,
        fg="black",
        bg="white",
        textvariable=string_address,
    )
    address_entry.grid(
        column=1,
        row=3,
        pady=10,
        padx=10,
    )
    gender_label.grid(column=0, row=5, pady=10, sticky="w")
    gender_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        state=DISABLED,
        fg="black",
        bg="white",
        textvariable=string_gender,
    )
    gender_entry.grid(
        column=1,
        row=5,
        pady=10,
        padx=10,
    )

def remove_data_window(root):
    canBeRemoved = StringVar()
    canBeRemoved.set("FALSE")
    window = Toplevel(root, bg="#52595D")
    window.title("Remove Student Record")
    window.grab_set()
    window.geometry("550x500")
    window.resizable(False, False)
    frame_center = Frame(window, bg="#52595D")
    frame_center.place(relx=0.5, rely=0.5, anchor=CENTER)
    string_gender = StringVar()
    string_name = StringVar()
    string_roll = StringVar()
    string_contact = StringVar()
    string_address = StringVar()
    string_dob = StringVar()
    def getStudentAndFill():
        if len(string_roll.get()) != 0:
            if string_roll.get().isdigit():
                row = horizon.getStudentRecord(string_roll.get())
            else:
                messagebox.showerror(
                    "Error!", "Please Enter Valid Roll Number!", parent=window
                )
                return
        else:
            messagebox.showerror("Error!", "Please Enter Roll Number!", parent=window)
            return
        if row != None:
            canBeRemoved.set("TRUE")
            string_name.set(row.get("NAME"))
            string_gender.set(row.get("GENDER"))
            string_contact.set(row.get("CONTACT"))
            string_dob.set(row.get("DOB"))
            string_address.set(row.get("ADDRESS"))
            print(row)
        else:
            canBeRemoved.set("FALSE")
            window.grab_release()
            messagebox.showerror(
                "No record Found",
                f"No record with roll number\n{string_roll.get()}",
                parent=window,
            )
            window.grab_set()

    roll_label = Label(
        frame_center,
        text="Student ID :\t",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        justify=LEFT,
    )
    roll_label.grid(column=0, row=0, pady=10, sticky="we")
    roll_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        fg="black",
        bg="gray51",
        textvariable=string_roll,
    )
    roll_entry.grid(column=1, row=0, pady=10, padx=10)
    find_btn = Button(
        frame_center,
        text="Find",
        width=10,
        pady=5,
        command=getStudentAndFill,
    )
    find_btn.grid(column=2, row=0, pady=10, padx=10)
    name_label = Label(
        frame_center,
        text="Name :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    name_label.grid(column=0, row=1, pady=10, sticky="w")
    name_entry = Entry(
        frame_center,
        relief=RIDGE,
        state=DISABLED,
        font="none 15",
        fg="black",
        bg="white",
        textvariable=string_name,
    )
    name_entry.grid(column=1, row=1, pady=10, padx=10)
    contact_label = Label(
        frame_center,
        text="Contact :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    contact_label.grid(column=0, row=2, pady=10, sticky="w")
    contact_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        state=DISABLED,
        fg="black",
        bg="white",
        textvariable=string_contact,
    )
    contact_entry.grid(column=1, row=2, pady=10, padx=10)
    gender_label = Label(
        frame_center,
        text="Gender :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    dob_label = Label(
        frame_center,
        text="Date of Birth :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    dob_label.grid(column=0, row=4, pady=10, sticky="w")
    dob_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        fg="black",
        state=DISABLED,
        bg="white",
        textvariable=string_dob,
    )
    dob_entry.insert(0, "2021-08-21")
    dob_entry.grid(column=1, row=4, pady=10, padx=10)
    address_label = Label(
        frame_center,
        text="Address :",
        font="none 15 bold",
        fg="white",
        bg="#52595D",
        anchor="w",
    )
    address_label.grid(column=0, row=3, pady=10, sticky="w")
    address_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        state=DISABLED,
        fg="black",
        bg="white",
        textvariable=string_address,
    )
    address_entry.grid(
        column=1,
        row=3,
        pady=10,
        padx=10,
    )
    gender_label.grid(column=0, row=5, pady=10, sticky="w")
    gender_entry = Entry(
        frame_center,
        relief=RIDGE,
        font="none 15",
        state=DISABLED,
        fg="black",
        bg="white",
        textvariable=string_gender,
    )
    gender_entry.grid(
        column=1,
        row=5,
        pady=10,
        padx=10,
    )

    def removeData():
        if canBeRemoved.get() == "TRUE":
            horizon.removeRecord(string_roll)
            string_roll.set("")
            string_name.set("")
            string_contact.set("")
            string_address.set("")
            string_dob.set("")
            string_gender.set("")
            canBeRemoved.set("FALSE")
            messagebox.showinfo("Done", "Record Deleted Successfully!", parent=window)
            updateTreeView()

        else:
            messagebox.showinfo(
                "Ahh!", "Please First Find Valid Record!", parent=window
            )

    remove = Button(
        frame_center,
        text="Remove",
        width=10,
        pady=5,
        command=removeData,
    )
    remove.grid(columnspan=3, row=6, padx=10, pady=10)
    remove.grid_rowconfigure(0, weight=1)
    remove.grid_columnconfigure(0, weight=1)


def update_data_window(root):
    curItem = table.focus()
    valuesList = table.item(curItem)["values"]
    if len(valuesList) > 0:
        print(valuesList)
        window = Toplevel(root, bg="#52595D")
        window.title("Update Student Record")
        window.grab_set()
        window.geometry("550x500")
        window.resizable(False, False)
        frame_center = Frame(window, bg="#52595D")
        frame_center.place(relx=0.5, rely=0.5, anchor=CENTER)
        string_gender = StringVar()
        string_name = StringVar()
        string_roll = StringVar()
        string_contact = StringVar()
        string_address = StringVar()
        string_dob = StringVar()
        string_gender.set("Male")
        string_gender.set(valuesList[2])
        string_name.set(valuesList[1])
        string_roll.set(valuesList[0])
        string_contact.set(valuesList[3])
        string_address.set(valuesList[5])
        string_dob.set(valuesList[4])
        roll_label = Label(
            frame_center,
            text="Student ID :\t",
            font="none 15 bold",
            fg="white",
            bg="#52595D",
            justify=LEFT,
        )
        roll_label.grid(column=0, row=0, pady=10, sticky="we")
        roll_entry = Entry(
            frame_center,
            relief=RIDGE,
            font="none 15",
            fg="black",
            bg="white",
            state=DISABLED,
            textvariable=string_roll,
        )
        roll_entry.grid(column=1, row=0, pady=10, padx=10)
        name_label = Label(
            frame_center,
            text="Name :",
            font="none 15 bold",
            fg="white",
            bg="#52595D",
            anchor="w",
        )
        name_label.grid(column=0, row=1, pady=10, sticky="w")
        name_entry = Entry(
            frame_center,
            relief=RIDGE,
            font="none 15",
            fg="black",
            bg="white",
            textvariable=string_name,
        )
        name_entry.grid(column=1, row=1, pady=10, padx=10)
        contact_label = Label(
            frame_center,
            text="Contact :",
            font="none 15 bold",
            fg="white",
            bg="#52595D",
            anchor="w",
        )
        contact_label.grid(column=0, row=2, pady=10, sticky="w")
        contact_entry = Entry(
            frame_center,
            relief=RIDGE,
            font="none 15",
            fg="black",
            bg="white",
            textvariable=string_contact,
        )
        contact_entry.grid(column=1, row=2, pady=10, padx=10)
        gender_label = Label(
            frame_center,
            text="Gender :",
            font="none 15 bold",
            fg="white",
            bg="#52595D",
            anchor="w",
        )
        dob_label = Label(
            frame_center,
            text="Date of Birth :",
            font="none 15 bold",
            fg="white",
            bg="#52595D",
            anchor="w",
        )
        dob_label.grid(column=0, row=4, pady=10, sticky="w")
        dob_entry = Entry(
            frame_center,
            relief=RIDGE,
            font="none 15",
            fg="black",
            bg="white",
            textvariable=string_dob,
        )
        dob_entry.grid(column=1, row=4, pady=10, padx=10)
        address_label = Label(
            frame_center,
            text="Address :",
            font="none 15 bold",
            fg="white",
            bg="#52595D",
            anchor="w",
        )
        address_label.grid(column=0, row=3, pady=10, sticky="w")
        address_entry = Entry(
            frame_center,
            relief=RIDGE,
            font="none 15",
            fg="black",
            bg="white",
            textvariable=string_address,
        )
        address_entry.grid(
            column=1,
            row=3,
            pady=10,
            padx=10,
        )
        gender_label.grid(column=0, row=5, pady=10, sticky="w")
        gender_frame = Frame(frame_center, bg="mistyrose2")
        gender_frame.grid(column=1, row=5, pady=10, padx=10)
        C1 = Radiobutton(
            gender_frame,
            text="Male",
            variable=string_gender,
            value="Male",
            anchor="w",
            bg="white",
            activebackground="white",
            activeforeground="green",
            fg="black",
            font="none 15",
            padx=5,
        )
        C2 = Radiobutton(
            gender_frame,
            text="Female",
            variable=string_gender,
            value="Female",
            anchor="e",
            bg="white",
            activebackground="white",
            activeforeground="green",
            fg="black",
            font="none 15",
            padx=5,
        )
        C1.pack(side=LEFT, anchor="w", fill=X)
        C2.pack(side=RIGHT, anchor="e", fill=X)

        def updateData():
            if (
                len(string_roll.get()) == 0
                or len(string_name.get()) == 0
                or len(string_contact.get()) == 0
                or len(string_address.get()) == 0
            ):
                messagebox.showerror(
                    "Error!", "All Fields are Required!", parent=window
                )
            else:
                if string_roll.get().isdigit() and string_contact.get().isdigit():
                    if len(string_contact.get()) < 20:
                        regex = r"[0-2][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]"
                        if re.fullmatch(regex, string_dob.get()):
                            horizon.updateRecord(
                                string_roll.get(),
                                string_name.get(),
                                string_gender.get(),
                                string_contact.get(),
                                string_dob.get(),
                                string_address.get(),
                            )
                            updateTreeView()
                            messagebox.showinfo("Done", "Data Updated!", parent=window)
                        else:
                            messagebox.showerror(
                                "Error",
                                "Date Of Birth Format\nYYYY-MM-DD",
                                parent=window,
                            )

                    else:
                        messagebox.showerror(
                            "Error!",
                            "Mobile Number Must Be 19 Digits Long!",
                            parent=window,
                        )
                else:
                    messagebox.showerror(
                        "Error!",
                        "Contact and Roll Number Must \nBe In Digits!",
                        parent=window,
                    )

        update = Button(
            frame_center, text="Update", width=10, pady=5, command=updateData
        )
        update.grid(columnspan=2, row=6, padx=10, pady=10)

    else:
        messagebox.showerror("Error!", "No Item Selected To Update!", parent=root)

def updateTreeView():
    """
    Updating data content in table
    """
    try:
        rows = horizon.getAllStudents()
    except Exception as e:
        print("Error")
        rows = dict()
        messagebox.showerror("Database Error", f"Error Cause :\n{e}")
        return
    table.delete(*table.get_children())
    if len(rows) > 0:
        for row in rows:
            table.insert(
                "",
                "end",
                text="L1",
                values=(
                    row["ROLL"],
                    row["NAME"],
                    row["GENDER"],
                    row["CONTACT"],
                    row["DOB"],
                    row["ADDRESS"],
                ),
            )


def addDataToDatabase(argumentList):
    (
        string_roll,
        string_name,
        string_contact,
        string_gender,
        string_dob,
        string_address,
    ) = argumentList
    try:
        connection = horizon.connect()
        connection.close()
    except Exception as e:
        root = Tk()
        root.withdraw()
        messagebox.showerror(
            "Database Error",
            f"Please Check Database Connection!",
        )
        return
    try:
        horizon.insertRecord (
            string_roll.get(),
            string_name.get(),
            string_gender.get(),
            string_contact.get(),
            string_dob.get(),
            string_address.get(),
        )
        updateTreeView()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    draw_main_screen()
