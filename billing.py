import tkinter as tk

class RestaurantBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Restaurant Billing System")
        self.root.configure(bg='light gray')

        # Variables
        self.food_items = {
            "Burger": 5.99,
            "Pizza": 7.99,
            "Pasta": 6.49,
            "Salad": 3.99,
            "Soda": 1.99,
            "Water": 0.99
        }
        self.order = {}

        # UI Elements
        self.create_ui()

    def create_ui(self):
        self.create_title_label()
        self.create_food_selection()
        self.create_quantity_entry()
        self.create_add_remove_buttons()
        self.create_receipt_display()
        self.create_total_display()

    def create_title_label(self):
        title_label = tk.Label(self.root, text="Restaurant Billing System", font=("Arial", 24), bg="light gray")
        title_label.pack(pady=10)

    def create_food_selection(self):
        food_label = tk.Label(self.root, text="Select Food:", font=("Arial", 16), bg="light gray")
        food_label.pack()

        self.food_var = tk.StringVar()
        self.food_var.set("Burger")

        food_dropdown = tk.OptionMenu(self.root, self.food_var, *self.food_items.keys())
        food_dropdown.pack()

    def create_quantity_entry(self):
        quantity_label = tk.Label(self.root, text="Quantity:", font=("Arial", 16), bg="light gray")
        quantity_label.pack()

        self.quantity_entry = tk.Entry(self.root, font=("Arial", 16))
        self.quantity_entry.pack()

    def create_add_remove_buttons(self):
        add_button = tk.Button(self.root, text="Add Item", font=("Arial", 16), command=self.add_item)
        add_button.pack(pady=10)

        remove_button = tk.Button(self.root, text="Remove Item", font=("Arial", 16), command=self.remove_item)
        remove_button.pack()

    def create_receipt_display(self):
        receipt_label = tk.Label(self.root, text="Receipt", font=("Arial", 20), bg="light gray")
        receipt_label.pack(pady=10)

        self.receipt_text = tk.Text(self.root, font=("Arial", 14), width=40, height=10)
        self.receipt_text.pack()

    def create_total_display(self):
        total_label = tk.Label(self.root, text="Total:", font=("Arial", 18), bg="light gray")
        total_label.pack(pady=10)

        self.total_amount_label = tk.Label(self.root, text="", font=("Arial", 18), bg="light gray")
        self.total_amount_label.pack()

        calculate_button = tk.Button(self.root, text="Calculate Total", font=("Arial", 16), command=self.calculate_and_update_total)
        calculate_button.pack()

    def add_item(self):
        item = self.food_var.get()
        quantity = int(self.quantity_entry.get())

        if item in self.order:
            self.order[item] += quantity
        else:
            self.order[item] = quantity

        self.update_receipt()

    def remove_item(self):
        item = self.food_var.get()
        if item in self.order:
            del self.order[item]

        self.update_receipt()

    def calculate_total(self):
        total = sum([self.food_items[item] * self.order[item] for item in self.order])
        return total

    def update_receipt(self):
        self.receipt_text.delete(1.0, tk.END)
        total = 0
        for item, quantity in self.order.items():
            price = self.food_items[item]
            subtotal = price * quantity
            self.receipt_text.insert(tk.END, f"{item} x{quantity} = ${subtotal:.2f}\n")
            total += subtotal
        self.receipt_text.insert(tk.END, f"Total: ${total:.2f}")
        self.calculate_and_update_total()

    def calculate_and_update_total(self):
        total = self.calculate_total()
        self.total_amount_label.config(text=f"${total:.2f}")

if _name_ == "_main_":
    root = tk.Tk()
    app = RestaurantBillingSystem(root)
    root.mainloop()
