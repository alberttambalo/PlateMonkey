import pygame

pygame.init()

WIN = pygame.display.set_mode((750,750))
pygame.display.set_caption("Plate Monkey!")

bar = []

base_font = pygame.font.Font(None,32)

def draw_bar():
    pygame.draw.rect(WIN, (255,255,255), (0,360,80,30))

def add_25s(x):
    pygame.draw.rect(WIN, (255, 0, 0), (60*(x), 200, 50, 350),border_radius=10)
    wt = base_font.render("25", True, (0,0,0))
    WIN.blit(wt, (60*(x)+12.5, 360));

def add_20s(x):
    pygame.draw.rect(WIN, (0, 0, 255), (60*(x), 200, 50, 350),border_radius=10)
    wt = base_font.render("20", True, (0,0,0))
    WIN.blit(wt, (60*(x)+12.5, 360));

def add_15s(x):
    pygame.draw.rect(WIN, (255, 255, 0), (60*(x), 200, 50, 350),border_radius=10)
    wt = base_font.render("15", True, (0,0,0))
    WIN.blit(wt, (60*(x)+12.5, 360));

def add_10s(x):
    pygame.draw.rect(WIN, (0, 255, 0), (60*(x), 225, 50, 300),border_radius=10)
    wt = base_font.render("10", True, (0,0,0))
    WIN.blit(wt, (60*(x)+12.5, 360));

def add_5s(x):
    pygame.draw.rect(WIN, (255, 255, 255), (60*(x), 250, 50, 250),border_radius=10)
    wt = base_font.render("5", True, (0,0,0))
    WIN.blit(wt, (60*(x)+12.5, 360));

def add_2p5s(x):
    pygame.draw.rect(WIN, (0, 0, 0), (60*(x), 275, 50, 200),border_radius=10)
    wt = base_font.render("2.5", True, (255,255,255))
    WIN.blit(wt, (60*(x)+12.5, 360));

def add_1s(x):
    pygame.draw.rect(WIN, (192, 192, 192), (60*(x), 300, 50, 150),border_radius=10)
    wt = base_font.render("1", True, (0,0,0))
    WIN.blit(wt, (60*(x)+12.5, 360));

def add_p5s(x):
    pygame.draw.rect(WIN, (192, 192, 192), (60*(x), 325, 50, 100),border_radius=10)
    wt = base_font.render(".5", True, (0,0,0))
    WIN.blit(wt, (60*(x)+12.5, 360));

def load_bar():
    i = 0
    for b in bar:
        if b == 45: draw_bar()
        elif b == 25: add_25s(i)
        elif b == 20: add_20s(i)
        elif b == 15: add_15s(i)
        elif b == 10: add_10s(i)
        elif b == 5: add_5s(i)
        elif b == 2.5: add_2p5s(i)
        elif b == 1: add_1s(i)
        elif b == .5: add_p5s(i)
        i += 1

def validate(x):
    if x.isdigit() or x == '' : return True
    else: return False

def calculate_bar(x):
    if(x < 20):
        return
    temp = x
    if(temp-20 >= 0):
        bar.append(45)
        temp = temp-20
    while(temp-(2*25) >= 0):
        bar.append(25)
        temp = temp-(2*25)
    while(temp-(2*20) >= 0):
        bar.append(20)
        temp = temp-(2*20)
    while(temp-(2*15) >= 0):
        bar.append(15)
        temp = temp-(2*15)
    while(temp-(2*10) >= 0):
        bar.append(10)
        temp = temp-(2*10)
    while(temp-(2*5) >= 0):
        bar.append(5)
        temp = temp-(2*5)
    while(temp-(2*2.5) >= 0):
        bar.append(2.5)
        temp = temp-(2*2.5)
    while(temp-(2*1) >= 0):
        bar.append(1)
        temp = temp-(2*1)
    while(temp-(2*.5) >= 0):
        bar.append(.5)
        temp = temp-(2*.5)


def main():
    run = True
    WIN.fill((211,211,211))
    draw_bar()
    user_text = ''
    mode = "kilo"
    while run:
        WIN.fill((211, 211, 211))
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_BACKSPACE:
                     user_text = user_text[0:-1]
                 else:
                    user_text += event.unicode
             if event.type == pygame.MOUSEBUTTONDOWN:
                mode = "kilo" if mode == "pound" else "pound"
        text_surface = base_font.render(user_text,True,(255,255,255))
        WIN.blit(text_surface,(10,100));

        if validate(user_text):
            if(user_text != ''):
                bar.clear()
                if mode == "kilo":
                    calculate_bar(int(user_text))
                else:
                    calculate_bar(int(user_text) / 2.205)
                load_bar()
        else:
            error_message = base_font.render("NOT A VALID WEIGHT", True, (255, 0, 0))
            WIN.blit(error_message, (10, 130));

        mode_s = base_font.render(mode, True, (255, 0, 0))
        WIN.blit(mode_s, (650, 100));


        pygame.display.update()

main()