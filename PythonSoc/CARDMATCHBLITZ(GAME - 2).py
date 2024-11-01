import pygame as py
import cv2
import random as rand

# Initialize Pygame
py.init()
class x:
    # Static variables
    count = 0
    r = 0
    c = 0
    s = 0
    shuffleCount = 0
    startButton = None
    backButton = None
    exitButton = None
    singlePlayerButton = None
    multiPlayerButton = None
    scoreButton = None
    triesButton = None
    timeLimitBtn = None
    continueBtn = None
    homeBtn = None
    replayBtn = None
    reactionTime = 0
    timeC = 0
    pos = 0
    score = 0
    tries = 5
    cardFlag = [0 for i in range(18)]
    back_click = False

    yesButtonColor = "green"
    yesTextColor = "white"
    yesButton = py.Rect(600, 360, 90, 70)

    nobuttonColor = "red"
    notextcolor = "white"
    noButton = py.Rect(820, 360, 90, 70)

    matched_cards = {}
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
    card_slot_15 = py.Rect(100, 20, 150, 230)
    card_slot_16 = py.Rect(100, 265, 150, 230)
    card_slot_17 = py.Rect(100, 510, 150, 230)

    card_slots_list = [(300, 20, card_slot_0), (500, 20, card_slot_1), (700, 20, card_slot_2), (900, 20, card_slot_3),
                       (1100, 20, card_slot_4), (300, 265, card_slot_5), (500, 265, card_slot_6),
                       (700, 265, card_slot_7),
                       (900, 265, card_slot_8), (1100, 265, card_slot_9), (300, 510, card_slot_10),
                       (500, 510, card_slot_11),
                       (700, 510, card_slot_12), (900, 510, card_slot_13), (1100, 510, card_slot_14),
                       (100, 20, card_slot_15), (100, 265, card_slot_16), (100, 510, card_slot_17)]

    _10ofClubs = py.image.load("data/cards/10 of clubs.png")
    _10ofClubs = py.transform.scale(_10ofClubs, (150, 230))

    _10ofHearts = py.image.load("data/cards/10 of hearts.png")
    _10ofHearts = py.transform.scale(_10ofHearts, (150, 230))

    _10ofDiamonds = py.image.load("data/cards/10 of diamonds.png")
    _10ofDiamonds = py.transform.scale(_10ofDiamonds, (150, 230))

    _10ofSpades = py.image.load("data/cards/10 of spades.png")
    _10ofSpades = py.transform.scale(_10ofSpades, (150, 230))

    _jackOfClubs = py.image.load("data/cards/jack of clubs.png")
    _jackOfClubs = py.transform.scale(_jackOfClubs, (150, 230))

    _jackOfSpades = py.image.load("data/cards/jack of spades.png")
    _jackOfSpades = py.transform.scale(_jackOfSpades, (150, 230))

    _jackOfHearts = py.image.load("data/cards/jack of hearts.png")
    _jackOfHearts = py.transform.scale(_jackOfHearts, (150, 230))

    _jackOfDiamonds = py.image.load("data/cards/jack of diamonds.png")
    _jackOfDiamonds = py.transform.scale(_jackOfDiamonds, (150, 230))

    _queenOfClubs = py.image.load("data/cards/queen of clubs.png")
    _queenOfClubs = py.transform.scale(_queenOfClubs, (150, 230))

    _queenOfSpades = py.image.load("data/cards/queen of spades.png")
    _queenOfSpades = py.transform.scale(_queenOfSpades, (150, 230))

    _queenOfHearts = py.image.load("data/cards/queen of hearts.png")
    _queenOfHearts = py.transform.scale(_queenOfHearts, (150, 230))

    _queenOfDiamonds = py.image.load("data/cards/queen of diamonds.png")
    _queenOfDiamonds = py.transform.scale(_queenOfDiamonds, (150, 230))

    _kingOfClubs = py.image.load("data/cards/king of clubs.png")
    _kingOfClubs = py.transform.scale(_kingOfClubs, (150, 230))

    _kingOfSpades = py.image.load("data/cards/king of spades.png")
    _kingOfSpades = py.transform.scale(_kingOfSpades, (150, 230))

    _kingOfHearts = py.image.load("data/cards/king of hearts.png")
    _kingOfHearts = py.transform.scale(_kingOfHearts, (150, 230))

    _kingOfDiamonds = py.image.load("data/cards/king of diamonds.png")
    _kingOfDiamonds = py.transform.scale(_kingOfDiamonds, (150, 230))


    cardList = [_queenOfHearts, _kingOfSpades, _10ofDiamonds, _kingOfClubs, _queenOfDiamonds, _jackOfSpades,
                _10ofHearts, _jackOfClubs,_kingOfDiamonds, _queenOfHearts, _kingOfSpades, _10ofDiamonds, _kingOfClubs,
                _queenOfDiamonds, _jackOfSpades, _10ofHearts, _jackOfClubs, _kingOfDiamonds ]

    button_highlight = {(625, 290): (270, 320), (625, 410): (270, 320)}
    button_highlight_dialogBox = {(575, 245): (140, 300), (800, 245): (130, 300)}
    start_time = 0
    timer_limit = 0
    remaining_time = 1
    highScore = 0
def shuffle2():
    excluded_indices = list(clickedCards.keys())
    new_cardList = [x.cardList[i] for i in range(len(x.cardList)) if i not in excluded_indices]
    rand.shuffle(new_cardList)
    for i in range(len(x.cardList)):
        if i not in excluded_indices:
            x.cardList[i] = new_cardList.pop(0)


def createButton(x, y, wd, ht, txtFont, text, btcolor, tcolor, image=None, imgx=None, imgy=None, bdradius=25):
    Button = py.Rect(x, y, wd, ht)
    py.draw.rect(screen, btcolor, Button, border_radius=bdradius)
    if image != None:
        screen.blit(image, (imgx, imgy))
    Text = txtFont.render(text, True, tcolor)
    screen.blit(Text, (Button.x + (Button.width - Text.get_width()) // 2,
                       Button.y + (Button.height - Text.get_height()) // 2))
    return Button


py.mixer.init(channels=4)

# Screen design
screen = py.display.set_mode((1500, 750))
py.display.set_icon(py.image.load('data/images/logo.png'))
py.display.set_caption("CARD MATCH BLITZ")
interface_img = py.image.load('data/images/logo.png')

# For videos
cap = cv2.VideoCapture("data/Video/backgorund cards game.mp4")
loadCap = cv2.VideoCapture("data/Video/loadingvideo.mp4")
flamecard = cv2.VideoCapture("data/Video/card-video-flames_IMU4Su6i (online-video-cutter.com).mp4")

# Images
bg_image = py.image.load("data/images/singlebackground.jpg")
bg_image = py.transform.scale(bg_image, (1500, 750))
game_back_pic = py.image.load("data/images/playbackground.jpg")
game_back_pic = py.transform.scale(game_back_pic, (1500, 750))
jokerpic = py.image.load("data/images/jokerpic.png")
jokerpic = py.transform.scale(jokerpic, (600, 800))
buttonback = py.image.load('data/images/buttonback.png')

# play images
backcard = py.image.load("data/images/backcardimg.jpg")
backcard = py.transform.scale(backcard, (150, 230))
back_button_img = py.image.load("data/images/backButtoimggg.webp")
back_button_img = py.transform.scale(back_button_img, (130, 130))
button_highlighter = py.image.load('data/images/buttonHIGH-removebg-preview (1).png')
scoreButton = py.image.load('data/images/scoreimage-removebg-preview.png');
scoreButton = py.transform.scale(scoreButton, (300, 300))
clock = py.image.load('data/images/clock-removebg-preview.png')
clock = py.transform.scale(clock,(200,170))
instructions_img = py.image.load("data/images/INSTRUCTIONS.png")
instructions_img = py.transform.scale(instructions_img, (1500, 750))
youWInImg = py.image.load("data/images/youWin.png")
youWInImg = py.transform.scale(youWInImg, (1500, 750))
button_back = py.image.load('data/images/button background.png')
button_back = py.transform.scale(button_back, (300, 150))
timeUpImg = py.image.load("data/images/timeupimg.png")
timeUpImg = py.transform.scale(timeUpImg, (1500, 750))
# Reactions
yesReaction = py.image.load("data/reactions/yes-removebg-preview.png")
yesReaction = py.transform.scale(yesReaction, (500, 500))

# Fonts
titleFont = py.font.Font('data/Fonts/BruceForeverRegular-X3jd2.ttf', 70)
font = py.font.SysFont('Arial', 40)
startFont = py.font.SysFont('Comic Sans', 40)
backFont = py.font.SysFont('Comic Sans', 130)
dialogBox_font = py.font.Font('data/Fonts/Rafgins-Regular.otf', 50)
player_button_font = py.font.Font('data/Fonts/Roman SD.ttf', 45)
pixelFont = py.font.Font('data/Fonts/ARCADECLASSIC.TTF', 70)
pixelTimeFont = py.font.Font('data/Fonts/ARCADECLASSIC.TTF', 50)
# Music
py.mixer.music.load("data/Audio/bg_music.mp3")
py.mixer.music.set_volume(0.5)

gameBgm = py.mixer.Sound("data/Audio/AUD-20241025-WA0002.mp3")
gameChannel = py.mixer.Channel(1)

playbgm = py.mixer.Sound("data/Audio/MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3")
playChannel = py.mixer.Channel(2)

bt_click = py.mixer.Sound("data/Audio/old-radio-button-click-97549.mp3")
st_click_sound = py.mixer.Sound("data/Audio/startclick.wav")
exit_click_sound = py.mixer.Sound("data/Audio/mixkit-click-error-1110.wav")
back_clk_sound = py.mixer.Sound("data/Audio/mixkit-positive-interface-beep-221.wav")
card_flip_sound = py.mixer.Sound("data/Audio/card flip sound.mp3")
card_mismatch_sound = py.mixer.Sound('data/Audio/error-call-to-attention-129258.mp3')
score_increase_sound = py.mixer.Sound("data/Audio/mixkit-arcade-bonus-alert-767.wav")
time_tick = py.mixer.Sound("data/Audio/timer-with-chime-101253.mp3")
time_channel = py.mixer.Channel(3)
you_win_sound = py.mixer.Sound("data/Audio/mixkit-magic-sweep-game-trophy-257.wav")
you_lose_sound = py.mixer.Sound("data/Audio/mixkit-unlock-new-item-game-notification-254.wav")
def print_cardslots():
    for i in range(len(x.cardList)):
        py.draw.rect(screen, "white", x.card_slots_list[i][2])
        screen.blit(backcard, (x.card_slots_list[i][0], x.card_slots_list[i][1]))


def titleDisplay():
    if x.c < 1:
        py.time.wait(10)
        colors = ['red', 'green', 'blue', 'orange', 'violet', 'yellow', 'pink', 'black', 'cyan']
        x.r = (x.r + 1) % len(colors)
        titleImg = titleFont.render("CARD MATCH BLITZ", True, colors[x.r])
        createButton(280, 245, 1015, 90, titleFont, ' ', 'white', "white")
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
    x.backButton = createButton(40, 40, 70, 70, backFont, " ", 'brown', 'white', bdradius=70, image=back_button_img,
                                imgx=10, imgy=10)
def back_button_for_play():
    x.backButton = createButton(1375, 650, 70, 70, backFont, " ", 'brown', 'white', bdradius=70, image=back_button_img,
                                imgx=1340, imgy=625)

def exit_button():
    x.exitButton = createButton(670, 530, 180, 80, startFont, "EXIT", 'red', 'white')


def singleplayer_button():
    x.singlePlayerButton = createButton(580, 250, 300, 60, player_button_font, "SINGLE PLAYER", "brown", 'black',
                                        image=buttonback, imgx=500, imgy=100)


def multiplayer_button():  # game - 2 button
    x.multiPlayerButton = createButton(580, 380, 300, 60, player_button_font, "GAME-2", "#21D4DB", 'black',
                                       image=buttonback, imgx=500, imgy=230)


def score():
    x.scoreButton = createButton(1310, 50, 150, 60, pixelFont, (str(x.score)), 'yellow', 'black', bdradius=10,
                                 image=scoreButton, imgx=1230, imgy=-50)


def home_btn():
    x.homeBtn = createButton(270,635,180,80,pixelFont,"HOME","blue","white",image=button_back,imgx=200,imgy=600)
def replay_btn():
    x.replayBtn = createButton(1060, 635, 180, 80, pixelFont, "REPLAY", "blue", "white", image=button_back, imgx=1000,
                                 imgy=600)
def continue_btn():
    x.continueBtn = createButton(670, 630, 180, 80, player_button_font, "CONTINUE", 'blue', 'black',image=buttonback,imgx=580,imgy=510)


def yesReactions():
    screen.blit(yesReaction, (500, 70))
    flip_timer = py.time.get_ticks()
    flip_back_delay = 1500
    while py.time.get_ticks() - flip_timer < flip_back_delay:
        screen.blit(x.cardList[firstKey], clickedCards[firstKey])
        screen.blit(x.cardList[secondKey], clickedCards[secondKey])
        py.display.update()


def BUTTON_HIGHLIGHT(dict, buttonhighlighter):
    try:
        place = list(dict.keys())
        buttonhighlighter = py.transform.scale(buttonhighlighter, dict[place[x.pos]])
        screen.blit(buttonhighlighter, place[x.pos])
    except IndexError:
        x.pos = 0

def timeLimit():
    elapsed_time = (py.time.get_ticks() - x.start_time) // 1000
    x.remaining_time = max(0, x.timer_limit - elapsed_time)
    createButton(1365, 255, 50, 50, pixelTimeFont, f"{x.remaining_time} s", 'white', 'black', bdradius=0,image=clock,imgx=1280,imgy=180)

def shuffling():
    createButton(280, 245, 900, 90, titleFont, 'Shuffling', 'white', "white")

# states
HOME = 0
GAME = 1
EXIT_CONFIRM = 2
GO_BACK = 4
PLAY2 = 5
INSTRUCTIONS = 6
YOU_WIN = 7
YOU_LOSE = 8
state = HOME
card_number = None
clickedCards = {}
cardx = 0
cardy = 0
shuffle2()

# Mainloop
while True:
    # events
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
        if event.type == py.KEYDOWN:
            if state == HOME:
                if event.key == py.K_DOWN:
                    x.pos += 1
                if event.key == py.K_UP:
                    x.pos -= 1
                if event.key == py.K_RETURN:
                    if x.pos == 0:
                        st_click_sound.play()
                        x.pos = 0
                        state = GAME
                    if x.pos == 1:
                        state = EXIT_CONFIRM
            if state == EXIT_CONFIRM:
                if event.key == py.K_RIGHT:
                    x.pos += 1
                if event.key == py.K_LEFT:
                    x.pos -= 1
                if event.key == py.K_RETURN:
                    if x.pos == 0:
                        py.quit()
                    if x.pos == 1:
                        x.pos = 0
                        exit_click_sound.play()
                        state = HOME
        if event.type == py.MOUSEBUTTONDOWN:
            if state == HOME:
                bt_click.play()
                if x.startButton.collidepoint(event.pos):
                    st_click_sound.play()
                    state = GAME
                if x.exitButton.collidepoint(event.pos):
                    exit_click_sound.play()
                    state = EXIT_CONFIRM
            elif state == EXIT_CONFIRM:
                bt_click.play()
                if x.yesButton.collidepoint(event.pos):
                    py.quit()
                elif x.noButton.collidepoint(event.pos):
                    exit_click_sound.play()
                    state = HOME
            elif state == GAME:
                bt_click.play()
                if x.backButton.collidepoint(event.pos):
                    back_clk_sound.play()
                    gameChannel.stop()
                    state = HOME
                if x.multiPlayerButton.collidepoint(event.pos):
                    gameChannel.stop()
                    x.back_click = False
                    state = INSTRUCTIONS
            elif state == INSTRUCTIONS:
                if x.continueBtn.collidepoint(event.pos):
                    st_click_sound.play()
                    x.start_time = py.time.get_ticks()
                    x.timer_limit = 60
                    state = PLAY2
            elif state == PLAY2:
                for i in range(len(x.card_slots_list)):
                    if x.card_slots_list[i][2].collidepoint(event.pos):
                        card_flip_sound.play()
                        cardx = x.card_slots_list[i][0]
                        cardy = x.card_slots_list[i][1]
                        clickedCards.update({i: (cardx, cardy)})
                        break
                if x.backButton.collidepoint(event.pos):
                    state = GO_BACK
                    playChannel.stop()
                    back_clk_sound.play()
                    time_channel.stop()
                if x.score == 90:
                    state = YOU_WIN
                    you_win_sound.play()
                if x.remaining_time == 0:
                    state = YOU_LOSE
                    you_lose_sound.play()
            elif state == YOU_WIN:
                if x.homeBtn.collidepoint(event.pos):
                    clickedCards.clear()  # game 2
                    card_number = None
                    x.score = 0
                    x.back_click = True
                    shuffle2()
                    bt_click.play()
                    state = GAME
                if x.replayBtn.collidepoint(event.pos):
                    clickedCards.clear()  # game 2
                    card_number = None
                    x.score = 0
                    x.back_click = True
                    shuffle2()
                    st_click_sound.play()
                    state = INSTRUCTIONS
            elif state == YOU_LOSE:
                if x.homeBtn.collidepoint(event.pos):
                    clickedCards.clear()  # game 2
                    card_number = None
                    x.score = 0
                    x.back_click = True
                    shuffle2()
                    bt_click.play()
                    state = GAME
                if x.replayBtn.collidepoint(event.pos):
                    clickedCards.clear()  # game 2
                    card_number = None
                    x.score = 0
                    x.back_click = True
                    shuffle2()
                    st_click_sound.play()
                    state = INSTRUCTIONS
            elif state == GO_BACK:
                bt_click.play()
                if x.yesButton.collidepoint(event.pos):
                    clickedCards.clear()  # game 2
                    card_number = None
                    x.score = 0
                    x.back_click = True
                    shuffle2()
                    state = GAME
                elif x.noButton.collidepoint(event.pos):
                    exit_click_sound.play()
                    state = PLAY2

    if state == HOME:
        InterfaceLoadingVideo()
        screen.fill((0, 0, 0))
        backgroundVideo()
        if not py.mixer.music.get_busy():
            py.mixer.music.play(-1)
        titleDisplay()
        start_button()
        exit_button()
        BUTTON_HIGHLIGHT(x.button_highlight, button_highlighter)
    elif state == GAME:
        py.mixer.music.stop()
        if not gameChannel.get_busy():
            gameChannel.set_volume(1)
            gameChannel.play(gameBgm)
        screen.blit(bg_image, (0, 0))
        screen.blit(jokerpic, (900, 0))
        buttonback = py.transform.scale(buttonback, (450, 360))
        back_button()
        multiplayer_button()

    elif state == EXIT_CONFIRM:
        dialog_box()
        BUTTON_HIGHLIGHT(x.button_highlight_dialogBox, button_highlighter)
    elif state == GO_BACK:
        dialog_box()
    elif state == INSTRUCTIONS:
        screen.blit(instructions_img,(0,0))
        buttonback = py.transform.scale(buttonback, (350, 320))
        continue_btn()
    elif state == PLAY2:
        if not time_channel.get_busy() and x.remaining_time>0:
            time_channel.play(time_tick)
            time_channel.set_volume(0.8,-1)
        if not playChannel.get_busy():
            playChannel.set_volume(0.8)
            playChannel.play(playbgm)
        y = 0
        z = 1
        screen.blit(game_back_pic, (0, 0))
        back_button_for_play()
        score()
        timeLimit()
        print_cardslots()
        for k, v in clickedCards.items():
            screen.blit(x.cardList[k], v)
        if len(clickedCards) % 2 == 0 and len(clickedCards) > 1:
            z = len(clickedCards) - 1
            y = z - 1
            firstKey = list(clickedCards.keys())[y]
            secondKey = list(clickedCards.keys())[z]
            if x.cardList[firstKey] == x.cardList[secondKey]:
                if x.cardFlag[firstKey] == 0 and x.cardFlag[secondKey] == 0:
                    shuffle2()
                    yesReactions()
                    x.score += 10
                    if x.score > x.highScore:
                        x.highScore = x.score
                    score_increase_sound.play()
                x.cardFlag[firstKey] = 1
                x.cardFlag[secondKey] = 1
            else:
                flip_timer = py.time.get_ticks()
                flip_back_delay = 1300
                while py.time.get_ticks() - flip_timer < flip_back_delay:
                    screen.blit(x.cardList[firstKey], clickedCards[firstKey])
                    screen.blit(x.cardList[secondKey], clickedCards[secondKey])
                    py.display.update()
                card_mismatch_sound.play()
                if x.score >= 50:
                    shuffle2()
                clickedCards.pop(firstKey, None)
                clickedCards.pop(secondKey, None)
    if state == YOU_WIN:
        screen.blit(youWInImg, (0, 0))
        createButton(690,350,80,60,pixelFont,f"{x.score}","#F4EDCE","black")
        createButton(690, 500, 80, 60, pixelFont, f"{x.score}", "#F4EDCE", "black")
        createButton(690, 650, 80, 60, pixelFont, f"{(x.timer_limit-x.remaining_time)}", "#F4EDCE", "black")
        home_btn()
        replay_btn()
    if state == YOU_LOSE:
        screen.blit(timeUpImg, (0, 0))
        createButton(690, 350, 80, 60, pixelFont, f"{x.score}", "#F4EDCE", "black")
        createButton(690, 500, 80, 60, pixelFont, f"{x.score}", "#F4EDCE", "black")
        createButton(690, 650, 80, 60, pixelFont, f"{(x.timer_limit - x.remaining_time)}", "#F4EDCE", "black")
        home_btn()
        replay_btn()
    py.display.update()

cap.release()
py.quit()
