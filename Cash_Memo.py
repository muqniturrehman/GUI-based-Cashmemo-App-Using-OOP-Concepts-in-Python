import tkinter as tk #Library For GUI development
from tkinter import messagebox, ttk #importing Message box to show generated bill
import customtkinter as ctk # Library for enhancing GUI

from reportlab.lib.pagesizes import letter #Library for making PDF of bill
from reportlab.pdfgen import canvas #to write on PDF(canvas)


#Date Class
class Date:
    def __init__(self, d, m: str, y):
        self.__day = d
        self.__month = m
        self.__year = y

        #Exception Handelling(day should be between 1-31, month 1-12, and year greater then 1800)
        if 1 <= self.__day <= 31 and 1 <= self.__month <= 12 and self.__year >= 1800:
            pass
        else:
            raise Exception("Enter a Valid __date")

#building Methods
    def __str__(self): #month number will be represented as Abrivations(to show how str is built)
        if self.__month == 1:
            __month = "Jan"
        if self.__month == 2:
            __month = "Feb"
        if self.__month == 3:
            __month = "Mar"
        if self.__month == 4:
            __month = "Apr"
        if self.__month == 5:
            __month = "May"
        if self.__month == 6:
            __month = "Jun"
        if self.__month == 7:
            __month = "Jul"
        if self.__month == 8:
            __month = "Aug"
        if self.__month == 9:
            __month = "Sept"
        if self.__month == 10:
            __month = "Oct"
        if self.__month == 11:
            __month = "Nov"
        if self.__month == 12:
            __month = "Dec"
        return f"{self.__day} - {__month} - {self.__year}"


    #calling __str__ in repr
    def __repr__(self):
        return str(self)

    #Getter & Setters:
    def get_day(self):
        return self.__day

    def set_day(self, value):
        self.__day = value

    def get_month(self):
        return self.__month

    def set_month(self, value):
        self.__month = value

    def get_year(self):
        return self.__year

    def set_year(self, value):
        self.__year = value


#Customer Name Class:
class Name:
    def __init__(self, f: str, l: str): #2 data members, 1 for 1st name and other for last name
        self.__first_name = f
        self.__last_name = l


    #proper case function is added to add some extra functionality. this can also be achieved by using capatalize() function
    def __repr__(self):#checks if ascii of chracter at 0 index & after space is between 65-97 else will make it capatalize
        i = 0
        x = ""
        if ord("a") <= ord(self.__first_name[i]) <= ord("z"):
            x = x + chr(ord(self.__first_name[i]) - 32)
            i += 1
        while i < len(self.__first_name):
            if ord(self.__first_name[i - 1]) == 32 and ord("a") <= ord(
                self.__first_name[i]) <= ord("z"):
                x = x + chr(ord(self.__first_name[i]) - 32)
            else:
                x = x + self.__first_name[i]
            i += 1
        i = 0
        y = ""
        if ord("a") <= ord(self.__last_name[i]) <= ord("z"):
            y = y + chr(ord(self.__last_name[i]) - 32)
            i += 1
        while i < len(self.__last_name):
            if ord(self.__last_name[i - 1]) == 32 and ord("a") <= ord(
                self.__last_name[i]
            ) <= ord("z"):
                y = y + chr(ord(self.__last_name[i]) - 32)
            else:
                y = y + self.__last_name[i]
            i += 1
        return f"{x} {y}"


    #Getter & Setter
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, value):
        self.__first_name = value

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, value):
        self.__last_name = value


#Class Address
class Address:
    def __init__(self, h, s, t, c):
        self.__house_no = h
        self.__street_no = s
        self.__town = t
        self.__city = c

    #creating Repr to show on print Screen
    def __repr__(self):
        return f"House no. {self.__house_no}, Street no. {self.__street_no}, {self.__town}, {self.__city}"


    #Getter & Setter
    def get_house_no(self):
        return self.__house_no

    def set_house_no(self, value):
        self.__house_no = value

    def get_street_no(self):
        return self.__street_no

    def set_street_no(self, value):
        self.__street_no = value

    def get_town(self):
        return self.__town

    def set_town(self, value):
        self.__town = value

    def get_city(self):
        return self.__city

    def set_city(self, value):
        self.__city = value


#Class Object(Particulars)
class Object:

    def __init__(self, Qty, part, rate):
        self.__Qty = Qty
        self.__part = part
        self.__rate = rate

    def __repr__(self):
        s = f"{self.__Qty}".ljust(15)
        s += f"{self.__part}".ljust(22)
        s += f"{self.__rate}".ljust(14)
        s += f"{self.__Qty*self.__rate}".ljust(10)
        s += f"\n"
        return s
#Getter and Setters
    def get_qty(self):
        return self.__Qty

    def set_qty(self, value):
        self.__Qty = value

    def get_part(self):
        return self.__part

    def set_part(self, value):
        self.__part = value

    def get_rate(self):
        return self.__rate

    def set_rate(self, value):
        self.__rate = value


# Cashmemo class that is aggeregated from Name, Date, Object class.
class CashMemo:
    shop_name = "MOBILO" #class level data member
    def __init__(self, date, No, name, adress, obj):
        self.__date = date
        self.__no = No
        self.__name = name
        self.__adress = adress
        self.__obj = [] # all object(particulars) bought will be added to array
        self.__obj.extend(obj)

    #claculating total amount
    def total(self):
        total = 0
        for item in self.__obj:
            total += int(item.get_qty()) * int(item.get_rate())
        return total

    #print bill Function(Repr)
    def __repr__(self):
        s = ""
        s += f"\n\n\t\t\t  {CashMemo.shop_name} \n\t\t         MOBILE CITY \n\t\tDEALS IN ALL KIND OF ACCESORIES \n=================================================================\n"
        s +=f"No. {self.__no}".ljust(44)
        s+=f"Date: {self.__date}\nName: {self.__name}\nAddress: {self.__adress}\n=================================================================\nQty            Particularts          Rate          Amount\n=================================================================\n"
        for item in self.__obj:
            s += f"{item}"
        s += ("=================================================================")
        s += (f"\nSignature  ____________\t\tTotal Amount:\t{self.total()}")
        return s

    #Getter & Setter
    def get_date(self):
        return self.__date

    def set_date(self, value):
        self.__date = value

    def get_no(self):
        return self.__no

    def set_no(self, value):
        self.__no = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_adress(self):
        return self.__adress

    def set_adress(self, value):
        self.__adress = value

    def get_obj(self):
        return self.__obj

    def set_obj(self, value):
        self.__obj = value

"""Here GUI is just an extra functionality, this code can be converted to CLI.
You just need to replace all the remaining code below the comment with the following main function code:



def main():
    serial = int(input("Enter serial number: "))
    name1 = str(input("Enter First Name: "))
    name2 = str(input("Enter second Name: "))
    print("Enter Address")
    house = input("Enter house number: ")
    st = input("Enter Street number:  ")
    Town = input("Enter Town/Area: ")
    city = input("Enter city: ")
    print("Enter bill")
    items = []
    while True:
        p = input("Enter particulars (enter 0 to terminate): ")
        if p == '0':
            break
        r = int(input("Enter rate: "))
        q = int(input("Enter Quantity: "))
        if r == 0 or q == 0:
            break
        items.append(Object(q, p, r))

    O = CashMemo(Date(12, 4, 2023), serial, Name(name1, name2), Address(house, st, Town, city),items)
    print(O)
main()"""


#class to make GUI
#here in class "CashMemoApp" diffrent entries and buttons are created that serves as inputs for bills and function callers
class CashMemoApp(CashMemo):

    def __init__(self, root):
        self.root = root #window that will appear as a cash memo app
        self.root.title("Cash Memo System")
        self.items = []

        #creating frame for customer, serial number details
        self.frame_customer = ctk.CTkFrame(root, corner_radius=10)
        self.frame_customer.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        #label at the top of customer frame
        ctk.CTkLabel(self.frame_customer, text="Customer Information", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # label and entry for serial number
        ctk.CTkLabel(self.frame_customer, text="Serial Number:").grid(row=1, column=0, pady=5, padx = 10)
        self.entry_serial = ctk.CTkEntry(self.frame_customer)
        self.entry_serial.grid(row=1, column=1, pady=5)

        # label and entry for Date
        ctk.CTkLabel(self.frame_customer, text="Date :").grid(row=1, column=2, pady=5, padx = 10)
        self.entry_date = ctk.CTkEntry(self.frame_customer, placeholder_text = "dd, mm, yy")
        self.entry_date.grid(row=1, column=3, pady=5)

        # label and entry for First Name
        ctk.CTkLabel(self.frame_customer, text="First Name:").grid(row=2, column=0, pady=5, padx = 10)
        self.entry_first_name = ctk.CTkEntry(self.frame_customer)
        self.entry_first_name.grid(row=2, column=1, pady=5)


        # label and entry for Last Name
        ctk.CTkLabel(self.frame_customer, text="Last Name:").grid(row=2, column=2, pady=5, padx = 30)
        self.entry_last_name = ctk.CTkEntry(self.frame_customer)
        self.entry_last_name.grid(row=2, column=3, pady=5)

        # label and entry for House number
        ctk.CTkLabel(self.frame_customer, text="House Number:").grid(row=4, column=0, pady=5)
        self.entry_house_no = ctk.CTkEntry(self.frame_customer)
        self.entry_house_no.grid(row=4, column=1, pady=5)

        # label and entry for Street number
        ctk.CTkLabel(self.frame_customer, text="Street Number:").grid(row=4, column=2, pady=5)
        self.entry_street_no = ctk.CTkEntry(self.frame_customer)
        self.entry_street_no.grid(row=4, column=3, pady=5)

        # label and entry for Town
        ctk.CTkLabel(self.frame_customer, text="Town:").grid(row=6, column=0, pady=5)
        self.entry_town = ctk.CTkEntry(self.frame_customer)
        self.entry_town.grid(row=6, column=1, pady=5)

        # label and entry for City
        ctk.CTkLabel(self.frame_customer, text="City:").grid(row=6, column=2, pady=5)
        self.entry_city = ctk.CTkEntry(self.frame_customer)
        self.entry_city.grid(row=6, column=3, pady=5)

        #Frame for products details
        self.frame_items = ctk.CTkFrame(root, corner_radius=10)
        self.frame_items.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        #label
        ctk.CTkLabel(self.frame_items, text="Product Details", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # label and entry for Particulars
        ctk.CTkLabel(self.frame_items, text="Particulars:").grid(row=1, column=0, pady=5)
        self.entry_part = ctk.CTkEntry(self.frame_items)
        self.entry_part.grid(row=1, column=1, pady=5, padx = 5)

        # label and entry for Rate
        ctk.CTkLabel(self.frame_items, text="Rate:").grid(row=2, column=0, pady=5)
        self.entry_rate = ctk.CTkEntry(self.frame_items)
        self.entry_rate.grid(row=2, column=1, pady=5)

        # label and entry for Quantity
        ctk.CTkLabel(self.frame_items, text="Quantity:").grid(row=3, column=0, pady=5)
        self.entry_qty = ctk.CTkEntry(self.frame_items)
        self.entry_qty.grid(row=3, column=1, pady=5)

        # Frame for Buttons
        self.operation_frame = ctk.CTkFrame(root, corner_radius=10)
        self.operation_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # Button to Add item
        self.btn_add_item = ctk.CTkButton(self.operation_frame, text="Add Item", command=self.add_item)
        self.btn_add_item.grid(row=0, column=0, pady=10, padx=15)

        # Button to Edit Button
        self.btn_edit_item = ctk.CTkButton(self.operation_frame, text="Edit Item", command=self.edit_item)
        self.btn_edit_item.grid(row=0, column=1, pady=10, padx=15)

        # Button to Delete item
        self.btn_delete_item = ctk.CTkButton(self.operation_frame, text="Delete Item", command=self.delete_item)
        self.btn_delete_item.grid(row=0, column=2, pady=10, padx=60)

        # Button to Clear Entries
        self.btn_clear_entries = ctk.CTkButton(self.operation_frame, text="Clear Entries", command=self.clear_entries)
        self.btn_clear_entries.grid(row=0, column=3, pady=10, padx=15)

        # Button to Generate Cash Memo
        self.btn_generate_memo = ctk.CTkButton(self.operation_frame, text="Generate Cash Memo", command=self.generate_memo)
        self.btn_generate_memo.grid(row=1, column=2, pady=10, padx=5)

        # Button to Print to PDF
        self.btn_print_pdf = ctk.CTkButton(self.operation_frame, text="Print Bill to PDF", command=self.print_to_pdf)
        self.btn_print_pdf.grid(row=1, column=1, pady=10, padx=5)

        # View for the products(table)
        self.tree = ttk.Treeview(self.frame_items, columns=("Particulars", "Rate", "Quantity"), show='headings')
        self.tree.heading("Particulars", text="Particulars")
        self.tree.heading("Rate", text="Rate")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.grid(row=0, column=2,rowspan = 4, columnspan = 3, pady=5, padx=5)

    #function for add item button
    def add_item(self):
        part = self.entry_part.get()
        rate = self.entry_rate.get()
        qty = self.entry_qty.get()


        #Exception handelling
        if not part or not rate or not qty: #particular, price, quantity should not be empty
            messagebox.showerror("Error", "Please fill all item fields.")
            return

        try:
            rate = int(rate)
            qty = int(qty)
        except ValueError:
            messagebox.showerror("Error", "Rate and Quantity should be numbers.")
            return

        self.items.append(Object(qty, part, rate))
        self.tree.insert('', 'end', values=(part, rate, qty))

        self.entry_part.delete(0, tk.END)
        self.entry_rate.delete(0, tk.END)
        self.entry_qty.delete(0, tk.END)

    def edit_item(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_index = self.tree.index(selected_item[0])  # Get index of selected item
            item = self.items[item_index]  # Retrieve item from self.items list

            # Populate entry fields with item details
            self.entry_part.delete(0, tk.END)  # Clear existing text
            self.entry_part.insert(0, item.get_part())  # Insert new text

            self.entry_rate.delete(0, tk.END)
            self.entry_rate.insert(0, item.get_rate())

            self.entry_qty.delete(0, tk.END)
            self.entry_qty.insert(0, item.get_qty())

        else:
            ctk.CTkMessageBox.show_warning("Selection Error", "Please select an item to edit.")

    def delete_item(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_item = self.tree.selection()[0]
            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Selection Error", "Please select an item to delete.")

    #Deleting each entry form 0 to end
    def clear_entries(self):
        self.entry_serial.delete(0, ctk.END)
        self.entry_date.delete(0, ctk.END)
        self.entry_first_name.delete(0, ctk.END)
        self.entry_last_name.delete(0, ctk.END)
        self.entry_house_no.delete(0, ctk.END)
        self.entry_street_no.delete(0, ctk.END)
        self.entry_town.delete(0, ctk.END)
        self.entry_city.delete(0, ctk.END)
        self.entry_part.delete(0, ctk.END)
        self.entry_rate.delete(0, ctk.END)
        self.entry_qty.delete(0, ctk.END)



    #function for generate_memo button
    def generate_memo(self):
        serial = self.entry_serial.get()
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        house_no = self.entry_house_no.get()
        street_no = self.entry_street_no.get()
        town = self.entry_town.get()
        city = self.entry_city.get()

        if not serial or not first_name or not last_name or not house_no or not street_no or not town or not city:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        try:
            serial = int(serial)
        except ValueError:
            messagebox.showerror("Error", "Serial number should be a number.")
            return

        self.create_memo(serial, first_name, last_name, house_no, street_no, town, city, self.items)

    def create_memo(self, serial, first_name, last_name, house_no, street_no, town, city, items):
        try:
            date = Date(12, 4, 2023)
            name = Name(first_name, last_name)
            address = Address(house_no, street_no, town, city)
            cash_memo = CashMemo(date, serial, name, address, items)
            messagebox.showinfo("Cash Memo", str(cash_memo))
            self.print_memo(cash_memo)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    #print Cashmemo on Terminal
    def print_memo(self, memo):
        print(memo) # repr function for Cashmemo is called here


    def print_to_pdf(self):
        serial = self.entry_serial.get()
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        house_no = self.entry_house_no.get()
        street_no = self.entry_street_no.get()
        town = self.entry_town.get()
        city = self.entry_city.get()
        #Exception Handelling
        if not serial or not first_name or not last_name or not house_no or not street_no or not town or not city:
            messagebox.showerror("Error", "Please fill all fields.")
            return
# try except
        try:
            serial = int(serial)
        except ValueError:
            messagebox.showerror("Error", "Serial number should be a number.")
            return

        # Create CashMemo object
        from_date_entry = self.entry_date.get().split("-")
        date = Date(int(from_date_entry[0]), int(from_date_entry[1]), int(from_date_entry[2]))
        name = Name(first_name, last_name)
        address = Address(house_no, street_no, town, city)
        cash_memo = CashMemo(date, serial, name, address, self.items)

        # Generate PDF
        self.generate_pdf(cash_memo)

    # Generate a PDF
    def generate_pdf(self, cash_memo):
        filename = f"cash_memo_{cash_memo.get_no()}.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        c.setFont("Helvetica", 12)

        text = str(cash_memo).split('\n')
        y = 750

        for line in text:
            c.drawString(30, y, line)
            y -= 15

        c.save()
        messagebox.showinfo("PDF Created", f"PDF generated successfully: {filename}")


#main function to call GUI window
if __name__ == "__main__":
    root = tk.Tk()
    app = CashMemoApp(root) #Cash Memo Object is generated
    root.mainloop()
