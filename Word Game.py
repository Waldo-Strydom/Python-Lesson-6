from tkinter import *

import random
q_list = []
answer_list = []
all_answers = []
answer_class = ""
answer = ""
output = ""
show_questions = True 

board_list =      ["?", "?", "?",
                "?", "?", "?",
                "?", "?", "?"]

remove_list =      [0, 1, 2,
                    3, 4, 5,
                    6, 7, 8]

alphabet = ["A", "B", "C", "D", "E",
            "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y",
            "Z"
]
root = Tk()
root.title("Word game")
screen_w = 1000
screen_h = 800
root.geometry(f"{screen_w}x{screen_h}")
root.configure(bg="#67f5f0")

class Question:
    def __init__(self,id,answer,question):
        self.id = id
        self.answer = answer
        self.question = question
      

    def populate_board(self):
        global board_list
        i = 0
        while i<len(self.answer):
            ran = random.randint(0,len(remove_list)-1)
            ind = remove_list[ran]
            board_list[ind] = self.answer[i]
            del remove_list[ran]
            i+=1

        i=0
        while i<len(remove_list):
             ran = random.randint(0,len(alphabet)-1)
             ind = remove_list[i]
             board_list[ind]=alphabet[ran]
             i+=1
       
    




cat = Question(0,"CAT","I can purr.")
dog = Question(1,"DOG", "I'm man's best friend.")
bee = Question(2,"BEE", "I make honey.")

q_list.append(cat)
q_list.append(dog)
q_list.append(bee)

def make_Board():
    global board_list

    for btn in letter_frame.winfo_children():
        btn.destroy()

    row = 0
    col = 0

    for space in board_list:
        
        if col<=2:
                letter_btn = Button(letter_frame, text=space, font=("Arial",30), bg="#424747", fg="#eb8023", activebackground="#eb8023", activeforeground="#424747",  width=10, height=2,command=lambda b=space: letter_clicked(b))
                letter_btn.grid(row=row,column=col,padx=5,pady=5,sticky="nsew")
                col+=1
        else:
            row+=1
            col=0
            letter_btn = Button(letter_frame, text=space,font=("Arial",30), bg="#424747", fg="#eb8023", activebackground="#eb8023", activeforeground="#424747", width=10, height=2,command=lambda b=space: letter_clicked(b))
            letter_btn.grid(row=row,column=col,padx=5,pady=5,sticky="nsew")
            # have students fix by adding line below
            col+=1
  

def show_q_list():
     for question in question_frame.winfo_children():
         question.destroy()

         

     for question in q_list:
         q = Label(question_frame,text=question.question, font=("Arial", 30),bg="#424747", fg="#eb8023")
         q.pack(fill="x", expand=True, ) 

         all_answers.append(question.answer)


def pick_question():
    global answer, answer_class
    ran = random.randint(0,len(q_list)-1)
    # ran=0
    answer = q_list[ran].answer
    answer_class = q_list[ran]
    for l in answer:
         answer_list.append(l)
    
   


def show_hide_questions():
    global show_questions
    if show_questions:
        question_frame.grid_remove()
        show_questions = False
    else:
        question_frame.grid()
        show_questions = True

def letter_clicked(b):
    global output
    output+=b
    word_out.config(text=output)
    word_out.grid()
    i =0
    while i<len(all_answers):
        print(f"{all_answers[i]}  {output}  {all_answers}")
        if all_answers[i]==output:
            del all_answers[i]
            del q_list[i]
            output = ""
            word_out.config(text=output)
            main()
        i+=1

def main():
    global show_questions
    if len(q_list)>0:
        show_q_list()
        pick_question()
        answer_class.populate_board()
        word_out.grid_remove()
        make_Board()
    else:
        word_out.config(text="Game finished")
        show_questions = True
        show_hide_questions()
        letter_frame.grid_remove()

        
def clear():
    global output
    output = ""
    word_out.config(text=output) 
    word_out.grid_remove()

root.columnconfigure((0,1,2,3,4),weight=1)
  

questions_btn = Button(root, text="Show Questions", font=("Times New Roman", 20,"bold"), bg="#424747", fg="#eb8023", activebackground="#eb8023", activeforeground="#424747", command=show_hide_questions)
questions_btn.grid(row=0, column=4,  )


question_frame = Frame(root, bg="#424747", highlightthickness=5, borderwidth= 5, highlightbackground="#3d4040", relief="raised")
question_frame.grid(row=0, column=1, columnspan=3, ipady=20, ipadx=70 )
question_frame.rowconfigure(0, weight=1)

word_out = Label(root, text="",font=("Arial",50), bg="#424747", fg="#eb8023", activebackground="#eb8023", activeforeground="#424747", )
word_out.grid(row=1, column=0, columnspan=3)

clear_btn = Button(root, text="Clear", font=("Times New Roman", 20,"bold"), bg="#424747", fg="#eb8023", activebackground="#eb8023", activeforeground="#424747", command=clear)
clear_btn.grid(row=1, column=4, )

letter_frame = Frame(root, bg="#eb8023", highlightthickness=5, borderwidth= 5, highlightbackground="#3d4040", relief="raised")
letter_frame.grid(row=2,column=0, columnspan=5, pady=30)
letter_frame.rowconfigure((0,1,2),weight=1)
letter_frame.columnconfigure((0,1,2),weight=1)






main()
root.mainloop()

