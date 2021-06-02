from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("Rock-Paper-Scissors")
root.configure(background="#9b59b6")

# picture
rock_img = Image.open("rock-user.png")
paper_img = Image.open("paper-user.png")
scissors_img = Image.open("scissors-user.png")
rock_img_user2 = Image.open("rock.png")
paper_img_user2 = Image.open("paper.png")
scissors_img_user2 = Image.open("scissors.png")

rock_small_img = ImageTk.PhotoImage(rock_img.resize((int(rock_img.size[0]/1.9), int(rock_img.size[1]/1.9))))
paper_small_img = ImageTk.PhotoImage(paper_img.resize((int(paper_img.size[0]/1.9), int(paper_img.size[1]/1.9))))
scissors_small_img = ImageTk.PhotoImage(scissors_img.resize((int(scissors_img.size[0]/1.9), int(scissors_img.size[1]/1.9))))
rock_small_img_user2 = ImageTk.PhotoImage(rock_img_user2.resize((int(rock_img_user2.size[0]/1.9), int(rock_img_user2.size[1]/1.9))))
paper_small_img_user2 = ImageTk.PhotoImage(paper_img_user2.resize((int(paper_img_user2.size[0]/1.9), int(paper_img_user2.size[1]/1.9))))
scissors_small_img_user2 = ImageTk.PhotoImage(scissors_img_user2.resize((int(scissors_img_user2.size[0]/1.9), int(scissors_img_user2.size[1]/1.9))))


rock_big_img = ImageTk.PhotoImage(rock_img)
paper_big_img = ImageTk.PhotoImage(paper_img)
scissors_big_img = ImageTk.PhotoImage(scissors_img)
rock_big_img_user2 = ImageTk.PhotoImage(rock_img_user2)
paper_big_img_user2 = ImageTk.PhotoImage(paper_img_user2)
scissors_big_img_user2 = ImageTk.PhotoImage(scissors_img_user2)
# insert picture
user1_pos1 = Label(root, image=paper_small_img, bg="#9b59b6")
user1_pos2 = Label(root, image=rock_small_img, bg="#9b59b6")
user1_pos3 = Label(root, image=scissors_big_img, bg="#9b59b6")
user2_pos1 = Label(root, image=paper_small_img_user2, bg="#9b59b6")
user2_pos2 = Label(root, image=rock_small_img_user2, bg="#9b59b6")
user2_pos3 = Label(root, image=scissors_big_img_user2, bg="#9b59b6")
user2_pos1.grid(row=1, column=1)
user2_pos2.grid(row=2, column=0)
user2_pos3.grid(row=2, column=2)

user1_pos1.grid(row=1, column=5)
user1_pos2.grid(row=2, column=6)
user1_pos3.grid(row=2, column=4)

# scores
user1Score = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
user2Score = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
user2Score.grid(row=1, column=2)
user1Score.grid(row=1, column=4)

# indicators
user1_indicator = Label(root, font=50, text="USER1", bg="#9b59b6", fg="white")
user2_indicator = Label(root, font=50, text="USER2",
                       bg="#9b59b6", fg="white")
user1_indicator.grid(row=0, column=4)
user2_indicator.grid(row=0, column=2)

# messages
msg = Label(root, font=200, bg="#9b59b6", fg="white")
msg.grid(row=6, column=3)

# update message


def updateMessage(x):
    msg['text'] = x

# update user1 score


def updateUser1Score():
    score = int(user1Score["text"])
    score += 1
    user1Score["text"] = str(score)

# update user2 score


def updateUser2Score():
    score = int(user2Score["text"])
    score += 1
    user2Score["text"] = str(score)

# check winner


def checkWin(user1, user2):
    if user1 == user2:
        updateMessage("Its a tie!!!")
    elif user1 == "rock":
        if user2 == "paper":
            updateMessage('User2 wins!')
            updateUser2Score()
        else:
            updateMessage('User1 wins')
            updateUser1Score()
    elif user1 == "paper":
        if user2 == "scissors":
            updateMessage('User2 wins!')
            updateUser2Score()
        else:
            updateMessage('User1 wins!')
            updateUser1Score()
    elif user1 == "scissors":
        if user2 == "rock":
            updateMessage('User2 wins!')
            updateUser2Score()
        else:
            updateMessage('User1 wins!')
            updateUser1Score()

    else:
        pass


# update choices

choices = ["rock", "paper", "scissors"]

def updateChoice2(user2Choice):
    # for user2
    if user2Choice == "rock":
        user2_pos3.configure(image=rock_big_img_user2)
        user2_pos1.configure(image=paper_small_img_user2)
        user2_pos2.configure(image=scissors_small_img_user2)
    elif user2Choice == "paper":
        user2_pos3.configure(image=paper_big_img_user2)
        user2_pos2.configure(image=rock_small_img_user2)
        user2_pos1.configure(image=scissors_small_img_user2)
    else:
        user2_pos3.configure(image=scissors_big_img_user2)
        user2_pos2.configure(image=rock_small_img_user2)
        user2_pos1.configure(image=paper_small_img_user2)
    global user2Chosen
    user2Chosen = user2Choice

def updateChoice1(user1Choice):
    # for user1
    if user1Choice == "rock":
        user1_pos3.configure(image=rock_big_img)
        user1_pos1.configure(image=paper_small_img)
        user1_pos2.configure(image=scissors_small_img)
    elif user1Choice == "paper":
        user1_pos3.configure(image=paper_big_img)
        user1_pos2.configure(image=rock_small_img)
        user1_pos1.configure(image=scissors_small_img)
    else:
        user1_pos3.configure(image=scissors_big_img)
        user1_pos2.configure(image=rock_small_img)
        user1_pos1.configure(image=paper_small_img)

    checkWin(user1Choice, user2Chosen)

def restart_button():
  user1_pos3.configure(image=scissors_big_img)
  user1_pos2.configure(image=rock_small_img)
  user1_pos1.configure(image=paper_small_img)
  user2_pos3.configure(image=scissors_big_img_user2)
  user2_pos2.configure(image=rock_small_img_user2)
  user2_pos1.configure(image=paper_small_img_user2)
  user1Score['text'] = '0'
  user2Score['text'] = '0'
  updateMessage(' ')


# buttons
rock2 = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice2("rock")).grid(row=3, column=0)
paper2 = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice2("paper")).grid(row=3, column=1)
scissors2 = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice2("scissors")).grid(row=3, column=2)

rock1 = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice1("rock")).grid(row=3, column=6)
paper1 = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice1("paper")).grid(row=3, column=5)
scissors1 = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice1("scissors")).grid(row=3, column=4)

resart = Button(root, width=20, height=2, text="RESTART",
                 bg="purple", fg="white", command= restart_button).grid(row=4, column=3, pady=20)
#two_players = Button(root, width=20, height=2, text="2-Players",
 #                bg="purple", fg="white", command= reset_button).grid(row=5, column=3)

root.mainloop()
