import tkinter as tk


class CalculatorUI:

    def __init__(self, logic):
        self.logic = logic

        self.window = tk.Tk()
        self.window.title("Calculator App")
        self.window.geometry("350x400")

        self.show_home()

    # ---------------- HOME SCREEN ----------------
    def show_home(self):
        self.clear()

        tk.Label(
            self.window,
            text="HOME SCREEN",
            font=("Arial", 16, "bold")
        ).pack(pady=15)

        tk.Button(
            self.window,
            text="Calculator",
            width=20,
            command=self.show_calculator
        ).pack(pady=10)

        tk.Button(
            self.window,
            text="History",
            width=20,
            command=self.show_history
        ).pack(pady=10)

    # ---------------- CALCULATOR SCREEN ----------------
    def show_calculator(self):
        self.clear()

        tk.Label(
            self.window,
            text="CALCULATOR",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        self.e1 = tk.Entry(self.window)
        self.e1.pack(pady=5)

        self.e2 = tk.Entry(self.window)
        self.e2.pack(pady=5)

        self.result = tk.Label(self.window, text="Result")
        self.result.pack(pady=10)

        tk.Button(self.window, text="+", command=lambda: self.calculate("+")).pack()
        tk.Button(self.window, text="-", command=lambda: self.calculate("-")).pack()
        tk.Button(self.window, text="*", command=lambda: self.calculate("*")).pack()
        tk.Button(self.window, text="/", command=lambda: self.calculate("/")).pack()
        tk.Button(self.window, text="%", command=lambda: self.calculate("%")).pack()
        tk.Button(self.window, text="^", command=lambda: self.calculate("^")).pack()

        tk.Button(
            self.window,
            text="Back",
            command=self.show_home
        ).pack(pady=10)

    def calculate(self, op):
        try:
            a = float(self.e1.get())
            b = float(self.e2.get())

            result = self.logic.calculate(a, b, op)
            self.result.config(text=f"Result: {result}")

        except ValueError:
            self.result.config(text="Result: Invalid Input")

    # ---------------- HISTORY SCREEN ----------------
    def show_history(self):
        self.clear()

        tk.Label(
            self.window,
            text="HISTORY",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        data = self.logic.db.get_history()

        if not data:
            tk.Label(self.window, text="No history found").pack()
        else:
            for exp, res in data:
                tk.Label(self.window, text=f"{exp} = {res}").pack()

        tk.Button(
            self.window,
            text="Back",
            command=self.show_home
        ).pack(pady=10)

    # ---------------- CLEAR SCREEN ----------------
    def clear(self):
        for widget in self.window.winfo_children():
            widget.destroy()