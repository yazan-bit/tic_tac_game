from tkinter import *
import random


#row and col are the coordinates of our player symbol(x or o)
def next_tern(row,col):
    global player
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            #put player 1 symbol inside the button
            game_btns[row][col]["text"] = player

            if check_winner() == False:
                #switch player
                player = players[1]
                label.config(text=player + " turn")

            elif check_winner() == True:
                #display the winner on a label
                label.config(text=player + " wins!")
                game_btns[row][col].config(bg ="red")            

            elif check_winner() == "tie":
                label.config(text="Tie , no winners!!")



        elif player == players[1]:
            #put player2 symbol inside button
            game_btns[row][col]["text"] = player

            if check_winner() == False:
                #switch player
                player = players[0]
                label.config(text=player + " turn")

            elif check_winner() == True:
                #display the winner on a label
                label.config(text=player + " wins!")
                game_btns[row][col].config(bg ="red")               

            elif check_winner() == "tie":
                label.config(text="Tie , no winners!!")


def check_winner():
    #check all e horizental conditions
    for row in range(3):
        for col in range(3):
            if game_btns[row][0]["text"] == game_btns[row][1]["text"] == game_btns[row][2]["text"] != "":
                return True
            
    for row in range(3):
        for col in range(3):
            if game_btns[0][col]["text"] == game_btns[1][col]["text"] == game_btns[2][col]["text"] != "":
                return True
            
    if game_btns[0][0]["text"] == game_btns[1][1]["text"] == game_btns[2][2]["text"] != "":
        return True
             
    if game_btns[0][2]["text"] == game_btns[1][1]["text"] == game_btns[2][0]["text"] != "":
        return True

    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg ="red")
        return "tie"
    
    else:
        return False
    

#check if no player wins
def check_empty_spaces():
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]["text"] == "":
                return True
    
    return False


def start_new_game():
    for row in range(3):
        for col in range(3):
            game_btns[row][col]["text"] = ""
            game_btns[row][col].config(bg ="white")



#create our game window
window = Tk()
window.title("Tix Tac")

#our players that are x or o that will be placed in the table
players = ["zen","yousef"]

#the player how will start the game will be first selected randomly
player = random.choice(players)

#those are the buttons that describe the net or the table that will be played on
game_btns = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#let's create a label for the current player
label = Label(text=player+" turn",font=('consolas',40))
label.pack(side="top")

#let's create a restart btn
restart_btn = Button(text="restart",font=('consolas',20),command=start_new_game)
restart_btn.pack(side="top")

#let's create the frame that contains the table or the 9 cels of our game field
btns_frame = Frame(window)
btns_frame.pack()

#let's create the "9*9 buttons" which the player will click on to place either x or o
for row in range(3):
    for col in range(3):

        #for each cel in our game_btns table we will place a button with a call bback function
            #we will place those buttons on btns_frame
                #at first we will fill them with empty str
                 
        game_btns[row][col] = Button(btns_frame , text="" ,font=('consolas',50),width=4,height=1,
                                     command = lambda row=row,col=col:next_tern(row,col))
        
        #I don't know what thats mean
        game_btns[row][col].grid(row=row,column =col)


window.mainloop()