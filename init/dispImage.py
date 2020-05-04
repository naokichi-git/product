import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    #画像を読み込む
    newImage = PIL.Image.open(path).resize((300, 300))
    #そのイメージをラベルに表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imagelabel.configure(image = imageData)
    imagelabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command = openFile)
imagelabel = tk.Label()
btn.pack()
imagelabel.pack()
tk.mainloop()