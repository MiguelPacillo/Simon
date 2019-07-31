from tkinter import *
import random

window = Tk()
window.title("Simon")
window.resizable(0, 0)
window.configure(background="white")
window.geometry("500x500")

sequence_label = Label(window, text="", bg="white", fg="black", font="arial 20 bold")
sequence_label.grid(row=0, column=0, pady=(20, 0), padx=10)

all = ["A", "B", "C", "D"]

cpu_sequence = ""
player_sequence = ""

round_chckr = True
cpu_round = 0
player_round = 0

def restart():

    global cpu_sequence

    cpu_sequence = ""

    sequence_label.configure(text="")

def main():

    global cpu_sequence, round_chckr, cpu_round, player_sequence, player_round

    if round_chckr == True:

        cpu_sequence = cpu_sequence + random.choice(all)

        sequence_label.configure(text=str(cpu_sequence))

        round_chckr = False

        cpu_round += 1

        player_sequence = ""
        player_round = 0

        a_butt.configure(state=NORMAL)
        b_butt.configure(state=NORMAL)
        c_butt.configure(state=NORMAL)
        d_butt.configure(state=NORMAL)

def a_seq():

    global player_sequence, player_round, round_chckr, cpu_sequence

    player_sequence = player_sequence + "A"

    player_round += 1

    if player_round == cpu_round:

        if player_sequence != cpu_sequence:

            restart()

        elif player_sequence == cpu_sequence:

            round_chckr = True

            main()

def b_seq():

    global player_sequence, player_round, round_chckr, cpu_sequence

    player_sequence = player_sequence + "B"

    player_round += 1

    if player_round == cpu_round:

        if player_sequence != cpu_sequence:

            restart()

        elif player_sequence == cpu_sequence:

            round_chckr = True

            main()

def c_seq():

    global player_sequence, player_round, round_chckr, cpu_sequence

    player_sequence = player_sequence + "C"

    player_round += 1

    if player_round == cpu_round:

        if player_sequence != cpu_sequence:

            restart()

        elif player_sequence == cpu_sequence:

            round_chckr = True

            main()


def d_seq():

    global player_sequence, player_round, round_chckr, cpu_sequence

    player_sequence = player_sequence + "D"

    player_round += 1

    if player_round == cpu_round:

        if player_sequence != cpu_sequence:

            restart()

        elif player_sequence == cpu_sequence:

            round_chckr = True

            main()


a_butt = Button(window, text="A", bg="green", fg="white", font="arial 15 bold", command=a_seq, state=DISABLED)
a_butt.grid(row=2, column=0, pady=20)

b_butt = Button(window, text="B", bg="red", fg="white", font="arial 15 bold", command=b_seq, state=DISABLED)
b_butt.grid(row=2, column=1, pady=20)

c_butt = Button(window, text="C", bg="blue", fg="white", font="arial 15 bold", command=c_seq, state=DISABLED)
c_butt.grid(row=2, column=2, pady=20)

d_butt = Button(window, text="D", bg="orange", fg="white", font="arial 15 bold", command=d_seq, state=DISABLED)
d_butt.grid(row=2, column=3, pady=20)

start_butt = Button(window, text="START", bg="pink", fg="white", font="arial 15 bold", command=main)
start_butt.grid(row=2, column=4, pady=20)

window.mainloop()