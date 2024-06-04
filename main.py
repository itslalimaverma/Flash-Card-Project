from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current={}
learn = {}

try:
    data=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pd.read_csv("data/french_words.csv")
    learn = org_data.to_dict(orient="records")
else:
    learn=data.to_dict(orient="records") #{french: , english:},{}....
def next_card():
    global current, flip
    window.after_cancel((flip))
    current=random.choice(learn)
    canvas.itemconfig(card_title,text = "French",fill="black")
    canvas.itemconfig(card_word, text = current["French"],fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip = window.after(3000, func=flip_card)


def flip_card():
    # global current
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text = current["English"],fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    word = learn.remove(current)
    data=pd.DataFrame(learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


window=Tk()
window.title("FLASHHYY!")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip = window.after(3000, func=flip_card)

canvas=Canvas(width=800,height=526)
card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",40,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross=PhotoImage(file="images/wrong.png")
unknown=Button(image=cross,highlightthickness=0,command=next_card)
unknown.grid(row=1,column=0)

check=PhotoImage(file="images/right.png")
known=Button(image=check,highlightthickness=0,command=is_known)
known.grid(row=1,column=1)

next_card()

window.mainloop()
