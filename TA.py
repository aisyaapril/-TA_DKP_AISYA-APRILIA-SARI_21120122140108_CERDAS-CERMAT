from tkinter import *
from tkinter import messagebox
import json

infoabout = """
Welcome to our quiz 🤗 

Nama saya Aisya Aprilia Sari dengan NIM 21120122140108. Tugas Akhir Praktikum DKP yang saya buat adalah program cerdas cermat.
Tercantum 7 modul yaitu Modul1 (Variabel, Array, Tipedata), Modul2 (Pengkondisian), Modul3 (Perulangan), Modul4 (Class dan Constructor), Modul5 (Function dan Method), Modul6(Getter dan Setter), dan Modul8 (GUI).

ENJOY 😎 !!!
"""
info1 = """
Waoww, kamu bisa mengerjakan dengan sangat baik 👍
Congrast 🥳 !!!
"""
info2 = """
Waduhh, dikerjakan lagi yukk 🥲
You can do it !!!
"""
info3 = """
Ehmmm 🤔 bagus sih, tapi coba kerjakan lagi
You can do it !!! 
"""
with open('quiz.json') as f:
    obj = json.load(f)
s = (obj['Soal'])
p = (obj['Pilihan'])
j = (obj['Jawaban'])

Win = Tk()
Win.title("Cerdas Cermat by Ais")
Win.geometry("770x300")
Win.resizable(FALSE, FALSE)
Win.config(background="light blue")
user_screen = Frame(background="light blue")
user_screen.pack()
root = Frame(Win, background="light blue")
root.pack_forget()

class Quiz :
    def __init__(self) :
        self.Soal_no = 0
        self.correct = 0
        self.soal = Label(root, font="Times 15", text=s[self.Soal_no], background="light blue")
        self.soal.grid(column=0, row=0, pady=15)
        self.Selected_option = IntVar()
        self.pil = self.checkbtn()
        self.display_pilihan(self.Soal_no)
        self.button()
        
    def checkbtn(self) :
        val = 0
        b = []
        while val < 3 :
            pilgan = Checkbutton(root, text=" ", variable=self.Selected_option, onvalue=val + 1, font="Times 13", background="light blue", activebackground="light blue", cursor="hand2")
            b.append(pilgan)
            pilgan.grid(pady=10)
            val += 1
        return b
        
    def display_pilihan(self, Soal_no):
        val = 0
        self.Selected_option.set(0)
        self.soal.config(text=s[Soal_no])
        for op in p[Soal_no]:
            self.pil[val]['text'] = op
            val += 1
    def button(self):
        nextbtn = Button(root, text="Next", font=("Times 15"), cursor="hand2", activebackground="light grey", command=self.nextb)
        nextbtn.grid(columnspan=2, column=0, row=4, ipady=5, ipadx=65, pady=20, padx=10)
    def checkjawaban(self, Soal_no):
        if self.Selected_option.get() == j[Soal_no]:
            return True
    def nextb(self):
        if self.checkjawaban(self.Soal_no):
            self.correct += 1
        
        self.Soal_no += 1

        if self.Soal_no == len(s):
            root.pack_forget()
            score.place(relx=.5, rely=.3,anchor=CENTER)
            back.place(relx=.5, rely=.5, anchor=CENTER)
            lagi.place(relx=.5, rely=.7, anchor=CENTER)
            score.config(text="Score anda adalah " + str(self.correct), font=("Times 15"))
            if self.correct > 5 :
                messagebox.showinfo("Cerdas Cermat by Ais", info1)
            elif self.correct < 5 :
                messagebox.showwarning("Cerdas Cermat by Ais", info2)
            else :
                self.correct == 5
                messagebox.showinfo("Cerdas Cermas by Ais", info3)
        else:
            self.display_pilihan(self.Soal_no)       

def mulai_game():
    user_screen.pack_forget()
    root.pack()

    
def kembali():
    quiz.Soal_no = 0
    quiz.correct = 0
    quiz.Selected_option.set(0)
    quiz.display_pilihan(quiz.Soal_no)
    quiz.button()
    root.pack_forget()
    user_screen.pack()
    back.place_forget()
    lagi.place_forget()
    score.place_forget() 

def mulai_lagi():
    quiz.Soal_no = 0
    quiz.correct = 0
    quiz.Selected_option.set(0)
    quiz.display_pilihan(quiz.Soal_no)
    quiz.button()
    root.pack()
    back.place_forget()
    lagi.place_forget()
    score.place_forget()
   
def about() :
    messagebox.showinfo("Cerdas Cermat by Ais", infoabout)

# Label
label1 = Label(user_screen, text="Programmazione Divertente Quiz 🖥️", font="Times 25", background="light blue")
label1.grid(columnspan=2, column=0, row=0, pady=20, padx=125)
label2 = Label(user_screen, text="You can do it!!", font="Times 20", background="light blue")
label2.grid(columnspan=2, column=0, row=1, padx=60)

# Button
score = Button(Win, relief=SUNKEN)
score.place_forget()

start = Button(user_screen, text="Mulai", activebackground="light grey", cursor="hand2", font="Times 15", relief=RIDGE, bd=5, command=mulai_game)
start.grid(columnspan=2, column=0, row=2, ipady=5, ipadx=75, pady=15, padx=10)

exit = Button(user_screen, text="Keluar", activebackground="light grey", cursor="hand2", font="Times 15", relief=RIDGE, bd=5, command=quit)
exit.grid(columnspan=2, column=0, row=3, ipady=5, ipadx=75, pady=10, padx=10)

back = Button(Win, text="Kembali", activebackground="light grey", cursor="hand2", font="Times 15", relief=RIDGE, bd=5, command=kembali)
back.place_forget()

lagi = Button(Win, text="Mulai Lagi", activebackground="light grey", cursor="hand2", font="Times 15", relief=RIDGE, bd=5, command=mulai_lagi)
lagi.place_forget()

# menu bar
menubar = Menu(Win, tearoff=0)
itemhelp = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=itemhelp)
itemhelp.add_command(label="About Us", command=about)
Win.config(menu=menubar)

quiz = Quiz()
Win.mainloop()