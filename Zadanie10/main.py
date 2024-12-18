import tkinter as tk
import random

class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jednoręki Bandyta")
        self.root.geometry("400x400")
        self.root.configure(bg="#e6f7ff")

        self.symbols = [1, 1, 1, 2, 3, 4, 5]  
        self.balance = 200  

        self.create_widgets()

    def create_widgets(self):
        self.label1 = self.create_symbol_label()
        self.label1.grid(row=0, column=0, padx=20, pady=20)

        self.label2 = self.create_symbol_label()
        self.label2.grid(row=0, column=1, padx=20, pady=20)

        self.label3 = self.create_symbol_label()
        self.label3.grid(row=0, column=2, padx=20, pady=20)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 24), bg="#e6f7ff")
        self.result_label.grid(row=1, column=0, columnspan=3, pady=20)

        self.balance_label = tk.Label(self.root, text=f"Saldo: {self.balance} zł", font=("Helvetica", 18), bg="#e6f7ff")
        self.balance_label.grid(row=2, column=0, columnspan=3, pady=10)

        self.spin_button = tk.Button(self.root, text="Zakręć", command=self.spin, font=("Helvetica", 18), bg="#007acc", fg="white", bd=0, relief="flat")
        self.spin_button.grid(row=3, column=0, columnspan=3, pady=20)

    def create_symbol_label(self):
        label = tk.Label(self.root, text="", font=("Helvetica", 48), width=2, borderwidth=5, relief="groove", bg="#ffffff")
        return label

    def spin(self):
        if self.balance <= 0:
            self.result_label.config(text="Brak środków!", fg="red")
            return

        self.balance -= 10  

        result1 = random.choice(self.symbols)
        result2 = random.choice(self.symbols)
        result3 = random.choice(self.symbols)

        self.animate_label(self.label1, result1)
        self.animate_label(self.label2, result2)
        self.animate_label(self.label3, result3)

        if result1 == result2 == result3:
            win_amount = 50
            self.balance += win_amount
            self.result_label.config(text=f"Wygrana! +{win_amount} zł", fg="green")
        else:
            self.result_label.config(text="Spróbuj ponownie!", fg="red")

        self.balance_label.config(text=f"Saldo: {self.balance} zł")

    def animate_label(self, label, result):
        original_color = label.cget("bg")
        label.config(bg="#ffcc66")
        label.after(100, lambda: label.config(bg=original_color, text=result))

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()
