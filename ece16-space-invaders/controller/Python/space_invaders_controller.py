"""
@author: Ramsin Khoshabeh
"""

from ECE16Lib.Communication import Communication
from time import sleep
import socket, pygame

# Setup the Socket connection to the Space Invaders game
host = "127.0.0.1"
port = 65432
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mySocket.connect((host, port))
mySocket.setblocking(False)

"""
send a random message to the game
"""
mySocket.send("holderString".encode("UTF-8"))



class PygameController:
  comms = None

  def __init__(self, serial_name, baud_rate):
    self.comms = Communication(serial_name, baud_rate)

  def run(self):
    # 1. make sure data sending is stopped by ending streaming
    self.comms.send_message("stop")
    self.comms.clear()

    # 2. start streaming orientation data
    input("Ready to start? Hit enter to begin.\n")
    self.comms.send_message("start")

    # 3. Forever collect orientation and send to PyGame until user exits
    print("Use <CTRL+C> to exit the program.\n")
    while True:
      message = self.comms.receive_message()
      try:
        msg, _ = mySocket.recvfrom(1024) # receive 1024 bytes
        msg = msg.decode('utf-8')
        print(msg)
        self.comms.send_message(str(msg))
      except:
        pass

      if(message != None):
        command = None
        message = int(message)
        # if message == 0:
        #   command = "FLAT"
        # if message == 1:
        #   command = "UP"
        if message == 1:
          command = "FIRE"
          mySocket.send(command.encode("UTF-8"))
          command = "LEFT"
          print("fireL")
        elif message == 2:
          command = "FIRE"
          mySocket.send(command.encode("UTF-8"))
          command = "RIGHT"
          print("fireR")
        elif message == 3:
          command = "LEFT"
          print("left")
        elif message == 4:
          command = "RIGHT"
          print("right")
        elif message == 5:
          command = "FIRE"
          print("fire")

        if command is not None:
          mySocket.send(command.encode("UTF-8"))


if __name__== "__main__":
  serial_name = "COM8"
  baud_rate = 115200
  controller = PygameController(serial_name, baud_rate)

  try:
    controller.run()
  except(Exception, KeyboardInterrupt) as e:
    print(e)
  finally:
    print("Exiting the program.")
    controller.comms.send_message("stop")
    controller.comms.close()
    mySocket.send("QUIT".encode("UTF-8"))
    mySocket.close()

  input("[Press ENTER to finish.]")
