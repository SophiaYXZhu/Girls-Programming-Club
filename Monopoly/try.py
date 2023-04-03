import os
import pygame
from inputBox import inputBox
import sys
# import random
from config import *
# from video import Video

dice_map = {1: 'dice_one.png', 2: 'dice_two.png', 3: 'dice_three.png', 4: 'dice_four.png', 5: 'dice_five.png', 6: 'dice_six.png'}
screen = pygame.display.set_mode([1500,800])
pygame.display.set_caption("大富翁")
screen.fill([255,255,255])

def easy_one_init(screen):
    screen.fill([255,255,255])
    easyone = pygame.image.load(os.path.join(IMAGE_DATA_PATH, 'easy1.png'))
    easyone_rect = easyone.get_rect()
    easyone_rect.center = (650,400)
    screen.blit(easyone, (easyone_rect.x, easyone_rect.y))

    pygame.font.init()
    font = pygame.font.Font(None, 50)
    txt_surface = font.render("STATUS", True, [0,0,0])
    screen.blit(txt_surface, (1252,70))
    font = pygame.font.Font(None, 30)
    txt_surface = font.render("Liquid Assets: $150000", True, [0,0,0])
    screen.blit(txt_surface, (1192,120))
    txt_surface = font.render("Bank Deposits: $150000", True, [0,0,0])
    screen.blit(txt_surface, (1192,160))
    txt_surface = font.render("Land Owned: Land 1, 2, 3, 4", True, [0,0,0])
    screen.blit(txt_surface, (1192,200))
    txt_surface = font.render("Land Owned by", True, [0,0,0])
    screen.blit(txt_surface, (1192,240))
    cland = "Competitor: Land 1, 2, 3, 4"
    txt_surface = font.render(cland, True, [0,0,0])
    screen.blit(txt_surface, (1192,265))
    txt_surface = font.render("Luck: 100.0", True, [0,0,0])
    screen.blit(txt_surface, (1192,305))
    txt_surface = font.render("Life: 100", True, [0,0,0])
    screen.blit(txt_surface, (1192,345))
    font = pygame.font.Font(None, 50)
    txt_surface = font.render("Price of Lands", True, [0,0,0])
    screen.blit(txt_surface, (1210,395))
    font = pygame.font.Font(None, 30)
    for i in range(4):
        txt_surface = font.render("Land "+str(i+1)+": $1000", True, [0,0,0])
        screen.blit(txt_surface, (1192,445+i*40))
    dice2_pic = pygame.image.load(
        os.path.join(IMAGE_DATA_PATH, "dice_one.png"))
    dice2_pic = pygame.transform.scale(dice2_pic, (150,150))
    dice2_pic_rect = dice2_pic.get_rect()
    dice2_pic_rect.center = (1250,675)
    screen.blit(dice2_pic, (dice2_pic_rect.x, dice2_pic_rect.y))
    dice2_pic = pygame.image.load(
        os.path.join(IMAGE_DATA_PATH, "dice_one.png"))
    dice2_pic = pygame.transform.scale(dice2_pic, (150,150))
    dice2_pic_rect = dice2_pic.get_rect()
    dice2_pic_rect.center = (1400,675)
    screen.blit(dice2_pic, (dice2_pic_rect.x, dice2_pic_rect.y))

    pygame.display.update()
    pygame.display.flip()

def deposit(screen):
    easy_one_init(screen)
    # ask the player which land does he want to exchange
    trade = pygame.image.load(
        os.path.join(IMAGE_DATA_PATH, 'trade_land.png'))
    trade = pygame.transform.scale(trade, (1200, 550))
    trade_rect = trade.get_rect()
    trade_rect.center = (750,350)
    screen.blit(trade, (trade_rect.x, trade_rect.y))
    box = inputBox(screen)
    land_trade = int(box.input_box((675, 625), "easy_map1", "trade", land = [1,2,3,4]))
    pygame.display.update()
    pygame.display.flip()
    if land_trade == -1:
        ### quit the trade function
        no_pic = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'trade_no.png'))
        no_pic = pygame.transform.scale(no_pic, (1200, 550))
        no_rect = no_pic.get_rect()
        no_rect.center = (750,350)
        screen.blit(no_pic, (no_rect.x, no_rect.y))
    else:
        bought = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'trade_bought.png'))
        bought = pygame.transform.scale(bought, (1200, 550))
        bought_rect = bought.get_rect()
        bought_rect.center = (750,350)
        screen.blit(bought, (bought_rect.x, bought_rect.y))
    pygame.display.update()
    pygame.display.flip()

pygame.font.init()
font = pygame.font.Font(None, 95)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            easyone = pygame.image.load(os.path.join(IMAGE_DATA_PATH, 'easy1.png'))
            easyone_rect = easyone.get_rect()
            easyone_rect.center = (650,400)
            screen.blit(easyone, (easyone_rect.x, easyone_rect.y))
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button==1:
                    print(event.pos)
            trade = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'trade_land.png'))
            trade = pygame.transform.scale(trade, (1200, 430))
            trade_rect = trade.get_rect()
            trade_rect.center = (750,350)
            screen.blit(trade, (trade_rect.x, trade_rect.y))
            pygame.font.init()
            font = pygame.font.Font(None, 95)
            txt_surface = font.render("1, 2, 3, 4", True, [255,255,255])
            screen.blit(txt_surface, (993,240))
            screen.blit(txt_surface, (336,455))
            # easy_one_init(screen)
            pygame.display.update()
            pygame.display.flip()

# class Try:
#     def __init__(self):
#         self.screen = pygame.display.set_mode([1500,800])
    
#     def play(self):
#         self.screen.fill([255,255,255])
#         pygame.display.set_caption("大富翁")
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()
#                 if event.type == pygame.MOUSEBUTTONUP:
#                     if event.button==1:
#                         print(event.pos)
#                         dice1 = random.randint(1,6)
#                         dice1_pic = pygame.image.load(
#                             os.path.join(IMAGE_DATA_PATH, 'dice_one.png'))
#                         dice1_pic = pygame.transform.scale(dice1_pic, (150,150))
#                         dice1_pic_rect = dice1_pic.get_rect()
#                         dice1_pic_rect.center = (75,750)
#                         self.screen.blit(dice1_pic, (dice1_pic_rect.x, dice1_pic_rect.y))
#             pygame.display.update()
#             pygame.display.flip()
    
# if __name__ == "__main__":
#     a = Try()
#     a.play()