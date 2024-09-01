from tkinter import *
import random
import os
#from playsound import playsound - couldnt get module to work on replit worked on my Desktop IDE


#Establish main window with title
root = Tk()
root.title("Spanish Vocabulary")
root.geometry('650x550' )
root.resizable(False, False)

#Establish global variables
master_list = []
vocab_list=[]
correct_words=[]
voc_index=0
counter = 0
selection1="0"
selection2="0"
button_check = []
removed_buttons=[]
number_guesses=0
number_error = 0

#Button creation
button_spanish1 = Button(root, padx=40, pady=20, width=8, fg='black', text="word", bd =10,command= lambda :button_click_spanish(button_spanish1))
button_spanish2 = Button(root, padx=40, pady=20, width=8, fg='black',text="word", bd =10,command= lambda :button_click_spanish(button_spanish2))
button_spanish3 = Button(root, padx=40, pady=20, width=8, fg='black',text="word", bd =10,command= lambda :button_click_spanish(button_spanish3))
button_spanish4 = Button(root, padx=40, pady=20, width=8, fg='black',text="word", bd =10,command= lambda :button_click_spanish(button_spanish4))
button_spanish5 = Button(root, padx=40, pady=20, width=8, fg='black',text="word", bd =10,command= lambda :button_click_spanish(button_spanish5))

button_english1 = Button(root, padx=40, pady=20, width=8, fg='black',text="word", bd =10, command= lambda :button_click_english(button_english1))
button_english2 = Button(root, padx=40, pady=20, width=8, fg='black',text="word", bd =10, command= lambda :button_click_english(button_english2))
button_english3 = Button(root, padx=40, pady=20, width=8, fg='black',text="word", bd =10, command= lambda :button_click_english(button_english3))
button_english4 = Button(root, padx=40, pady=20, width=8, fg='black',text="word", bd =10, command= lambda :button_click_english(button_english4))
button_english5 = Button(root, padx=40, pady=20, width=8, fg='black',text="word",bd =10, command= lambda :button_click_english(button_english5))


#Group buttons based on language so that the columns will stay uniform
english_buttons = [button_english1, button_english2, button_english3, button_english4, button_english5]
spanish_buttons = [button_spanish1, button_spanish2, button_spanish3, button_spanish4, button_spanish5]


#function pool

#Establish master list from txt file
#Expandanle idea - make list user specific to track score and mastered words/trouble words
def grab_master_list():
    fin = open('vocab.txt', 'r')
    for line in fin:
        line=line.replace('\n','').split(", ")
        print(line)
        master_list.append(line)
    fin.close()

#First function to set the board/buttons/lists
def reset_words():
    global english_buttons, spanish_buttons

    english_buttons = [button_english1, button_english2, button_english3, button_english4, button_english5]
    spanish_buttons = [button_spanish1, button_spanish2, button_spanish3, button_spanish4, button_spanish5]
    random_list()
    assign_english()
    assign_spanish()

#using random module first pulling/removing 5 pairs from master list
def random_list():
    for x in range(5):
        vac_index = random.randrange(0, len(master_list)-1)
        vocab_list.append(master_list[vac_index])
        master_list.remove(master_list[vac_index])
      
#assigning buttons using random so that they are in scrabbled order
def assign_english():
    bank=[0,1,2,3,4]
    used_n=[]
    for button in english_buttons:
            print(button)
            n = random.choice(bank)
            button['text'] = vocab_list[n][0]
            button['fg'] = 'black'
            button['state'] = 'normal'
            used_n.append(n)
            bank.remove(n)
      
#assigning buttons using random so that they are in scrabbled order
def assign_spanish():
    bank=[0,1,2,3,4]
    used_n=[]
    for button in spanish_buttons:
            n = random.choice(bank)
            button['text'] = vocab_list[n][1]
            button['fg'] = 'black'
            button['state'] = 'normal'
            used_n.append(n)
            bank.remove(n)

#function for button is selected it resets all in column to black and then sets the button selected
def selected_button(selected_button, language_button):
    for button in language_button:
       button['fg'] = 'black'
    selected_button['fg'] = 'green'
    #playsound('touch.wav') - module doesnt work in Replit



#fuctions to grab text in button to compair to match list
def button_click_english(button):
    global selection1
    selection1= button['text']
    selected_button(button, english_buttons)
    check_match(button)
  
def button_click_spanish(button):
    global selection2
    selection2= button['text']
    selected_button(button, spanish_buttons)
    check_match(button)


#functions to reset button to default color if incorrectly guessed
def reset_english():
    for button in english_buttons:
         button['fg'] = 'black'

def reset_spanish():
    print("reset_spanish called")
    for button in spanish_buttons:
        button['fg'] = 'black'

#function to create pop up window when level is complete
def score_window(score):
    scoreWindow = Toplevel(root)
    scoreWindow.title("Congratulations!")
    scoreWindow.geometry("300x200+175+175")
    Label(scoreWindow, text = score).pack()

    #conditional to react if master list is out of match pair, i.e. end of game
    if len(master_list) > 5:
        Label(scoreWindow, text="Would you like to play again?").pack()
        Button(scoreWindow, text="Yes", command=lambda: [reset_words(), scoreWindow.destroy()]).pack()
        Button(scoreWindow, text="Exit", command=root.destroy).pack()
    else:
        Label(scoreWindow, text="Congratulations you have completed all matches!").pack()
        Button(scoreWindow, text="Exit", command=root.destroy).pack()


#function to pull correctly guessed pairs out of the vocab list so that they will not be reset
#fuction triggers pop up window function when all pairs are guessed correctly
def set_to_win(remove_list):
    global number_error, number_guesses
    for button in removed_buttons:
            if button in english_buttons:
                english_buttons.remove(button)
            elif button in spanish_buttons:
                spanish_buttons.remove(button)
            else:
                pass
    if len(removed_buttons)%10 == 0:
        score = "You had {} accuracy on that round.".format(int(((number_error/number_guesses)-1)*-100))
        score_window(score)
        vocab_list.clear()
    else:
        pass

#function to compair two selected buttons to vocab_list to see if there is a match adds matchs to removed_buttons for settings updates
#triggers function set_to_match
def check_match(button):
    global button_check, selection1, selection2, number_error, number_guesses
    button_check.append(button)
    user_guess = [selection1, selection2]

    #check to see if two buttons match
    if "0" not in user_guess:
        number_guesses += 1
        if user_guess in vocab_list:
            #playsound('success.wav') - module doesn't work in replit
            for button in button_check:
                removed_buttons.append(button)
                button['state']= 'disabled'
            button_check = []
            selection1= "0"
            selection2= "0"
            set_to_win(removed_buttons)


        else:
            print(user_guess)
            #playsound('error.wav') - mod doesnt work in replit
            button_check = []
            selection1= '0'
            selection2= '0'
            number_error += 1
            reset_english()
            reset_spanish()


    else:
        return


# Window Styling


#Gaps and Labels 
wholeGap1 = Label(root, text= "     Spanish Vocabulary Matching Game", font =('Times', 20, 'bold'), pady=30)
wholeGap2 = Label(root, text= " ", font = 20, padx=35, pady=30)
wholeGap3 = Label(root, text= " ", font = 20, padx=45, pady=30)
wholeGap4 = Label(root, text= " ", font = 20, padx=45, pady=30)
wholeGap5 = Label(root, text= " ", font = 20, padx=35, pady=30)

#Button placement

#Spanish row 1
button_spanish1.grid(row=1, column=1)
button_spanish2.grid(row=2, column=1)
button_spanish3.grid(row=3, column=1)
button_spanish4.grid(row=4, column=1)
button_spanish5.grid(row=5, column=1)


#English row 2
button_english1.grid(row=1, column=4)
button_english2.grid(row=2, column=4)
button_english3.grid(row=3, column=4)
button_english4.grid(row=4, column=4)
button_english5.grid(row=5, column=4)

#Gap and Label placement
wholeGap1.grid(row=0, column=0, columnspan=5)
#wholeGap2.grid(row=1, column=0, rowspan=4)
wholeGap4.grid(row=1, column=3, rowspan=4)
#wholeGap5.grid(row=1, column=5, rowspan=4)


#starts the game
grab_master_list()
reset_words()
root.mainloop()