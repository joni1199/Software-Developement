import tkinter as tk

window = tk.Tk()
window.geometry('150x220')
window.title('Taschenechner')

gui_items = list()
button_values = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 '+', '-', '*', '/', '=', 'AC']

calculation = str()

def create_button(value):
    button = tk.Button(text=value)
    gui_items.append(button)

for val in button_values:
    create_button(val)

output_label = tk.Label(text='Hallo')
output_label.grid(row=0, columnspan=10)

column_count = 0
row_count = 1
max_columns = 3

for item in gui_items:
    item.grid(row=row_count, column=column_count)

    column_count += 1
    if column_count == max_columns:
        column_count = 0
        row_count += 1

if __name__ == '__main__':
    window.mainloop()