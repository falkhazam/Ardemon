from player import *
from creatures import *
from display import *
import time
import random

class Battle:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.displays = [Display(player1), Display(player2)]
        self.turn = 0
    
    def begin(self):
        self.displays[0].select_ardemon(False)
        self.displays[1].select_ardemon(False)
        
        last_tilt0 = 0
        last_tilt1 = 0

        while (self.players[0].battling == False or self.players[1].battling == False):
            message0 = self.players[0].receive()

            message1 = self.players[1].receive()
                
            if not self.players[0].battling:
                if(message0 != None):
                    try:
                        msg0 = message0.strip()
                        if msg0 == "SELECTED":
                            # print(message0)
                            self.players[0].battling = True
                            self.displays[0].select_ardemon(True)
                            
                        elif msg0 == "TILT":
                            if (time.time() - last_tilt0 > 0.45):
                                self.players[0].switch_ardemon()
                                last_tilt0 = time.time()
                                self.displays[0].select_ardemon(False)

                    except ValueError:        # if corrupted data, skip the sample
                        pass

            if not self.players[1].battling:
                if(message1 != None):
                    try:
                        msg1 = message1.strip()
                        if msg1 == "SELECTED":
                            # print(message0)
                            self.players[1].battling = True
                            self.displays[1].select_ardemon(True)
                            
                        elif msg1 == "TILT":
                            if (time.time() - last_tilt1 > 0.45):
                                self.players[1].switch_ardemon()
                                last_tilt1 = time.time()
                                self.displays[1].select_ardemon(False)

                    except ValueError:        # if corrupted data, skip the sample
                        pass

        self.displays[0].ready_screen(self.players[1].active_ardemon) 
        self.displays[1].ready_screen(self.players[0].active_ardemon)

        time.sleep(3)


    def fight(self):
        while (self.players[0].active_ardemon.health > 0 and self.players[1].active_ardemon.health > 0):
            self.displays[self.turn].turn_screen(self.players[1-self.turn].active_ardemon, True)
            self.displays[1-self.turn].turn_screen(self.players[self.turn].active_ardemon, False)
            time.sleep(5)
            self.displays[self.turn].select_attack()

            attack_selected = False
            last_tilt = 0
            while (not attack_selected):
                message = self.players[self.turn].receive()
                if(message != None):
                        try:
                            msg = message.strip()
                            if msg == "SELECTED":
                                self.displays[self.turn].select_attack(True)
                                attack_selected = True
                                time.sleep(2)
                            elif msg == "TILT":
                                if (time.time() - last_tilt > 0.45):
                                    self.players[self.turn].change_attack()
                                    last_tilt = time.time()
                                    self.displays[self.turn].select_attack(False)
                        except ValueError:        # if corrupted data, skip the sample
                            pass
           
            successful = random.randint(1, 100) <= self.players[self.turn].active_ardemon.accuracy
            if successful:
                att = self.players[self.turn].active_ardemon.attack(self.players[1-self.turn].active_ardemon, self.players[self.turn].active_ardemon.active_attack)
                self.displays[self.turn].attack(self.players[1-self.turn].active_ardemon, att)

                self.displays[1-self.turn].attack(self.players[self.turn].active_ardemon, att)
                # TODO: Buzz Motors of both
                time.sleep(3)
            else:
                self.displays[self.turn].attack(self.players[1-self.turn].active_ardemon, "Missed!")
                self.displays[1-self.turn].attack(self.players[self.turn].active_ardemon, "Missed!")
                time.sleep(3)

            self.turn = 1 - self.turn
            
    def end(self):
        if self.players[0].active_ardemon.health <= 0 and self.players[1].active_ardemon.health <= 0: # draw
            self.displays[0].draw()
            self.displays[1].draw()

        elif self.players[0].active_ardemon.health <= 0: # player1 wins
            xp = self.players[0].active_ardemon.level * 400
            self.players[0].active_ardemon.available_xp -= xp
            self.players[0].active_ardemon.total_xp -= xp

            if (self.players[0].active_ardemon.total_xp < 0):
                self.players[0].active_ardemon.total_xp = 0

            if (self.players[0].active_ardemon.available_xp < 0):
                self.players[0].active_ardemon.available_xp = 0

            self.players[1].active_ardemon.available_xp += xp
            self.players[1].active_ardemon.total_xp += xp

            self.displays[0].loss(xp)
            self.displays[1].win(xp)
            
        else: # player0 wins
            xp = self.players[1].active_ardemon.level * 400
            self.players[1].active_ardemon.available_xp -= xp
            self.players[1].active_ardemon.total_xp -= xp

            if (self.players[1].active_ardemon.total_xp < 0):
                self.players[1].active_ardemon.total_xp = 0

            if (self.players[1].active_ardemon.available_xp < 0):
                self.players[1].active_ardemon.available_xp = 0

            self.players[0].active_ardemon.available_xp += xp
            self.players[0].active_ardemon.total_xp += xp

            self.displays[1].loss(xp)
            self.displays[0].win(xp)
        
        self.reset() # restore health, damage
        time.sleep(10)
    
    def reset(self):
        self.players[0].active_ardemon.reset()
        self.players[1].active_ardemon.reset()
        self.players[0].battling = False
        self.players[1].battling = False


    def play(self):
        self.begin()
        self.fight()
        self.end()

    __call__ = play


            



