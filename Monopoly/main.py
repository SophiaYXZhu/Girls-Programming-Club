import pygame
import random
import sys
from config import *
import os

class daFuWen():
    def __init__(self):
        print("Welcome!")

    def da_fu_wen(self):
        screen = pygame.display.set_mode([1500,800])
        pygame.display.set_caption("大富翁")
        screen.fill([255,255,255])
        easy = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'easy.png'))
        easy_rect = easy.get_rect()
        easy_rect.center = (375,400)
        screen.blit(easy, (easy_rect.x, easy_rect.y))
        hard = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'hard.png'))
        hard_rect = hard.get_rect()
        hard_rect.center = (1125,400)
        screen.blit(hard, (hard_rect.x, hard_rect.y))
        pygame.display.update()
        pygame.display.flip()
        easy = False
        hard = False
        one = False
        multi = False
        easy_map1 = False
        easy_map2=False
        hard_map1=False
        hard_map2=False
        while not easy and not hard: #chose easy or hard
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        position = event.pos
                        if 180<=position[0]<=600 and 190<=position[1]<=570: #easy
                            print('easy')
                            screen.fill([255,255,255])
                            one_v = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, '1v1.png'))
                            one_rect = one_v.get_rect()
                            one_rect.center = (375,400)
                            screen.blit(one_v, (one_rect.x, one_rect.y))
                            many = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, '1vn.png'))
                            many_rect = many.get_rect()
                            many_rect.center = (1125,400)
                            screen.blit(many, (many_rect.x, many_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            easy = True
                        elif 920<=position[0]<=1350 and 190<=position[1]<=570: #hard
                            print('hard')
                            screen.fill([255,255,255])
                            one_v = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, '1v1.png'))
                            one_rect = one_v.get_rect()
                            one_rect.center = (375,400)
                            screen.blit(one_v, (one_rect.x, one_rect.y))
                            many = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, '1vn.png'))
                            many_rect = many.get_rect()
                            many_rect.center = (1125,400)
                            screen.blit(many, (many_rect.x, many_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            hard = True
        while not one and not multi: #chose 1v1 or 1vn
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        position = event.pos
                        if 50<=position[0]<=700 and 235<=position[1]<=550 and easy: #1v1, easy
                            print('1v1')
                            screen.fill([255,255,255])
                            map1 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'easy_chose1.png'))
                            map1 = pygame.transform.scale(map1, (600,400))
                            map1_rect = map1.get_rect()
                            map1_rect.center = (375,400)
                            screen.blit(map1, (map1_rect.x, map1_rect.y))
                            map2 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'easy_chose2.png'))
                            map2 = pygame.transform.scale(map2, (600,400))
                            map2_rect = map2.get_rect()
                            map2_rect.center = (1125,400)
                            screen.blit(map2, (map2_rect.x, map2_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            one = True
                        elif 800<=position[0]<=1450 and 235<=position[1]<=550 and easy: #1vn, easy
                            print('1vn')
                            screen.fill([255,255,255])
                            map1 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'easy_chose1.png'))
                            map1 = pygame.transform.scale(map1, (600,400))
                            map1_rect = map1.get_rect()
                            map1_rect.center = (375,400)
                            screen.blit(map1, (map1_rect.x, map1_rect.y))
                            map2 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'easy_chose2.png'))
                            map2 = pygame.transform.scale(map2, (600,400))
                            map2_rect = map2.get_rect()
                            map2_rect.center = (1125,400)
                            screen.blit(map2, (map2_rect.x, map2_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            multi = True
                        elif 50<=position[0]<=700 and 235<=position[1]<=550 and hard: #1v1, hard
                            print('1v1')
                            screen.fill([255,255,255])
                            map1 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'hard_chose1.png'))
                            map1 = pygame.transform.scale(map1, (600,400))
                            map1_rect = map1.get_rect()
                            map1_rect.center = (375,400)
                            screen.blit(map1, (map1_rect.x, map1_rect.y))
                            map2 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'hard_chose2.png'))
                            map2 = pygame.transform.scale(map2, (600,400))
                            map2_rect = map2.get_rect()
                            map2_rect.center = (1125,400)
                            screen.blit(map2, (map2_rect.x, map2_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            one = True
                        elif 800<=position[0]<=1450 and 235<=position[1]<=550 and hard: #1vn, hard
                            print('1vn')
                            screen.fill([255,255,255])
                            map1 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'hard_chose1.png'))
                            map1 = pygame.transform.scale(map1, (600,400))
                            map1_rect = map1.get_rect()
                            map1_rect.center = (375,400)
                            screen.blit(map1, (map1_rect.x, map1_rect.y))
                            map2 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'hard_chose2.png'))
                            map2 = pygame.transform.scale(map2, (600,400))
                            map2_rect = map2.get_rect()
                            map2_rect.center = (1125,400)
                            screen.blit(map2, (map2_rect.x, map2_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            multi = True

        while not easy_map1 and not easy_map2 and not hard_map1 and not hard_map2: #select map
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        position = event.pos
                        if easy:
                            if 77<=position[0]<=204 and 644<=position[1]<=574: #easy, map1
                                screen.fill([255,255,255])
                                map1 = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'easy1.png'))
                                map1_rect = map1.get_rect()
                                map1_rect.center = (750,400)
                                screen.blit(map1, (map1_rect.x, map1_rect.y))
                                pygame.display.update()
                                pygame.display.flip()
                                easy_map1 = True
                            elif 825<=position[0]<=1425 and 200<=position[1]<=600: #easy, map2
                                screen.fill([255,255,255])
                                map2 = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'easy2.png'))
                                map2_rect = map2.get_rect()
                                map2_rect.center = (750,400)
                                screen.blit(map2, (map2_rect.x, map2_rect.y))
                                pygame.display.update()
                                pygame.display.flip()
                                easy_map2 = True
                        elif hard:
                            if 77<=position[0]<=204 and 64<=position[1]<=574: #hard, map1
                                screen.fill([255,255,255])
                                map1 = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'hard1.png'))
                                map1_rect = map1.get_rect()
                                map1_rect.center = (750,400)
                                screen.blit(map1, (map1_rect.x, map1_rect.y))
                                pygame.display.update()
                                pygame.display.flip()
                                hard_map1 = True
                            elif 825<=position[0]<=1425 and 200<=position[1]<=600: #hard, map2
                                screen.fill([255,255,255])
                                map2 = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'hard2.png'))
                                map2_rect = map2.get_rect()
                                map2_rect.center = (750,400)
                                screen.blit(map2, (map2_rect.x, map2_rect.y))
                                pygame.display.update()
                                pygame.display.flip()
                                hard_map2 = True
        player = 0
        machine = 0
        while True: #play the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        position = event.pos
                        print(position)
                        if easy_map1 and one:
                            occur = ['start','trade1,3', 'deposit','forward3','?','deposit','trade2','backward3','trade3,4','forward2','spin','?','trade1,4','surprise','prison','end']
                            # roll the dice
                            for i in range(5):
                                dice1 = random.randint(1,6)
                                if dice1 == 1:
                                    dice1_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_one.png'))
                                elif dice1 == 2:
                                    dice1_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_two.png'))
                                elif dice1 == 3:
                                    dice1_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_three.png'))
                                elif dice1 == 4:
                                    dice1_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_four.png'))
                                elif dice1 == 5:
                                    dice1_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_five.png'))
                                elif dice1 == 6:
                                    dice1_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_six.png'))
                                dice1_pic = pygame.transform.scale(dice1_pic, (75,75))
                                dice1_pic_rect = dice1_pic.get_rect()
                                dice1_pic_rect.center = (100,700)
                                screen.blit(dice1_pic, (dice1_pic_rect.x, dice1_pic_rect.y))
                                dice2 = random.randint(1,6)
                                if dice2 == 1:
                                    dice2_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_one.png'))
                                elif dice2 == 2:
                                    dice2_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_two.png'))
                                elif dice2 == 3:
                                    dice2_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_three.png'))
                                elif dice2 == 4:
                                    dice2_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_four.png'))
                                elif dice2 == 5:
                                    dice2_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_five.png'))
                                elif dice2 == 6:
                                    dice2_pic = pygame.image.load(
                                        os.path.join(IMAGE_DATA_PATH, 'dice_six.png'))
                                dice2_pic = pygame.transform.scale(dice2_pic, (75,75))
                                dice2_pic_rect = dice2_pic.get_rect()
                                dice2_pic_rect.center = (200,700)
                                screen.blit(dice2_pic, (dice2_pic_rect.x, dice2_pic_rect.y))
                                pygame.display.update()
                                pygame.display.flip()
                            print(dice1, dice2)
                            player_same = False
                            player_land = []
                            if dice1 == dice2:
                                plyer_same = True
                                player += dice1
                            else:
                                player += (dice1+dice2)//2
                            if occur[player] == 'trade1,3':
                                
                            elif occur[player] == 'deposit':
                                
                            elif occur[player] == 'forward3':
                                player += 3
                            elif occur[player] == '?':
                                
                            elif occur[player] == 'trade2':
                                
                            elif occur[player] == 'backward3':
                                player -= 3
                            elif occur[player] == 'trade3,4':

                            elif occur[player] == 'forward2':
                                player += 2
                            elif occur[player] == 'spin':

                            elif occur[player] == 'trade1,4':

                            elif occur[player] == 'surprise':

                            elif occur[player] == 'prison':

                        elif easy_map1 and multi:
                        
                        elif easy_map2 and one:

                        elif easy_map2 and multi:

                        elif hard_map1 and one:

                        elif hard_map1 and multi:

                        elif hard_map2 and one:

                        elif hard_map2 and multi:


       
if __name__ == '__main__':
    a = daFuWen()
    a.da_fu_wen()