import tkinter as tk 
from tkinter import messagebox 



def main():
    try:
        num = int(entry.get())
        result= factorial(num)
        messagebox.showinfo("Result", f"{num}! is equal to {result}")
    except ValueError:
         messagebox.showinfo("Error", "enter a valid integer")
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

root = tk.Tk()
root.title("Factorial Calculator")

label = tk.Label(root,text="Enter a number:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Calculate", command=main)
button.pack(pady=10)

root.mainloop()


