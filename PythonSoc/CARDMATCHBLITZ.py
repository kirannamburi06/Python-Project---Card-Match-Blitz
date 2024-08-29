import pygame as py
import cv2
import time
#import pygame.image


class x:
    # for static variables
    count = 0
    r = 0
    c = 0
    s = 0
    #start button hover effect
    buttonColor = "blue"
    textColor = "white"
    rectButton = py.Rect(670, 410, 180, 80)

    #quit button hover effect
    quitbuttonColor = "red"
    quittextcolor = "white"
    quitButton = py.Rect(20, 20, 140, 60)

    #exit button and its hover effect
    exitButtonColor = "red"
    exitTextColor = "white"
    exitButton = py.Rect(670 , 530 , 180 , 80)

    #yes button
    yesButtonColor = "green"
    yesTextColor = "white"
    yesButton = py.Rect(600,360,90,70)
    nobuttonColor = "red"
    notextcolor = "white"
    noButton = py.Rect(800, 360, 90, 70)


py.init()
py.mixer.init()

#screen design
screen = py.display.set_mode((1500,750))
py.display.set_icon(py.image.load('data/logo.png'))
py.display.set_caption("CARD MATCH BLITZ")
interface_img = py.image.load('data/logo.png')

#for videos
cap = cv2.VideoCapture("data/backgorund cards game.mp4")
loadCap = cv2.VideoCapture("data/loadingvideo.mp4")

#images
bg_image = py.image.load("data/backgrouund__.jpg")
bg_image = py.transform.scale(bg_image,(1500,750))

#fonts
titleFont=py.font.Font('data/BruceForeverRegular-X3jd2.ttf',70)
font = py.font.SysFont('Arial', 40)
startFont=py.font.SysFont('Comic Sans',40)
dialogBox_font = py.font.Font('data/Rafgins-Regular.otf',50)

#Music
py.mixer.music.load("data/bg_music.mp3")

def titleDisplay():
    if x.c<1:
        list = ['red', 'green', 'blue','orange','violet','yellow']
        x.r = (x.r+1) % (len(list))
        titleImg = titleFont.render("CARD MATCH BLITZ",True,list[x.r])
        title_width , title_height = titleImg.get_size()
        pad = 20
        back_rect = py.Rect(290,240,title_width+pad,title_height+pad)
        py.draw.rect(screen,'white',back_rect)
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
        while frames < 240 :
            ret, loadFrame = loadCap.read()
            if not ret:
                continue
            loadFrame = cv2.cvtColor(loadFrame, cv2.COLOR_BGR2RGB)
            loadFrame = cv2.resize(loadFrame, (400, 100))
            loadFrame = py.surfarray.make_surface(loadFrame.swapaxes(0, 1))
            screen.blit(loadFrame, (540, 650))
            py.display.update()
            frames+=1
        py.time.wait(1000)
        x.count += 1

def start_button():
    py.draw.rect(screen, x.buttonColor, x.rectButton)
    startText = startFont.render("START", True, x.textColor)
    screen.blit(startText, (x.rectButton.x + (x.rectButton.width - startText.get_width()) // 2,
                            x.rectButton.y + (x.rectButton.height - startText.get_height()) // 2))

def quit_button():
    py.draw.rect(screen,x.quitbuttonColor,x.quitButton)
    quitText = startFont.render("QUIT",True,x.quittextcolor)
    screen.blit(quitText, (x.quitButton.x + (x.quitButton.width - quitText.get_width()) // 2,
                           x.quitButton.y + (x.quitButton.height - quitText.get_height()) // 2))

def exit_button():
    py.draw.rect(screen, x.exitButtonColor, x.exitButton)
    exitText = startFont.render("EXIT", True, x.exitTextColor)
    screen.blit(exitText, (x.exitButton.x + (x.exitButton.width - exitText.get_width()) // 2,
                            x.exitButton.y + (x.exitButton.height - exitText.get_height()) // 2))

def dialog_box():
    confirm_box = py.Rect(550,230, 450,260)
    py.draw.rect(screen,"white",confirm_box)
    confirm_font = dialogBox_font.render("Want to exit ? ",True,"black")
    screen.blit(confirm_font,(600,280))
    py.draw.rect(screen,x.yesButtonColor,x.yesButton)
    py.draw.rect(screen,x.nobuttonColor,x.noButton)
    yesButtonFont = startFont.render("YES",True,x.yesTextColor)
    noButtonfont = startFont.render("NO",True, x.notextcolor)
    screen.blit(yesButtonFont, (x.yesButton.x + (x.yesButton.width - yesButtonFont.get_width()) // 2,
                           x.yesButton.y + (x.yesButton.height - yesButtonFont.get_height()) // 2))
    screen.blit(noButtonfont, (x.noButton.x + (x.noButton.width - noButtonfont.get_width()) // 2,
                                x.noButton.y + (x.noButton.height - noButtonfont.get_height()) // 2))

#Flags
start_click = False
window = True
bgMusic_state = False
yes_click = False
exit_click = False
no_click = False
#Mainloop
while window :
    #events
    for event in py.event.get():
        if event.type == py.QUIT:
            window = False
        if event.type == py.MOUSEBUTTONDOWN:
            if x.rectButton.collidepoint(event.pos):
                x.buttonColor = "aqua"
                x.textColor = "black"
            if x.quitButton.collidepoint(event.pos):
                x.quitbuttonColor = "orange"
                x.quittextcolor = "black"
            if x.exitButton.collidepoint(event.pos):
                x.exitButtonColor = "white"
                x.exitTextColor = "black"
        if event.type == py.MOUSEBUTTONUP:
            if x.rectButton.collidepoint(event.pos):
                x.buttonColor = "blue"
                x.textColor = "white"
                start_click = True
            if x.quitButton.collidepoint(event.pos):
                x.quitbuttonColor = "red"
                x.quittextcolor = "white"
                start_click = False
            if x.exitButton.collidepoint(event.pos):
                x.exitButtonColor = "red"
                x.exitTextColor = "white"
                exit_click = True
            if x.yesButton.collidepoint(event.pos):
                yes_click = True
            if x.noButton.collidepoint(event.pos):
                no_click = True


    if start_click :
        screen.blit(bg_image, (0,0))
        py.mixer.music.stop()
        quit_button()
    else:
        InterfaceLoadingVideo()
        screen.fill((0,0,0))
        bgMusic_state = backgroundVideo()
        if bgMusic_state and not py.mixer.music.get_busy():
            py.mixer.music.play()

        titleDisplay()
        start_button()
        exit_button()
        if exit_click and not no_click:
            dialog_box()
            eve = py.event.wait()
            if eve.type == py.MOUSEBUTTONDOWN:
                no_click = False
                exit_click = False
            if yes_click:
                exit()

    py.display.update()

cap.release()

py.quit()