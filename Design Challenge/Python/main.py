import time
from player import *
from display import *
from game import *
import random

ardemon = [Ardizard, Ardtoise, Ardusaur, Pikardchu, Boolbasaur, Floartle]

# sample Ardemons
ardtoise1 = Ardtoise(3)
ardtoise1.available_xp = 190

pikardchu1 = Pikardchu(3)

ardizard1 = Ardizard(2)

boolbasaur1 = Boolbasaur(2)

player1 = Player("COM5", [ardtoise1, pikardchu1, ardizard1, boolbasaur1])
display1 = Display(player1)

pikarchu2 = Pikardchu(3)
ardusaur2 = Ardusaur(4)
ardtoise2 = Ardtoise(3)
floartle2 = Floartle(3)

player2 = Player("COM9", [pikarchu2, ardusaur2, ardtoise2, floartle2])
display2 = Display(player2)

players = [player1, player2]
displays = [display1, display2]

if __name__ == "__main__":

    try:
        previous_time = [0]*len(players)
        
        last_tilt = [0]*len(players)

        last_pet = [0]*len(players)

        spawned = [0]*len(players)
        
        while (True):
            for i in range(len(players)):
                message = players[i].receive()
                if (message != None):

                    if players[i].active_ardemon.upgrade_amount() < players[i].active_ardemon.available_xp:
                        players[i].level_up()
                        displays[i].level_up()
                        last_pet[i] = time.time() # dont ask

                    if (not players[i].selecting) and (not players[i].spawn) and (not players[i].challenge) and (not players[i].incoming):
                        try:
                            (m1, m2, m3, m4) = message.split(',')
                            
                            # Collect data in the pedometer
                            m1, m2, m3, m4 = int(m1), int(m2), int(m3), int(m4)
                            players[i].pedometer.add(m2, m3, m4)

                            if (time.time() - previous_time[i] > 1 and time.time() - last_pet[i] > 3): #update every second
                                previous_time[i] = time.time()
                                steps, _, _ = players[i].pedometer.process()
                                players[i].add_steps(steps)
                                displays[i].update()
                            
                        except:  # if corrupted data, skip the sample
                            pass

                        try:
                            msg = message.strip()
                            
                            if msg == "SELECTED":
                                players[i].selecting = True
                                displays[i].select_ardemon(False)
                            

                            elif msg == "PET":
                                if (time.time() - last_pet[i] > 0.45): 
                                    delay = 600 # 10 minutes
                                    response = players[i].pet(time.time(), delay)
                                    displays[i].pet(response, delay)
                                    last_pet[i] = time.time()
                            
                            elif msg == "BATTLE":
                                players[i].challenge = True
                                players[i].challenge_time = time.time()
                                displays[i].searching()

                                displays[1-i].challenged()
                                players[1-i].incoming = True
                            
                        except ValueError:  # if corrupted data, skip the sample
                            pass
                        
                        if players[i].total_steps % 1000 == 0 and players[i].total_steps != 0:
                            spawned[i] = random.choice(ardemon)(random.randint(1,round(sum([x.level for x in players[i].ardemon])/2)))
                            players[i].spawn = True
                            displays[i].offer(spawned[i])

                    elif players[i].selecting:
                        try:
                            msg = message.strip()
                            if msg == "SELECTED":
                                players[i].selecting = False
                                displays[i].select_ardemon(True)
                            elif msg == "TILT":
                                if (time.time() - last_tilt[i] > 0.45):
                                    players[i].switch_ardemon()
                                    last_tilt[i] = time.time()
                                    displays[i].select_ardemon(False)
                        except ValueError:
                            pass
                    
                    elif players[i].spawn:
                        try:
                            msg = message.strip()
                            if msg == "PET":
                                players[i].spawn = False
                                displays[i].decline(spawned[i])
                                last_pet[i] = time.time() # egregious reuse of variable
                                players[i].pedometer.steps += 1
                                players[i].total_steps += 1
                                
                            elif msg == "SELECTED":
                                players[i].spawn = False
                                displays[i].accept(spawned[i])
                                players[i].ardemon.append(spawned[i])
                                players[i].pedometer.steps += 1
                                players[i].total_steps += 1
                                last_pet[i] = time.time() # egregious reuse of variable
                        except ValueError:
                            pass
                    
                    elif players[i].challenge:
                        if time.time() - players[i].challenge_time > 15:
                            players[i].challenge = False
                            displays[i].time_out()
                            last_pet[i] = time.time() # egregious reuse of variable

                            displays[1-i].time_out()
                            players[1-i].incoming = False
                            last_pet[1-i] = time.time() # egregious reuse of variable
                    
                    elif players[i].incoming:
                        try:
                            msg = message.strip()
                            if msg == "PET":
                                players[1-i].challenge = False
                                displays[i].time_out()
                                last_pet[i] = time.time() # egregious reuse of variable

                                displays[1-i].time_out()
                                players[i].incoming = False
                                last_pet[1-i] = time.time() # egregious reuse of variable
                                
                            elif msg == "SELECTED":
                                players[1-i].challenge = False
                                players[i].incoming = False

                                displays[i].starting()
                                displays[1-i].starting()
                                time.sleep(3)

                                Battle(players[i], players[1-i])()
                        except ValueError:
                            pass

    except(Exception, KeyboardInterrupt) as e:
        print(e)  # Exiting the program due to exception
    finally:
        print("Closing connection.")
        for player in players:
            player.write("sleep")  # stop sending data
            player.comms.close()