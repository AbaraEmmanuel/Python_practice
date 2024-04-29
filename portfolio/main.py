from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from datetime import date
from mydb import Database

# Create database object
data = Database(db='myexpense.db')

class ExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Office Expense')

        # Global variables
        self.selected_rowid = 0
        self.budget = 0

        # Frame widgets
        self.f1 = Frame(
            root,
            padx=10,
            pady=10,
        )
        self.f1.pack(expand=True, fill=BOTH)

        # Label Widget
        Label(self.f1, text='ITEM NAME').grid(row=0, column=0, sticky=W)
        Label(self.f1, text='ITEM PRICE').grid(row=1, column=0, sticky=W)
        Label(self.f1, text='PURCHASE DATE').grid(row=2, column=0, sticky=W)

        # Entry Widgets
        self.item_name = Entry(self.f1)
        self.item_amt = Entry(self.f1)
        self.transaction_date = Entry(self.f1)
        
        # Entry grid placement
        self.item_name.grid(row=0, column=1, sticky=EW, padx=(10, 0))
        self.item_amt.grid(row=1, column=1, sticky=EW, padx=(10, 0))
        self.transaction_date.grid(row=2, column=1, sticky=EW, padx=(10, 0))

        # Action buttons
        self.cur_date = Button(
            self.f1, 
            text='Current Date', 
            bg='#04C4D9', 
            command=self.set_date,
            width=15
        )

        self.submit_btn = Button(
            self.f1, 
            text='Save Record', 
            command=self.save_record, 
            bg='#42602D', 
            fg='white'
        )

        self.clear_btn = Button(
            self.f1, 
            text='Clear Entry', 
            command=self.clear_entries, 
            bg='#D9B036', 
            fg='white'
        )

        self.update_btn = Button(
            self.f1, 
            text='Update', 
            command=self.update_record, 
            bg='#C2BB00', 
            fg='white'
        )

        self.delete_btn = Button(
            self.f1, 
            text='Delete', 
            command=self.delete_record, 
            bg='#BD2A2E', 
            fg='white'
        )

        self.exit_btn = Button(
            self.f1, 
            text='Exit', 
            command=root.quit, 
            bg='#D33532', 
            fg='white'
        )

        self.total_bal_btn = Button(
            self.f1, 
            text='Total Balance', 
            command=self.total_balance, 
            bg='#486966', 
            fg='white'
        )

        self.budget_btn = Button(
            self.f1, 
            text='Set Budget', 
            command=self.set_budget, 
            bg='#0066ff', 
            fg='white'
        )

        # Button grid placement
        self.cur_date.grid(row=3, column=0, sticky=EW, padx=(10, 0))
        self.submit_btn.grid(row=0, column=2, sticky=EW, padx=(10, 0))
        self.clear_btn.grid(row=1, column=2, sticky=EW, padx=(10, 0))
        self.update_btn.grid(row=2, column=2, sticky=EW, padx=(10, 0))
        self.delete_btn.grid(row=3, column=2, sticky=EW, padx=(10, 0))
        self.exit_btn.grid(row=4, column=2, sticky=EW, padx=(10, 0))
        self.total_bal_btn.grid(row=4, column=0, sticky=EW, padx=(10, 0))
        self.budget_btn.grid(row=5, column=0, sticky=EW, padx=(10, 0))

        # Treeview to view the record
        self.tv = ttk.Treeview(root, selectmode='browse', columns=(1, 2, 3, 4), show='headings', height=8)
        self.tv.pack(side="left")

        self.tv.column(1, anchor=CENTER, stretch=NO, width=70)
        self.tv.column(2, anchor=CENTER)
        self.tv.column(3, anchor=CENTER)
        self.tv.column(4, anchor=CENTER)
        self.tv.heading(1, text="Serial no")
        self.tv.heading(2, text="Item Name")
        self.tv.heading(3, text="Item Price")
        self.tv.heading(4, text="Purchase Date")

        self.scrollbar = Scrollbar(root, orient='vertical')
        self.scrollbar.configure(command=self.tv.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.tv.config(yscrollcommand=self.scrollbar.set)

        # Fetch and display records
        self.fetch_records()

        # Bind select record function
        self.tv.bind("<ButtonRelease-1>", self.select_record)

    def set_date(self):
        # Set current date to transaction_date entry
        self.transaction_date.delete(0, END)
        self.transaction_date.insert(END, date.today().strftime("%Y-%m-%d"))

    def save_record(self):
        # Fetch values from entries
        item_name = self.item_name.get()
        item_price = float(self.item_amt.get())
        purchase_date = self.transaction_date.get()

        # Check if the total expense exceeds the budget
        total_expense = data.fetchRecord('SELECT SUM(item_price) FROM expense_record')[0][0]
        if total_expense + item_price > self.budget:
            messagebox.showwarning('Budget Exceeded', f'The total expense will exceed the monthly budget of {self.budget}.')
        else:
            # Insert record into database
            data.insertRecord(item_name=item_name, item_price=item_price, purchase_date=purchase_date)

            # Refresh record list
            self.fetch_records()

            # Clear entries after saving
            self.clear_entries()

    def fetch_records(self):
        # Clear existing records
        for item in self.tv.get_children():
            self.tv.delete(item)

        # Fetch records from database and display in Treeview
        records = data.fetchRecord('SELECT rowid, * FROM expense_record')
        for rec in records:
            self.tv.insert(parent='', index='end', values=(rec[0], rec[1], rec[2], rec[3]))

    def select_record(self, event):
        # Get selected record from Treeview
        selected_item = self.tv.selection()[0]
        record_values = self.tv.item(selected_item, 'values')

        # Update entry fields with selected record values
        self.selected_rowid = record_values[0]
        self.item_name.delete(0, END)
        self.item_name.insert(END, record_values[1])
        self.item_amt.delete(0, END)
        self.item_amt.insert(END, record_values[2])
        self.transaction_date.delete(0, END)
        self.transaction_date.insert(END, record_values[3])

    def clear_entries(self):
        # Clear entry fields
        self.item_name.delete(0, END)
        self.item_amt.delete(0, END)
        self.transaction_date.delete(0, END)

    def update_record(self):
        # Fetch values from entries
        item_name = self.item_name.get()
        item_price = float(self.item_amt.get())
        purchase_date = self.transaction_date.get()

        # Update record in database
        data.updateRecord(item_name=item_name, item_price=item_price, purchase_date=purchase_date, rid=self.selected_rowid)

        # Refresh record list
        self.fetch_records()

        # Clear entries after updating
        self.clear_entries()

    def delete_record(self):
        # Delete selected record from database
        data.removeRecord(self.selected_rowid)

        # Refresh record list
        self.fetch_records()

    def total_balance(self):
        # Fetch total expense from database and calculate total balance
        total_expense = data.fetchRecord('SELECT SUM(item_price) FROM expense_record')[0][0]
        total_balance = self.budget - total_expense
        messagebox.showinfo('Total Balance', f'Total Expense: {total_expense}\nBalance Remaining: {total_balance}')

    def set_budget(self):
        # Prompt user to set monthly budget
        budget = simpledialog.askfloat("Set Monthly Budget", "Enter the monthly budget:")
        if budget is not None:
            self.budget = budget
            messagebox.showinfo('Budget Set', f'Monthly budget set to {budget}')

# Create main window
root = Tk()
app = ExpenseApp(root)
root.mainloop()
