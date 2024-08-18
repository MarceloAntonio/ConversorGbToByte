import tkinter as tk
import pyperclip 


root = tk.Tk()
root.title("")
root.geometry("700x300")
root.configure(background= "#DCD0FE")


def change():

  conversão = int(entry.get())

  gb = conversão * 1073741824

  labelResul.config(text = gb)
  buttonCopy.pack(pady=10)


def copy():
  pyperclip.copy(labelResul['text'])



titulo = tk.Label(root, text="Digite a quantidade de gb que deseja converter para bytes", background="#DCD0FE", font="jetbtrains")
titulo.pack(pady=10)

entry = tk.Entry(root, font="jetrains",border=0)
entry.pack(pady=10)

button = tk.Button(root, text="Converter", command=change, border=0,font="jetbtrains")
button.pack(pady=10)

labelResul = tk.Label(root, text="",background="#DCD0FE",font="jetbtrains",border=0)
labelResul.pack(pady=10)

buttonCopy = tk.Button(root, text="Copiar", command=copy,font="jetbtrains",border=0)






root.mainloop()
