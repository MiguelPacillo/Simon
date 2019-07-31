from tkinter import *
import random

window = Tk()
window.title("Simon")
window.resizable(0, 0)
window.configure(background="black")

all = ["A", "B", "C", "D"]

cpu_sequence = ""
player_sequence = ""

round_chckr = True
cpu_round = 0
player_round = 0

def restart():

    global cpu_sequence

    cpu_sequence = ""

    start_butt.configure(text="ass")

def main():

    global cpu_sequence, round_chckr, cpu_round, player_sequence, player_round

    if round_chckr == True:

        start_butt.configure(state=DISABLED)

        cpu_sequence = cpu_sequence + random.choice(all)

        round_chckr = False

        cpu_round += 1

        player_sequence = ""
        player_round = 0

        for x in cpu_sequence:

            if x == "A":
                a_butt.after(300)
                a_butt.configure(bg="red4")
                a_butt.update()
                a_butt.after(300)
                a_butt.configure(bg="red")
                a_butt.update()

            elif x == "B":
                b_butt.after(300)
                b_butt.configure(bg="dark green")
                a_butt.update()
                b_butt.after(300)
                b_butt.configure(bg="green")
                a_butt.update()

            elif x == "C":
                c_butt.after(300)
                c_butt.configure(bg="blue4")
                a_butt.update()
                c_butt.after(300)
                c_butt.configure(bg="blue")
                a_butt.update()

            elif x == "D":
                d_butt.after(300)
                d_butt.configure(bg="yellow4")
                a_butt.update()
                d_butt.after(300)
                d_butt.configure(bg="yellow")
                a_butt.update()

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


a_butt = Button(window, bg="red", command=a_seq, state=DISABLED, height=5, width=10)
a_butt.grid(row=0, column=1)

b_butt = Button(window, bg="green", command=b_seq, state=DISABLED, height=5, width=10)
b_butt.grid(row=1, column=0)

c_butt = Button(window, bg="blue", command=c_seq, state=DISABLED, height=5, width=10)
c_butt.grid(row=1, column=2)

d_butt = Button(window, bg="yellow", command=d_seq, state=DISABLED, height=5, width=10)
d_butt.grid(row=2, column=1)

start_butt = Button(window, text="START", bg="black", fg="white", font="arial 15 bold", command=main, height=5, width=10)
start_butt.grid(row=1, column=1)


window.mainloop()