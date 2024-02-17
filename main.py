from tkinter import *
import pandas
from random import choice

# -------- Flashcard generator --------
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
flashcard_dict = {row.French: row.English for (index, row) in data.iterrows()}
current_french_word = "Start"
current_english_word = "Start"
testing_started = False
def make_flashcard():
    global testing_started, flip_timer
    testing_started = True
    window.after_cancel(flip_timer)

    global current_french_word, current_english_word
    current_french_word, current_english_word = choice(list(flashcard_dict.items()))
    canvas.itemconfig(word, text=current_french_word, fill="black")
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(card_side, image=card_front)
    flip_timer = window.after(3000,show_answer)

# -------- show answer --------
def show_answer():
    if testing_started:
        canvas.itemconfig(card_side, image=card_back)
        canvas.itemconfig(language, text="English", fill="white")
        canvas.itemconfig(word, text=current_english_word, fill="white")

# -------- correct guess, remove card from list --------
def is_known():
    if testing_started:
        del flashcard_dict[current_french_word]
    make_flashcard()
    record = pandas.DataFrame(list(flashcard_dict.items()), columns=["French", "English"])
    print(record)
    record.to_csv("./data/words_to_learn.csv", index=False)


# -------- UI --------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,  background=BACKGROUND_COLOR)

flip_timer = window.after(3000, show_answer)

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
right_button = Button(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR, image=right, command=is_known)
right_button.grid(column=1, row=1)


window.mainloop()
