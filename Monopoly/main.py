from re import S
from turtle import Turtle
import pygame
import random
import sys
from config import *
import os
from video import Video
from easyOnePlayer import easyOnePlayer
from easyOneComputer import easyOneComputer
# from easyTwo import easyTwo
# from hardOne import hardOne
# from hardTwo import hardTwo

class Monopoly():
    def __init__(self):
        self.screen = pygame.display.set_mode([1500,800])
        # array keeping track of dice
        self.dice_map = {1: 'dice_one.png', 2: 'dice_two.png', 3: 'dice_three.png', 4: 'dice_four.png', 5: 'dice_five.png', 6: 'dice_six.png'}
        print("Welcome to Monopoly")
    
    def easy_one_init(self, player_land, computer_land, land, player:easyOnePlayer):
        self.screen.fill([255,255,255])
        easyone = pygame.image.load(os.path.join(IMAGE_DATA_PATH, 'easy1.png'))
        easyone_rect = easyone.get_rect()
        easyone_rect.center = (650,400)
        self.screen.blit(easyone, (easyone_rect.x, easyone_rect.y))
        ### display values of age, luck, money, and land owned by player and comuter in the margin
        pygame.font.init()
        font = pygame.font.Font(None, 50)
        txt_surface = font.render("STATUS", True, [0,0,0])
        self.screen.blit(txt_surface, (1252,70))
        font = pygame.font.Font(None, 30)
        txt_surface = font.render("Liquid Assets: $"+str(round(player.money,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (1192,120))
        txt_surface = font.render("Bank Deposits: $"+str(round(player.bank_money,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (1192,160))
        pland = "Land Owned: "
        own = False
        for i in range(4):
            if player_land[i]:
                own = True
                pland += str(i+1)+", "
        if not own:
            pland += "None"
        else:
            pland = pland[:-2]
        txt_surface = font.render(pland, True, [0,0,0])
        self.screen.blit(txt_surface, (1192,200))
        txt_surface = font.render("Land Owned by", True, [0,0,0])
        self.screen.blit(txt_surface, (1192,240))
        cland = "Competitor: "
        own = False
        for i in range(4):
            if computer_land[i]:
                own = True
                cland += str(i+1)+", "
        if not own:
            cland += "None"
        else:
            cland = cland[:-2]
        txt_surface = font.render(cland, True, [0,0,0])
        self.screen.blit(txt_surface, (1192,265))
        txt_surface = font.render("Luck: "+str(round(player.luck*100,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (1192,305))
        txt_surface = font.render("Life: "+str(player.life), True, [0,0,0])
        self.screen.blit(txt_surface, (1192,345))
        font = pygame.font.Font(None, 58)
        txt_surface = font.render("Price of Lands", True, [0,0,0])
        self.screen.blit(txt_surface, (1200,395))
        font = pygame.font.Font(None, 35)
        for i in range(4):
            txt_surface = font.render("Land "+str(i+1)+": $"+str(round(land[i],2)), True, [0,0,0])
            self.screen.blit(txt_surface, (1192,445+i*50))
        #######
        pygame.display.update()
        pygame.display.flip()
    
    def click_to_moveon(self, player, computer, player_land, comp_land, land, player_obj): # for easyone only
        pos_player = [(162,144),(162,272),(162,399),(162,520),(162,650),(286,650),(418,650),(546,650),(676,650),(799,650),(926,650),(1056,650),(1056,520),(1056,399),(1056,272),(1056,144)]
        pos_computer =[(232,144),(232,272),(232,399),(232,520),(232,650),(356,650),(485,650),(612,650),(739,650),(868,650),(996,650),(1122,650),(1122,520),(1122,399),(1122,272),(1122,144)]
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.easy_one_init(player_land, comp_land, land, player_obj)
                    self.blit_player_icon(pos_player[player])
                    self.blit_comp_icon(pos_computer[computer])
                    done = True
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.easy_one_init(player_land, comp_land, land, player_obj)
                        self.blit_player_icon(pos_player[player])
                        self.blit_comp_icon(pos_computer[computer])
                        done = True
                        break
        pygame.display.update()
        pygame.display.flip()

    def blit_player_icon(self,center):
        icon = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'player_icon.png'))
        icon = pygame.transform.scale(icon, (50, 50))
        icon_rect = icon.get_rect()
        icon_rect.center = center
        self.screen.blit(icon, (icon_rect.x, icon_rect.y))
        pygame.display.update()
        pygame.display.flip()

    def blit_comp_icon(self,center):
        icon = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'comp_icon.png'))
        icon = pygame.transform.scale(icon, (50, 50))
        icon_rect = icon.get_rect()
        icon_rect.center = center
        self.screen.blit(icon, (icon_rect.x, icon_rect.y))
        pygame.display.update()
        pygame.display.flip()

    def player_dead(self):
        dead = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'player_died.png'))
        dead = pygame.transform.scale(dead, (1150,200))
        dead_rect = dead.get_rect()
        dead_rect.center = (750,400)
        self.screen.blit(dead, (dead_rect.x, dead_rect.y))
        pygame.display.update()
        pygame.display.flip()
        die_pic = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'comp_win.png'))
        die_pic = pygame.transform.scale(die_pic, (1150,200))
        die_rect = die_pic.get_rect()
        die_rect.center = (750,400)
        self.screen.blit(die_pic, (die_rect.x, die_rect.y))
        pygame.time.wait(5000)
        sys.exit()
    
    def comp_dead(self):
        die_pic = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'comp_die.png'))
        die_pic = pygame.transform.scale(die_pic, (1150,200))
        die_rect = die_pic.get_rect()
        die_rect.center = (750,400)
        self.screen.blit(die_pic, (die_rect.x, die_rect.y))
        pygame.display.update()
        pygame.display.flip()
        die_pic = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'player_win.png'))
        die_pic = pygame.transform.scale(die_pic, (1150,200))
        die_rect = die_pic.get_rect()
        die_rect.center = (750,400)
        self.screen.blit(die_pic, (die_rect.x, die_rect.y))
        pygame.time.wait(5000)
        sys.exit()

    def roll_dice(self, can_be_same, player, computer,player_land, comp_land, land, player_obj):
        pos_player = [(162,144),(162,272),(162,399),(162,520),(162,650),(286,650),(418,650),(546,650),(676,650),(799,650),(926,650),(1056,650),(1056,520),(1056,399),(1056,272),(1056,144)]
        pos_computer = [(232,144),(232,272),(232,399),(232,520),(232,650),(356,650),(485,650),(612,650),(739,650),(868,650),(996,650),(1122,650),(1122,520),(1122,399),(1122,272),(1122,144)]
        prev = -1
        for i in range(3):
            dice1 = random.randint(1,6)
            while dice1 == prev:
                dice1 = random.randint(1,6)
            prev = dice1
            dice1_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, self.dice_map[dice1]))
            dice1_pic = pygame.transform.scale(dice1_pic, (150,150))
            dice1_pic_rect = dice1_pic.get_rect()
            dice1_pic_rect.center = (1260,690)
            self.screen.blit(dice1_pic, (dice1_pic_rect.x, dice1_pic_rect.y))
            pygame.display.update()
            pygame.display.flip()
            pygame.time.delay(250)
            self.easy_one_init(player_land, comp_land, land, player_obj)
            self.blit_player_icon(pos_player[player])
            self.blit_comp_icon(pos_computer[computer])
        dice1 = random.randint(1,6)
        while dice1 == prev:
            dice1 = random.randint(1,6)
        dice1_pic = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, self.dice_map[dice1]))
        dice1_pic = pygame.transform.scale(dice1_pic, (150,150))
        dice1_pic_rect = dice1_pic.get_rect()
        dice1_pic_rect.center = (1260,690)
        self.screen.blit(dice1_pic, (dice1_pic_rect.x, dice1_pic_rect.y))
        pygame.display.update()
        pygame.display.flip()
        pygame.time.delay(800)
        prev = -1
        for i in range(3):
            dice2 = random.randint(1,6)
            while dice2 == prev:
                dice2 = random.randint(1,6)
            prev = dice2
            dice2_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, self.dice_map[dice2]))
            dice2_pic = pygame.transform.scale(dice2_pic, (150,150))
            dice2_pic_rect = dice2_pic.get_rect()
            dice2_pic_rect.center = (1390,690)
            self.screen.blit(dice2_pic, (dice2_pic_rect.x, dice2_pic_rect.y))
            pygame.display.update()
            pygame.display.flip()
            pygame.time.delay(250)
            self.easy_one_init(player_land, comp_land, land, player_obj)
            self.blit_player_icon(pos_player[player])
            self.blit_comp_icon(pos_computer[computer])
            dice1_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, self.dice_map[dice1]))
            dice1_pic = pygame.transform.scale(dice1_pic, (150,150))
            dice1_pic_rect = dice1_pic.get_rect()
            dice1_pic_rect.center = (1260,690)
            self.screen.blit(dice1_pic, (dice1_pic_rect.x, dice1_pic_rect.y))
        dice2 = random.randint(1,6)
        if not can_be_same:
            while dice2 == dice1 or dice2 == prev:
                dice2 = random.randint(1,6)
        else:
            while dice2 == prev:
                dice2 = random.randint(1,6)
        dice2_pic = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, self.dice_map[dice2]))
        dice2_pic = pygame.transform.scale(dice2_pic, (150,150))
        dice2_pic_rect = dice2_pic.get_rect()
        dice2_pic_rect.center = (1390,690)
        self.screen.blit(dice2_pic, (dice2_pic_rect.x, dice2_pic_rect.y))
        pygame.display.update()
        pygame.display.flip()
        pygame.time.delay(800)
        return dice1, dice2

    def blit_status(self,player_obj,computer_obj,player_land,computer_land, land, player_score, comp_score):
        print("printing status...")
        self.screen.fill([255,255,255])
        pygame.font.init()
        font = pygame.font.Font(None,45)
        txt_surface = font.render("Your total liquid asset: "+str(round(player_obj.money,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (300,70))
        txt_surface = font.render("Your total bank deposit: "+str(round(player_obj.bank_money,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (300,110))
        pland = ""
        pland_money = 0
        for i in range(4):
            if player_land[i]:
                pland += str(i)+", "
                pland_money += land[i]
        txt_surface = font.render("Land that's yours: "+pland[:-2], True, [0,0,0])
        self.screen.blit(txt_surface, (300,150))
        txt_surface = font.render("Your total assets hold in form of lands: "+str(round(pland_money,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (300,190))
        txt_surface = font.render("Your luck points: "+str(round(player_obj.luck,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (300,230))
        txt_surface = font.render("Your life expectancy: "+str(player_obj.life), True, [0,0,0])
        self.screen.blit(txt_surface, (300,270))
        txt_surface = font.render("Your prison sentence: "+str(player_obj.prison_years), True, [0,0,0])
        self.screen.blit(txt_surface, (300,310))
        txt_surface = font.render("The other side's total liquid asset: "+str(round(computer_obj.money,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (300,350))
        txt_surface = font.render("The other side's total bank deposit: "+str(round(computer_obj.bank_money,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (300,390))
        cland = ""
        cland_money = 0
        for i in range(4):
            if computer_land[i]:
                cland += str(i)+", "
                cland_money += land[i]
        txt_surface = font.render("Land that's the other side's: "+cland[:-2], True, [0,0,0])
        self.screen.blit(txt_surface, (300,430))
        txt_surface = font.render("The other side's total assets hold in form of lands: "+str(round(cland_money,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (300,470))
        txt_surface = font.render("The other side's luck points: "+str(round(computer_obj.luck,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (300,510))
        txt_surface = font.render("The other side's life expectancy: "+str(computer_obj.life), True, [0,0,0])
        self.screen.blit(txt_surface, (300,550))
        txt_surface = font.render("The other side's prison sentence: "+str(computer_obj.prison_years), True, [0,0,0])
        self.screen.blit(txt_surface, (300,590))
        font = pygame.font.Font(None,80)
        txt_surface = font.render("Your total score: "+str(round(player_score,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (300,650))
        txt_surface = font.render("The other side's total score: "+str(round(comp_score,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (300,710))
        pygame.display.update()
        pygame.display.flip()
        print("status printed")

    def game_end(self):
        end = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, "game_end.png"))
        end = pygame.transform.scale(end, (1150,200))
        end_rect = end.get_rect()
        end_rect.center = (750,400)
        self.screen.blit(end, (end_rect.x, end_rect.y))
        pygame.display.update()
        pygame.display.flip()
        pygame.time.delay(2000)

    def monopoly(self):
        pygame.display.set_caption("大富翁")
        self.screen.fill([0,0,0])
        rules_done = False
        rules = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'rules.png'))
        rules = pygame.transform.scale(rules, (1100, 800))
        rules_rect = rules.get_rect()
        rules_rect.center = (750,400)
        self.screen.blit(rules, (rules_rect.x, rules_rect.y))
        pygame.display.update()
        pygame.display.flip()
        while not rules_done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        rules_done = True

        self.screen.fill([255,255,255])
        easy = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'easy.png'))
        easy_rect = easy.get_rect()
        easy_rect.center = (375,400)
        self.screen.blit(easy, (easy_rect.x, easy_rect.y))
        hard = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'hard.png'))
        hard_rect = hard.get_rect()
        hard_rect.center = (1125,400)
        self.screen.blit(hard, (hard_rect.x, hard_rect.y))
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
                            self.screen.fill([255,255,255])
                            one_v = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, '1v1.png'))
                            one_rect = one_v.get_rect()
                            one_rect.center = (375,400)
                            self.screen.blit(one_v, (one_rect.x, one_rect.y))
                            many = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, '1vn.png'))
                            many_rect = many.get_rect()
                            many_rect.center = (1125,400)
                            self.screen.blit(many, (many_rect.x, many_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            easy = True
                        elif 920<=position[0]<=1350 and 190<=position[1]<=570: #hard
                            print('hard')
                            self.screen.fill([255,255,255])
                            one_v = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, '1v1.png'))
                            one_rect = one_v.get_rect()
                            one_rect.center = (375,400)
                            self.screen.blit(one_v, (one_rect.x, one_rect.y))
                            many = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, '1vn.png'))
                            many_rect = many.get_rect()
                            many_rect.center = (1125,400)
                            self.screen.blit(many, (many_rect.x, many_rect.y))
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
                            self.screen.fill([255,255,255])
                            map1 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'easy_chose1.png'))
                            map1 = pygame.transform.scale(map1, (600,400))
                            map1_rect = map1.get_rect()
                            map1_rect.center = (375,400)
                            self.screen.blit(map1, (map1_rect.x, map1_rect.y))
                            map2 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'easy_chose2.png'))
                            map2 = pygame.transform.scale(map2, (600,400))
                            map2_rect = map2.get_rect()
                            map2_rect.center = (1125,400)
                            self.screen.blit(map2, (map2_rect.x, map2_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            one = True
                        elif 800<=position[0]<=1450 and 235<=position[1]<=550 and easy: #1vn, easy
                            print('1vn')
                            self.screen.fill([255,255,255])
                            map1 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'easy_chose1.png'))
                            map1 = pygame.transform.scale(map1, (600,400))
                            map1_rect = map1.get_rect()
                            map1_rect.center = (375,400)
                            self.screen.blit(map1, (map1_rect.x, map1_rect.y))
                            map2 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'easy_chose2.png'))
                            map2 = pygame.transform.scale(map2, (600,400))
                            map2_rect = map2.get_rect()
                            map2_rect.center = (1125,400)
                            self.screen.blit(map2, (map2_rect.x, map2_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            multi = True
                        elif 50<=position[0]<=700 and 235<=position[1]<=550 and hard: #1v1, hard
                            print('1v1')
                            self.screen.fill([255,255,255])
                            map1 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'hard_chose1.png'))
                            map1 = pygame.transform.scale(map1, (600,400))
                            map1_rect = map1.get_rect()
                            map1_rect.center = (375,400)
                            self.screen.blit(map1, (map1_rect.x, map1_rect.y))
                            map2 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'hard_chose2.png'))
                            map2 = pygame.transform.scale(map2, (600,400))
                            map2_rect = map2.get_rect()
                            map2_rect.center = (1125,400)
                            self.screen.blit(map2, (map2_rect.x, map2_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            one = True
                        elif 800<=position[0]<=1450 and 235<=position[1]<=550 and hard: #1vn, hard
                            print('1vn')
                            self.screen.fill([255,255,255])
                            map1 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'hard_chose1.png'))
                            map1 = pygame.transform.scale(map1, (600,400))
                            map1_rect = map1.get_rect()
                            map1_rect.center = (375,400)
                            self.screen.blit(map1, (map1_rect.x, map1_rect.y))
                            map2 = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'hard_chose2.png'))
                            map2 = pygame.transform.scale(map2, (600,400))
                            map2_rect = map2.get_rect()
                            map2_rect.center = (1125,400)
                            self.screen.blit(map2, (map2_rect.x, map2_rect.y))
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
                            if 86<=position[0]<=664 and 208<=position[1]<=568: #easy, map1
                                easy_map1 = True
                            elif 825<=position[0]<=1425 and 200<=position[1]<=600: #easy, map2
                                easy_map2 = True
                        elif hard:
                            if 77<=position[0]<=204 and 64<=position[1]<=574: #hard, map1
                                hard_map1 = True
                            elif 825<=position[0]<=1425 and 200<=position[1]<=600: #hard, map
                                hard_map2 = True
                        pygame.display.flip()
        # positions of player and computer
        player = 0
        computer = 0
        # initialize the values of the player's attributes
        luck = 0.5
        money = 50000
        life = 80
        # initialize the values of the computer's attributes
        luck1 = 0.5
        money1 = 50000
        life1 = 80
        # initialize GANGSTER as False
        gangster = False
        gangster1 = False
        # initialize LUCK_LOCK as False
        luck_lock = False
        luck_lock1 = False
        # initialize prison as false
        if easy_map1 and one:
            # array keeping track of centers 
            centers_player = [(162,144),(162,272),(162,399),(162,520),(162,650),(286,650),(418,650),(546,650),(676,650),(799,650),(926,650),(1056,650),(1056,520),(1056,399),(1056,272),(1056,144)]
            centers_comp = [(232,144),(232,272),(232,399),(232,520),(232,650),(356,650),(485,650),(612,650),(739,650),(868,650),(996,650),(1122,650),(1122,520),(1122,399),(1122,272),(1122,144)]
            # define the list of occurances in easy_map1
            # occur = ['start','trade1,3', 'deposit','forward3','?','deposit','trade2','backward3','trade3,4','forward2','spin','?','trade1,4','surprise','prison','end']
            land = [700,1000,1350,1200]
            player_land = [False, False, False, False]
            computer_land = [False, False, False, False]
            # set the rate of growth of the lands
            land_rate = {}
            for i in range(1,5):
                land_rate[i] = random.randint(7,15)/100
            # screen, land, player_land, computer_land, occur, luck, money, life, gangster, luck_lock
            play_player = easyOnePlayer(self.screen, luck, money, life, gangster, luck_lock, land_rate)
            play_comp = easyOneComputer(self.screen, luck1, money1, life1, gangster1, luck_lock1, land_rate)
            # load the background as easy_map_one
            self.easy_one_init(player_land, computer_land, land, play_player)
            # display the position of the player_icon (part of easy_one_init, but we can't call between easy_one_init() and blit_player_icon())
            self.blit_player_icon(centers_player[player])
            self.blit_comp_icon(centers_comp[computer])
            while True: # play the game
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            position = event.pos
                            if play_player.prison_years == 0:
                                dice1, dice2 = self.roll_dice(True, player, computer, player_land, computer_land, land, play_player) # roll the dice
                                print("dice 1:",dice1,"; dice 2:",dice2)
                                self.easy_one_init(player_land, computer_land, land, play_player)
                                self.blit_player_icon(centers_player[player])
                                self.blit_comp_icon(centers_comp[computer])
                                player_same = False 
                                if dice1 == dice2: # if the two dice rolls the same number, then the player gets an extra round after this role
                                    player_same = True
                                    player_new = dice1
                                else:
                                    player_new = (dice1+dice2)//2
                                if player+player_new >= 15 or computer >= 15:
                                    # ends the game
                                    print("GAME ENDS")
                                    for i in range(15-player):
                                        self.easy_one_init(player_land, computer_land, land, play_player)
                                        self.blit_player_icon(centers_player[player+i+1])
                                        self.blit_comp_icon(centers_comp[computer])
                                        pygame.time.delay(750)
                                    self.game_end()
                                    player_land_money = 0
                                    for i in player_land:
                                        if i:
                                            player_land_money += land[i-1]
                                    player_score = play_player.life*100 + play_player.luck*10000 + play_player.money + player_land_money + play_player.bank_money - play_player.prison_years*100
                                    comp_land_money = 0
                                    for i in computer_land:
                                        if i:
                                            comp_land_money += land[i-1]
                                    comp_score = play_comp.life*100 + play_comp.luck*10000 + play_comp.money + comp_land_money + play_comp.bank_money -  play_comp.prison_years*100
                                    if player_score > comp_score:
                                        print("win")
                                        win = pygame.image.load(
                                                os.path.join(IMAGE_DATA_PATH, 'player_win.png'))
                                        win = pygame.transform.scale(win, (1150,200))
                                        win_rect = win.get_rect()
                                        win_rect.center = (750,400)
                                        self.screen.blit(win, (win_rect.x, win_rect.y))
                                    elif player_score == comp_score:
                                        print("tie")
                                        win = pygame.image.load(
                                                os.path.join(IMAGE_DATA_PATH, 'tie.png'))
                                        win = pygame.transform.scale(win, (1150,200))
                                        win_rect = win.get_rect()
                                        win_rect.center = (750,400)
                                        self.screen.blit(win, (win_rect.x, win_rect.y))
                                    else:
                                        print("lose")
                                        win = pygame.image.load(
                                                os.path.join(IMAGE_DATA_PATH, 'comp_win.png'))
                                        win = pygame.transform.scale(win, (1150,200))
                                        win_rect = win.get_rect()
                                        win_rect.center = (750,400)
                                        self.screen.blit(win, (win_rect.x, win_rect.y))
                                    pygame.display.update()
                                    pygame.display.flip()
                                    self.click_to_moveon(player, computer,player_land, computer_land, land, play_player)
                                    self.blit_status(play_player, play_comp, player_land, computer_land, land, player_score, comp_score)
                                    self.click_to_moveon(player, computer,player_land, computer_land, land, play_player)
                                    if player_score > comp_score:
                                        Video.play_video(os.path.join(IMAGE_DATA_PATH, 'jojo.mp4'), self.screen)
                                    elif player_score < comp_score:
                                        Video.play_video(os.path.join(IMAGE_DATA_PATH, 'king.mp4'), self.screen)
                                    sys.exit()
                                # blit the player's icon by adding the steps to the center
                                for i in range(player_new):
                                    self.easy_one_init(player_land, computer_land, land, play_player)
                                    self.blit_player_icon(centers_player[player+i+1])
                                    self.blit_comp_icon(centers_comp[computer])
                                    pygame.time.delay(750)
                                player += player_new
                                if player_same:
                                    print(land)
                                    player, land, player_land = play_player.turn(player, computer, land, player_land, computer_land) # play the first roll for the player
                                    if not land: # player is dead
                                        # blit the GG picture
                                        self.player_dead()
                                    # Here, insert another roll of dice, because the player can play another turn
                                    dice1, dice2 = self.roll_dice(False, player, computer, player_land, computer_land, land, play_player)
                                    print(False, "dice 1:",dice1,"; dice 2:",dice2)
                                    self.easy_one_init(player_land, computer_land, land, play_player)
                                    self.blit_player_icon(centers_player[player])
                                    self.blit_comp_icon(centers_comp[computer])
                                    # add the player's second role to he's position
                                    player_new = (dice1+dice2)//2
                                    if player+player_new >= 15 or computer >= 15:
                                        # ends the game
                                        print("GAME ENDS")
                                        for i in range(15-player):
                                            self.easy_one_init(player_land, computer_land, land, play_player)
                                            self.blit_player_icon(centers_player[player+i+1])
                                            self.blit_comp_icon(centers_comp[computer])
                                            pygame.time.delay(750)
                                        self.game_end()
                                        player_land_money = 0
                                        for i in player_land:
                                            if i:
                                                player_land_money += land[i-1]
                                        player_score = play_player.life*100 + play_player.luck*10000 + play_player.money + player_land_money + play_player.bank_money - play_player.prison_years*100
                                        comp_land_money = 0
                                        for i in computer_land:
                                            if i:
                                                comp_land_money += land[i-1]
                                        comp_score = play_comp.life*100 + play_comp.luck*10000 + play_comp.money + comp_land_money + play_comp.bank_money -  play_comp.prison_years*100
                                        if player_score > comp_score:
                                            print("win")
                                            win = pygame.image.load(
                                                    os.path.join(IMAGE_DATA_PATH, 'player_win.png'))
                                            win = pygame.transform.scale(win, (1150,200))
                                            win_rect = win.get_rect()
                                            win_rect.center = (750,400)
                                            self.screen.blit(win, (win_rect.x, win_rect.y))
                                        elif player_score == comp_score:
                                            print("tie")
                                            win = pygame.image.load(
                                                    os.path.join(IMAGE_DATA_PATH, 'tie.png'))
                                            win = pygame.transform.scale(win, (1150,200))
                                            win_rect = win.get_rect()
                                            win_rect.center = (750,400)
                                            self.screen.blit(win, (win_rect.x, win_rect.y))
                                        else:
                                            print("lose")
                                            win = pygame.image.load(
                                                    os.path.join(IMAGE_DATA_PATH, 'comp_win.png'))
                                            win = pygame.transform.scale(win, (1150,200))
                                            win_rect = win.get_rect()
                                            win_rect.center = (750,400)
                                            self.screen.blit(win, (win_rect.x, win_rect.y))
                                        pygame.display.update()
                                        pygame.display.flip()
                                        self.click_to_moveon(player, computer,player_land, computer_land, land, play_player)
                                        self.blit_status(play_player, play_comp, player_land, computer_land, land, player_score, comp_score)
                                        self.click_to_moveon(player, computer,player_land, computer_land, land, play_player)
                                        if player_score > comp_score:
                                            Video.play_video(os.path.join(IMAGE_DATA_PATH, 'jojo.mp4'), self.screen)
                                        elif player_score < comp_score:
                                            Video.play_video(os.path.join(IMAGE_DATA_PATH, 'king.mp4'), self.screen)
                                        sys.exit()
                                    for i in range(player_new):
                                        self.easy_one_init(player_land, computer_land, land, play_player)
                                        self.blit_player_icon(centers_player[player+i+1])
                                        self.blit_comp_icon(centers_comp[computer])
                                        pygame.time.delay(750)
                                    player += player_new
                                    # After the other roll, play.player() turn again
                                    player, land, player_land = play_player.turn(player, computer, land, player_land, computer_land)
                                    if not land: # player is dead
                                        self.player_dead()
                                else: # if the player did not roll two dices of the same value
                                    player, land, player_land = play_player.turn(player, computer, land, player_land, computer_land)
                                    if not land: # player is dead
                                        self.player_dead()
                                pygame.time.delay(1500)
                            else:
                                player, land, player_land = play_player.turn(player, computer, land, player_land, computer_land)
                            # IT IS THE COMPUTER'S TURN
                            if play_comp.prison_years == 0:
                                dice1 = random.randint(1,6)
                                dice2 = random.randint(1,6)
                                while dice2 == dice1:
                                    dice2=random.randint(1,6)
                                computer_new = (dice1+dice2)//2
                                if computer+computer_new >= 15 or player >= 15:
                                    print("GAME ENDS")
                                    # ends the game
                                    for i in range(15-computer):
                                        self.easy_one_init(player_land, computer_land, land, play_player)
                                        self.blit_player_icon(centers_player[player])
                                        self.blit_comp_icon(centers_comp[computer+i+1])
                                        pygame.time.delay(750)
                                    self.game_end()
                                    player_land_money = 0
                                    for i in player_land:
                                        if i:
                                            player_land_money += land[i-1]
                                    player_score = play_player.life*100 + play_player.luck*10000 + play_player.money + player_land_money + play_player.bank_money - play_player.prison_years*100
                                    comp_land_money = 0
                                    for i in computer_land:
                                        if i:
                                            comp_land_money += land[i-1]
                                    comp_score = play_comp.life*100 + play_comp.luck*10000 + play_comp.money + comp_land_money + play_comp.bank_money -  play_comp.prison_years*100
                                    if player_score > comp_score:
                                        print("win")
                                        win = pygame.image.load(
                                                os.path.join(IMAGE_DATA_PATH, 'player_win.png'))
                                        win = pygame.transform.scale(win, (1150,200))
                                        win_rect = win.get_rect()
                                        win_rect.center = (750,400)
                                        self.screen.blit(win, (win_rect.x, win_rect.y))
                                    elif player_score == comp_score:
                                        print("tie")
                                        win = pygame.image.load(
                                                os.path.join(IMAGE_DATA_PATH, 'tie.png'))
                                        win = pygame.transform.scale(win, (1150,200))
                                        win_rect = win.get_rect()
                                        win_rect.center = (750,400)
                                        self.screen.blit(win, (win_rect.x, win_rect.y))
                                    else:
                                        print("lose")
                                        win = pygame.image.load(
                                                os.path.join(IMAGE_DATA_PATH, 'comp_win.png'))
                                        win = pygame.transform.scale(win, (1150,200))
                                        win_rect = win.get_rect()
                                        win_rect.center = (750,400)
                                        self.screen.blit(win, (win_rect.x, win_rect.y))
                                    pygame.display.update()
                                    pygame.display.flip()
                                    self.click_to_moveon(player, computer,player_land, computer_land, land, play_player)
                                    self.blit_status(play_player, play_comp, player_land, computer_land, land, player_score, comp_score)
                                    self.click_to_moveon(player, computer,player_land, computer_land, land, play_player)
                                    if player_score > comp_score:
                                        Video.play_video(os.path.join(IMAGE_DATA_PATH, 'jojo.mp4'), self.screen)
                                    elif player_score < comp_score:
                                        Video.play_video(os.path.join(IMAGE_DATA_PATH, 'king.mp4'), self.screen)
                                    sys.exit()
                                for i in range(computer_new):
                                    self.easy_one_init(player_land, computer_land, land, play_player)
                                    self.blit_comp_icon(centers_comp[computer+i+1])
                                    self.blit_player_icon(centers_player[player])
                                    pygame.time.delay(750)
                                computer += computer_new
                                computer, land, computer_land = play_comp.turn(player, computer, land, player_land, computer_land, play_player)
                                if not land: # computer is dead
                                    self.comp_dead()
                            else:
                                computer, land, computer_land = play_comp.turn(player, computer, land, player_land, computer_land, play_player)
                            self.click_to_moveon(player, computer,player_land, computer_land, land, play_player)
                        # initialize the screen as the background easy_map1 again
                        self.easy_one_init(player_land, computer_land, land, play_player)
                        self.blit_player_icon(centers_player[player])
                        self.blit_comp_icon(centers_comp[computer])
                        for i in range(4):
                            land[i] *= (1+land_rate[i+1])
                        print(land)
            # we do not plan to finish other maps other than easy, map1, 1v1 currently due to time limit
            # elif easy_map1 and multi:
            
            # elif easy_map2 and one:

            # elif easy_map2 and multi:

            # elif hard_map1 and one:

            # elif hard_map1 and multi:

            # elif hard_map2 and one:

            # elif hard_map2 and multi:

if __name__ == '__main__':
    a = Monopoly()
    a.monopoly()