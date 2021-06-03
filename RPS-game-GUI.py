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
rock_img_comp = Image.open("rock.png")
paper_img_comp = Image.open("paper.png")
scissors_img_comp = Image.open("scissors.png")

rock_small_img = ImageTk.PhotoImage(rock_img.resize((int(rock_img.size[0]/1.9), int(rock_img.size[1]/1.9))))
paper_small_img = ImageTk.PhotoImage(paper_img.resize((int(paper_img.size[0]/1.9), int(paper_img.size[1]/1.9))))
scissors_small_img = ImageTk.PhotoImage(scissors_img.resize((int(scissors_img.size[0]/1.9), int(scissors_img.size[1]/1.9))))
rock_small_img_comp = ImageTk.PhotoImage(rock_img_comp.resize((int(rock_img_comp.size[0]/1.9), int(rock_img_comp.size[1]/1.9))))
paper_small_img_comp = ImageTk.PhotoImage(paper_img_comp.resize((int(paper_img_comp.size[0]/1.9), int(paper_img_comp.size[1]/1.9))))
scissors_small_img_comp = ImageTk.PhotoImage(scissors_img_comp.resize((int(scissors_img_comp.size[0]/1.9), int(scissors_img_comp.size[1]/1.9))))


rock_big_img = ImageTk.PhotoImage(rock_img)
paper_big_img = ImageTk.PhotoImage(paper_img)
scissors_big_img = ImageTk.PhotoImage(scissors_img)
rock_big_img_comp = ImageTk.PhotoImage(rock_img_comp)
paper_big_img_comp = ImageTk.PhotoImage(paper_img_comp)
scissors_big_img_comp = ImageTk.PhotoImage(scissors_img_comp)
# insert picture
user_pos1 = Label(root, image=paper_small_img, bg="#9b59b6")
user_pos2 = Label(root, image=rock_small_img, bg="#9b59b6")
user_pos3 = Label(root, image=scissors_big_img, bg="#9b59b6")
comp_pos1 = Label(root, image=paper_small_img_comp, bg="#9b59b6")
comp_pos2 = Label(root, image=rock_small_img_comp, bg="#9b59b6")
comp_pos3 = Label(root, image=scissors_big_img_comp, bg="#9b59b6")
comp_pos1.grid(row=1, column=1)
comp_pos2.grid(row=2, column=0)
comp_pos3.grid(row=2, column=2)

user_pos1.grid(row=1, column=5)
user_pos2.grid(row=2, column=6)
user_pos3.grid(row=2, column=4)

# scores
userScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=2)
userScore.grid(row=1, column=4)

# indicators
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       bg="#9b59b6", fg="white")
user_indicator.grid(row=0, column=4)
comp_indicator.grid(row=0, column=2)

# messages
msg = Label(root, font=200, bg="#9b59b6", fg="white")
msg.grid(row=6, column=3)

# update message


def updateMessage(x):
    msg['text'] = x

# update user score
def updateUserScore(playerScore):
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)


# check winner
def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage('You lose!')
            updateUserScore(computerScore)
        else:
            updateMessage('You win!')
            updateUserScore(userScore)
    elif player == "paper":
        if computer == "scissors":
            updateMessage('You lose!')
            updateUserScore(computerScore)
        else:
            updateMessage('You win!')
            updateUserScore(userScore)
    elif player == "scissors":
        if computer == "rock":
            updateMessage('You lose!')
            updateUserScore(computerScore)
        else:
            updateMessage('You win!')
            updateUserScore(userScore)

    else:
        pass


# update choices

choices = ["rock", "paper", "scissors"]


def updateChoice(userChoice):
    
# for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_pos3.configure(image=rock_big_img_comp)
        comp_pos1.configure(image=paper_small_img_comp)
        comp_pos2.configure(image=scissors_small_img_comp)
    elif compChoice == "paper":
        comp_pos3.configure(image=paper_big_img_comp)
        comp_pos2.configure(image=rock_small_img_comp)
        comp_pos1.configure(image=scissors_small_img_comp)
    else:
        comp_pos3.configure(image=scissors_big_img_comp)
        comp_pos2.configure(image=rock_small_img_comp)
        comp_pos1.configure(image=paper_small_img_comp)


# for user
    if userChoice == "rock":
        user_pos3.configure(image=rock_big_img)
        user_pos1.configure(image=paper_small_img)
        user_pos2.configure(image=scissors_small_img)
    elif userChoice == "paper":
        user_pos3.configure(image=paper_big_img)
        user_pos2.configure(image=rock_small_img)
        user_pos1.configure(image=scissors_small_img)
    else:
        user_pos3.configure(image=scissors_big_img)
        user_pos2.configure(image=rock_small_img)
        user_pos1.configure(image=paper_small_img)

    checkWin(userChoice, compChoice)

def restart_button():
  user_pos3.configure(image=scissors_big_img)
  user_pos2.configure(image=paper_small_img)
  user_pos1.configure(image=rock_small_img)
  comp_pos3.configure(image=scissors_big_img_comp)
  comp_pos2.configure(image=paper_small_img_comp)
  comp_pos1.configure(image=rock_small_img_comp)
  playerScore['text'] = '0'
  computerScore['text'] = '0'
  updateMessage(' ')


# buttons
rock = Button(root, width=20, height=2, text="ROCK",
              bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock")).grid(row=3, column=2)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("paper")).grid(row=3, column=3)
scissors = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissors")).grid(row=3, column=4)
resart = Button(root, width=20, height=2, text="RESTART",
                 bg="purple", fg="white", command= restart_button).grid(row=4, column=3, pady=20)
#two_players = Button(root, width=20, height=2, text="2-Players",
 #                bg="purple", fg="white", command= reset_button).grid(row=5, column=3)

root.mainloop()
