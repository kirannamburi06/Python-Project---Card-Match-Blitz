import pygame as py
import cv2

class x:
    # for static variables
    count = 0
    r = 0
    c = 0
    s = 0
    buttonColor = "blue"
    textColor = "white"
    rectButton = py.Rect(670, 410, 180, 80)

    quitbuttonColor = "red"
    quittextcolor = "white"
    quitButton = py.Rect(20, 20, 140, 60)

    backbuttonColor = "red"
    backtextcolor = "white"
    backButton = py.Rect(20, 20, 140, 60)

    exitButtonColor = "red"
    exitTextColor = "white"
    exitButton = py.Rect(670 , 530 , 180 , 80)

    yesButtonColor = "green"
    yesTextColor = "white"
    yesButton = py.Rect(600,360,90,70)

    nobuttonColor = "red"
    notextcolor = "white"
    noButton = py.Rect(820, 360, 90, 70)

    singlebuttoncolor = "#21D4DB"
    singletextcolor = "black"
    multibuttoncolor = "#21D4DB"
    multitextcolor = "black"
    singleButton = py.Rect(580, 250, 300, 60)
    multiButton = py.Rect(580, 400, 300, 60)

    card_slot_1 = py.Rect(300,20,150,200)
    card_slot_2 = py.Rect(500, 20, 150, 230)
    card_slot_3 = py.Rect(700, 20, 150, 230)
    card_slot_4 = py.Rect(900, 20, 150, 230)
    card_slot_5 = py.Rect(1100, 20, 150, 230)
    card_slot_6 = py.Rect(300, 265, 150, 230)
    card_slot_7 = py.Rect(500, 265, 150, 230)
    card_slot_8 = py.Rect(700, 265, 150, 230)
    card_slot_9 = py.Rect(900, 265, 150, 230)
    card_slot_10 = py.Rect(1100, 265, 150, 230)
    card_slot_11 = py.Rect(300, 510, 150, 230)
    card_slot_12 = py.Rect(500, 510, 150, 230)
    card_slot_13 = py.Rect(700, 510, 150, 230)
    card_slot_14 = py.Rect(900, 510, 150, 230)
    card_slot_15 = py.Rect(1100, 510, 150, 230)

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
king_card = py.image.load("data/king card.png")
king_card = py.transform.scale(king_card,(150,200))

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

def cardslots():
    py.draw.rect(screen,"white",x.card_slot_1)
    py.draw.rect(screen, "white", x.card_slot_2)
    py.draw.rect(screen, "white", x.card_slot_3)
    py.draw.rect(screen, "white", x.card_slot_4)
    py.draw.rect(screen, "white", x.card_slot_5)
    py.draw.rect(screen, "white", x.card_slot_6)
    py.draw.rect(screen, "white", x.card_slot_7)
    py.draw.rect(screen, "white", x.card_slot_8)
    py.draw.rect(screen, "white", x.card_slot_9)
    py.draw.rect(screen, "white", x.card_slot_10)
    py.draw.rect(screen, "white", x.card_slot_11)
    py.draw.rect(screen, "white", x.card_slot_12)
    py.draw.rect(screen, "white", x.card_slot_13)
    py.draw.rect(screen, "white", x.card_slot_14)
    py.draw.rect(screen, "white", x.card_slot_15)
    screen.blit(backcard, (300,20))
    screen.blit(backcard, (500, 20))
    screen.blit(backcard, (700, 20))
    screen.blit(backcard, (900, 20))
    screen.blit(backcard, (1100, 20))
    screen.blit(backcard, (300, 265))
    screen.blit(backcard, (500, 265))
    screen.blit(backcard, (700, 265))
    screen.blit(backcard, (900, 265))
    screen.blit(backcard, (1100, 265))
    screen.blit(backcard, (300, 510))
    screen.blit(backcard, (500, 510))
    screen.blit(backcard, (700, 510))
    screen.blit(backcard, (900, 510))
    screen.blit(backcard, (1100, 510))


def titleDisplay():
    if x.c < 1:
        colors = ['red', 'green', 'blue', 'orange', 'violet', 'yellow']
        x.r = (x.r + 1) % len(colors)
        titleImg = titleFont.render("CARD MATCH BLITZ", True, colors[x.r])
        title_width, title_height = titleImg.get_size()
        pad = 20
        back_rect = py.Rect(290, 240, title_width + pad, title_height + pad)
        py.draw.rect(screen, 'white', back_rect, border_radius=10)
        screen.blit(titleImg, (300, 250))
        py.time.wait(50)

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

def start_button():
    py.draw.rect(screen, x.buttonColor, x.rectButton, border_radius=25)
    startText = startFont.render("START", True, x.textColor)
    screen.blit(startText, (x.rectButton.x + (x.rectButton.width - startText.get_width()) // 2,
                            x.rectButton.y + (x.rectButton.height - startText.get_height()) // 2))

def quit_button():
    py.draw.rect(screen, x.quitbuttonColor, x.quitButton, border_radius=25)
    quitText = startFont.render("BACK", True, x.quittextcolor)
    screen.blit(quitText, (x.quitButton.x + (x.quitButton.width - quitText.get_width()) // 2,
                           x.quitButton.y + (x.quitButton.height - quitText.get_height()) // 2))

def back_button():
    py.draw.rect(screen, x.backbuttonColor, x.backButton, border_radius=25)
    backText = startFont.render("BACK", True, x.backtextcolor)
    screen.blit(backText, (x.backButton.x + (x.backButton.width - backText.get_width()) // 2,
                           x.backButton.y + (x.backButton.height - backText.get_height()) // 2))

def exit_button():
    py.draw.rect(screen, x.exitButtonColor, x.exitButton, border_radius=25)
    exitText = startFont.render("EXIT", True, x.exitTextColor)
    screen.blit(exitText, (x.exitButton.x + (x.exitButton.width - exitText.get_width()) // 2,
                            x.exitButton.y + (x.exitButton.height - exitText.get_height()) // 2))

def singleplayer_button():
    py.draw.rect(screen, x.singlebuttoncolor, x.singleButton, border_radius=25)
    screen.blit(buttonback, (500, 100))
    singleplayer = player_button_font.render("SINGLE PLAYER", True, x.singletextcolor)
    screen.blit(singleplayer, (x.singleButton.x + (x.singleButton.width - singleplayer.get_width()) // 2,
                            x.singleButton.y + (x.singleButton.height - singleplayer.get_height()) // 2))

def multiplayer_button():
    py.draw.rect(screen, x.multibuttoncolor, x.multiButton, border_radius=25)
    screen.blit(buttonback, (500, 250))
    multiplayer = player_button_font.render("MULTI PLAYER", True, x.singletextcolor)
    screen.blit(multiplayer, (x.multiButton.x + (x.multiButton.width - multiplayer.get_width()) // 2,
                            x.multiButton.y + (x.multiButton.height - multiplayer.get_height()) // 2))

def dialog_box():
    confirm_box = py.Rect(550, 230, 450, 260)
    py.draw.rect(screen, "white", confirm_box, border_radius=25)
    confirm_font = dialogBox_font.render("Want to exit ?", True, "black")
    screen.blit(confirm_font, (600, 280))
    py.draw.rect(screen, x.yesButtonColor, x.yesButton, border_radius=25)
    py.draw.rect(screen, x.nobuttonColor, x.noButton, border_radius=25)
    yesButtonFont = startFont.render("YES", True, x.yesTextColor)
    noButtonfont = startFont.render("NO", True, x.notextcolor)
    screen.blit(yesButtonFont, (x.yesButton.x + (x.yesButton.width - yesButtonFont.get_width()) // 2,
                           x.yesButton.y + (x.yesButton.height - yesButtonFont.get_height()) // 2))
    screen.blit(noButtonfont, (x.noButton.x + (x.noButton.width - noButtonfont.get_width()) // 2,
                                x.noButton.y + (x.noButton.height - noButtonfont.get_height()) // 2))

#states
HOME = 0
GAME = 1
EXIT_CONFIRM = 2
PLAY = 3
back_click=False
exit_click=False
state = HOME

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
                if x.rectButton.collidepoint(event.pos):
                    st_click_sound.play()
                    x.buttonColor = "white"
                    x.textColor = "blue"
                    #state = GAME
                elif x.quitButton.collidepoint(event.pos):
                    x.quitbuttonColor = "white"
                    x.quittextcolor = "red"
                    #quit_click = True
                    #state = EXIT_CONFIRM
                elif x.exitButton.collidepoint(event.pos):
                    exit_click_sound.play()
                    x.exitButtonColor = "white"
                    x.exitTextColor = "red"
                    #state = EXIT_CONFIRM
            elif state == EXIT_CONFIRM:
                if x.yesButton.collidepoint(event.pos):
                    x.yesButtonColor = "white"
                    x.yesTextColor = "green"
                elif x.noButton.collidepoint(event.pos):
                    x.nobuttonColor = "white"
                    x.notextcolor = "red"
                    exit_click_sound.play()
                    #state = HOME
            elif state == GAME:
                if x.backButton.collidepoint(event.pos):
                    x.backbuttonColor = "white"
                    x.backtextcolor = "red"
                    back_clk_sound.play()
                    #state = HOME
                if x.singleButton.collidepoint(event.pos):
                    st_click_sound.play()
                    x.singlebuttoncolor = "white"
                    x.singletextcolor = "black"
            elif state == PLAY:
                if x.backButton.collidepoint(event.pos):
                    back_clk_sound.play()
                    x.backbuttonColor  = "white"
                    x.backtextcolor = "red"


        if event.type == py.MOUSEBUTTONUP:
            if state == HOME:
                if x.rectButton.collidepoint(event.pos):
                    x.buttonColor = "blue"
                    x.textColor = "white"
                    state = GAME
                elif x.quitButton.collidepoint(event.pos):
                    x.quitbuttonColor = "red"
                    x.quittextcolor = "white"
                    quit_click = True
                    #state = EXIT_CONFIRM
                elif x.exitButton.collidepoint(event.pos):
                    x.exitButtonColor = "red"
                    x.exitTextColor = "white"
                    #exit_click_sound.play()
                    state = EXIT_CONFIRM
            elif state == EXIT_CONFIRM:
                if x.yesButton.collidepoint(event.pos):
                    x.yesButtonColor = "green"
                    x.yesTextColor = "white"
                    py.quit()
                    exit()
                elif x.noButton.collidepoint(event.pos):
                    x.nobuttonColor  = "red"
                    x.notextcolor = "white"
                    #exit_click_sound.play()
                    state = HOME
            elif state == GAME:
                if x.backButton.collidepoint(event.pos):
                    x.backbuttonColor  = "red"
                    x.backtextcolor = "white"
                    state = HOME
                if x.singleButton.collidepoint(event.pos):
                    x.singlebuttoncolor = "#21D4DB"
                    x.singletextcolor = "black"
                    state = PLAY
            elif state == PLAY:
                if x.backButton.collidepoint(event.pos):
                    x.backbuttonColor  = "red"
                    x.backtextcolor = "white"
                    state = GAME

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
        quit_button()
        singleplayer_button()
        multiplayer_button()
        if back_click:
            state = HOME

    elif state == EXIT_CONFIRM:
        dialog_box()

    elif state == PLAY:
        screen.blit(game_back_pic,(0,0))
        cardslots()
        back_button()

    py.display.update()

cap.release()
py.quit()
