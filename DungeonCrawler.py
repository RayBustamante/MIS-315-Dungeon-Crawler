#In this program, I plan on creating a simple dungeon-crawler combat game inspired by several games
# such as Castle Crashers, Darkest Dungeon, Might and Magic, Dungeons and Dragons, Warhammer, etc.
# I in no way have any claims to pixel assets, art or music that is used in this program.

import tkinter
from tkinter import messagebox
from tkinter import *

from tkVideoPlayer import TkinterVideo

import csv
import time
import os

import winsound
from pygame import mixer

import random



#------------------------------------------
#Global Variables

#Variables for Hero Stats
heroLevel = 1
heroName = "Richard the Lionheart"
heroHP = 300
heroInitialHP = heroHP
heroSTR = 5
heroDEF = 5

#Variables for Hero level progression
herolevelProgression = 0
herolevelCap = 0

#Variables for xp based on enemy type
banditBounty = 10
beastmenBounty = 25
skeletonBounty = 15

#initialize the enemyHP to 0, until a battle function calls, in which a new value will be added
enemyHP = 0

#initialized variable for dropdown box values
enemySelected = ""


#------------------------------------------
#initialize mixer for sound effects
mixer.init()


def combatMenu():
    
    #grabs all the global variables that I will use
    global banditBounty
    global beastmenBounty
    global skeletonBounty
    
    global enemySelected

    global heroLevel
    global heroHP
    global heroSTR
    global heroDEF
    global heroName
    
    # Stops the previous soundtrack from playing, destroys the old window and starts a new soundtrack.
    winsound.PlaySound(None, winsound.SND_ASYNC)
    root.destroy()
    winsound.PlaySound("combatMenu", winsound.SND_ASYNC | winsound.SND_ALIAS )
    
    # Creates the tkinter window
    combatMenuWindow = tkinter.Tk()
    combatMenuWindow.title("Dungeon Crawler: Combat Menu")
    combatMenuWindow.geometry('800x720')
    combatMenuWindow.configure(background = "black")    
    
    #-------------------------------------------------------------
    #combat menu image
    combatMenuCanvas = Canvas(combatMenuWindow, width = 790, height = 290)
    combatMenuCanvas.grid(row = 0, column = 0)    
    combatMenuImage = tkinter.PhotoImage(file = './combatMenu.png')    
    combatMenuCanvas.create_image(0, 0, anchor = NW, image = combatMenuImage)
    #-------------------------------------------------------------
    #bounty poster image with Labels
    combatMenuCanvasBounty = Canvas(combatMenuWindow, width = 230, height = 80)
    combatMenuCanvasBounty.place(x=500, y=300)
    
    combatMenuImage2 = tkinter.PhotoImage(file = './bountyposter.png')    
    combatMenuCanvasBounty.create_image(0, 0, anchor = NW, image = combatMenuImage2)
    
    
    #Bounty Text Labels with unique price based on current real-time rates
    currentBanditBounty = "$" + str(banditBounty)
    currentBeastmenBounty = "$" + str(beastmenBounty)
    currentSkeletonBounty = "$" + str(skeletonBounty)
    
    #Bandit Bounty Label
    combatMenuBountyLabel1 = Label(combatMenuWindow, text = "Dead or Alive - Bandits:", font = "Gothic")
    combatMenuBountyLabel1.configure(fg = "white", bg = "black")
    combatMenuBountyLabel1.place(x=520, y=400)
    
    combatMenuBountyLabel1a = Label(combatMenuWindow, text = currentBanditBounty, font = "Gothic")
    combatMenuBountyLabel1a.configure(fg = "white", bg = "black", font=("Gothic", 15))
    combatMenuBountyLabel1a.place(x=600, y=420)  

    #Beastmen Bounty Label
    combatMenuBountyLabel2 = Label(combatMenuWindow, text = "Dead or Alive - Beastmen:", font = "Gothic")
    combatMenuBountyLabel2.configure(fg = "white", bg = "black")
    combatMenuBountyLabel2.place(x=520, y=470)
    
    combatMenuBountyLabel2a = Label(combatMenuWindow, text = currentBeastmenBounty, font = "Gothic")
    combatMenuBountyLabel2a.configure(fg = "white", bg = "black", font=("Gothic", 15))
    combatMenuBountyLabel2a.place(x=600, y=500)
    
    #Skeleton Bounty Label
    combatMenuBountyLabel3 = Label(combatMenuWindow, text = "Dead or Alive - Skeleton:", font = "Gothic")
    combatMenuBountyLabel3.configure(fg = "white", bg = "black")
    combatMenuBountyLabel3.place(x=520, y=540)
    
    combatMenuBountyLabel3a = Label(combatMenuWindow, text = currentSkeletonBounty, font = "Gothic")
    combatMenuBountyLabel3a.configure(fg = "white", bg = "black", font=("Gothic", 15))
    combatMenuBountyLabel3a.place(x=600, y=570)  
    
    #Bounty Tooptip Labels
    bountyToolTip = Label(combatMenuWindow, text = ("Tooltip: Bounties earned contribute  \n   to your Level progression. \n"), font = "Gothic")
    bountyToolTip.configure(fg = "white", bg = "black", font=("Gothic", 9))
    bountyToolTip.place(x=520, y=620)  


    #-------------------------------------------------------------
    #If a previous hero was loaded, the values will change from its initial values to the ones that was loaded.
    #All labels will reflect this!
    
    #combat menu Hero labels & entry input
    currentHeroLevel = ("Hero Level: " + str(heroLevel))
    
    #Hero Level Label
    combatMenuHeroLevel = Label(combatMenuWindow, text = currentHeroLevel, font = "Gothic")
    combatMenuHeroLevel.configure(fg = "white", bg = "black")
    combatMenuHeroLevel.place(x=50, y=300)    
    
    #Hero Name Input
    combatMenuNameLabel = Label(combatMenuWindow, text = "Name of Character:  ", font = "Gothic")
    combatMenuNameLabel.configure(fg = "white", bg = "black")
    combatMenuNameLabel.place(x=50, y=350)
    
    #Hero Name Entrybox. Contains an initial name 
    combatMenuNameBox = Entry(combatMenuWindow)
    combatMenuNameBox.place(x=50, y=380)
    combatMenuNameBox.insert(0, heroName)  
    
    #Hero Stat HP Labels
    currentHeroHP_text = "Hero Stats - Health: " + str(heroHP)
    combatMenu_HeroHP = Label(combatMenuWindow, text = currentHeroHP_text, font = "Gothic")
    combatMenu_HeroHP.configure(fg = "white", bg = "black")
    combatMenu_HeroHP.place(x=50, y=420)
    
    combatMenu_HeroHP_desc = Label(combatMenuWindow, text = "    Tooltip: How much damage your hero can take", font = "Gothic")
    combatMenu_HeroHP_desc.configure(fg = "white", bg = "black", font=("Gothic", 10))
    combatMenu_HeroHP_desc.place(x=50, y=450)   
    
    #Hero Stat STR Labels    
    currentHeroSTR_text = "Hero Stats - Strength: " + str(heroSTR)
    combatMenu_HeroSTR = Label(combatMenuWindow, text = currentHeroSTR_text, font = "Gothic")
    combatMenu_HeroSTR.configure(fg = "white", bg = "black")
    combatMenu_HeroSTR.place(x=50, y=480)

    combatMenu_HeroSTR_desc = Label(combatMenuWindow, text = "    Tooltip: Modifier for your attack moves", font = "Gothic")
    combatMenu_HeroSTR_desc.configure(fg = "white", bg = "black", font=("Gothic", 10))
    combatMenu_HeroSTR_desc.place(x=50, y=510)
    
    #Hero Stat DEF Labels    
    currentHeroDEF_text = "Hero Stats - Defence: " + str(heroDEF)
    combatMenu_HeroDEF = Label(combatMenuWindow, text = currentHeroDEF_text, font = "Gothic")
    combatMenu_HeroDEF.configure(fg = "white", bg = "black")
    combatMenu_HeroDEF.place(x=50, y=540)

    combatMenu_HeroDEF_desc = Label(combatMenuWindow, text = "    Tooltip: Flat Damage Reduction", font = "Gothic")
    combatMenu_HeroDEF_desc.configure(fg = "white", bg = "black", font=("Gothic", 10))
    combatMenu_HeroDEF_desc.place(x=50, y=570)   
     

    #-------------------------------------------------------------
    # Enemy Dropdown Selection Label
    combatMenu_EnemyLabel = Label(combatMenuWindow, text = "Enemy Dropdown Selection: ", font = "Gothic")
    combatMenu_EnemyLabel.configure(fg = "white", bg = "black")
    combatMenu_EnemyLabel.place(x=50, y=600)
    
    # Dropdown box. Whenever the user picks an enemy, the function getValueDropdown is called, grabbing the dropdown value to be used for battle selection
    combatMenu_Dropdown_desc = StringVar()
    combatMenu_Dropdown_desc.set("Who do you want to hunt?")
    combatMenu_Dropdown = OptionMenu(combatMenuWindow, combatMenu_Dropdown_desc, "Bandit", command=getValueDropdown)
    combatMenu_Dropdown.place(x=50, y=620)
    
    
    #-------------------------------------------------------------
    # Create Start Button and MainLoop
    
    #Start battle button will start the function battleSelection() and pass two parameters, the window and the name inputted.
    startBattle = Button(combatMenuWindow, text='Start Battle', width=15, height=1, bd='5', command = lambda: battleSelection(combatMenuWindow, combatMenuNameBox))  
    startBattle.place(x=340, y=620)    
    
    combatMenuWindow.mainloop()
    
    return combatMenuWindow
    
def getValueDropdown(selection):
    
    #Grabs the value of the dropdown menu upon selection and automatically attaches value to global enemySelected variable    
    varTemp = selection
    
    #calls global variable and attachs new value from groupdown menu
    global enemySelected    
    enemySelected = str(varTemp)
    
def battleSelection(combatMenuWindow, combatMenuNameBox):
    
    #Once the parameters pass, it will be assigned to two new variables
    global heroName
    guiWindow = combatMenuWindow    
    nameInput = combatMenuNameBox.get()
    
    #Assigned new name if user inputted a new name into global variable.
    heroName = nameInput
    
    #This function checks to see which enemy was selected and to run a battle scenario of that particular enemy type.
    global enemySelected
    
    enemyType = str(enemySelected)
    
    #If function to decide which enemy was selected. Because of time constraint, I was only able to finish one enemy battle situation
    if(enemyType == "Bandit"):
        
        #When the user picks the bandit option, the previous window will close and start the battleBandit() function. I did this
        # as a workaround as I had troubles open and closing windows.
        guiWindow.destroy()
        banditBattle()
        
    elif(enemyType =="Beastmen"):
        
        #Message popup saying that the Beastmen battle scenario is still in development
        messagebox.showinfo("Beastmen Selected", "Sorry, still under development!")
        
    elif(enemyType =="Skeleton"):
        
        #message popup saying that the Skekelton battle scenario is still in development
        messagebox.showinfo("Skeleton Selected", "Sorry, still under development!")
        
    else:
        messagebox.showerror('Error', 'Please select an enemy to fight!')
    

def banditBattle():
    
    #This is the window screen for the Bandit Battle
    
    #Grabs global variables to be used in this window
    global heroName
    global heroLevel
    global enemyHP
    
    #initialize the enemy hp. Since this is the banditBattle, all bandit options will always have 50 HP
    enemyHP = 50
    
    #Closes previous soundtrack and starts new battle OST
    winsound.PlaySound(None, winsound.SND_ASYNC)
    winsound.PlaySound("battleOST", winsound.SND_ASYNC | winsound.SND_ALIAS )
    
    #Creates the bandit battle window
    banditBattle = tkinter.Tk()
    banditBattle.title("Dungeon Crawler: Bandits")
    banditBattle.geometry('800x500')
    banditBattle.configure(background = "black")       
    
    
    #-------------------------------------------------------------
    #combat menu image
    banditCanvas = Canvas(banditBattle, width = 790, height = 290)
    banditCanvas.grid(row = 0, column = 0)    
    image2 = tkinter.PhotoImage(file = './banditBattleScreen.png')    
    banditCanvas.create_image(0, 0, anchor = NW, image = image2)

    #-------------------------------------------------------------
    #Hero Name labels and Bandit Name
    
    characterText = "Lvl " + str(heroLevel) + " - " + heroName
    
    slash_LabelTitle = Label(banditBattle, text = characterText, font = "Gothic")
    slash_LabelTitle.configure(fg = "white", bg = "black", font=("Gothic", 13))
    slash_LabelTitle.place(x=30, y=250)
    
    slash_LabelTitle = Label(banditBattle, text = "Drakwald Bandit", font = "Gothic")
    slash_LabelTitle.configure(fg = "white", bg = "black", font=("Gothic", 13))
    slash_LabelTitle.place(x=640, y=250)    

    #-------------------------------------------------------------
    #Slash label and button with description
    slash_Button = Button(banditBattle, text='Slash Attack', width=20, height=2, bd='10', command = create_windowSlashAnimation)  
    slash_Button.place(x=100, y=380)
    
    slash_LabelTitle = Label(banditBattle, text = "Slash Attack: \n Deals 200% STR damage against your opponents. ", font = "Gothic")
    slash_LabelTitle.configure(fg = "white", bg = "black", font=("Gothic", 10))
    slash_LabelTitle.place(x=20, y=320)
    
    #-------------------------------------------------------------
    #Charge label and button with description
    charge_Button = Button(banditBattle, text='Bull Charge', width=20, height=2, bd='10', command = create_windowChargeAnimation)  
    charge_Button.place(x=500, y=380)
    
    charge_LabelTitle = Label(banditBattle, text = "Bull Charge: \n 100% STR damage & 50% chance for 3x damage. ", font = "Gothic")
    charge_LabelTitle.configure(fg = "white", bg = "black",font=("Gothic", 10))
    charge_LabelTitle.place(x=420, y=320)
    
    
    banditBattle.mainloop()


def close_videoBanditAttackAnimation1(win):
    global heroLevel
    global heroHP
    global heroSTR
    global heroDEF
    global heroName
    global enemyHP    
    
    if win.winfo_exists():
        win.destroy()
        time.sleep(1.5)
        mixer.music.load("metalSound.wav")
        mixer.music.play()
        #Combat description
        print("The bandit charges you, smashing with great force, dealing 10 damage!")
            
        #Bandit damage initialization.
        banditDamage1 = 10
            
        #Hero def value will stop some (or all) of the damage dealt) 
        defCalculation = 10 - heroDEF
            
        #Hero HP calculation is done
        heroHP = heroHP - defCalculation
            
        #More combat description
        time.sleep(1.5)
        print("...")
            
        #Combat description showing user the damage dealth
        print(str(heroName) + " defends himself, using his DEF " + str(heroDEF) + " to only take " + str(defCalculation) + " damage!")
        print(str(heroName) + ": HP " + str(heroHP))
            
        #starts the defeatWindow() function to check if hero died.
        defeatWindow() 

def create_windowBanditAttackAnimation1():
    
    #The pygame mixer plays a soundfile that is located in the local folder where this game is based. This is the hero's voice
    
    window = tkinter.Toplevel()
    window.lift()
    window.geometry('700x500') 

    player = TkinterVideo(master=window, scaled=True)
    player.load("banditAttackAnimation.mp4")
    player.pack(expand=True, fill="both")

    window.after(3000, close_videoBanditAttackAnimation1, window) # close win after 2 sec
    player.bind("<<Ended>>", lambda event: close_videoBanditAttackAnimation1(window)) # close the win if video ended

    player.play() # play the video


def close_videoBanditAttackAnimation2(win):
    global heroLevel
    global heroHP
    global heroSTR
    global heroDEF
    global heroName
    global enemyHP    
    
    if win.winfo_exists():
        win.destroy()
        time.sleep(1.5)
        mixer.music.load("slashSound.wav")
        mixer.music.play()
        print("The bandit marches towards you with a glacing blow, dealing 8 damage!")
            
        banditDamage2 = 8
            
        defCalculation = 8 - heroDEF
            
        heroHP = heroHP - defCalculation

        time.sleep(1.5)
        print("...")

        print(str(heroName) + " defends himself, using his DEF " + str(heroDEF) + " to only take " + str(defCalculation) + " damage!")
        print(str(heroName) + ": HP " + str(heroHP))
        defeatWindow() 

def create_windowBanditAttackAnimation2():
    
    #The pygame mixer plays a soundfile that is located in the local folder where this game is based. This is the hero's voice
    
    window = tkinter.Toplevel()
    window.lift()
    window.geometry('700x500') 

    player = TkinterVideo(master=window, scaled=True)
    player.load("banditAttack2-Finished.mp4")
    player.pack(expand=True, fill="both")

    window.after(3000, close_videoBanditAttackAnimation2, window) # close win after 2 sec
    player.bind("<<Ended>>", lambda event: close_videoBanditAttackAnimation2(window)) # close the win if video ended

    player.play() # play the video

def close_videoBanditAttackAnimation3(win):
    global heroLevel
    global heroHP
    global heroSTR
    global heroDEF
    global heroName
    global enemyHP    
    
    if win.winfo_exists():
        win.destroy()
        time.sleep(1.5)
        mixer.music.load("thudSound.wav")
        mixer.music.play()
        print("The bandit goes berserk, slamming his body against you, dealing 15 damage!")
            
        banditDamage3 = 15
            
        defCalculation = 15 - heroDEF
            
        heroHP = heroHP - defCalculation

        time.sleep(1.5)
        print("...")

        print(str(heroName) + " defends himself, using his DEF " + str(heroDEF) + " to only take " + str(defCalculation) + " damage!")
        print(str(heroName) + ": HP " + str(heroHP))
        defeatWindow()

def create_windowBanditAttackAnimation3():
    
    #The pygame mixer plays a soundfile that is located in the local folder where this game is based. This is the hero's voice
    
    window = tkinter.Toplevel()
    window.lift()
    window.geometry('700x500') 

    player = TkinterVideo(master=window, scaled=True)
    player.load("banditAttack3-Finished.mp4")
    player.pack(expand=True, fill="both")

    window.after(3000, close_videoBanditAttackAnimation3, window) # close win after 2 sec
    player.bind("<<Ended>>", lambda event: close_videoBanditAttackAnimation3(window)) # close the win if video ended

    player.play() # play the video



def close_videoSlashAnimation(win):
    if win.winfo_exists():
        win.destroy()
        time.sleep(1.5)
        heroSlashAttack()

def create_windowSlashAnimation():
    
    #The pygame mixer plays a soundfile that is located in the local folder where this game is based. This is the hero's voice
    mixer.music.load("heroAttack1.mp3")
    mixer.music.play()
    
    window = tkinter.Toplevel()
    window.lift()
    window.geometry('700x500') 

    player = TkinterVideo(master=window, scaled=True)
    player.load("hero_Slash.mp4")
    player.pack(expand=True, fill="both")

    window.after(3000, close_videoSlashAnimation, window) # close win after 2 sec
    player.bind("<<Ended>>", lambda event: close_videoSlashAnimation(window)) # close the win if video ended

    player.play() # play the video
    
  

def heroSlashAttack():
    
    #This function calculates the damage done towards the bandit. It will also conduct a return attack from the bandits.
    
    #Grabs global variables that will be used in this function.
    
    
    global heroLevel
    global heroHP
    global heroSTR
    global heroDEF
    global heroName
    global enemyHP
    
    #initialize damage value incase of unexpected errors
    damageValue = 0

    #-------------------------------------------------------------
    #Using pygame, I was able to play sounds like sword clanks whilst also having background music play
    #Waits for 1.5 seconds before second sound of the sword hitting its mark
    
    mixer.music.load("slashSound.wav")
    mixer.music.play()
    
    #calculation of the damage. Since its Slash Attack, the damage value is 200% of hero's STR rating
    damageValue = heroSTR * 2
    
    #terminal text to keep track of whats happening
    print(" ")
    print(str(heroName) + " strikes with a wide arc, using his STR of " + str(heroSTR) + " to deal " + str(damageValue) + " to the Bandit")
    
    #enemy HP calculation
    enemyHP = int(enemyHP) - int(damageValue)
    
    #wait timer as well as text descrption
    time.sleep(1.5)
    print(" ")    
    print("...")
    print("Drakwald Bandit HP: " + str(enemyHP))
    #-------------------------------------------------------------
    # random number generator with initial variable value
    varNum = 0
    varNum = random.randint(1,3)
    
    #If function to check to see if enemyHP reaches 0 or below.
    if(enemyHP <= 0):
        
        #If HP reaches zero, the victory screen function will popup
        victoryWindow()
    else:
        
        #If enemy is still alive, it will broadcast its move
        print(" ")
        print("The bandit prepares a move...")
        time.sleep(1.5)
        print("...")
        time.sleep(1.5)
        print("...")
        time.sleep(1.5)
        print("...")
        
        #Because the number generator has only 3 values, it gives it a 30% chance to do one of three possible attacks
        if(varNum == 1):
            #Bandit grunts and attack sound
            mixer.music.load("brutishGrunt.wav")
            mixer.music.play()
            
            create_windowBanditAttackAnimation1()
            
            
        elif(varNum == 2):
            mixer.music.load("annoyedGrunt.wav")
            mixer.music.play()
            
            create_windowBanditAttackAnimation2()
               
        elif(varNum == 3):
            mixer.music.load("brutishGrunt.wav")
            mixer.music.play()

            create_windowBanditAttackAnimation3()
            


def close_videoChargeAnimation(win):
    if win.winfo_exists():
        win.destroy()
        time.sleep(1.5)
        heroChargeAttack()

def create_windowChargeAnimation():
    
    #The pygame mixer plays a soundfile that is located in the local folder where this game is based. This is the hero's voice
    mixer.music.load("heroAttack2.mp3")
    mixer.music.play()
    
    window = tkinter.Toplevel()
    window.lift()
    window.geometry('700x500') 

    player = TkinterVideo(master=window, scaled=True)
    player.load("chargeAnimation.mp4")
    player.pack(expand=True, fill="both")

    window.after(2000, close_videoSlashAnimation, window) # close win after 2 sec
    player.bind("<<Ended>>", lambda event: close_videoChargeAnimation(window)) # close the win if video ended

    player.play() # play the video            
        
    
def heroChargeAttack():
    
    global heroLevel
    global heroHP
    global heroSTR
    global heroDEF
    global heroName
    global enemyHP

    #------------------------------------------------------------- 
    
    damageValue = 0
    damageValue = heroSTR * 1
    
    print(" ")
    print(str(heroName) + " bull charges at the foe, using his STR of " + str(heroSTR) + " to slam and deal " + str(damageValue) + " to the Bandit")
   
    time.sleep(1.5)
    mixer.music.load("thudSound.wav")
    mixer.music.play()
    
    varNum = 0
    varNum = random.randint(1,2)
    if(varNum == 1):
        damageValue = damageValue * 3
        
        print("Critical Hit! " + str(heroName) + " did " + str(damageValue) + " of bonus damage!")        
        
    
    elif(varNum == 2):
        print("Critical Miss! The Bandit avoided much of the heavy blow")
    
    enemyHP = enemyHP - damageValue
    
    time.sleep(1.5)
    print(" ")
    print("...")
    print("Drakwald Bandit HP: " + str(enemyHP))
    #-------------------------------------------------------------        
    varNum = 0
    varNum = random.randint(1,3)
    
    if(enemyHP <= 0):
        victoryWindow()
    else:
        #-------------------------------------------------------------     
        print(" ")
        print("The bandit prepares a move...")
        time.sleep(1.5)
        print("...")
        time.sleep(1.5)
        print("...")
        time.sleep(1.5)
        print("...")
        
        if(varNum == 1):
            mixer.music.load("brutishGrunt.wav")
            mixer.music.play()
            time.sleep(1.5)
            mixer.music.load("metalSound.wav")
            mixer.music.play()
            print("The bandit charges you, smashing with great force, dealing 10 damage!")
            
            banditDamage1 = 10
            
            defCalculation = 10 - heroDEF
            
            heroHP = heroHP - defCalculation
            
            time.sleep(1.5)
            print("...")
            
            print(str(heroName) + " defends himself, using his DEF " + str(heroDEF) + " to only take " + str(defCalculation)  + " damage!")
            print(str(heroName) + ": HP " + str(heroHP))
            defeatWindow()            
            
            
        elif(varNum == 2):
            mixer.music.load("annoyedGrunt.wav")
            mixer.music.play()
            time.sleep(1.5)
            mixer.music.load("slashSound.wav")
            mixer.music.play()
            print("The bandit marches towards you with a glacing blow, dealing 8 damage!")
            
            banditDamage2 = 8
            
            defCalculation = 8 - heroDEF
            
            heroHP = heroHP - defCalculation

            time.sleep(1.5)
            print("...")

            print(str(heroName) + " defends himself, using his DEF " + str(heroDEF) + " to only take " + str(defCalculation) + " damage!")
            print(str(heroName) + ": HP " + str(heroHP))
            defeatWindow()
               
        elif(varNum == 3):
            mixer.music.load("brutishGrunt.wav")
            mixer.music.play()
            time.sleep(1.5)
            mixer.music.load("thudSound.wav")
            mixer.music.play()
            print("The bandit goes berserk, slamming his body against you, dealing 15 damage!")
            
            banditDamage3 = 15
            
            defCalculation = 15 - heroDEF
            
            heroHP = heroHP - defCalculation

            time.sleep(1.5)
            print("...")

            print(str(heroName) + " defends himself, using his DEF " + str(heroDEF) + " to only take " + str(defCalculation)  + " damage!")
            print(str(heroName) + ": HP " + str(heroHP))
            defeatWindow()
    
def defeatWindow():
    
    #function to check to see if hero died. I made it so that it is almost impossible to die because of how strong your hero is.
    # For the purpose of this project, I wanted to make my game dummy proof to show that it works.
    global heroHP
    
    #Regardless, if SOMEHOW you died, a message will popup saying in Mushu's voice (the dragon from Mulan), mocking you on how you were able to lose against such an easy opponent!
    if(heroHP <= 0):
        messagebox.showinfo("You lost?!", "Mushu from Mulan: You lost?! How could you lose! It was so easy for you! \n \n Your hero has died by the hands of your enemy! Thanks for playing and please try again!")
        #Once the message is done, the program will close and you would have to try again.
        quit()
  
  
def victoryWindow():
    
    #Victory function for when your enemy reaches 0 HP
    
    #Grabs global variables to be used for the level upgrade
    global heroLevel
    global heroInitialHP
    global heroSTR
    global heroDEF
    global heroName
    global banditBounty
    global herolevelCap
    
    #Turns off battle OSt and starts victory soundtrack
    winsound.PlaySound(None, winsound.SND_ASYNC)
    winsound.PlaySound("victoryOST", winsound.SND_ASYNC | winsound.SND_ALIAS )
    
    #Calculations to check to see the level cap. Its based on heroLevel * 7. So hero level 3 would have a cap of 21 xp.
    levelCap = heroLevel * 7
    
    #Grabs the xp earnd from bandit.
    levelXPEarned = banditBounty 
    
    #if the xp earned exceeds cap, a new level is earned!
    if(levelXPEarned > levelCap):
        
        print("Leveling Up!")
        
        #grabs the leftover xp to be used for next level progression
        levelProgression = levelXPEarned - levelCap
        
        #For every 1+ level, the following are added to the character stats.
        new_HeroLevel = heroLevel + 1
        new_HeroHP = heroInitialHP + 20
        new_HeroSTR = heroSTR + 1
        new_HeroDEF = heroDEF + 2
        
        newLevelCap = new_HeroLevel * 7
        
        #assign all the data into an array/list
        listData = [heroName, new_HeroLevel, new_HeroHP, new_HeroSTR, new_HeroDEF, levelProgression, newLevelCap]
        
        #Write the list into a csv file which will contain the hero's stats.
        with open("heroSaveFile.csv", "w") as file:
            writer = csv.writer(file)
            
            writer.writerow(listData)
        
        # Initialize string which will contain information about level upgrade and progression
        victoryText = ("You've defeated your opponent!\n \n Current Bounty on Bandit: " + str(banditBounty) + "xp"
                        + "\n \n New Level Earned!" +
                       "\n \n Name: " + str(heroName) + 
                       "\n Level: " + str(heroLevel) + " + 1"
                       "\n HP: " + str(heroInitialHP) + " + 20"
                       "\n STR: " + str(heroSTR) + " + 1"
                       "\n DEF: " + str(heroDEF) + " + 2"
                        + "\n \n Current Level Progression: " + str(levelProgression) + "xp / " + str(newLevelCap) + "xp" + " \n \n Character saved! Thank you for playing!")
        
        #Message box will appear showing the victory text and a congradulations.
        messagebox.showinfo("Victory!", victoryText)
        
        #when done, it will close the program.
        quit()
    else:
        
        print("No Progress!")
        
        new_HeroLevel = heroLevel 
        new_HeroHP = heroInitialHP 
        new_HeroSTR = heroSTR 
        new_HeroDEF = heroDEF
        newLevelCap = new_HeroLevel 
        #If no level upgrade has been reached, the calculations will still happen, just not with the new added values. Old values are kept. Only the xp is saved.
        levelProgression = levelXPEarned - levelCap
        listData = [heroName, new_HeroLevel, new_HeroHP, new_HeroSTR, new_HeroDEF, levelProgression, newLevelCap]
        
        
        #Write the list into a csv file which will contain the hero's stats.
        with open("heroSaveFile.csv", "w") as file:
            writer = csv.writer(file)
            
            writer.writerow(listData)
        
        victoryText = ("You've defeated your opponent! \n \n Current Bounty on Bandit: " + str(banditBounty) + "xp"
                   + "\n Current Level Progression: " + str(levelXPEarned) + "xp / " + str(levelCap) + "xp")

        #closes program.
        quit()
    
                        #Initial Startscreen GUI setup
#-------------------------------------------------------------

def loadSave():
    
    #Grabs all global variable for the player character including xp progresion
    global heroLevel 
    global heroName 
    global heroHP 
    global heroInitialHP 
    global heroSTR 
    global heroDEF 

    global herolevelProgression 
    global herolevelCap   
    
    #creates an array to store the csv data
    loadArray = []
    
    #a counter to keep track of which data I want to assign
    counter = 0
    
    #Opens the csv file
    try:
        with open('heroSaveFile.csv', 'r') as file:
                
            read = csv.reader(file)
            
            #iterates through the csv file
            for lines in read:
                
                #A counter will be used to determine which data gets assgined. In  this case, the first data value will be
                # the name of the character, the second data value will be his level, and so forth.
                if(counter == 0):
                    heroName = (lines[0])
                    counter = counter + 1
                if(counter == 1):
                    heroLevel = int(lines[1])
                    counter = counter + 1
                if(counter == 2):
                    heroHP = int(lines[2])
                    counter = counter + 1
                if(counter == 3):
                    heroSTR = int(lines[3])
                    counter = counter + 1
                if(counter == 4):
                    heroDEF = int(lines[4])
                    counter = counter + 1
                if(counter == 5):
                    herolevelProgression = int(lines[5])
                    counter = counter + 1
                if(counter == 6):
                    herolevelCap = int(lines[6])
                    counter = counter + 1
            #upon completion, a message box will alert the user that it was successful, as well as what data was retrieved.
            victoryText = ("Character loaded successfully! "
                            + " " +
                           "\n \n Name: " + str(heroName) + 
                           "\n Level: " + str(heroLevel) + " "
                           "\n HP: " + str(heroHP) + " "
                           "\n STR: " + str(heroSTR) + " "
                           "\n DEF: " + str(heroDEF) + " "
                            + "\n \n Current Level Progression: " + str(herolevelProgression) + "xp / " + str(herolevelCap) + "xp" + " \n \n ")
        
            messagebox.showinfo("Victory!", victoryText)
          
        #When done, launches the combatMenu which will now contain the new global variables
        combatMenu()        
        
    except:
        #Should there be no file found, an error message will shoot.
        messagebox.showerror("Error!", "No save file found! \n You must play the game for a save file to be created!")
        

                        #Initial Startscreen GUI setup
#-------------------------------------------------------------
#tkinter initialization
root = tkinter.Tk()
root.title("Sooo totally not Darkest Dungeon rip-off")
root.geometry('800x500')
root.configure(background = "black")       
#-------------------------------------------------------------
# startscreen Image
canvas = Canvas(root, width = 790, height = 290)
canvas.grid(row = 0, column = 0)    
image1 = tkinter.PhotoImage(file = './openScreen.png')    
canvas.create_image(0, 0, anchor = NW, image = image1)
#-------------------------------------------------------------
# Two button widgets, one to start a new game and the other to start loadSave() function      
newGameButton = Button(root, text='New Game', width=40, height=5, bd='10', command= combatMenu)
newGameButton.place(x=50, y=330)
    
loadGameButton = Button(root, text='Load Previous Save', width=40, height=5, bd='10', command = loadSave)
loadGameButton.place(x=450, y=330)
#-------------------------------------------------------------
#Background Soundtrack Music
winsound.PlaySound("soundtrack", winsound.SND_ASYNC | winsound.SND_ALIAS )
root.mainloop()
