# Importing
import pygame
import os
import ast
import random
import sys
import googletrans

homepath = os.getcwd()

account = input("Which account do you want? new for new account")

#Creating a new account
if account == "new":
    newaccountname = input("What is the new account name?")
if account == "new" and os.path.isdir(os.getcwd() + "/Files/" + newaccountname) == False:
    UserPath = os.getcwd() + "/Files/" + newaccountname
    os.mkdir(UserPath)
    os.mkdir(UserPath+"/Files")
    os.mkdir(UserPath+"/Settings")
    os.chdir(UserPath)
    langforcreate = input("What language do you speak (Google Translate Code)?")
    file = open("Settings/setup","w+")
    file.write("f")
    file.close()
    file = open("Settings/lang","w+")
    file.write(langforcreate)
    file.close()
elif account == "new":
    print("That Account Exists, Opening It Now.")
if account == "new":
    account=newaccountname
else:
    if os.path.isdir(os.getcwd() + "/Files/" + account) == False:
        sys.exit("That account does not exist.")

# Pathways
AppDataPath = homepath + "/App Data"
FilesPath = homepath + "/Files/"+account+"/Files"
SettingsPath = homepath + "/Files/"+account+"/Settings"

# Logging in
os.chdir(SettingsPath)
file = open("setup","r")
file.seek(0)
loaded = file.read()
file.close()
os.chdir(SettingsPath)
file = open("lang","r")
lang = file.read()
file.close()
translator = googletrans.Translator()
if loaded =="t":
    file = open("username","r")
    file.seek(0)
    username = file.read()
    file.close()
    file = open("password","r")
    file.seek(0)
    password = file.read()
    file.close()
    loop = True
    loopnum = 0
    while loop:
        guess = [input(translator.translate("What is your username?",dest=lang).text),input(translator.translate("What is you password?",dest=lang).text)]
        if guess == [username,password]:
            running = True
            loop = False
        else:
            loopnum += 1
            print(translator.translate("Wrong username and/or password",dest=lang).text)
        if loopnum == 3:
            print(translator.translate("You ran out of guesses.",dest=lang).text)
            loop = False
            running = False
elif loaded == "f":
    username = input(translator.translate("What do you want your username to be?",dest=lang).text)
    password = input(translator.translate("What do you want your password to be?",dest=lang).text)
    file = open("username","w+")
    file.write(username)
    file.close()
    file = open("password","w+")
    file.write(password)
    file.close()
    file = open("backnum","w+")
    file.write("1")
    file.close()
    file = open("setup","w")
    file.seek(0)
    file.write("t")
    file.close()
    sys.exit(translator.translate("You will have to restart the program to log in.",dest=lang).text)

# Initalizing and Setting Up Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
# Setting up icon image
os.chdir(AppDataPath+"/universal")
icon=pygame.Surface((32,32))
icon.set_colorkey((0,0,0))
rawicon=pygame.image.load("logo.png")
for i in range(0,32):
    for j in range(0,32):
        icon.set_at((i,j), rawicon.get_at((i,j)))
pygame.display.set_icon(icon)

window = pygame.display.set_mode([600,600])

# Variables
screen = "Home"
WHITE = (255,255,255)
editfile = ""
loaded = False
bank_logginnum = 0
bank_loggedin = False

# Functions
def background(backgroundpic):
    os.chdir(AppDataPath+"/universal")
    backpic = pygame.image.load("back"+str(backgroundpic)+".png")
    window.blit(backpic,(0,0))

def openfile(filename):
    os.chdir(FilesPath)
    file = open(str(filename),"r")
    file.seek(0)
    lines = file.read().splitlines()
    file.close()
    return lines

def printer(text,lang=lang):
    print(translator.translate(text,dest=lang).text)

def popup(question,lang=lang):
    question = translator.translate(question,dest=lang).text
    return langsys.transto(input(question),"en")

class music():
    def playeffect(path,sound):
        os.chdir(path)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(sound))
    class background():
        def play(path,song):
            os.chdir(path)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(song))
        def stop():
            pygame.mixer.Channel(0).stop()
        def pause():
            pygame.mixer.Channel(0).pause()
        def unpause():
            pygame.mixer.Channel(0).unpause()
        def playsong(path,numofsongs):
            if pygame.mixer.Channel(0).get_busy() == False:
                numofsong = random.randint(1,numofsongs)
                music.background.play(path,"song"+str(numofsong)+".wav")
    def stopeffect():
        pygame.mixer.Channel(1).stop()

class bank():
    def deposit(accountnum,loggedin,amount):
        printer("Work in Progress")
    def withdraw(accountnum,loggedin,amount):
        printer("Work in Progress")
    def transfer(accountnumfrom,loggedin,accountnumto,amount):
        printer("Work in Progress")
    def balancecheck(accountnum):
        printer("Work in Progress")
    def loggin(accountnum):
        printer("Work in Progress")

class langsys():
    def transto(text,lang):
        transtext = translator.translate(text,dest=lang)
        return transtext.text
    def detectlang(text):
        translang = translator.detect(text)
        return translang.lang

def tsplit(s, sep):
    stack = [s]
    for char in sep:
        pieces = []
        for substr in stack:
            pieces.extend(substr.split(char))
        stack = pieces
    return stack

# Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # Saving
            # Pixlr
            if screen == "Pixlr":
                os.chdir(FilesPath)
                filename = str(editfile)
                file = open(filename,"w")
                file.write("Pixlr")
                for x in color:
                    file.write("\n")
                    file.write(str(x))
                file.close()

    # All Pre-Draw Screen Things
    # Veriable Settings
    mousepos = pygame.mouse.get_pos()
    mouseclicks = pygame.mouse.get_pressed()
    buttons_pressed = pygame.key.get_pressed()
    window.fill(WHITE)
    # Saved Veriables
    os.chdir(SettingsPath)
    file = open("backnum","r")
    file.seek(0)
    backpic = int(file.read())
    file.close()

    # Home Screen
    if screen == "Home":
        pygame.display.set_caption("Home")
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        background(backpic)
        # music.background.playsong(AppDataPath+""/universal"",7)"
        os.chdir(AppDataPath+"/home")
        folder_app = pygame.image.load("Folder App.png")
        folder_files = pygame.image.load("Folder Files.png")
        settings_pic = pygame.image.load("Settings Pic.png")
        browser_pic = pygame.image.load("Browser Pic.png")
        window.blit(folder_app,(100,100))
        window.blit(folder_files,(250,100))
        window.blit(settings_pic,(400,100))
        window.blit(browser_pic,(100,250))
        if mouseclicks[0] == True and mousepos[0] >= 100 and mousepos[0] <= 200 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            screen = "Apps"
            rest = True
            pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 250 and mousepos[0] <= 350 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            level = 1
            screen = "Files"
            rest = True
            pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 400 and mousepos[0] <= 500 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            screen = "Settings"
            rest = True
            pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 100 and mousepos[0] <= 200 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            screen = "Apps"
            rest = True
            pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 100 and mousepos[0] <= 200 and mousepos[1] >= 250 and mousepos[1] <= 350 and rest == False:
            screen = "Browser"
            site = ""
            rest = True
            pygame.time.wait(100)
        
    # Apps View Screen
    if screen == "Apps":
        pygame.display.set_caption("Apps")
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        background(backpic)
        os.chdir(AppDataPath+"/universal")
        back_arrow = pygame.image.load("Back Arrow.png")
        os.chdir(AppDataPath+"/apps")
        calc_icon = pygame.image.load("Calc Icon.png")
        pixlr_icon = pygame.image.load("Pixlr Icon.png")
        window.blit(back_arrow,(100,100))
        window.blit(calc_icon,(250,100))
        window.blit(pixlr_icon,(400,100))
        if mouseclicks[0] == True and mousepos[0] >= 100 and mousepos[0] <= 200 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            screen = "Home"
            rest = True
            pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 250 and mousepos[0] <= 350 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            screen = "Calc"
            rest = True
            pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 400 and mousepos[0] <= 500 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            screen = "Pixlr"
            editfile = ""
            loaded = False
            rest = True
            pygame.time.wait(100)

    # Files View Screen
    if screen == "Files":
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        blocks = ((100,100),(250,100),(400,100),(100,250),(250,250),(400,250),(100,400),(250,400),(400,400))
        pygame.display.set_caption("Files - Screen "+str(level))
        background(backpic)
        os.chdir(AppDataPath+"/universal")
        back_arrow = pygame.image.load("Back Arrow.png")
        os.chdir(AppDataPath+"/files")
        back = pygame.image.load("back.png")
        next_arrow = pygame.image.load("next.png")
        file = pygame.image.load("file.png")
        os.chdir(FilesPath)
        listy = os.listdir(FilesPath)
        numoffiles = len(listy)
        window.blit(back_arrow,(100,100))
        window.blit(back,(100,250))
        window.blit(next_arrow,(400,250))
        # File Stuff
        if level * 6 - 5 <= numoffiles:
            lines = openfile(listy[level * 6 - 6])
            if lines[0] == "Pixlr":
                pos = ((0,0),(75,0),(150,0),(225,0),(300,0),(375,0),(450,0),(525,0),(0,75),(75,75),(150,75),(225,75),(300,75),(375,75),(450,75),(525,75),(0,150),(75,150),(150,150),(225,150),(300,150),(375,150),(450,150),(525,150),(0,225),(75,225),(150,225),(225,225),(300,225),(375,225),(450,225),(525,225),(0,300),(75,300),(150,300),(225,300),(300,300),(375,300),(450,300),(525,300),(0,375),(75,375),(150,375),(225,375),(300,375),(375,375),(450,375),(525,375),(0,450),(75,450),(150,450),(225,450),(300,450),(375,450),(450,450),(525,450),(0,525),(75,525),(150,525),(225,525),(300,525),(375,525),(450,525),(525,525))
                color = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                for x in range(64):
                    color[x] = ast.literal_eval(lines[x + 1])
                for x in range(64):
                    pygame.draw.rect(window,color[x],(blocks[1][0]+(pos[x][0]/6),blocks[1][1]+(pos[x][1]/6),(100/8),100/8))
            else:
                window.blit(file,blocks[1])
        if level * 6 - 4 <= numoffiles:
            lines = openfile(listy[level * 6 - 5])
            if lines[0] == "Pixlr":
                pos = ((0,0),(75,0),(150,0),(225,0),(300,0),(375,0),(450,0),(525,0),(0,75),(75,75),(150,75),(225,75),(300,75),(375,75),(450,75),(525,75),(0,150),(75,150),(150,150),(225,150),(300,150),(375,150),(450,150),(525,150),(0,225),(75,225),(150,225),(225,225),(300,225),(375,225),(450,225),(525,225),(0,300),(75,300),(150,300),(225,300),(300,300),(375,300),(450,300),(525,300),(0,375),(75,375),(150,375),(225,375),(300,375),(375,375),(450,375),(525,375),(0,450),(75,450),(150,450),(225,450),(300,450),(375,450),(450,450),(525,450),(0,525),(75,525),(150,525),(225,525),(300,525),(375,525),(450,525),(525,525))
                color = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                for x in range(64):
                    color[x] = ast.literal_eval(lines[x + 1])
                for x in range(64):
                    pygame.draw.rect(window,color[x],(blocks[2][0]+(pos[x][0]/6),blocks[2][1]+(pos[x][1]/6),(100/8),100/8))
            else:
                window.blit(file,blocks[2])
        if level * 6 - 3 <= numoffiles:
            lines = openfile(listy[level * 6 - 4])
            if lines[0] == "Pixlr":
                pos = ((0,0),(75,0),(150,0),(225,0),(300,0),(375,0),(450,0),(525,0),(0,75),(75,75),(150,75),(225,75),(300,75),(375,75),(450,75),(525,75),(0,150),(75,150),(150,150),(225,150),(300,150),(375,150),(450,150),(525,150),(0,225),(75,225),(150,225),(225,225),(300,225),(375,225),(450,225),(525,225),(0,300),(75,300),(150,300),(225,300),(300,300),(375,300),(450,300),(525,300),(0,375),(75,375),(150,375),(225,375),(300,375),(375,375),(450,375),(525,375),(0,450),(75,450),(150,450),(225,450),(300,450),(375,450),(450,450),(525,450),(0,525),(75,525),(150,525),(225,525),(300,525),(375,525),(450,525),(525,525))
                color = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                for x in range(64):
                    color[x] = ast.literal_eval(lines[x + 1])
                for x in range(64):
                    pygame.draw.rect(window,color[x],(blocks[4][0]+(pos[x][0]/6),blocks[4][1]+(pos[x][1]/6),(100/8),100/8))
            else:
                window.blit(file,blocks[4])
        if level * 6 - 2 <= numoffiles:
            lines = openfile(listy[level * 6 - 3])
            if lines[0] == "Pixlr":
                pos = ((0,0),(75,0),(150,0),(225,0),(300,0),(375,0),(450,0),(525,0),(0,75),(75,75),(150,75),(225,75),(300,75),(375,75),(450,75),(525,75),(0,150),(75,150),(150,150),(225,150),(300,150),(375,150),(450,150),(525,150),(0,225),(75,225),(150,225),(225,225),(300,225),(375,225),(450,225),(525,225),(0,300),(75,300),(150,300),(225,300),(300,300),(375,300),(450,300),(525,300),(0,375),(75,375),(150,375),(225,375),(300,375),(375,375),(450,375),(525,375),(0,450),(75,450),(150,450),(225,450),(300,450),(375,450),(450,450),(525,450),(0,525),(75,525),(150,525),(225,525),(300,525),(375,525),(450,525),(525,525))
                color = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                for x in range(64):
                    color[x] = ast.literal_eval(lines[x + 1])
                for x in range(64):
                    pygame.draw.rect(window,color[x],(blocks[6][0]+(pos[x][0]/6),blocks[6][1]+(pos[x][1]/6),(100/8),100/8))
            else:
                window.blit(file,blocks[6])
        if level * 6 - 1 <= numoffiles:
            lines = openfile(listy[level * 6 - 2])
            if lines[0] == "Pixlr":
                color = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                for x in range(64):
                    color[x] = ast.literal_eval(lines[x + 1])
                for x in range(64):
                    pygame.draw.rect(window,color[x],(blocks[7][0]+(pos[x][0]/6),blocks[7][1]+(pos[x][1]/6),(100/8),100/8))
            else:
                window.blit(file,blocks[7])
        if level * 6 - 0 <= numoffiles:
            lines = openfile(listy[level * 6 - 1])
            if lines[0] == "Pixlr":
                pos = ((0,0),(75,0),(150,0),(225,0),(300,0),(375,0),(450,0),(525,0),(0,75),(75,75),(150,75),(225,75),(300,75),(375,75),(450,75),(525,75),(0,150),(75,150),(150,150),(225,150),(300,150),(375,150),(450,150),(525,150),(0,225),(75,225),(150,225),(225,225),(300,225),(375,225),(450,225),(525,225),(0,300),(75,300),(150,300),(225,300),(300,300),(375,300),(450,300),(525,300),(0,375),(75,375),(150,375),(225,375),(300,375),(375,375),(450,375),(525,375),(0,450),(75,450),(150,450),(225,450),(300,450),(375,450),(450,450),(525,450),(0,525),(75,525),(150,525),(225,525),(300,525),(375,525),(450,525),(525,525))
                color = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
                for x in range(64):
                    color[x] = ast.literal_eval(lines[x + 1])
                for x in range(64):
                    pygame.draw.rect(window,color[x],(blocks[8][0]+(pos[x][0]/6),blocks[8][1]+(pos[x][1]/6),(100/8),100/8))
            else:
                window.blit(file,blocks[8])
        if mouseclicks[0] == True and mousepos[0] >= 100 and mousepos[0] <= 200 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            screen = "Home"
            rest = True
            pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 400 and mousepos[0] <= 500 and mousepos[1] >= 250 and mousepos[1] <= 350 and rest == False:
            if level * 6 + 1 <= numoffiles:
                level += 1
                rest = True
                pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 100 and mousepos[0] <= 200 and mousepos[1] >= 250 and mousepos[1] <= 350 and rest == False:
            if level != 1:
                level -= 1
                rest = True
                pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 250 and mousepos[0] <= 350 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            if level * 6 - 5 <= numoffiles:
                lines = openfile(listy[level * 6 - 6])
                screen = lines[0]
                editfile = str(listy[level * 6 - 6])
                loaded = False
                rest = True
                pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 400 and mousepos[0] <= 500 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            if level * 6 - 4 <= numoffiles:
                lines = openfile(listy[level * 6 - 5])
                screen = lines[0]
                editfile = str(listy[level * 6 - 5])
                loaded = False
                rest = True
                pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 250 and mousepos[0] <= 350 and mousepos[1] >= 250 and mousepos[1] <= 350 and rest == False:
            if level * 6 - 3 <= numoffiles:
                lines = openfile(listy[level * 6 - 4])
                screen = lines[0]
                editfile = str(listy[level * 6 - 4])
                loaded = False
                rest = True
                pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 100 and mousepos[0] <= 200 and mousepos[1] >= 400 and mousepos[1] <= 500 and rest == False:
            if level * 6 - 2 <= numoffiles:
                lines = openfile(listy[level * 6 - 3])
                screen = lines[0]
                editfile = str(level * 6 - 2)
                loaded = False
                rest = True
                pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 250 and mousepos[0] <= 350 and mousepos[1] >= 400 and mousepos[1] <= 500 and rest == False:
            if level * 6 - 1 <= numoffiles:
                lines = openfile(listy[level * 6 - 2])
                screen = lines[0]
                editfile = str(listy[level * 6 - 2])
                loaded = False
                rest = True
                pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 400 and mousepos[0] <= 500 and mousepos[1] >= 400 and mousepos[1] <= 500 and rest == False:
            if level * 6 <= numoffiles:
                lines = openfile(listy[level * 6 - 1])
                screen = lines[0]
                editfile = str(listy[level * 6 - 1])
                loaded = False
                rest = True
                pygame.time.wait(100)

    # Settings
    if screen == "Settings":
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        pygame.display.set_caption("Settings")
        background(backpic)
        os.chdir(AppDataPath+"/universal")
        back_arrow = pygame.image.load("Back Arrow.png")
        os.chdir(AppDataPath+"/settings")
        change_background = pygame.image.load("Change Background.png")
        window.blit(back_arrow,(100,100))
        window.blit(change_background,(250,100))
        if mouseclicks[0] == True and mousepos[0] >= 100 and mousepos[0] <= 200 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            screen = "Home"
            rest = True
            pygame.time.wait(100)
        if mouseclicks[0] == True and mousepos[0] >= 250 and mousepos[0] <= 350 and mousepos[1] >= 100 and mousepos[1] <= 200 and rest == False:
            backpictest = popup("What do you want the new background to be? (1-3)")
            if backpictest == "1" or backpictest == "2" or backpictest == "3":
                os.chdir(SettingsPath)
                file = open("backnum","w")
                file.seek(0)
                file.write(backpictest)
                file.close()
            else:
                printer("Error")
            rest = True
            pygame.time.wait(100)

    # Pixlr
    if screen == "Pixlr":
        pygame.display.set_caption("Pixlr - "+editfile)
        if loaded == False and editfile != "":
            lines = openfile(editfile)
            color = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
            for x in range(64):
                color[x] = ast.literal_eval(lines[x + 1])
            loaded = True
            tool = "Basic"
            pos = ((0,0),(75,0),(150,0),(225,0),(300,0),(375,0),(450,0),(525,0),(0,75),(75,75),(150,75),(225,75),(300,75),(375,75),(450,75),(525,75),(0,150),(75,150),(150,150),(225,150),(300,150),(375,150),(450,150),(525,150),(0,225),(75,225),(150,225),(225,225),(300,225),(375,225),(450,225),(525,225),(0,300),(75,300),(150,300),(225,300),(300,300),(375,300),(450,300),(525,300),(0,375),(75,375),(150,375),(225,375),(300,375),(375,375),(450,375),(525,375),(0,450),(75,450),(150,450),(225,450),(300,450),(375,450),(450,450),(525,450),(0,525),(75,525),(150,525),(225,525),(300,525),(375,525),(450,525),(525,525))
            pixlr_colorchange = [255,255,255]
            history = []
        elif loaded == False:
            pos = ((0,0),(75,0),(150,0),(225,0),(300,0),(375,0),(450,0),(525,0),(0,75),(75,75),(150,75),(225,75),(300,75),(375,75),(450,75),(525,75),(0,150),(75,150),(150,150),(225,150),(300,150),(375,150),(450,150),(525,150),(0,225),(75,225),(150,225),(225,225),(300,225),(375,225),(450,225),(525,225),(0,300),(75,300),(150,300),(225,300),(300,300),(375,300),(450,300),(525,300),(0,375),(75,375),(150,375),(225,375),(300,375),(375,375),(450,375),(525,375),(0,450),(75,450),(150,450),(225,450),(300,450),(375,450),(450,450),(525,450),(0,525),(75,525),(150,525),(225,525),(300,525),(375,525),(450,525),(525,525))
            color = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
            loaded = True
            tool = "Basic"
            pixlr_colorchange = [255,255,255]
            history = []
        for x in range(64):
            pygame.draw.rect(window,color[x],(pos[x][0],pos[x][1],75,75))
        if mouseclicks[0] == True:
            for x in range(64):
                if mousepos[0] >= pos[x][0] and mousepos[0] <= pos[x][0] + 75 and mousepos[1] >= pos[x][1] and mousepos[1] <= pos[x][1] + 75 and rest == False:
                    listerer = (x,color[x])
                    history.append(listerer)
                    if tool == "Basic":
                        if color[x] != pixlr_colorchange:
                            color[x] = list(pixlr_colorchange)
                            history.append([x,list(pixlr_colorchange)])
                    if tool == "Colordropper":
                        pixlr_colorchange = color[x]
                    if tool == "Mixer":
                        colors = []
                        if (pos[x][0]+150,pos[x][1]) in pos:
                            colors.append(color[x+1])
                        if (pos[x][0]-150,pos[x][1]) in pos:
                            colors.append(color[x-1])
                        if (pos[x][0],pos[x][1]+150) in pos:
                            colors.append(color[x+8])
                        if (pos[x][0],pos[x][1]-150) in pos:
                            colors.append(color[x-8])

                        changeinr = 0
                        changeing = 0
                        changeinb = 0

                        for y in colors:
                            changeinr += y[0]
                            changeing += y[1]
                            changeinb += y[2]

                        if color[x] != [int(changeinr/len(colors)),int(changeing/len(colors)),int(changeinb/len(colors))]:
                            color[x] = [int(changeinr/len(colors)),int(changeing/len(colors)),int(changeinb/len(colors))]
                            history.append([x,[int(changeinr/len(colors)),int(changeing/len(colors)),int(changeinb/len(colors))]])
        # r
        if buttons_pressed[114] == True:
            pixlr_colorchange[0] = int(popup("What new red value do you want?")) 
        # g
        if buttons_pressed[103] == True:
            pixlr_colorchange[1] = int(popup("What new green value do you want?"))    
        # b
        if buttons_pressed[98] == True:
            pixlr_colorchange[2] = int(popup("What new blue value do you want?"))
        # a
        if buttons_pressed[97] == True:
            pixlr_colorchange = popup("What new color values do you want?")
            pixlr_colors = ("red","green","blue","white","black","yellow","cyan","pink","silver","grey","maroon","purple","teal","navy","gold","turquoise","chocolate","tan","lavender","ivory","honeydew","orange")
            pixlr_colorchanges = [[255,0,0],[0,255,0],[0,0,255],[255,255,255],[0,0,0],[255,255,0],[0,255,255],[255,0,255],[192,192,192],[128,128,128],[128,0,0],[128,0,128],[0,128,128],[0,0,128],[255,215,0],[64,224,208],[210,105,30],[210,180,140],[230,230,250],[255,255,240],[240,255,240],[255,165,0]]
            if pixlr_colorchange in pixlr_colors:
                loope = 0
                for x in pixlr_colors:
                    if x == pixlr_colorchange:
                        pixlr_colorchange = [0,0,0]
                        pixlr_colorchange[0] = pixlr_colorchanges[loope][0]
                        pixlr_colorchange[1] = pixlr_colorchanges[loope][1]
                        pixlr_colorchange[2] = pixlr_colorchanges[loope][2]
                    loope += 1
            else:
                pixlr_colorchange = pixlr_colorchange.split()
                pixlr_colorchange[0] = int(pixlr_colorchange[0])
                pixlr_colorchange[1] = int(pixlr_colorchange[1])
                pixlr_colorchange[2] = int(pixlr_colorchange[2])
        # Space
        if buttons_pressed[32] == True:
            tool = "Basic"
        # d
        if buttons_pressed[100] == True :
            tool = "Colordropper"
        # m
        if buttons_pressed[109] == True:
            tool = "Mixer"
        # z
        if buttons_pressed[122] == True and len(history) > 0:
            color[history[len(history)-1][0]] = history[len(history)-1][1]
            lister = []
            for y in range(len(history)-1):
                lister.append(history[y])
            history = lister
        # s
        if buttons_pressed[115] == True:
            if editfile == "":
                os.chdir(FilesPath)
                filename = popup("What is the file name?")
                while os.path.isdir(FilesPath+"/"+filename):
                    filename = popup("What is the file name?")
                file = open(filename,"w+")
                file.write("Pixlr")
                for x in color:
                    file.write("\n")
                    file.write(str(x))
                editfile = filename
                file.close()
            else:
                os.chdir(FilesPath)
                filename = str(editfile)
                file = open(filename,"w")
                file.write("Pixlr")
                for x in color:
                    file.write("\n")
                    file.write(str(x))
                file.close()
        # q
        if buttons_pressed[113] == True:
            if editfile == "":
                os.chdir(FilesPath)
                file = open("files","r")
                file.seek(0)
                numbersoffiles = len(file.read().split())
                file.close()
                filename = str(str(numbersoffiles + 1))
                file = open(filename,"w")
                file.write("Pixlr")
                for x in color:
                    file.write("\n")
                    file.write(str(x))
                editfile = str(numbersoffiles + 1)
                file.close()
                file = open("files","r")
                file.seek(0)
                text = file.read()
                file.close()
                file = open("files","w")
                file.write(text)
                if len(text.split()) != 0:
                    file.write(" ")
                file.write(editfile)
                file.close()
            else:
                os.chdir(FilesPath)
                filename = str(editfile)
                file = open(filename,"w")
                file.write("Pixlr")
                for x in color:
                    file.write("\n")
                    file.write(str(x))
                file.close()
            screen = "Home"
        # Curser Setting
        os.chdir(AppDataPath+"/pixlr")
        if tool == "Basic":
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        if tool == "Colordropper":
            pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
            cursor_picture = pygame.image.load("droppermouse.png").convert_alpha()
            window.blit(cursor_picture, pygame.mouse.get_pos())
        if tool == "Mixer":
            pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
            cursor_picture = pygame.image.load("mixermouse.png").convert_alpha()
            window.blit(cursor_picture, pygame.mouse.get_pos())

    # Calc
    if screen == "Calc":
        printer("Work in Progress")
        screen = "Home"

    if screen == "Browser":
        pygame.display.set_caption("Browser - "+site)
        if site == "":
            window.fill(WHITE)
            os.chdir(AppDataPath+"/browser")
            icon = pygame.image.load("icon.png")
            window.blit(icon,(0,0))
            if rest == False:
                history = [""]
                site = popup("What site do you want to go to?")
                rest = True
                history.append(site)
        else:
            try:
                os.chdir(AppDataPath+"/browser/"+site)
                file = open("code","r")
            except OSError:
                print("That site/page does not exist.")
                #add 404 checker.loader
                site = ""
            else:
                file.seek(0)
                lines = file.read().splitlines()
                file.close()
                for line in lines:
                    sections = tsplit(line, "|")
                    if sections[0] == "show":
                        window.blit(pygame.image.load(sections[1]),ast.literal_eval(sections[2]))
                    if sections[0] == "goto":
                        if mousepos[0] >= ast.literal_eval(sections[1])[0] and mousepos[0] <= ast.literal_eval(sections[1])[0] + ast.literal_eval(sections[2])[0] and mousepos[1] >= ast.literal_eval(sections[1])[1] and mousepos[1] <= ast.literal_eval(sections[1])[1] + ast.literal_eval(sections[2])[1] and rest == False:
                            if sections[3] == "True":
                                if mouseclicks[0] == True:
                                    site = sections[4]
                                    history.append(site)
                                    rest = True
                            else:
                                site = sections[4]
                                history.append(site)
                                rest = True
                    if sections[0] == "download":
                        file = open(sections[1],"r")
                        file.seek(0)
                        text = file.read()
                        file.close()
                        os.chdir(FilesPath)
                        file = open("files","r")
                        file.seek(0)
                        numbersoffiles = len(file.read().split())
                        file.close()
                        filename = str(str(numbersoffiles + 1))
                        file = open(filename,"w")
                        file.write(text)
                        editfile = str(numbersoffiles + 1)
                        file.close()
                        file = open("files","r")
                        file.seek(0)
                        text = file.read()
                        file.close()
                        file = open("files","w")
                        file.write(text)
                        if len(text.split()) != 0:
                            file.write(" ")
                        file.write(editfile)
                        file.close()
                        os.chdir(AppDataPath+"/browser/"+site)
                    if sections[0] == "print":
                        printer(sections[1])
        # C and Left Shift
        if buttons_pressed[99] == True and buttons_pressed[304] == True:
            site = popup("What site do you want to go to?")
            shistory.append(site)
        # Z
        if buttons_pressed[122] == True and len(history) > 0:
            site = history[len(history)-1]
            lister = []
            for y in range(len(history)-1):
                lister.append(history[y])
            history = lister
            history.append(site)
            pygame.time.wait(300)
        # Q and Left Shift
        if buttons_pressed[113] == True and buttons_pressed[304] == True:
            screen = "Home"

    if screen == "Bank":
        printer("Work in Progress")
        screen = "Home"

    # All Screen Post Draw Things
    pygame.display.update()
    rest = False

pygame.quit()
