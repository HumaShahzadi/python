# Assignemnt 5
# Make an app for showroom for calculation different car rent out and car sale and give the result that car rent and car sold
import tkinter as tk
from tkinter import messagebox

class Showroom:
    def __init__(self, stock):
        self.stock = stock
        self.root = tk.Tk()
        self.root.title("Car Showroom")
        self.root.geometry("600x400")
        
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # Display available cars
        self.display_label = tk.Label(self.root, text="Cars in Stock:", font=("Arial", 14))
        self.display_label.pack(pady=10)
        
        self.stock_label = tk.Label(self.root, text=", ".join(self.stock), font=("Arial", 12))
        self.stock_label.pack(pady=10)
        
        # Rent a car
        self.rent_label = tk.Label(self.root, text="Enter car to rent:", font=("Arial", 12))
        self.rent_label.pack(pady=5)
        self.rent_entry = tk.Entry(self.root)
        self.rent_entry.pack(pady=5)
        self.rent_button = tk.Button(self.root, text="Rent Car", command=self.rent_car)
        self.rent_button.pack(pady=5)
        
        # Sold out a car
        self.sold_label = tk.Label(self.root, text="Enter car to mark as sold out:", font=("Arial", 12))
        self.sold_label.pack(pady=5)
        self.sold_entry = tk.Entry(self.root)
        self.sold_entry.pack(pady=5)
        self.sold_button = tk.Button(self.root, text="Mark as Sold Out", command=self.sold_out_car)
        self.sold_button.pack(pady=5)

        # Result
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12), fg="green")
        self.result_label.pack(pady=20)

        # Remaining cars count
        self.remaining_label = tk.Label(self.root, text=f"Remaining Cars: {len(self.stock)}", font=("Arial", 12))
        self.remaining_label.pack(pady=10)
        
    def rent_car(self):
        car_to_rent = self.rent_entry.get()
        if car_to_rent in self.stock:
            self.stock.remove(car_to_rent)
            self.result_label.config(text=f"Rented: {car_to_rent}")
            self.update_stock_display()
        else:
            messagebox.showerror("Error", f"{car_to_rent} is not available for rent.")

    def sold_out_car(self):
        car_to_sell = self.sold_entry.get()
        if car_to_sell in self.stock:
            self.stock.remove(car_to_sell)
            self.result_label.config(text=f"Sold Out: {car_to_sell}")
            self.update_stock_display()
        else:
            messagebox.showerror("Error", f"{car_to_sell} is not in stock.")

    def update_stock_display(self):
        self.stock_label.config(text=", ".join(self.stock))
        self.remaining_label.config(text=f"Remaining Cars: {len(self.stock)}")

# Initial stock of cars
stock = ["Toyota", "Honda", "Ford", "BMW", "Mercedes"]

# Initialize showroom
Showroom(stock)