import pygame as py
import cv2
import random as rand

class x:
    # Static variables
    count = 0
    r = 0
    c = 0
    s = 0
    shuffleCount = 0
    reveal_card_count = 0
    startButton = None
    backButton = None
    exitButton = None
    singlePlayerButton = None
    multiPlayerButton = None
    scoreButton = None
    triesButton = None
    revealed_card = None
    score = 0
    tries = 5
    reactionTime = 0
    clickedCards= -1
    yesButtonColor = "green"
    yesTextColor = "white"
    yesButton = py.Rect(600, 360, 90, 70)

    nobuttonColor = "red"
    notextcolor = "white"
    noButton = py.Rect(820, 360, 90, 70)

    card_slot_0 = py.Rect(300, 20, 150, 200)
    card_slot_1 = py.Rect(500, 20, 150, 230)
    card_slot_2 = py.Rect(700, 20, 150, 230)
    card_slot_3 = py.Rect(900, 20, 150, 230)
    card_slot_4 = py.Rect(1100, 20, 150, 230)
    card_slot_5 = py.Rect(300, 265, 150, 230)
    card_slot_6 = py.Rect(500, 265, 150, 230)
    card_slot_7 = py.Rect(700, 265, 150, 230)
    card_slot_8 = py.Rect(900, 265, 150, 230)
    card_slot_9 = py.Rect(1100, 265, 150, 230)
    card_slot_10 = py.Rect(300, 510, 150, 230)
    card_slot_11 = py.Rect(500, 510, 150, 230)
    card_slot_12 = py.Rect(700, 510, 150, 230)
    card_slot_13 = py.Rect(900, 510, 150, 230)
    card_slot_14 = py.Rect(1100, 510, 150, 230)
    revealed_card_slot = py.Rect(80,265,150,230)

    card_slots_list = [(300, 20,card_slot_0),(500, 20,card_slot_1),(700, 20,card_slot_2),(900, 20,card_slot_3),
                       (1100, 20,card_slot_4),(300, 265,card_slot_5),(500, 265,card_slot_6),(700, 265,card_slot_7),
                       (900, 265,card_slot_8),(1100, 265,card_slot_9),(300, 510,card_slot_10),(500, 510,card_slot_11),
                       (700, 510,card_slot_12),(900, 510,card_slot_13),(1100, 510,card_slot_14) ]

    shuffledCards = {}
    equalityList = []

def shuffle():
    cardDimensionsList = [(300, 20), (500, 20), (700, 20), (900, 20), (1100, 20),
                (300, 265), (500, 265), (700, 265), (900, 265), (1100, 265),
                (300, 510), (500, 510), (700, 510), (900, 510), (1100, 510)]
    cardList = [_jackOfClubs,_jackOfHearts,_jackOfSpades,_jackOfDiamonds,
                _queenOfClubs,_queenOfHearts,_queenOfSpades,_queenOfDiamonds,
                _kingOfClubs,_kingOfHearts,_kingOfSpades,_kingOfDiamonds,
                _10ofClubs,_10ofHearts,_10ofSpades,_10ofDiamonds]
    if x.shuffleCount<1:
        status = []
        slots = 0
        while slots < 15:
            card = rand.choice(cardList)
            if card not in status:
                status.append(card)
                x.shuffledCards[card] = cardDimensionsList[slots]
                slots = slots + 1
    x.shuffleCount += 1

def shuffle2():
    cardDimensionsList = [(300, 20), (500, 20), (700, 20), (900, 20), (1100, 20),
                          (300, 265), (500, 265), (700, 265), (900, 265), (1100, 265),
                          (300, 510), (500, 510), (700, 510), (900, 510), (1100, 510)]
    cardList = [_queenOfHearts,_kingOfSpades,_10ofDiamonds,_kingOfClubs,_queenOfDiamonds,_jackOfSpades,
                 _10ofHearts,   _jackOfClubs ,_queenOfHearts,_kingOfSpades,_10ofDiamonds,_kingOfClubs,
                _queenOfDiamonds,_jackOfSpades,_10ofHearts,]
    if x.shuffleCount<1:
        rand.shuffle(cardList)
        for i in range (len(cardDimensionsList)):
            x.shuffledCards[cardList[i]] = cardDimensionsList[i]
    x.shuffleCount += 1
def card_reveal():
    if x.reveal_card_count<1:
        cardList = [_jackOfClubs, _jackOfHearts, _jackOfSpades, _jackOfDiamonds,
                    _queenOfClubs, _queenOfHearts, _queenOfSpades, _queenOfDiamonds,
                    _kingOfClubs, _kingOfHearts, _kingOfSpades, _kingOfDiamonds,
                    _10ofClubs, _10ofHearts, _10ofSpades, _10ofDiamonds]
        r = rand.choice(cardList)
        x.revealed_card = r
    x.reveal_card_count += 1

def createButton( x, y, wd, ht, txtFont, text, btcolor, tcolor,image = None,imgx=None,imgy=None,bdradius=25):
    Button = py.Rect(x, y, wd, ht)
    py.draw.rect(screen, btcolor, Button,border_radius=bdradius)
    if image != None:
        screen.blit(image,(imgx,imgy))
    Text = txtFont.render(text, True, tcolor)
    screen.blit(Text, (Button.x + (Button.width - Text.get_width()) // 2,
                       Button.y + (Button.height - Text.get_height()) // 2))
    return Button


# Initialize Pygame
py.init()
py.mixer.init()

# Screen design
screen = py.display.set_mode((1500,750))
py.display.set_icon(py.image.load('data/logo.png'))
py.display.set_caption("CARD MATCH BLITZ")
interface_img = py.image.load('data/logo.png')

# For videos
cap = cv2.VideoCapture("data/backgorund cards game.mp4")
loadCap = cv2.VideoCapture("data/loadingvideo.mp4")
flamecard = cv2.VideoCapture("data/card-video-flames_IMU4Su6i (online-video-cutter.com).mp4")

# Images
bg_image = py.image.load("data/singlebackground.jpg")
bg_image = py.transform.scale(bg_image,(1500,750))
game_back_pic = py.image.load("data/playbackground.jpg")
game_back_pic = py.transform.scale(game_back_pic,(1500,750))
jokerpic = py.image.load("data/jokerpic.png")
jokerpic = py.transform.scale(jokerpic,(600,800))
buttonback = py.image.load('data/buttonback.png')
buttonback = py.transform.scale(buttonback,(450,360))

#play images
backcard = py.image.load("data/backcardimg.jpg")
backcard = py.transform.scale(backcard,(150,230))

#cards images

_10ofClubs = py.image.load("data/cards/10 of clubs.png")
_10ofClubs = py.transform.scale(_10ofClubs,(150,230))

_10ofHearts = py.image.load("data/cards/10 of hearts.png")
_10ofHearts = py.transform.scale(_10ofHearts,(150,230))

_10ofDiamonds = py.image.load("data/cards/10 of diamonds.png")
_10ofDiamonds = py.transform.scale(_10ofDiamonds,(150,230))

_10ofSpades = py.image.load("data/cards/10 of spades.png")
_10ofSpades = py.transform.scale(_10ofSpades,(150,230))

_jackOfClubs = py.image.load("data/cards/jack of clubs.png")
_jackOfClubs = py.transform.scale(_jackOfClubs,(150,230))

_jackOfSpades = py.image.load("data/cards/jack of spades.png")
_jackOfSpades = py.transform.scale(_jackOfSpades,(150,230))

_jackOfHearts = py.image.load("data/cards/jack of hearts.png")
_jackOfHearts = py.transform.scale(_jackOfHearts,(150,230))

_jackOfDiamonds = py.image.load("data/cards/jack of diamonds.png")
_jackOfDiamonds = py.transform.scale(_jackOfDiamonds,(150,230))

_queenOfClubs = py.image.load("data/cards/queen of clubs.png")
_queenOfClubs = py.transform.scale(_queenOfClubs,(150,230))

_queenOfSpades = py.image.load("data/cards/queen of spades.png")
_queenOfSpades = py.transform.scale(_queenOfSpades,(150,230))

_queenOfHearts = py.image.load("data/cards/queen of hearts.png")
_queenOfHearts = py.transform.scale(_queenOfHearts,(150,230))

_queenOfDiamonds = py.image.load("data/cards/queen of diamonds.png")
_queenOfDiamonds = py.transform.scale(_queenOfDiamonds,(150,230))

_kingOfClubs = py.image.load("data/cards/king of clubs.png")
_kingOfClubs = py.transform.scale(_kingOfClubs,(150,230))

_kingOfSpades = py.image.load("data/cards/king of spades.png")
_kingOfSpades = py.transform.scale(_kingOfSpades,(150,230))

_kingOfHearts = py.image.load("data/cards/king of hearts.png")
_kingOfHearts = py.transform.scale(_kingOfHearts,(150,230))

_kingOfDiamonds = py.image.load("data/cards/king of diamonds.png")
_kingOfDiamonds = py.transform.scale(_kingOfDiamonds,(150,230))

# Reactions
youLose = py.image.load('data/reactions/you_lose-removebg-preview.png')
youLose = py.transform.scale(youLose,(700,700))

youWin = py.image.load('data/reactions/you_win-removebg-preview.png')
youWin = py.transform.scale(youWin,(500,500))

oops = py.image.load('data/reactions/oops-removebg-preview.png')
oops = py.transform.scale(oops,(700,700))

looser = py.image.load("data/reactions/loser-removebg-preview.png")
looser = py.transform.scale(looser,(700,700))

yesReaction = py.image.load("data/reactions/yes-removebg-preview.png")
yesReaction = py.transform.scale(yesReaction,(500,500))

lastChance = py.image.load('data/reactions/last_chance-removebg-preview.png')
lastChance = py.transform.scale(lastChance,(600,700))

# Fonts
titleFont = py.font.Font('data/BruceForeverRegular-X3jd2.ttf', 70)
font = py.font.SysFont('Arial', 40)
startFont = py.font.SysFont('Comic Sans', 40)
dialogBox_font = py.font.Font('data/Rafgins-Regular.otf', 50)
player_button_font = py.font.Font('data/Roman SD.ttf', 45)

# Music
py.mixer.music.load("data/bg_music.mp3")
bt_click = py.mixer.Sound("data/old-radio-button-click-97549.mp3")
st_click_sound = py.mixer.Sound("data/startclick.wav")
exit_click_sound = py.mixer.Sound("data/mixkit-click-error-1110.wav")
back_clk_sound = py.mixer.Sound("data/mixkit-positive-interface-beep-221.wav")

def print_cardslots(clicked_card):
    for i in range(0,15):
        py.draw.rect(screen, "white", x.card_slots_list[i][2])
        if i not in clicked_card:
            screen.blit(backcard, (x.card_slots_list[i][0], x.card_slots_list[i][1]))
    py.draw.rect(screen, "white", x.revealed_card_slot)


def titleDisplay():
    if x.c < 1:
        py.time.wait(10)
        colors = ['red', 'green', 'blue', 'orange', 'violet', 'yellow','pink','black','cyan']
        x.r = (x.r + 1) % len(colors)
        titleImg = titleFont.render("CARD MATCH BLITZ", True, colors[x.r])
        createButton(280,245,1015,90,titleFont,' ','white',"white")
        screen.blit(titleImg, (300, 250))
        py.time.wait(0)

def backgroundVideo():
    val, frame = cap.read()
    if not val:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        val, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (1500, 750))
    frame = py.surfarray.make_surface(frame.swapaxes(0, 1))
    screen.blit(frame, (0, 0))
    x.bgMusic_state = True
    return True

def InterfaceLoadingVideo():
    if x.count < 1:
        screen.blit(interface_img, (500, 120))
        frames = 0
        while frames < 240:
            ret, loadFrame = loadCap.read()
            if not ret:
                continue
            loadFrame = cv2.cvtColor(loadFrame, cv2.COLOR_BGR2RGB)
            loadFrame = cv2.resize(loadFrame, (400, 100))
            loadFrame = py.surfarray.make_surface(loadFrame.swapaxes(0, 1))
            screen.blit(loadFrame, (540, 650))
            py.display.update()
            frames += 1
        py.time.wait(1000)
        x.count += 1

def dialog_box():
    confirm_box = py.Rect(550, 230, 450, 260)
    py.draw.rect(screen, "white", confirm_box, border_radius=25)
    confirm_font = dialogBox_font.render("Want to exit?", True, "black")
    screen.blit(confirm_font, (600, 280))
    py.draw.rect(screen, x.yesButtonColor, x.yesButton, border_radius=25)
    py.draw.rect(screen, x.nobuttonColor, x.noButton, border_radius=25)
    yesButtonFont = startFont.render("YES", True, x.yesTextColor)
    noButtonFont = startFont.render("NO", True, x.notextcolor)
    screen.blit(yesButtonFont, (x.yesButton.x + (x.yesButton.width - yesButtonFont.get_width()) // 2,
                                x.yesButton.y + (x.yesButton.height - yesButtonFont.get_height()) // 2))
    screen.blit(noButtonFont, (x.noButton.x + (x.noButton.width - noButtonFont.get_width()) // 2,
                               x.noButton.y + (x.noButton.height - noButtonFont.get_height()) // 2))

def start_button():
    x.startButton = createButton(670, 410, 180, 80, startFont, "START", 'blue', 'white')

def back_button():
    x.backButton = createButton(20, 20, 140, 60, startFont, "BACK", 'red', 'white')

def exit_button():
    x.exitButton = createButton(670, 530, 180, 80, startFont, "EXIT", 'red', 'white')

def singleplayer_button():
    x.singlePlayerButton = createButton(580, 250, 300, 60, player_button_font, "SINGLE PLAYER", "brown", 'black',image=buttonback,imgx=500,imgy=100)

def multiplayer_button():
    x.multiPlayerButton = createButton(580, 380, 300, 60, player_button_font, "MULTI PLAYER", "#21D4DB", 'black',image=buttonback,imgx=500,imgy=230)

def score ():
    x.scoreButton = createButton(1270,20,200,60,startFont, (" Score :  " + str(x.score)),'yellow','red',bdradius=10)
def tries():
    x.triesButton = createButton(1270, 100, 200, 60, startFont, (" Tries :  " + str(x.tries)) , 'black', 'white', bdradius=10)
def yesReactions():
    if x.reactionTime <1:
        screen.blit(yesReaction, (500, 70))
        py.display.update()
        py.time.delay(1500)
    x.reactionTime += 1
def oopsReaction():
    if x.reactionTime <1:
        screen.blit(oops, (400, 0))
        py.display.update()
        py.time.delay(1500)
    x.reactionTime += 1
def loserReaction():
    if x.reactionTime <1:
        screen.blit(looser, (400, 50))
        py.display.update()
        py.time.delay(1500)
    x.reactionTime += 1
def youloseReaction():
    if x.reactionTime <1:
        screen.blit(youLose, (500, 70))
        py.display.update()
        py.time.delay(1500)
    x.reactionTime += 1
def lastChanceReaction():
    if x.reactionTime <1:
        screen.blit(lastChance, (500, 70))
        py.display.update()
        py.time.delay(1500)
    x.reactionTime += 1

def findKey(value):
    for k,v in x.shuffledCards.items():
        if v == value:
            return k


#states
HOME = 0
GAME = 1
EXIT_CONFIRM = 2
PLAY = 3
GO_BACK = 4
PLAY2 = 5
back_click=False
exit_click=False
state = HOME
card_number = None
clicked_cards = []
card_reveal_now = False
cardx = 0
cardy = 0

# Mainloop
while True:
    #events
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.MOUSEBUTTONDOWN:
            bt_click.play()
            if state == HOME:
                if x.startButton.collidepoint(event.pos):
                    st_click_sound.play()
                    state = GAME
                elif x.backButton.collidepoint(event.pos):
                    quit_click = True
                    state = EXIT_CONFIRM
                elif x.exitButton.collidepoint(event.pos):
                    exit_click_sound.play()
                    state = EXIT_CONFIRM
            elif state == EXIT_CONFIRM:
                if x.yesButton.collidepoint(event.pos):
                    py.quit()
                elif x.noButton.collidepoint(event.pos):
                    exit_click_sound.play()
                    state = HOME
            elif state == GAME:
                if x.backButton.collidepoint(event.pos):
                    back_clk_sound.play()
                    state = HOME
                if x.singlePlayerButton.collidepoint(event.pos):
                    st_click_sound.play()
                    card_reveal_now = True
                    state = PLAY
                if x.multiPlayerButton.collidepoint(event.pos):
                    state = PLAY2
            elif state == PLAY:
                for i in range (len(x.card_slots_list)):
                    if x.card_slots_list[i][2].collidepoint(event.pos):
                        card_number=i
                        x.tries -= 1
                        x.reactionTime = 0
                        break
                if x.backButton.collidepoint(event.pos):
                    state = GO_BACK
                    back_clk_sound.play()
            elif state == GO_BACK:
                if x.yesButton.collidepoint(event.pos):
                    clicked_cards.clear()
                    card_number = None
                    x.tries = 5
                    state = GAME
                elif x.noButton.collidepoint(event.pos):
                    exit_click_sound.play()
                    state = PLAY
            elif state == PLAY2:
                for i in range(len(x.card_slots_list)):
                    if x.card_slots_list[i][2].collidepoint(event.pos):
                        clicked_cards.append(i)
                        cardx = x.card_slots_list[i][2].x
                        cardy = x.card_slots_list[i][2].y
                        x.tries -= 1
                        x.reactionTime = 0
                        break
                if x.backButton.collidepoint(event.pos):
                    state = GAME
                    back_clk_sound.play()

    if state == HOME:
        InterfaceLoadingVideo()
        screen.fill((0, 0, 0))
        bgMusic_state = backgroundVideo()
        if bgMusic_state and not py.mixer.music.get_busy():
            py.mixer.music.play()

        titleDisplay()
        start_button()
        exit_button()

        if exit_click:
            dialog_box()

    elif state == GAME:
        screen.blit(bg_image, (0, 0))
        screen.blit(jokerpic,(900,0))

        py.mixer.music.stop()
        back_button()
        singleplayer_button()
        multiplayer_button()
        if back_click:
            state = HOME

    elif state == EXIT_CONFIRM:
        dialog_box()
    elif state == GO_BACK:
        dialog_box()
    elif state == PLAY:
        cardFlag = [c for c in x.shuffledCards.keys()]
        screen.blit(game_back_pic,(0,0))
        back_button()
        score()
        tries()
        print_cardslots(clicked_cards)
        shuffle()
        card_reveal()
        if clicked_cards:
            for i in clicked_cards:
                card = cardFlag[i]
                screen.blit(card, x.shuffledCards[card])

        if card_reveal_now:
            screen.blit(x.revealed_card,(80,265))

        if card_number!= None:
            clicked_cards.append(card_number)
            card = cardFlag[card_number]
            if x.tries > 0:
                if x.revealed_card == card:
                    yesReactions()
                if x.revealed_card != card:
                    if x.tries == 4:
                        oopsReaction()
                    elif x.tries == 3:
                        loserReaction()
                    elif x.tries == 2:
                        oopsReaction()
                    elif x.tries == 1:
                        lastChanceReaction()
            else:
                youloseReaction()

    elif state == PLAY2:
        cardFlag = [c for c in x.shuffledCards.keys()]
        screen.blit(game_back_pic, (0, 0))
        back_button()
        score()
        tries()
        print_cardslots(clicked_cards)
        shuffle2()
        if clicked_cards:
            for i in clicked_cards:
                screen.blit(cardFlag[i],(cardx,cardy))






    py.display.update()

cap.release()
py.quit()
