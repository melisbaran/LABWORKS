import tkinter as tk
from tkinter import END


r= tk.Tk()
r.title("MELİS LAB 10")
r.geometry("750x750")



def readText():
    textbox.delete("1.0", tk.END)
    with open("C:\\Users\\Melo\\Desktop\\MARVEL.txt", 'r') as f:
        textMarvel = f.read()
        textbox.insert("end", textMarvel)
        print(textbox)


def calculate():
    textbox.delete("1.0", tk.END)
    freqDict = {}
    wordList = []
    with open("C:\\Users\\Melo\\Desktop\\MARVEL.txt", 'r') as f:

     for line in f:
        wordList.append(line.split())

    for item in wordList:
        for i in item:
            if (i in freqDict):
                freqDict[i] += 1
            else:
                freqDict[i] = 1
    for allKeys in freqDict:
        print("\"", allKeys, "\"", end=" ")
        print(freqDict[allKeys], end=" ")
        print()
        str_ = (allKeys, "=", (freqDict[allKeys]))
        textbox.insert(END, str_)
        textbox.insert(END, "\n")




textbox = tk.Text(r, font=("Times New Roman", 15), height=30, width=60)

readButton= tk.Button(r, text="READ", bd=8, command=readText())
calculateButton = tk.Button(r, text="CALCULATE", bd=8, command=calculate)

textbox.pack()
readButton.pack()
calculateButton.pack()

tk.mainloop()