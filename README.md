Name: Fahad Alkhazam | Arnav Saxena |


---
# **Final Project Lab Report**

_Note: I collaborated with Arnav for Ch.2., however, I worked alone on Ch.1_ 

## **Lab Objectives** 

>This is it; the final project! In this project, we get to work on a game controller to play the popular game "Space Invaders", and then work on a seperate, unique project. We have to first choose a need that we feel should be addressed, and utilize whatever tools provided to us in this class to solve it. We wanted to address the obesity epidemic by designing a game that requires steps to progress!

## **Challenge 1: Space Invaders Controller**


### How to use the Controller:

* Step 1: Upload the SpaceIvadersController Arduino sketch 
* Step 2: Run the game via spaceinvader.py
* Step 3: Run the controller via space_invaders_controller
* Step 4: Hit enter in the controller python terminal, and start the game!

### To play the game:

* Tilt to move spaceship
* Push button to fire
* DO NOT SLOUCH
* Shoot Invaders
* Avoid Incoming attacks
* Enjoy!



### **Improvements:**

*Improvement #1:* **Smoother Motion**
>When I first ran the code, I noticed that I was not getting consistent movements. I plotted the accelerometer values and noticed that the value of the accelerometer in the x direction shifted noticably when I moved the accelerometer left and right, thus, I decided to forego the code given to us and use a simpler method. I set the value of the accelerometer in the x direction as the only value used to determine the movement of the controller, and it yielded consistent results. 

*Improvement #2:* **Firing while Moving**
>I found it quite inconvenient to have to tilt the controller upwards to fire. Afterall, most buttons utilize some form of a button to call these actions. Thus, I decided to implement the button to fire which enabled the user to fire while they are moving the board. To make the button more consistent, I attached a resistor and connected it to power.

*Improvement #3:* **Detect When Flipped**
> Some parents (especially mine :/ ) HATE IT when their kids are laying on their backs with basd posture playing video games rather than sitting up straight. Thus, I decided to implement a feature in which the controller would buzz, light up in red, and display a message when the player is laying down. 

> This is basically the way I did it: When the player is laying down, they will tilt the controller in the z-direction to get into a comfortable position. Otherwise they will have to hold the controller in an awkward position. Thus, I implemented a function which tests the value of the accelerometer in the z-direction and infer if the controller is flipped.


### **Establishing a connection between the game, the controller python file, and the controller ino file**:

> I had to set up a connection between the spaceinvaders.py file and the  spaceinvaders_controller.py file in order to send the game's data to my controller. The code given established a connection between the two, and so I sent a holder string from the controller to the game to get the address of the controller. I then, used that address to send over a string of "-1" everytime the player is hit, and a string of the value of points gained when an enemy is hit.

>After the data has been recieved by the controller python files, it sends it over to the controller ino file over Serial, to which, the ino file converts the string into an int to utilize that information.

### **Features:**

*Feature #1:* **Buzz when Hit**
>When the player gets hit, the motor buzzes to let them know that they have been hit. To implement this, I imported the arduino file from Lab 3, and whenever the arduino file recieves a value of "-1", it infers that one life has been taken away, and thus buzzes the motor.

*Feature #2:* **Enemy Battleship LED Indicator**
>The controller lights up every time the player hits an enemy with the color of that enemy. Once the arduino recieves a string over Serial, it converts it into an integer and infers (based on how many points were gained) what enemy that was. 

This is the general breakdown:

* Green: 10 pts
* Blue: 20 pts
* Purple: 30 pts
* Red: 50, 100, 150, or 300 pts

> After that, the RGB LED displays the color respective to every enemy using the writeColor() function implemented..

*Feature #3:* **Game Data**
> The OLED display displays the score of the user and the amount of lives they have left. To achieve this, I sent over positive values for the score, and a "-1" for hit. Whenever, it gets hit, the ino file substracts 1 from the int variable "lives", and whenever it receives a positive integer, it adds that value to the "score" int variable.

>It continuously displays the score and lives left unless the user is laying down, or the game is over. 

*Feature #4:* **GAME OVER**
>Once the amount of lives goes below 0, the OLED display displays "GAME OVER". 


### **YouTube Demo Link:** 
https://www.youtube.com/watch?v=vMgQnQNbGO4


## **Challenge 2: Ardemon**

### **Need & Solution:**

>The rise of obesity over the past few decades cannot be ignored. According to the CDC, more the 2.8 million people die a year due to obesity related issues.

>It is clear that most people do not choose to go down that path, and in fact, would prefer the path of a more active lifestyle. On that note, being active does not neccesarily mean doing a rigorous exercise; it can be a simple walk. That precisly is what we are trying to achieve in this project: we want to motivate people to go out and walk. The way we do this is by building a game that has the player progress through activity (in this case steps).

>The reason we chose a game to motivate people is that different people have different passions. Some people, athletes for example, have a natural passion for exercising. However, there do exist people that do not share that passion and are instead more interested in progressing through a video. Those are the people we are after.

### **Implementation:**


>To implement a device that has this many capabilities, we used a good amount of the functionalities introduced to us in the course.

**OLED Display:**
> Displays the time, name of ardemon, Lvl and XP earned, and the amount of steps taken so far.

> In battle mode, it displays the enemy's HP, user's HP, and current move selected with an explanation of its stats.

**Photoresistor:** 
> Whenever the photoresistor stops recieving a high amount of light, it counts that as a tap. If this is done during the "walking" state, it counts that as a pet. However, there is a 10-minute cooldown so as to prevent the user from spamming it. It can also be used to reject a battle.

**Pedometer:**
> We improved the thresholds on the pedometer class introduced in Lab 5. We utilized this to count the steps taken and calculate the XP. We also added a functionality that spawns a random ardemon every 1000 steps.

**Toggle, RGB Light & Button:**
>We used the button and the accelerometer as the main registers from the user, the button would trigger a select, while the accelerometer would toggle between different setting (Ardemon, move, e.t.c.). We used the RGB LED to display the type of the Ardemon currently selected. 

**Color = Type:**
* Yellow = Lightning
* Green = Tree
* Blue = Ocean
* Red = Lava

### **Software:**

> We HEAVILY utililzed Object-Oriented-Programming in this project. Every different ardemon had its own class that defined its moves and the amount of damage/ healing each one dealt. When a user selects a move, it passes the type of the enemy into that class to calculate how much damage should be dealt to that enemy. It then passes that damage to the enemy which stores it and sends it over to both Arduinos to display for the user.

### **How to Play!**

* Every time you take a step it increases your XP based on your type.
* Every 1000 steps you encounter an ardemon that you can capture.
* You can toggle between which ardemon you would like to carry by clicking on the button, and then moving your device. Click the button again to select the ardemon. (Its type is indicated in the LED!)
* You can initiate a battle with a friend by clicking the lower button, your friend can accet it by clicking on his button, or decline it by tapping that photoresistor.
* You can choose which ardemon in your arsenal you would like to choose for battle, different types have different advantages (Tree is beafy, Lightning deals a lot of damage). 
* You can now select a move. The OLED will display information about that move. Different moves deal different damages based on the enemy's type.
* If you win you gain XP! If you lose, you lose XP. :(


### **YouTube Demo Link:** 

https://youtu.be/lnC-4wcUyzI

## **Division of Labor**

>Me and Arnav worked really well in this project, and I could not ask for a better teammate! He focused more on the OOP and Python side of the device, while I focused more on the Arduino and Hardware aspect. 

>It was not purely in this manner as he did help me out in the Arduino side by helping  with the toggle detector, and I did help him out in the OOP front by writing parts of the Ardemon characters/ moves algorithm.

---
**Thank you for all your help in this  quarter, and I wish you all the best in your future endevours!**



_A Lab Report by Fahad Alkhazam_
