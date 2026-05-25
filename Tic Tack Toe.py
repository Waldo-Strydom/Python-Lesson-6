from tkinter import *
import random
game_over = False
turn = "player"
symbol = "X"



v_board = [
    "", "", "",
    "", "", "",
    "", "", "",
]

pc_choices = [
    0,1,2,
    3,4,5,
    6,7,8
]

win_list = [
    [0,1,2],
    [3,4,5],
    [6,7,8],

    [0,3,6],
    [1,4,7],
    [2,5,8],

    [0,4,8],
    [2,4,6]
]



def btn_clicked (i):
    if game_over==False and turn=="player":
        place(i)
    



def place(i):
    if v_board[i]=="":
       v_board[i]=symbol
       item = pc_choices.index(i)
       del pc_choices[item]
     
       btn_widget = btn_frame.winfo_children()[i]
       btn_widget.config(text=symbol)
       
       check_win()
       


def switch_turn():
    global turn, symbol
    if turn=="player":
        turn="pc"
        symbol="O"
        pc_turn()
    else:
        turn="player"
        symbol="X"
       

def check_win():
    global game_over
    for list in win_list:
        if v_board[list[0]]==symbol and v_board[list[1]]==symbol and v_board[list[2]]==symbol:
            game_over= True

            msg = Label(root, text=f"Game over {turn} won", font=("Times New Roman", 30))
            msg.pack()
    
    if game_over==False:
        full()

def full():
    print("full")
    global game_over
    count = 0
    for i in v_board:
        if i=="":
            count+=1
    if count==0:
        game_over=True
        msg = Label(root, text=f"Game over no one won", font=("Times New Roman", 30))
        msg.pack()
    else:
        root.after(500,switch_turn)

def pc_turn():
    global pc_choices
    index = random.randint(0,len(pc_choices)-1)
    i = pc_choices[index]
    place(i)



root = Tk()
root.title("Tick Tack Toe")


screen_w = 900
screen_h = 700

root.geometry(f"{screen_w}x{screen_h}")

heading = Label(root, text="Tick Tack Toe", font=("Times New Roman", 30))
heading.pack()

btn_frame = Frame(root)
btn_frame.pack(pady=20)

# row 1
btn_0 = Button(btn_frame, text="0", font=("Times New Roman", 30), bg="yellow", width=3, height=1, command= lambda i = 0:btn_clicked(i))
btn_0.grid(row=0, column=0)

btn_1 = Button(btn_frame, text="1", font=("Times New Roman", 30), bg="yellow", width=3, height=1, command= lambda i = 1:btn_clicked(i))
btn_1.grid(row=0, column=1)

btn_2 = Button(btn_frame, text="2", font=("Times New Roman", 30), bg="yellow", width=3, height=1, command= lambda i = 2:btn_clicked(i))
btn_2.grid(row=0, column=2)

# row 2
btn_3 = Button(btn_frame, text="3", font=("Times New Roman", 30), bg="yellow", width=3, height=1, command= lambda i = 3:btn_clicked(i))
btn_3.grid(row=1, column=0)

btn_4 = Button(btn_frame, text="4", font=("Times New Roman", 30), bg="yellow", width=3, height=1, command= lambda i = 4:btn_clicked(i))
btn_4.grid(row=1, column=1)

btn_5 = Button(btn_frame, text="5", font=("Times New Roman", 30), bg="yellow", width=3, height=1, command= lambda i = 5:btn_clicked(i))
btn_5.grid(row=1, column=2)

# row 3
btn_6 = Button(btn_frame, text="6", font=("Times New Roman", 30), bg="yellow", width=3, height=1, command= lambda i = 6:btn_clicked(i))
btn_6.grid(row=2, column=0)

btn_7 = Button(btn_frame, text="7", font=("Times New Roman", 30), bg="yellow", width=3, height=1, command= lambda i = 7:btn_clicked(i))
btn_7.grid(row=2, column=1)

btn_8 = Button(btn_frame, text="8", font=("Times New Roman", 30), bg="yellow", width=3, height=1, command= lambda i = 8:btn_clicked(i))
btn_8.grid(row=2, column=2)








root.mainloop()