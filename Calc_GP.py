import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Taschenrechner")
        master.config(bg="lightgreen")

        # Erstelle ein Label für die Anzeige des Ergebnisses
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=0, column=0, columnspan=5, pady=6)

        # Erstelle Buttons für die Zahlen und die mathematischen Operationen
        button_values = [
            "C", "(", ")", "/"
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "%", "=",
        ]
        self.buttons = []
        for i, value in enumerate(button_values):
            button = tk.Button(master, text=value, width=5, height=2,
                               command=lambda value=value: self.button_click(value))
            row = i // 4 + 1
            col = i % 4
            button.grid(row=row, column=col)
            self.buttons.append(button)

    def button_click(self, value):
        if value == "C":
            # Lösche das Ergebnis und den aktuellen Operanden
            self.result_label.config(text="")
        elif value == "=":
            # Berechne das Ergebnis und zeige es an
            try:
                result = str(eval(self.result_label.cget("text")))
                self.result_label.config(text=result)
            except ZeroDivisionError:
                self.result_label.config(text="Fehler: Division durch Null")
            except:
                self.result_label.config(text="Fehler")
        else:
            # Füge den Button-Text zum aktuellen Operanden hinzu
            current_value = self.result_label.cget("text")
            new_value = current_value + value
            self.result_label.config(text=new_value)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
