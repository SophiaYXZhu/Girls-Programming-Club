from msvcrt import LK_UNLCK
import pygame
import random
from config import *
from inputBox import inputBox
from video import Video
import os
import sys

class easyOnePlayer():
    def __init__(self, screen, luck, money, life, gangster, luck_lock, land_rate):
        self.screen = screen
        self.occur = ['start','trade1,3', 'deposit','forward3','?','deposit','trade2','backward3','trade3,4','forward2','spin','?','trade1,4','surprise','prison','end']
        self.luck = luck
        self.money = money
        self.life = life
        self.gangster = gangster
        self.prison_years = 0
        self.luck_lock = luck_lock
        self.interest_rate = 0.02
        self.land_rate = land_rate
        self.bank_money = 0
        self.luck_lock_count = 0
        self.pos_player = [(162,144),(162,272),(162,399),(162,520),(162,650),(286,650),(418,650),(546,650),(676,650),(799,650),(926,650),(1056,650),(1056,520),(1056,399),(1056,272),(1056,144)]
        self.pos_computer = [(232,144),(232,272),(232,399),(232,520),(232,650),(356,650),(485,650),(612,650),(739,650),(868,650),(996,650),(1122,650),(1122,520),(1122,399),(1122,272),(1122,144)]
        print('easyOnePlayer')
    
    # initialize the screen
    def initialize_screen(self, player_land, computer_land, land):
        self.screen.fill([255, 255, 255])
        easyone = pygame.image.load(os.path.join(IMAGE_DATA_PATH, 'easy1.png'))
        easyone_rect = easyone.get_rect()
        easyone_rect.center = (650, 400)
        self.screen.blit(easyone, (easyone_rect.x, easyone_rect.y))
        ### display values of age, luck, money, and land owned by player and comuter in the margin
        pygame.font.init()
        font = pygame.font.Font(None, 50)
        txt_surface = font.render("STATUS", True, [0,0,0])
        self.screen.blit(txt_surface, (1252,70))
        font = pygame.font.Font(None, 30)
        txt_surface = font.render("Liquid Assets: $"+str(round(self.money,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (1192,120))
        txt_surface = font.render("Bank Deposits: $"+str(round(self.bank_money,2)), True, [0,0,0])
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
        txt_surface = font.render("Luck: "+str(round(self.luck*100,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (1192,305))
        txt_surface = font.render("Life: "+str(self.life), True, [0,0,0])
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

    def blit_player_icon(self,center):
        icon = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'player_icon.png'))
        icon = pygame.transform.scale(icon, (50, 50))
        icon_rect = icon.get_rect()
        icon_rect.center = center
        self.screen.blit(icon, (icon_rect.x, icon_rect.y))
        pygame.display.update()
        pygame.display.flip()
    
    def blit_computer_icon(self,center):
        icon = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'comp_icon.png'))
        icon = pygame.transform.scale(icon, (50, 50))
        icon_rect = icon.get_rect()
        icon_rect.center = center
        self.screen.blit(icon, (icon_rect.x, icon_rect.y))
        pygame.display.update()
        pygame.display.flip()

    def click_to_cancel(self, player, computer, player_land, computer_land, land):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.initialize_screen(player_land, computer_land, land)
                    self.blit_player_icon(self.pos_player[player])
                    self.blit_computer_icon(self.pos_computer[computer])
                    done = True
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.initialize_screen(player_land, computer_land, land)
                        self.blit_player_icon(self.pos_player[player])
                        self.blit_computer_icon(self.pos_computer[computer])
                        done = True
                        break
        pygame.display.update()
        pygame.display.flip()

    def trade(self, available_land, player_land, computer_land, land, player, computer):
        self.initialize_screen(player_land, computer_land, land)
        self.blit_player_icon(self.pos_player[player])
        self.blit_computer_icon(self.pos_computer[computer])
        # ask the player which land does he want to exchange
        trade = pygame.image.load(
            os.path.join(IMAGE_DATA_PATH, 'trade_land.png'))
        trade = pygame.transform.scale(trade, (1200, 430))
        trade_rect = trade.get_rect()
        trade_rect.center = (750,350)
        self.screen.blit(trade, (trade_rect.x, trade_rect.y))
        pygame.font.init()
        font = pygame.font.Font(None, 95)
        available = ""
        for i in available_land:
            available += str(i)+", "
        txt_surface = font.render(available[:-2], True, [255,255,255])
        self.screen.blit(txt_surface, (993,240))
        self.screen.blit(txt_surface, (336,455))
        box = inputBox(self.screen)
        land_trade = int(box.input_box((675, 550), "easy_map1", "trade", player, computer, player_obj = self, land = available_land, player_land = player_land, computer_land = computer_land, land_price = land))
        pygame.display.update()
        pygame.display.flip()
        if not land_trade:
            self.initialize_screen(player_land, computer_land, land)
            self.blit_player_icon(self.pos_player[player])
            self.blit_computer_icon(self.pos_computer[computer])
            prohibit = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'trade_not_valid.png'))
            prohibit = pygame.transform.scale(prohibit, (1150, 200))
            prohibit_rect = prohibit.get_rect()
            prohibit_rect.center = (750,400)
            self.screen.blit(prohibit, (prohibit_rect.x, prohibit_rect.y))
            pygame.display.update()
            pygame.display.flip()
            self.click_to_cancel(player, computer, player_land, computer_land, land)
            self.trade(available_land, player_land, computer_land, land, player, computer)
        if land_trade == -1:
            ### quit the trade function
            self.initialize_screen(player_land, computer_land, land)
            self.blit_player_icon(self.pos_player[player])
            self.blit_computer_icon(self.pos_computer[computer])
            no_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'trade_no.png'))
            no_pic = pygame.transform.scale(no_pic, (1150, 200))
            no_rect = no_pic.get_rect()
            no_rect.center = (750,350)
            self.screen.blit(no_pic, (no_rect.x, no_rect.y))
        elif player_land[land_trade-1]:
            self.initialize_screen(player_land, computer_land, land)
            self.blit_player_icon(self.pos_player[player])
            self.blit_computer_icon(self.pos_computer[computer])
            # blit picture that says the player sold the land to the government
            self.money += land[land_trade-1]
            player_land[land_trade-1] = False
            sold = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'trade_sold.png'))
            sold = pygame.transform.scale(sold, (1150, 200))
            sold_rect = sold.get_rect()
            sold_rect.center = (750,350)
            self.screen.blit(sold, (sold_rect.x, sold_rect.y))
        else:
            self.initialize_screen(player_land, computer_land, land)
            self.blit_player_icon(self.pos_player[player])
            self.blit_computer_icon(self.pos_computer[computer])
            # blit picture that says the player bought the land from the government
            self.money -= land[land_trade-1]
            player_land[land_trade-1] = True
            bought = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'trade_bought.png'))
            bought = pygame.transform.scale(bought, (1150, 200))
            bought_rect = bought.get_rect()
            bought_rect.center = (750,350)
            self.screen.blit(bought, (bought_rect.x, bought_rect.y))
        pygame.display.update()
        pygame.display.flip()
        self.click_to_cancel(player,computer,player_land, computer_land, land)
        return player_land
        
    def spin(self, player, computer, player_land, computer_land, land):
        self.initialize_screen(player_land, computer_land, land)
        self.blit_player_icon(self.pos_player[player])
        self.blit_computer_icon(self.pos_computer[computer])
        spin = ["disappear", "life", "luck", "nothing"]
        if self.luck == 0:
            event = 'disappear'
        else:
            disappear = 0.25
            life = disappear+(0.5+self.luck)/4
            luck = life+(0.5+self.luck)/4
            result = random.randint(0,11)/10
            if result <= disappear:
                event = spin[0]
            elif disappear < result <= life:
                event = spin[1]
            elif self.life < result <= luck:
                event = spin[2]
            else:
                event = spin[3]
        if event == "disappear": # the player disappear from the current universe
            # display the video of 团长
            Video.play_video(os.path.join(IMAGE_DATA_PATH, 'kibo.mp4'), self.screen)
        elif event == "life": # the player gets a chance to live for additional 10000 years
            self.life += 10000
            # blit the live++ pic onto the screen
            life_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'life_increase.png'))
            life_pic = pygame.transform.scale(life_pic, (1300, 179))
            life_rect = life_pic.get_rect()
            life_rect.center = (750,400)
            self.screen.blit(life_pic, (life_rect.x, life_rect.y))
            pygame.display.update()
            pygame.display.flip()
        elif event == "luck": # the luck of the player stays 1 for 5 tunrs
            self.luck = 1
            self.luck_lock = True
            # blit the luck_lock picture onto the screen
            luck_lock_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'luck_lock.png'))
            luck_lock_pic = pygame.transform.scale(luck_lock_pic, (1300, 179))
            luck_lock_rect = luck_lock_pic.get_rect()
            luck_lock_rect.center = (750,400)
            self.screen.blit(luck_lock_pic, (luck_lock_rect.x, luck_lock_rect.y))
            pygame.display.update()
            pygame.display.flip()
        elif event == "nothing": # the player did not receive anything
            # blit NOTHING img onto the screen
            nothing = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'NOTHING.png'))
            nothing = pygame.transform.scale(nothing, (1300, 179))
            nothing_rect = nothing.get_rect()
            nothing_rect.center = (750,400)
            self.screen.blit(nothing, (nothing_rect.x, nothing_rect.y))
            pygame.display.update()
            pygame.display.flip()
        self.click_to_cancel(player,computer,player_land, computer_land, land)

    def surprise(self, land, player, computer, player_land, computer_land):
        self.initialize_screen(player_land, computer_land, land)
        self.blit_player_icon(self.pos_player[player])
        self.blit_computer_icon(self.pos_computer[computer])
        add_have = self.luck*100
        positive_negative = []
        for i in range(100):
            if i < add_have:
                positive_negative.append(True)
            else:
                positive_negative.append(False)
        res = random.choice(positive_negative)
        have_land = []
        for i in range(4):
            if player_land[i]:
                have_land.append(i+1)
        if res and len(have_land) != 0:
            l = random.choice(have_land)
            land[l-1] += 200
            land_change = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'land'+str(l)+'+.png'))
        else:
            l = random.randint(1,4)
            p = random.randint(0,1)
            if p == 1:
                land[l-1] += 200
                land_change = pygame.image.load(
                    os.path.join(IMAGE_DATA_PATH, 'land'+str(l)+'+.png'))
            else:
                land[l-1] -= 200
                land_change = pygame.image.load(
                    os.path.join(IMAGE_DATA_PATH, 'land'+str(l)+'-.png'))
        land_change = pygame.transform.scale(land_change, (1150, 200))
        land_change_rect = land_change.get_rect()
        land_change_rect.center = (750,400)
        self.screen.blit(land_change, (land_change_rect.x, land_change_rect.y))
        pygame.display.update()
        pygame.display.flip()
        self.click_to_cancel(player,computer,player_land, computer_land, land)
        return land

    def deposit(self, player, computer,player_land, computer_land, land):
        self.initialize_screen(player_land, computer_land, land)
        self.blit_player_icon(self.pos_player[player])
        self.blit_computer_icon(self.pos_computer[computer])
        deposit = False
        withdraw = False
        deposit = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'deposit.png'))
        deposit = pygame.transform.scale(deposit, (650, 190))
        deposit_rect = deposit.get_rect()
        deposit_rect.center = (750,400)
        self.screen.blit(deposit, (deposit_rect.x, deposit_rect.y))
        pygame.display.update()
        pygame.display.flip()
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        position = event.pos
                        if 460<=position[0]<=573 and 451<=position[1]<=482: # deposit
                            self.initialize_screen(player_land, computer_land, land)
                            self.blit_player_icon(self.pos_player[player])
                            self.blit_computer_icon(self.pos_computer[computer])
                            deposit = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'deposit_number.png'))
                            deposit = pygame.transform.scale(deposit, (700, 130))
                            deposit_rect = deposit.get_rect()
                            deposit_rect.center = (750, 400)
                            self.screen.blit(deposit, (deposit_rect.x, deposit_rect.y))
                            box = inputBox(self.screen) # the INPUT BOX
                            money_value = round(float(box.input_box((675, 450), 'easy_map1', 'deposit', player, computer, player_obj = self, computer_land = computer_land, player_land = player_land, land_price = land)), 2)
                            if money_value == -1:
                                self.initialize_screen(player_land, computer_land, land)
                                self.blit_player_icon(self.pos_player[player])
                                self.blit_computer_icon(self.pos_computer[computer])
                                prohibit = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'invalid_value.png'))
                                prohibit = pygame.transform.scale(prohibit, (1150, 200))
                                prohibit_rect = prohibit.get_rect()
                                prohibit_rect.center = (750,400)
                                self.screen.blit(prohibit, (prohibit_rect.x, prohibit_rect.y))
                                pygame.display.update()
                                pygame.display.flip()
                                self.click_to_cancel(player, computer, player_land, computer_land, land)
                                self.deposit(player, computer,player_land, computer_land, land)
                            done = True
                            self.money -= money_value # minus the amount of money_value from money
                            self.bank_money += money_value
                            deposit_done = pygame.image.load(
                                os.path.join(IMAGE_DATA_PATH, 'deposit_done.png'))
                            deposit_done = pygame.transform.scale(deposit_done, (1150, 200))
                            done_rect = deposit_done.get_rect()
                            done_rect.center = (750,400)
                            self.screen.blit(deposit_done, (done_rect.x, done_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            break # break the for loop after deposit/withdraw/doing nothing once
                        elif 642<=position[0]<=844 and 451<=position[1]<=482: # withdraw
                            self.initialize_screen(player_land, computer_land, land)
                            self.blit_player_icon(self.pos_player[player])
                            self.blit_computer_icon(self.pos_computer[computer])
                            withdraw = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'withdraw_number.png'))
                            withdraw = pygame.transform.scale(withdraw, (700, 130))
                            withdraw_rect = withdraw.get_rect()
                            withdraw_rect.center = (750, 400)
                            self.screen.blit(withdraw, (withdraw_rect.x, withdraw_rect.y))
                            box = inputBox(self.screen) # the INPUT BOX
                            money_value = round(float(box.input_box((675, 450), 'easy_map1', 'withdraw', player, computer, player_obj = self, computer_land = computer_land, player_land = player_land, land_price = land)), 2)
                            if money_value == -1:
                                self.initialize_screen(player_land, computer_land, land)
                                self.blit_player_icon(self.pos_player[player])
                                self.blit_computer_icon(self.pos_computer[computer])
                                prohibit = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'invalid_value.png'))
                                prohibit = pygame.transform.scale(prohibit, (1150, 200))
                                prohibit_rect = prohibit.get_rect()
                                prohibit_rect.center = (750,400)
                                self.screen.blit(prohibit, (prohibit_rect.x, prohibit_rect.y))
                                pygame.display.update()
                                pygame.display.flip()
                                self.click_to_cancel(player, computer, player_land, computer_land, land)
                                self.deposit(player, computer,player_land, computer_land, land)
                            done = True
                            self.money += money_value # plus the amount of money_value to money
                            self.bank_money -= money_value
                            deposit_done = pygame.image.load(
                                os.path.join(IMAGE_DATA_PATH, 'withdraw_done.png'))
                            deposit_done = pygame.transform.scale(deposit_done, (1150, 200))
                            done_rect = deposit_done.get_rect()
                            done_rect.center = (750,400)
                            self.screen.blit(deposit_done, (done_rect.x, done_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            break # break the for loop after deposit/withdraw/doing nothing once
                        elif 957<=position[0]<=1018 and 451<=position[1]<=482: # no
                            self.initialize_screen(player_land, computer_land, land)
                            self.blit_player_icon(self.pos_player[player])
                            self.blit_computer_icon(self.pos_computer[computer])
                            # blit nothing happened
                            nothing = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'deposit_nothing.png'))
                            nothing = pygame.transform.scale(nothing, (700, 130))
                            no_rect = nothing.get_rect()
                            no_rect.center = (750, 400)
                            self.screen.blit(nothing, (no_rect.x, no_rect.y))
                            pygame.display.update()
                            pygame.display.flip()
                            done = True
                            break # break the for loop after deposit/withdraw/doing nothing once
        self.click_to_cancel(player,computer,player_land, computer_land, land)

    # helper method for question() when deciding exchange of life with money
    def yes_no(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        position = event.pos
                        if 568<=position[0]<=704 and 670<=position[1]<=720: # YES
                            if self.money >= 15000:
                                return True # the player is willing to exchange life with money
                            else:
                                # blit enter a valid value
                                invalid = pygame.image.load(
                                    os.path.join(IMAGE_DATA_PATH, 'invalid_choice.png'))
                                invalid = pygame.transform.scale(invalid, (1150, 200))
                                invalid_rect = invalid.get_rect()
                                invalid_rect.center = (750,400)
                                self.screen.blit(invalid, (invalid_rect.x, invalid_rect.y))
                                return -1
                        elif 790<=position[0]<=940 and 670<=position[1]<=720: # NO
                            return False # the player is unwilling to exchange life with money

    def question(self, player, computer, player_land, computer_land, land):
        self.initialize_screen(player_land, computer_land, land)
        self.blit_player_icon(self.pos_player[player])
        self.blit_computer_icon(self.pos_computer[computer])
        if self.gangster:
            question = ['NOTHING', 'LUCK--', 'LIFE--', 'MONEY--', 'MONEY-', 'LUCK++', 'LIFE++', 'MONEY++']
            neutral = 1/8
            negative = neutral+(5.5-3*self.luck)/8
            positive = negative+3/8*(0.5+self.luck)
            result = random.randint(0,11)/10
            if result <= neutral: # neutral
                result = question[0]
            elif neutral < result <= negative: # negative
                result = random.choice(question[1:5])
            elif negative < result: # positive
                result = random.choice(question[5:])
        else:
            question = ['NOTHING', 'GANGSTER', 'LUCK--', 'LIFE--', 'MONEY--', 'MONEY-', 'LUCK++', 'LIFE++', 'MONEY++']
            if self.luck == 0:
                result = 'GANGSTER'
            else:
                neutral = 1/9
                gangster = neutral+1/9
                negative = gangster+(5.5-3*self.luck)/9
                positive = negative+3/9*(0.5+self.luck)
                result = random.randint(0,11)/10
                if result <= neutral: # neutral
                    result = question[0]
                elif neutral < result <= gangster: # gangster
                    result = question[1]
                elif gangster < result <= negative:
                    result = random.choice(question[2:6])
                elif result > negative:
                    result = random.choice(question[6:])
        lifedown = False
        if result == 'LUCK++':
            if self.luck <= 0.8:
                self.luck += 0.2
            else:
                self.luck = 1
            luckup = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'LUCK++.png'))
            luckup = pygame.transform.scale(luckup, (1300, 179))
            luckup_rect = luckup.get_rect()
            luckup_rect.center = (750,400)
            self.screen.blit(luckup, (luckup_rect.x, luckup_rect.y))
        elif result == 'LIFE++':
            self.life += 5
            lifeup = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'LIFE++.png'))
            lifeup = pygame.transform.scale(lifeup,(1150, 275))
            lifeup_rect = lifeup.get_rect()
            lifeup_rect.center = (750,400)
            self.screen.blit(lifeup, (lifeup_rect.x, lifeup_rect.y))
        elif result == 'MONEY++':
            self.money += 2000
            if self.luck > 0.01:
                self.luck -= 0.01
            else:
                self.luck = 0
            moneyup = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'MONEY++.png'))
            moneyup = pygame.transform.scale(moneyup, (1300, 427))
            moneyup_rect = moneyup.get_rect()
            moneyup_rect.center = (750,400)
            self.screen.blit(moneyup, (moneyup_rect.x, moneyup_rect.y))
        elif result == 'LUCK--':
            if not self.luck_lock:
                if self.luck >= 0.2:
                    self.luck -= 0.2
                else:
                    self.luck = 0
                luckdown = pygame.image.load(
                    os.path.join(IMAGE_DATA_PATH, 'LUCK--.png'))
                luckdown = pygame.transform.scale(luckdown, (1300, 179))
                luckdown_rect = luckdown.get_rect()
                luckdown_rect.center = (750,400)
                self.screen.blit(luckdown, (luckdown_rect.x, luckdown_rect.y))
            else:
                luckdown = pygame.image.load(
                    os.path.join(IMAGE_DATA_PATH, 'LUCK_NO_CHANGE.png'))
                luckdown = pygame.transform.scale(luckdown, (1300, 179))
                luckdown_rect = luckdown.get_rect()
                luckdown_rect.center = (750,400)
                self.screen.blit(luckdown, (luckdown_rect.x, luckdown_rect.y))
        elif result == 'LIFE--':
            lifedown = True
            lifedown = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'LIFE--.png'))
            lifedown = pygame.transform.scale(lifedown, (1300, 489))
            lifedown_rect = lifedown.get_rect()
            lifedown_rect.center = (750,400)
            self.screen.blit(lifedown, (lifedown_rect.x, lifedown_rect.y))
            # ask whether the player is willing to exchange money for life or not
            # YES
            yes = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'yes.png'))
            yes = pygame.transform.scale(yes, (150, 83))
            yes_rect = yes.get_rect()
            yes_rect.center = (635, 700)
            self.screen.blit(yes, (yes_rect.x, yes_rect.y))
            # NO
            no = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'no.png'))
            no = pygame.transform.scale(no, (150, 83))
            no_rect = no.get_rect()
            no_rect.center = (865, 700)
            self.screen.blit(no, (no_rect.x, no_rect.y))
        elif result == 'MONEY--':
            self.money -= 2000
            moneydown = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'MONEY--.png'))
            moneydown = pygame.transform.scale(moneydown, (1300, 301))
            moneydown_rect = moneydown.get_rect()
            moneydown_rect.center = (750,400)
            self.screen.blit(moneydown, (moneydown_rect.x, moneydown_rect.y))
        elif result == 'MONEY-':
            self.money -= 1000
            moneydown_small = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'MONEY-.png'))
            moneydown_small = pygame.transform.scale(moneydown_small, (1300, 240))
            moneydownsmall_rect = moneydown_small.get_rect()
            moneydownsmall_rect.center = (750,400)
            self.screen.blit(moneydown_small, (moneydownsmall_rect.x, moneydownsmall_rect.y))
        elif result == 'GANGSTER':
            if not self.luck_lock:
                if self.luck >= 0.5:
                    self.luck -= 0.5
                else:
                    self.luck = 0
            self.money += 100000
            gangster = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'GANGSTER.png'))
            gangster = pygame.transform.scale(gangster, (1300, 604))
            gangster_rect = gangster.get_rect()
            gangster_rect.center = (750,400)
            self.screen.blit(gangster, (gangster_rect.x, gangster_rect.y))
            self.gangster = True
        else:
            nothing = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'NOTHING.png'))
            nothing = pygame.transform.scale(nothing, (1300, 179))
            nothing_rect = nothing.get_rect()
            nothing_rect.center = (750,400)
            self.screen.blit(nothing, (nothing_rect.x, nothing_rect.y))
        pygame.display.update()
        pygame.display.flip()
        if lifedown: # if the player gets to choose whether he wants to exchange life with money (MONEY--)
            # get the player to click either YES or NO
            exchange = self.yes_no()
            while exchange == -1:
                exchange = self.yes_no()
            if exchange:
                self.money -= 15000
                exchange_pic = pygame.image.load(
                        os.path.join(IMAGE_DATA_PATH, 'exchange.png'))
                exchange_pic = pygame.transform.scale(exchange_pic, (1350, 250))
                exchange_rect = exchange_pic.get_rect()
                exchange_rect.center = (750, 400)
                self.screen.blit(exchange_pic, (exchange_rect.x, exchange_rect.y))
            else:
                self.life -= 5
                exchange_pic = pygame.image.load(
                        os.path.join(IMAGE_DATA_PATH, 'noexchange.png'))
                exchange_pic = pygame.transform.scale(exchange_pic, (1350, 250))
                exchange_rect = exchange_pic.get_rect()
                exchange_rect.center = (750, 400)
                self.screen.blit(exchange_pic, (exchange_rect.x, exchange_rect.y))
            pygame.display.update()
            pygame.display.flip()
        self.click_to_cancel(player,computer,player_land, computer_land, land)

    def prison(self,player,computer,player_land, computer_land, land): # the player get in prison for a random number of turns between 3 to 6 turns
        self.initialize_screen(player_land, computer_land, land)
        self.blit_player_icon(self.pos_player[player])
        self.blit_computer_icon(self.pos_computer[computer])
        years = []
        for i in range(int(100*self.luck)):
            years.append(3)
        for i in range(int(round((50*self.luck - self.luck+1),0))):
            years.append(4)
        for i in range(int(round((50*(1-self.luck) - (1-self.luck)+1),0))):
            years.append(4)
        for i in range(int(100*(1-self.luck))):
            years.append(6)
        self.prison_years += random.choice(years)
        imprison = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'imprisoned.png'))
        imprison = pygame.transform.scale(imprison, (1150, 300))
        imprison_rect = imprison.get_rect()
        imprison_rect.center = (750, 400)
        self.screen.blit(imprison, (imprison_rect.x, imprison_rect.y))
        pygame.font.init()
        font = pygame.font.Font(None, 95)
        txt_surface = font.render(str(self.prison_years), True, [255,255,255])
        self.screen.blit(txt_surface, (728,335))
        self.screen.blit(txt_surface, (1035,462))
        pygame.display.update()
        pygame.display.flip()
        self.click_to_cancel(player,computer, player_land, computer_land, land)

    def turn(self, player, computer, land, player_land, computer_land):
        self.initialize_screen(player_land, computer_land, land)
        self.blit_player_icon(self.pos_player[player])
        self.blit_computer_icon(self.pos_computer[computer])
        print("player's turn")
        self.life -= 1 # after each turn, the life decreases by 1
        if self.prison_years == 0:
            self.bank_money *= (1+self.interest_rate)
            if self.luck_lock:
                if self.luck_lock_count <= 5:
                    self.luck_lock_count += 1
                else:
                    self.luck_lock_count = 0
                    self.luck_lock = False
                    luck_lock_no = pygame.image.load(
                            os.path.join(IMAGE_DATA_PATH, 'luck_lock_disappear.png'))
                    luck_lock_no = pygame.transform.scale(luck_lock_no, (1150, 200))
                    luck_lock_no_rect = luck_lock_no.get_rect()
                    luck_lock_no_rect.center = (750, 400)
                    self.screen.blit(luck_lock_no, (luck_lock_no_rect.x, luck_lock_no_rect.y))
                    pygame.display.update()
                    pygame.display.flip()
            # player is the index of the current position of the player
            # after rolling the die, the player moves forward by a certain unit and so does the computer automatically does.
            # this is done by the following
            if self.occur[player] == 'trade1,3':
                player_land = self.trade([1,3], player_land, computer_land, land, player, computer)
            elif self.occur[player] == 'deposit':
                self.deposit(player, computer,player_land, computer_land, land)
            elif self.occur[player] == 'forward3':
                for i in range(1,4):
                    self.initialize_screen(player_land, computer_land, land)
                    self.blit_computer_icon(self.pos_computer[computer])
                    self.blit_player_icon(self.pos_player[player+i])
                    pygame.time.delay(750)
                player += 3
                self.turn(player, computer, land, player_land, computer_land)
            elif self.occur[player] == '?':
                self.question(player, computer,player_land, computer_land, land)
            elif self.occur[player] == 'trade2':
                player_land = self.trade([2], player_land, computer_land, land, player, computer)
            elif self.occur[player] == 'backward3':
                for i in range(1,4):
                    self.initialize_screen(player_land, computer_land, land)
                    self.blit_computer_icon(self.pos_computer[computer])
                    self.blit_player_icon(self.pos_player[player-i])
                    pygame.time.delay(750)
                player -= 3
                self.turn(player, computer, land, player_land, computer_land)
            elif self.occur[player] == 'trade3,4':
                player_land = self.trade([3, 4], player_land, computer_land, land, player, computer)
            elif self.occur[player] == 'forward2':
                for i in range(1,3):
                    self.initialize_screen(player_land, computer_land, land)
                    self.blit_computer_icon(self.pos_computer[computer])
                    self.blit_player_icon(self.pos_player[player+i])
                    pygame.time.delay(750)
                player += 2
                self.turn(player, computer, land, player_land, computer_land)
            elif self.occur[player] == 'spin':
                self.spin(player, computer, player_land, computer_land, land)
            elif self.occur[player] == 'trade1,4':
                player_land = self.trade([1, 4], player_land, computer_land, land, player, computer)
            elif self.occur[player] == 'surprise':
                land = self.surprise(land, player, computer, player_land, computer_land)
            elif self.occur[player] == 'prison':
                self.prison(player, computer, player_land, computer_land, land)
            if self.life <= 0:
                return False, False, False
        else:
            self.prison_years -= 1
            prison_life = pygame.image.load(
                    os.path.join(IMAGE_DATA_PATH, 'prison_life.png'))
            prison_life = pygame.transform.scale(prison_life, (1150, 200))
            prison_rect = prison_life.get_rect()
            prison_rect.center = (750, 400)
            self.screen.blit(prison_life, (prison_rect.x, prison_rect.y))
            pygame.display.update()
            pygame.display.flip()
            self.click_to_cancel(player, computer, player_land, computer_land, land)
        print("\nplayer:",player,"\nmoney:",self.money,"\nlife:",self.life,"\nluck:",self.luck,"\nprison:",self.prison_years,"\nbank_money:",self.bank_money,"\nland:",land,"\nplayer_land:",player_land,"\ncomputer_land:",computer_land)
        return player, land, player_land