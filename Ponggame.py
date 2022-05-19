
from ast import While
from pickle import FALSE, TRUE
from turtle import right
import pygame, sys, random
from paddler import Paddle
#khoi tao
pygame.init()
clock = pygame.time.Clock()

#tao cua so game
screen_width = 1200
screen_height = 750
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong Game')
 
#nhac trong game
def chamvach():
    pygame.mixer.init()
    pygame.mixer.music.load('Pong!.mp3')
    pygame.mixer.music.play(0)
def ghidiem():
    pygame.mixer.init()
    pygame.mixer.music.load('pongscore.mp3')
    pygame.mixer.music.play(0)

# colors
BLACK=(0,0,0)# RGB
WHITE = (255, 255, 255) 
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (84, 86, 85)
BGCOLOR = (251, 234, 238)
bg_color = pygame.Color(BGCOLOR)
str1= 'Chào Mừng Bạn Đến Với Game Pong'
str2='Nhấn A để chọn VS PC'
str3='Nhấn B để chọn VS Player'
strRD = 'Bạn đã sẵn sàng'
strPC = 'Bạn chọn chơi với máy'
strPR = 'Bạn chọn 2 người chơi'
# Rectangles
m = 30 # chieu cao va chieu rong cua trai banh
ball = pygame.Rect(screen_width/2 - m/2,screen_height/2 - m/2,m,m)
player_right = pygame.Rect(screen_width - 20,screen_height/2 - 70, 10, 140)
player_left = pygame.Rect(10, screen_height/2 -70, 10, 140)


#toc do
speed = 6 # tốc độ di chuyển
ball_speed_x = speed * random.choice((1,-1))
ball_speed_y = speed * random.choice((1,-1))
player_speed = 0 #toc do nguoi choi
player_speedright=0
player_speedleft=0
player_left_speed = speed
player_right_speed = speed


# score
left_score = 0
right_score = 0
dem = 5
game_font = pygame.font.Font("Lato-Heavy.ttf",35)
def scoreshow():
    left_text = game_font.render(f"{left_score}",False,BLACK)
    screen.blit(left_text,(screen_width/2 -60,50))
 
    right_text = game_font.render(f"{right_score}",False,BLACK)
    screen.blit(right_text,(screen_width/2 +45,50))

# Draw
def draw():  
    # pygame.draw(surface, color, rect)
    screen.fill(bg_color)
    pygame.draw.ellipse(screen,BLUE,ball)
    pygame.draw.rect(screen,BLACK,player_right)
    pygame.draw.rect(screen,BLACK,player_left)
    pygame.draw.aaline(screen,BLACK,(screen_width/2,0),(screen_width/2,screen_height))
 
def ball_mover():
    global ball_speed_x, ball_speed_y,right_score,left_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
     
    if ball.top <= 0 or ball.bottom >= screen_height:
        chamvach()
        pygame.draw.ellipse(screen,RED,ball)
        ball_speed_y *= -1 
    if ball.left <= 0:
        right_score += 1
        ghidiem()
        ball_reset() # đặt lại trái banh về giữa màn hình
    if ball.right >= screen_width:
        left_score += 1
        ghidiem()
        ball_reset() # đặt lại trái banh về giữa màn hình
 
    if ball.colliderect(player_left) or ball.colliderect(player_right):
        ball_speed_x *= -1
def ball_reset():
    global ball_speed_x,ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))
def player_rightmover(): 
        player_right.y += player_speedright
        if player_right.top <= 0:
            player_right.top = 0
        if player_right.bottom >= screen_height:
            player_right.bottom = screen_height
def player_leftmover():
    player_left.y += player_speedleft
    if player_left.top <= 0:
        player_left.top = 0
    if player_left.bottom >= screen_height:
        player_left.bottom = screen_height
def player_pcmover():
    if player_left.top < ball.y:
        player_left.top += player_left_speed
    if player_left.bottom > ball.y:
        player_left.top -= player_left_speed
 
    if player_left.top <= 0:
        player_left.top = 0
    if player_left.bottom >= screen_height:
        player_left.bottom = screen_height
def player_rightclick():
    global player_speedright
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player_speedright -= speed
        if event.key == pygame.K_DOWN:
            player_speedright += speed
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            player_speedright += speed
        if event.key == pygame.K_DOWN:
            player_speedright -= speed
def player_leftclick():
    global player_speedleft
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            player_speedleft -= speed
        if event.key == pygame.K_s:
            player_speedleft += speed
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            player_speedleft += speed
        if event.key == pygame.K_s:
            player_speedleft -= speed   
 
#chao mung nguoi choi
def welcome():
    welcome= game_font.render(f"{str1}",False,WHITE)    #set chữ
    screen.blit(welcome,(screen_width/2-300 ,50))       #in chữ ra màn hình game
    option1= game_font.render(f"{str2}",False,WHITE)    
    screen.blit(option1,(50 ,150))    
    option2= game_font.render(f"{str3}",False,WHITE)    
    screen.blit(option2,(screen_width/2 + 100 ,150))   

def readytwoplayer():# màn hình chờ của người vs người
    option= game_font.render(f"{strPR}",False,WHITE)    #set chữ
    screen.blit(option,(screen_width/2 -150 ,100))      #in chữ ra màn hình game
    ready = game_font.render(f"{strRD}",FALSE,WHITE)    
    screen.blit(ready,(screen_width/2 -100, 250))
      
    pygame.draw.ellipse(screen,BLUE,ball)               #vẽ qua banh giữ màn hình
    pygame.draw.rect(screen, GREY, (screen_width/2 -170, screen_height/2 + 200, 402, 60)) #vẽ phông nền dưới chữ
    textSurface = game_font.render('Press SPACE To Continue', False, (255, 255, 255))
    screen.blit(textSurface, (screen_width/2 -170, screen_height/2 +200))

def readypcplayer(): # màn hình chờ của người vs máy
    option= game_font.render(f"{strPC}",False,WHITE)    #set chữ
    screen.blit(option,(screen_width/2 -150 ,100))      #set chữ
    ready = game_font.render(f"{strRD}",FALSE,WHITE)
    screen.blit(ready,(screen_width/2 -100, 250))

    pygame.draw.ellipse(screen,BLUE,ball)               #vẽ qua banh giữ màn hình
    pygame.draw.rect(screen, GREY, (screen_width/2 -170, screen_height/2 + 200, 402, 60))
    textSurface = game_font.render('Press SPACE To Continue', False, (255, 255, 255))       #vẽ phông nền dưới chữ
    screen.blit(textSurface, (screen_width/2 -170, screen_height/2 +200))
#pause
def pause():
    paused = True
    while paused:
        for event_pause in pygame.event.get():
            if event_pause.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event_pause.type == pygame.KEYDOWN:
                if event_pause.key == pygame.K_c:
                    paused = False
                elif event_pause.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.fill(BLACK)
        textSurface = game_font.render('I I', False, (255, 255, 255))
        screen.blit(textSurface, (screen_width/2 , 100))
        textSurface = game_font.render('PAUSED', False, (255, 255, 255))
        screen.blit(textSurface, (screen_width/2-60 , 200))
        pygame.draw.rect(screen, RED, (screen_width/2 -150, screen_height/2, 320, 60))
        textSurface = game_font.render('Press C To Continue', False, (255, 255, 255))
        screen.blit(textSurface, (screen_width/2 -150, screen_height/2))

        pygame.display.update()

twoplayer = False
pcplayer = False
readyplayer = True
readypc = True
introOn = True
conra = True
while introOn:
    welcome()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type ==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                introOn = False
                readyplayer = False
                # break
            elif event.key==pygame.K_b:
                introOn = False
                readypc = False
                # break
            else: 
                textSurface = game_font.render('Bạn nhấn sai hãy nhấn lại', False, RED)
                screen.blit(textSurface, (screen_width/2 -100, 500))
                pygame.display.update()    
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                pygame.quit()
        
   
#man hinh ready cua pc
while readypc:
    screen.fill(BLACK)
    readypcplayer()
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                pygame.quit()
        # User did something
        if event.type == pygame.KEYDOWN:  # If user clicked close
            if event.key == pygame.K_SPACE:
                readypc = False  # Flag that we are done so we exit this loop
                pcplayer = True
    
    
    
#man hinh ready cua nguoi
while readyplayer:
    screen.fill(BLACK)
    readytwoplayer()
    pygame.display.update()
   
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                pygame.quit()
        # User did something
        if event.type == pygame.KEYDOWN:  # If user clicked close
            if event.key == pygame.K_SPACE:
                readyplayer = False  # Flag that we are done so we exit this loop
                twoplayer = True
    
    


# Loop vs Player
while twoplayer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            twoplayer = False  # Flag that we are done so we exit this loop
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                twoplayer = False
            elif event.key == pygame.K_p:
                pause()
        elif left_score == dem or right_score == dem:
            twoplayer =False
        player_rightclick()
        player_leftclick()
        
    if left_score == dem or right_score == dem:
        twoplayer =False
    

    ball_mover()# banh di chuyen
    player_rightmover()
    player_leftmover()
    

    draw()#ve cac chi tiet
    scoreshow()# show bang diem
    
    # cap nhat cua so
    pygame.display.flip()
    clock.tick(60)
# loop vs PC
while pcplayer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            pcplayer = False  # Flag that we are done so we exit this loop
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                pcplayer = False
            elif event.key == pygame.K_p:
                pause()
        
        player_rightclick()
    
    if left_score == dem or right_score == dem:
        pcplayer =False

    ball_mover()# banh di chuyen
    player_rightmover()
    player_pcmover()
    

    draw()#ve cac chi tiet
    scoreshow()# show bang diem
    
    # cap nhat cua so
    pygame.display.flip()
    clock.tick(60)
conra = True
while conra:
    screen.fill(BLACK)
    if left_score > right_score:
        textSurface = game_font.render('Player 1 Wins!', False, RED)
        screen.blit(textSurface, (screen_width/2 -100, 200))
        conti = game_font.render('Press SPACE To ExitGame', False, RED)
        screen.blit(conti, (screen_width/2 -170, screen_height/2))
    elif left_score < right_score:
        textSurface = game_font.render('Player 2 Wins', False, RED)
        screen.blit(textSurface, (screen_width/2-100, 200))
        conti = game_font.render('Press SPACE To Exitgame', False, RED)
        screen.blit(conti, (screen_width/2 -170, screen_height/2))
    else:
        textSurface = game_font.render('YOU DREW!', False, RED)
        screen.blit(textSurface, (screen_width/2-100, 200))
    


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                pygame.quit()
        # User did somethingh
        if event.type == pygame.KEYDOWN:  # If user clicked close
            if event.key == pygame.K_SPACE:
                conra = False  # Flag that we are done so we exit this loop


pygame.quit()