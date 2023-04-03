from gettext import pgettext
import pygame as pg
import sys
import os
from config import *

class inputBox():
    def __init__(self, screen):
        self.screen = screen
        print('This is the input box class.')

    def blit_player_icon(self,center):
        icon = pg.image.load(
            os.path.join(IMAGE_DATA_PATH, 'player_icon.png'))
        icon = pg.transform.scale(icon, (50, 50))
        icon_rect = icon.get_rect()
        icon_rect.center = center
        self.screen.blit(icon, (icon_rect.x, icon_rect.y))
        pg.display.update()
        pg.display.flip()
    
    def blit_computer_icon(self,center):
        icon = pg.image.load(
            os.path.join(IMAGE_DATA_PATH, 'comp_icon.png'))
        icon = pg.transform.scale(icon, (50, 50))
        icon_rect = icon.get_rect()
        icon_rect.center = center
        self.screen.blit(icon, (icon_rect.x, icon_rect.y))
        pg.display.update()
        pg.display.flip()

    def blit_menu(self,player_land, computer_land, land, player_obj):
        ### display values of age, luck, money, and land owned by player and comuter in the margin
        pg.font.init()
        font = pg.font.Font(None, 50)
        txt_surface = font.render("STATUS", True, [0,0,0])
        self.screen.blit(txt_surface, (1252,70))
        font = pg.font.Font(None, 30)
        txt_surface = font.render("Liquid Assets: $"+str(round(player_obj.money,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (1192,120))
        txt_surface = font.render("Bank Deposits: $"+str(round(player_obj.bank_money,2)), True, [0,0,0])
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
        txt_surface = font.render("Luck: "+str(round(player_obj.luck*100,2)), True, [0,0,0])
        self.screen.blit(txt_surface, (1192,305))
        txt_surface = font.render("Life: "+str(player_obj.life), True, [0,0,0])
        self.screen.blit(txt_surface, (1192,345))
        font = pg.font.Font(None, 58)
        txt_surface = font.render("Price of Lands", True, [0,0,0])
        self.screen.blit(txt_surface, (1200,395))
        font = pg.font.Font(None, 35)
        for i in range(4):
            txt_surface = font.render("Land "+str(i+1)+": $"+str(round(land[i],2)), True, [0,0,0])
            self.screen.blit(txt_surface, (1192,445+i*50))

    def trade_easyone(self, player, computer, player_land, computer_land, land, player_obj, available_land):
        pos_player = [(162,144),(162,272),(162,399),(162,520),(162,650),(286,650),(418,650),(546,650),(676,650),(799,650),(926,650),(1056,650),(1056,520),(1056,399),(1056,272),(1056,144)]
        pos_computer = [(232,144),(232,272),(232,399),(232,520),(232,650),(356,650),(485,650),(612,650),(739,650),(868,650),(996,650),(1122,650),(1122,520),(1122,399),(1122,272),(1122,144)]
        self.screen.fill([255,255,255])
        map1 = pg.image.load(
                os.path.join(IMAGE_DATA_PATH, 'easy1.png'))
        map1_rect = map1.get_rect()
        map1_rect.center = (650,400)
        self.screen.blit(map1, (map1_rect.x, map1_rect.y))
        trade = pg.image.load(
            os.path.join(IMAGE_DATA_PATH, 'trade_land.png'))
        trade = pg.transform.scale(trade, (1200, 430))
        trade_rect = trade.get_rect()
        trade_rect.center = (750,350)
        self.screen.blit(trade, (trade_rect.x, trade_rect.y))
        pg.font.init()
        font = pg.font.Font(None, 95)
        available = ""
        for i in available_land:
            available += str(i)+", "
        txt_surface = font.render(available[:-2], True, [255,255,255])
        self.screen.blit(txt_surface, (993,240))
        self.screen.blit(txt_surface, (336,455))
        self.blit_player_icon(pos_player[player])
        self.blit_computer_icon(pos_computer[computer])
        self.blit_menu(player_land, computer_land, land, player_obj)

    def deposit_easyone(self, player, computer, player_land, computer_land, land, player_obj):
        pos_player = [(162,144),(162,272),(162,399),(162,520),(162,650),(286,650),(418,650),(546,650),(676,650),(799,650),(926,650),(1056,650),(1056,520),(1056,399),(1056,272),(1056,144)]
        pos_computer = [(232,144),(232,272),(232,399),(232,520),(232,650),(356,650),(485,650),(612,650),(739,650),(868,650),(996,650),(1122,650),(1122,520),(1122,399),(1122,272),(1122,144)]
        self.screen.fill([255,255,255])
        map1 = pg.image.load(
                os.path.join(IMAGE_DATA_PATH, 'easy1.png'))
        map1_rect = map1.get_rect()
        map1_rect.center = (650,400)
        self.screen.blit(map1, (map1_rect.x, map1_rect.y))
        deposit = pg.image.load(
                os.path.join(IMAGE_DATA_PATH, 'deposit_number.png'))
        deposit = pg.transform.scale(deposit, (700, 130))
        deposit_rect = deposit.get_rect()
        deposit_rect.center = (750,400)
        self.screen.blit(deposit, (deposit_rect.x, deposit_rect.y))
        self.blit_player_icon(pos_player[player])
        self.blit_computer_icon(pos_computer[computer])
        self.blit_menu(player_land, computer_land, land, player_obj)

    def withdraw_easyone(self, player, computer, player_land, computer_land, land, player_obj):
        pos_player = [(162,144),(162,272),(162,399),(162,520),(162,650),(286,650),(418,650),(546,650),(676,650),(799,650),(926,650),(1056,650),(1056,520),(1056,399),(1056,272),(1056,144)]
        pos_computer = [(232,144),(232,272),(232,399),(232,520),(232,650),(356,650),(485,650),(612,650),(739,650),(868,650),(996,650),(1122,650),(1122,520),(1122,399),(1122,272),(1122,144)]
        self.screen.fill([255,255,255])
        map1 = pg.image.load(
                os.path.join(IMAGE_DATA_PATH, 'easy1.png'))
        map1_rect = map1.get_rect()
        map1_rect.center = (650,400)
        self.screen.blit(map1, (map1_rect.x, map1_rect.y))
        withdraw = pg.image.load(
                os.path.join(IMAGE_DATA_PATH, 'withdraw_number.png'))
        withdraw = pg.transform.scale(withdraw, (700, 130))
        withdraw_rect = withdraw.get_rect()
        withdraw_rect.center = (750,400)
        self.screen.blit(withdraw, (withdraw_rect.x, withdraw_rect.y))
        self.blit_player_icon(pos_player[player])
        self.blit_computer_icon(pos_computer[computer])
        self.blit_menu(player_land, computer_land, land, player_obj)

    def input_box(self, start_coor, map_no, action, player, computer, player_obj=None, land = [], computer_land = [], player_land = [], land_price = []):
        # start_coor is a tuple with the start coordinate of the textbox on the up-left corner
        easy_map1, easy_map2, hard_map1, hard_map2, withdraw, deposit, trade = False, False, False, False, False, False, False
        if map_no == 'easy_map1':
            easy_map1 = True
        elif map_no == 'easy_map2':
            easy_map2 = True
        elif map_no == 'hard_map1':
            hard_map1 = True
        elif map_no == 'hard_map2':
            hard_map2 = True
        if action == 'withdraw':
            withdraw = True
        elif action == 'deposit':
            deposit = True
        elif action == "trade":
            trade = True
        pg.font.init()
        font = pg.font.Font(None, 32)
        input_box = pg.Rect(start_coor[0], start_coor[1], 150, 35) # length = 150, height = 35
        color_inactive = pg.Color('red') # CHANGE THE COLOR
        color_active = pg.Color('orange')
        color = color_inactive
        active = False
        text = ''
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN:
                    if active:
                        if event.key == pg.K_RETURN:
                            print(text)
                            if deposit and easy_map1:
                                valid = True
                                try:
                                    float(text)
                                except Exception:
                                    valid = False
                                if valid and float(text) >= 0 and float(text) <= player_obj.money:
                                    return text # return the text message in the input box
                                else:
                                    print("not valid, try again")
                                    return -1
                            elif withdraw and easy_map1:
                                valid = True
                                try:
                                    float(text)
                                except Exception:
                                    valid = False
                                if valid and float(text) >= 0 and float(text)<=player_obj.bank_money:
                                    return text # return the text message in the input box
                                else:
                                    print("not valid, try again")
                                    return -1
                            elif trade and easy_map1:
                                valid = True
                                try:
                                    float(text)
                                except Exception:
                                    valid = False
                                if valid:
                                    print("trade user enter:",int(text))
                                if valid and (text == "-1" or (float(text) == int(float(text)) and not computer_land[int(text)-1] and land_price[int(text)-1]<=player_obj.money and int(text) in land)):
                                    return text
                                else:
                                    print("not valid, try again.")
                                    return False
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                            # fill the screen with what it originally is again, instead of paint it pure white
                            # the way to solve this issue is to define another method for each case possible in the game that uses a text box
                            # and call the method here by some means
                            if easy_map1:
                                if deposit:
                                    self.deposit_easyone(player, computer, player_land, computer_land, land_price, player_obj)
                                elif withdraw:
                                    self.withdraw_easyone(player, computer, player_land, computer_land, land_price, player_obj)
                                elif trade:
                                    self.trade_easyone(player, computer, player_land, computer_land, land_price, player_obj, land)
                            # elif easy_map2:
                            #     if deposit:
                            #         deposit_easyTwo()
                            #     elif withdraw:
                            #         withdraw_easyTwo()
                            # elif hard_map1:
                            #     if deposit:
                            #         deposit_hardOne()
                            #     elif withdraw:
                            #         withdraw_hardOne()
                            # elif hard_map2:
                            #     if deposit:
                            #         deposit_hardTwo()
                            #     elif withdraw:
                            #         withdraw_hardTwo()
                            pg.display.update()
                            pg.display.flip()
                        else:
                            text += event.unicode
            # Render the current text.
            txt_surface = font.render(text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            self.screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pg.draw.rect(self.screen, color, input_box, 2)
            pg.display.update()
            pg.display.flip()

if __name__ == '__main__':
    screen = pg.display.set_mode([1500,800])
    pg.display.set_caption("大富翁")
    screen.fill([255,255,255])
    trade = pg.image.load(
            os.path.join(IMAGE_DATA_PATH, 'trade_land.png'))
    trade = pg.transform.scale(trade, (1200, 550))
    trade_rect = trade.get_rect()
    trade_rect.center = (750,350)
    screen.blit(trade, (trade_rect.x, trade_rect.y))
    box = inputBox(screen) # inputbox
    box.input_box((675, 625), "easy_map1", "trade", land = [1,2,3,4])
    pg.display.update()
    pg.display.flip()