import tkinter as tk

class CalculatorUI:
    def __init__(self, logic):
        self.logic = logic

        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.geometry("400x450")
        self.window.configure(bg="#f0f0f0")

        title = tk.Label(
            self.window,
            text="Calculator",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0"
        )
        title.pack(pady=15)

        self.entry1 = tk.Entry(self.window, font=("Arial", 14), width=20)
        self.entry1.pack(pady=5)

        self.entry2 = tk.Entry(self.window, font=("Arial", 14), width=20)
        self.entry2.pack(pady=5)

        self.result = tk.Label(
            self.window,
            text="Result: ",
            font=("Arial", 14),
            bg="#f0f0f0"
        )
        self.result.pack(pady=15)

        button_frame = tk.Frame(self.window, bg="#f0f0f0")
        button_frame.pack()

        tk.Button(button_frame, text="+", width=10,
                  command=lambda: self.calculate("+")).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(button_frame, text="-", width=10,
                  command=lambda: self.calculate("-")).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(button_frame, text="*", width=10,
                  command=lambda: self.calculate("*")).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(button_frame, text="/", width=10,
                  command=lambda: self.calculate("/")).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(button_frame, text="%", width=10,
                  command=lambda: self.calculate("%")).grid(row=2, column=0, padx=5, pady=5)

        tk.Button(button_frame, text="^", width=10,
                  command=lambda: self.calculate("^")).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(
            self.window,
            text="Clear",
            width=22,
            command=self.clear_entries
        ).pack(pady=10)

    def calculate(self, op):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())

            result = self.logic.calculate(a, b, op)
            self.result.config(text=f"Result: {result}")

        except ValueError:
            self.result.config(text="Result: Please enter valid numbers")

    def clear_entries(self):
        self.entry1.delete(0, tk.END)
        self.entry2.delete(0, tk.END)
        self.result.config(text="Result: ")

    def run(self):
        self.window.mainloop()
