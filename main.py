from tkinter import *
import pandas as pd
from random import choice

# -------- Flashcard generator --------
data = pd.read_csv("./data/french_words.csv")
flashcard_dict = {row.French: row.English for (index, row) in data.iterrows()}
def make_flashcard():
    canvas
    f_word, e_word = choice(list(flashcard_dict.items()))
    canvas.itemconfig(word, text=f_word, fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(card_side, image=card_front)
    canvas.after(3000, lambda: show_answer(e_word))

# -------- show answer --------
def show_answer(e_word):
    canvas.itemconfig(card_side, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=e_word, fill="white")

# -------- UI --------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,  background=BACKGROUND_COLOR)

# Flashcard
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
card_side = canvas.create_image(400,263, image=card_front)
language = canvas.create_text(400,150, text="French", font=("Ariel", 40,"italic"))
word = canvas.create_text(400,263, text="french word", font=("Ariel", 60,"bold"))


# Wrong Button
wrong = PhotoImage(file="./images/wrong.png")
wrong_button = Button(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR, image=wrong, command=make_flashcard)
wrong_button.grid(column=0, row=1)

# Right Button
right = PhotoImage(file="./images/right.png")
right_button = Button(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR, image=right, command=make_flashcard)
right_button.grid(column=1, row=1)




window.mainloop()