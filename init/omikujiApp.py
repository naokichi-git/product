import tkinter as tk
import random

def dispLabel():
    kuji = ["大吉", "中吉", "小吉", "凶"]
    lbl.configure(text = random.choice(kuji))

root = tk.Tk()
root.geometry("400x200")

lbl = tk.Label(text = "運勢を占おう！")
btn = tk.Button(text = "クリック", command = dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()