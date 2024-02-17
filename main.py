from tkinter import *

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
wrong_button = Button(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR, image=wrong)
wrong_button.grid(column=0, row=1)

# Right Button
right = PhotoImage(file="./images/right.png")
right_button = Button(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR, image=right)
right_button.grid(column=1, row=1)




window.mainloop()