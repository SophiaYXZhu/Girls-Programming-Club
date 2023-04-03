from tokenize import Triple
import pygame
import random
from config import *
from inputBox import inputBox
from video import Video
import os
import sys

class easyOneComputer():
    def __init__(self, screen, luck, money, life, gangster, luck_lock, land_rate):
        self.screen = screen
        self.occur = ['start','trade1,3', 'deposit','forward3','?','deposit','trade2','backward3','trade3,4','forward2','spin','?','trade1,4','surprise','prison','end']
        self.luck = luck
        self.money = money
        self.life = life
        self.gangster = gangster
        self.luck_lock = luck_lock
        self.interest_rate = 0.02
        self.land_rate = land_rate
        self.bank_money = 0
        self.luck_lock_count = 0
        self.comp_land_sell_map = {1:"comp_land1.png",2:"comp_land2.png",3:"comp_land3.png",4:"comp_land4.png"}
        self.comp_land_buy_map = {1:"comp_buy_land1.png", 2:"comp_buy_land2.png", 3:"comp_buy_land3.png", 4:"comp_buy_land4.png"}
        self.pos_player = [(162,144),(162,272),(162,399),(162,520),(162,650),(286,650),(418,650),(546,650),(676,650),(799,650),(926,650),(1056,650),(1056,520),(1056,399),(1056,272),(1056,144)]
        self.pos_computer = [(232,144),(232,272),(232,399),(232,520),(232,650),(356,650),(485,650),(612,650),(739,650),(868,650),(996,650),(1122,650),(1122,520),(1122,399),(1122,272),(1122,144)]
        self.prison_years = 0
        print('easyOnePlayer')
    
    # initialize the screen
    def initialize_screen(self, player_land, computer_land, land, player):
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

    def trade(self, available_land, player_land, computer_land, land):
        can_buy = False
        can_sell = False
        for land_trade in available_land:
            if not player_land[land_trade-1] and not computer_land[land_trade-1]:
                can_buy = True
                break
            elif computer_land[land_trade-1]:
                sell_land = land_trade
                can_sell = True
        if can_buy:
            # buy land_trade, priority higher than sell
            computer_land[land_trade-1] = True
            self.money -= land[land_trade-1]
            land_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, self.comp_land_buy_map[land_trade]))
            land_pic = pygame.transform.scale(land_pic, (1150, 200))
            land_rect = land_pic.get_rect()
            land_rect.center = (750,400)
            self.screen.blit(land_pic, (land_rect.x, land_rect.y))
        elif can_sell:
            # sell land_trade
            computer_land[sell_land-1] = False
            self.money -= land[sell_land-1]
            land_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, self.comp_land_sell_map[sell_land]))
            land_pic = pygame.transform.scale(land_pic, (1150, 200))
            land_rect = land_pic.get_rect()
            land_rect.center = (750,400)
            self.screen.blit(land_pic, (land_rect.x, land_rect.y))
        else:
            # blit the picture that the computer did not do anything
            land_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, "comp_trade_nothing.png"))
            land_pic = pygame.transform.scale(land_pic, (1150, 200))
            land_rect = land_pic.get_rect()
            land_rect.center = (750,400)
            self.screen.blit(land_pic, (land_rect.x, land_rect.y))
        pygame.display.update()
        pygame.display.flip()
        return computer_land
        
    def spin(self):
        spin = ["disappear", "life", "luck", "nothing"]
        if self.luck == 0:
            event = 'disappear'
        else:
            disappear = 1/4
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
            return True
        elif event == "life":
            self.life += 10000
            life_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'comp_life_increase.png'))
            life_pic = pygame.transform.scale(life_pic, (1150, 200))
            life_rect = life_pic.get_rect()
            life_rect.center = (750,400)
            self.screen.blit(life_pic, (life_rect.x, life_rect.y))
            pygame.display.update()
            pygame.display.flip()
        elif event == "luck":
            self.luck = 1
            self.luck_lock = True
            luck_lock_pic = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'comp_luck_lock.png'))
            luck_lock_pic = pygame.transform.scale(luck_lock_pic, (1150, 300))
            luck_lock_rect = luck_lock_pic.get_rect()
            luck_lock_rect.center = (750,400)
            self.screen.blit(luck_lock_pic, (luck_lock_rect.x, luck_lock_rect.y))
            pygame.display.update()
            pygame.display.flip()
        elif event == "nothing":
            nothing = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'comp_trade_nothing.png')) # use the same picture as the nothing picture in trading for computer
            nothing = pygame.transform.scale(nothing, (1150, 200))
            nothing_rect = nothing.get_rect()
            nothing_rect.center = (750,400)
            self.screen.blit(nothing, (nothing_rect.x, nothing_rect.y))
            pygame.display.update()
            pygame.display.flip()
        return False

    def surprise(self, land, computer_land):
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
            if computer_land[i]:
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
        return land

    def deposit(self):
        if self.bank_money >= 50 and self.money >= 50:
            result = random.choice(["dep", "wd", "no"])
        elif self.bank_money >= 50 and self.money < 50:
            result = random.choice(["wd", "no"])
        elif self.bank_money < 50 and self.money >= 50:
            result = random.choice(["dep", "no"])
        else:
            result = "no"
        if result == "dep": # deposit
            money_value = self.money*random.randint(10,75)/100
            self.money -= money_value # minus the amount of money_value from money
            self.bank_money += money_value
            deposit = pygame.image.load(
                    os.path.join(IMAGE_DATA_PATH, 'comp_deposit.png'))
            deposit = pygame.transform.scale(deposit, (1150, 200))
            deposit_rect = deposit.get_rect()
            deposit_rect.center = (750, 400)
            self.screen.blit(deposit, (deposit_rect.x, deposit_rect.y))
        elif result == "wd": # withdraw
            money_value = self.bank_money
            self.money += money_value # minus the amount of money_value from money
            self.bank_money -= money_value
            withdraw = pygame.image.load(
                    os.path.join(IMAGE_DATA_PATH, 'comp_withdraw.png'))
            withdraw = pygame.transform.scale(withdraw, (1150, 200))
            withdraw_rect = withdraw.get_rect()
            withdraw_rect.center = (750, 400)
            self.screen.blit(withdraw, (withdraw_rect.x, withdraw_rect.y))
        elif result == "no": # no
            # blit nothing happened
            no = pygame.image.load(
                    os.path.join(IMAGE_DATA_PATH, 'comp_trade_nothing.png'))
            no = pygame.transform.scale(no, (700, 130))
            no_rect = no.get_rect()
            no_rect.center = (750, 400)
            self.screen.blit(no, (no_rect.x, no_rect.y))
        pygame.display.update()
        pygame.display.flip()

    # helper method to question
    def comp_buff_blit(self):
        buff = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'comp_buff.png'))
        buff = pygame.transform.scale(buff, (1150, 200))
        buff_rect = buff.get_rect()
        buff_rect.center = (750, 400)
        self.screen.blit(buff, (buff_rect.x, buff_rect.y))
        pygame.display.update()
        pygame.display.flip()

    # helper method to question
    def comp_debuff_blit(self):
        debuff = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'comp_debuff.png'))
        debuff = pygame.transform.scale(debuff, (1150, 200))
        debuff_rect = debuff.get_rect()
        debuff_rect.center = (750, 400)
        self.screen.blit(debuff, (debuff_rect.x, debuff_rect.y))
        pygame.display.update()
        pygame.display.flip()

    def question(self):
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
            self.comp_buff_blit()
        elif result == 'LIFE++':
            self.life += 5
            self.comp_buff_blit()
        elif result == 'MONEY++':
            self.money += 2000
            if self.luck > 0.01:
                self.luck -= 0.01
            else:
                self.luck = 0
            self.comp_buff_blit()
        elif result == 'LUCK--':
            if not self.luck_lock:
                if self.luck >= 0.2:
                    self.luck -= 0.2
                else:
                    self.luck = 0
                self.comp_debuff_blit()
            else:
                no = pygame.image.load(
                        os.path.join(IMAGE_DATA_PATH, 'comp_trade_nothing.png'))
                no = pygame.transform.scale(no, (700, 130))
                no_rect = no.get_rect()
                no_rect.center = (750, 400)
                self.screen.blit(no, (no_rect.x, no_rect.y))
                pygame.display.update()
                pygame.display.flip()
        elif result == 'LIFE--':
            self.comp_debuff_blit()
            result = random.randint(0,1)
            if result == 1:
                self.money -= 15000
            else:
                self.life -= 5
            self.comp_debuff_blit()
        elif result == 'MONEY--':
            self.money -= 2000
            self.comp_debuff_blit()
        elif result == 'MONEY-':
            self.money -= 1000
            self.comp_debuff_blit()
        elif result == 'GANGSTER':
            if not self.luck_lock:
                if self.luck >= 0.6:
                    self.luck -= 0.6
                else:
                    luck = 0
            self.money += 100000
            gang = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'comp_gang.png'))
            gang = pygame.transform.scale(gang, (1150, 200))
            gang_rect = gang.get_rect()
            gang_rect.center = (750,400)
            self.screen.blit(gang, (gang_rect.x, gang_rect.y))
            pygame.display.update()
            pygame.display.flip()
            self.gangster = True
        else:
            nothing = pygame.image.load(
                os.path.join(IMAGE_DATA_PATH, 'comp_trade_nothing.png'))
            nothing = pygame.transform.scale(nothing, (1150, 200))
            nothing_rect = nothing.get_rect()
            nothing_rect.center = (750,400)
            self.screen.blit(nothing, (nothing_rect.x, nothing_rect.y))
            pygame.display.update()
            pygame.display.flip()

    def prison(self): 
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
                os.path.join(IMAGE_DATA_PATH, 'comp_imprison.png'))
        imprison = pygame.transform.scale(imprison, (1150, 300))
        imprison_rect = imprison.get_rect()
        imprison_rect.center = (750, 400)
        self.screen.blit(imprison, (imprison_rect.x, imprison_rect.y))
        pygame.font.init()
        font = pygame.font.Font(None, 95)
        txt_surface = font.render(str(self.prison_years), True, [255,255,255])
        self.screen.blit(txt_surface, (935,327))
        self.screen.blit(txt_surface, (1040,405))
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

    def turn(self, player, computer, land, player_land, computer_land, player_obj):
        print("computer's turn")
        self.life -= 1 # after each turn, the life decreases by 1
        if self.prison_years == 0:
            self.bank_money *= (1+self.interest_rate)
            if self.luck_lock:
                if self.luck_lock_count <= 5:
                    self.luck_lock_count += 1
                else:
                    self.luck_lock_count = 0
                    self.luck_lock = False
            if self.occur[computer] == 'trade1,3':
                computer_land = self.trade([1,3], player_land, computer_land, land)
                # pop up a box that ask whether the player wants to buy the land(s) or not
            elif self.occur[computer] == 'deposit':
                # pop up a box that ask how much the player wants to deposit or withdraw
                self.deposit()
            elif self.occur[computer] == 'forward3':
                for i in range(1,4):
                    self.initialize_screen(player_land, computer_land, land, player_obj)
                    self.blit_player_icon(self.pos_player[player])
                    self.blit_computer_icon(self.pos_computer[computer+i])
                    pygame.time.delay(750)
                computer += 3
                self.turn(player, computer, land, player_land, computer_land, player_obj)
            elif self.occur[computer] == '?':
                self.question()
            elif self.occur[computer] == 'trade2':
                computer_land = self.trade([2], player_land, computer_land, land)
            elif self.occur[computer] == 'backward3':
                for i in range(1,4):
                    self.initialize_screen(player_land, computer_land, land, player_obj)
                    self.blit_player_icon(self.pos_player[player])
                    self.blit_computer_icon(self.pos_computer[computer-i])
                    pygame.time.delay(750)
                computer -= 3
                self.turn(player, computer, land, player_land, computer_land, player_obj)
            elif self.occur[computer] == 'trade3,4':
                computer_land = self.trade([3, 4], player_land, computer_land, land)
            elif self.occur[computer] == 'forward2':
                for i in range(1,3):
                    self.initialize_screen(player_land, computer_land, land, player_obj)
                    self.blit_player_icon(self.pos_player[player])
                    self.blit_computer_icon(self.pos_computer[computer+i])
                    pygame.time.delay(750)
                computer += 2
                self.turn(player, computer, land, player_land, computer_land, player_obj)
            elif self.occur[computer] == 'spin':
                disappear = self.spin()
                if disappear:
                    # display image of computer vanished due to magical power
                    disappear = pygame.image.load(
                            os.path.join(IMAGE_DATA_PATH, 'other_disappear.png'))
                    disappear = pygame.transform.scale(disappear, (1150, 300))
                    disappear_rect = disappear.get_rect()
                    disappear_rect.center = (750, 400)
                    self.screen.blit(disappear, (disappear_rect.x, disappear_rect.y))
                    pygame.display.update()
                    pygame.display.flip()
                    return False, False, False
            elif self.occur[computer] == 'trade1,4':
                computer_land = self.trade([1, 4], player_land, computer_land, land)
            elif self.occur[computer] == 'surprise':
                land = self.surprise(land, computer_land)
            elif self.occur[computer] == 'prison':
                self.prison()
            if self.life <= 0:
                return False, False, False
        else:
            self.prison_years -= 1
            prison_life = pygame.image.load(
                    os.path.join(IMAGE_DATA_PATH, 'comp_in_jail.png'))
            prison_life = pygame.transform.scale(prison_life, (1150, 300))
            prison_rect = prison_life.get_rect()
            prison_rect.center = (750, 400)
            self.screen.blit(prison_life, (prison_rect.x, prison_rect.y))
            pygame.display.update()
            pygame.display.flip()
        print("\ncomputer:",computer,"\nmoney:",self.money,"\nlife:",self.life,"\nluck:",self.luck,"\nprison:",self.prison_years,"\nbank_money:",self.bank_money,land,"\nplayer_land:",player_land,"\ncomputer_land:",computer_land)
        return computer, land, computer_land