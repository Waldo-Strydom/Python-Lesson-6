from tkinter import *
decode = True
encrypted_text = ""
decrypted_text = ""
plain_text = ""
cypher_list = []
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def display():
    plain.config(text=plain_text)
    if decode:
        msg.config(text=decrypted_text)
    else:
        msg.config(text=encrypted_text)


def clear():
    print("clear")
    global encrypted_text, decrypted_text, plain_text
    encrypted_text = ""
    decrypted_text = ""
    plain_text = ""

    display()

def btn_clicked(button):
    global plain_text
    let = button
    plain_text+=let
    display()

def create_Cypher(prop):
    global cypher_list, letters
    print("prop",prop)
    shift = 0
    shift = int(prop)
    start = 26-shift
    while start!=26:
        cypher_list.append(letters[start])
        start+=1
    stopper = cypher_list[0]
    i=0
    while letters[i]!=stopper:
        cypher_list.append(letters[i])
        i+=1
    print(cypher_list)


def decrypt():
    global cypher_list, letters, plain_text,decrypted_text
    decrypted_text=""
    for l in plain_text:
        for c in cypher_list:
            if l == c:
                i = cypher_list.index(c)
                decrypted_text+=letters[i]
    display()

def encrypt():
    global cypher_list, letters, plain_text,decrypted_text
    decrypted_text=""
    for l in plain_text:
        for c in cypher_list:
            if l==c:
                print(c,l)
                i = letters.index(l)
                print(i)
                decrypted_text+=cypher_list[i]
    display()

root = Tk()
root.title("Cypher")
bg_img = PhotoImage(file="./Assets/RomanEagle.png")
# Tk.
root.configure(bg="#040403")

screen_w = 900
screen_h = 700

root.geometry(f"{screen_w}x{screen_h}")


key_options = []

i = 1
while i<=26:
    key_options.append(i)
    i+=1
print(key_options)

key = StringVar(root)
key.set(key_options[0])


bg_label = Label(root, image=bg_img, )
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

heading = Label(root, text="Cypher", font=("Arial", 16, "bold"))
heading.pack(side="top", fill="none", expand=False, pady= 20)

dropdown = OptionMenu(root, key, *key_options, command=create_Cypher)
dropdown.pack(side="top", fill="none", expand=False, pady= 20)

plain = heading = Label(root, text="Plain Text", font=("Arial", 16, "bold"))
plain.pack(side="top", fill="none", expand=False, pady= 20)

msg = heading = Label(root, text="Message", font=("Arial", 16, "bold"))
msg.pack(side="top", fill="none", expand=False, pady= 20)

btn_frame = Frame(root,)
btn_frame.pack(side="top", fill="none", expand=False,)

ctrl_frame = Frame(root, width=70, )
ctrl_frame.pack(side="top", fill="none", expand=False,pady=(30,0))


clear_btn = Button(ctrl_frame,text="Clear", font=("Arial", 16, "bold"), command= clear)
clear_btn.grid(row=0,column=0, sticky="W", padx=(0,180))


decrypt_btn = Button(ctrl_frame,text="Decrypt", font=("Arial", 16, "bold"),command= decrypt)
decrypt_btn.grid(row=0,column=3, sticky="N", padx=(90,90))

encrypt_btn = Button(ctrl_frame,text="Encrypt", font=("Arial", 16, "bold"), command=encrypt )
encrypt_btn.grid(row=0,column=5, sticky="E", padx=(180,0))



col = 0
for btn in letters:
    # print(letters.index(btn))
    if letters.index(btn)<13:
        btn = Button(btn_frame, text=btn, font=("Arial", 16, "bold"), width=4, command=lambda b=btn: btn_clicked(b) )
        btn.grid(row=0, column=col, sticky="N")
        col+=1
        if col>=13:
            col= 0
    else:
        btn = Button(btn_frame, text=btn, font=("Arial", 16, "bold"), width=4,command=lambda b=btn: btn_clicked(b))
        btn.grid(row=1, column=col, sticky="N")
        col+=1
        # if col>=13:
        #     col= 0
    

# btns = Widget.winfo_children()
# for btn in btns:




root.mainloop()
