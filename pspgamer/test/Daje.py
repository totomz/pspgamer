import logging

import pygame
import boto3
from dotenv import load_dotenv
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
from pspgamer.test.Speecher import Speecher

load_dotenv()

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])

# Initialize pygame here, so the others have half work done!
pygame.init()
pygame.joystick.init()
pygame.mixer.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
# joystick = joysticks[0]
# print(joystick.get_name())
#
# # Initialize it to use it
# joystick.init()

logging.info("Loading messages")
speecher = Speecher()

# Loop until the user clicks the close button.
done = False
while not done:
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        print("ping")
        print(event.type)

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            print(f"KEY! {event.key}")

            if event.key == pygame.K_a:
                print("AAAAAAAAAA")
            if event.key == pygame.K_b:
                print("BBBBBBBBBBB")
            if event.key == pygame.K_c:
                print("CCCCCCCCCC")

        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button {n} pressed.".format(n=event.button))

            # if event.button == 4:
            #     speecher.say(message="Cura della persona", voice="Carla")
            # elif event.button == 6:
            #     speecher.say(message="Devo andare a cagare", voice="Giorgio")
            # elif event.button == 3:
            #     speecher.say(message="Daria, tuo marito e' una bomba sexy. Lo sai, vero? Te lo ruberei...", voice="Bianca")
            # elif event.button == 2:
            #     speecher.say(message="Io pure lo trovo un bomber. Mi farei aprire come una cozza.", voice="Giorgio")
            # elif event.button == 0:
            #     speecher.say(message="LOL", voice="Giorgio")

        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button {n} released.".format(n=event.button))
        elif event.type == pygame.JOYAXISMOTION:
            print("Joystick AXIS")
            print(event.dict)


# pygame.mixer.quit()
#
# from array import array
# from time import sleep
#
# import pygame
# from pygame.mixer import Sound, get_init, pre_init
#
# class Note(Sound):
#
#     def __init__(self, frequency, volume=.1):
#         self.frequency = frequency
#         Sound.__init__(self, self.build_samples())
#         self.set_volume(volume)
#
#     def build_samples(self):
#         period = int(round(get_init()[0] / self.frequency))
#         samples = array("h", [0] * period)
#         amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
#         for time in range(period):
#             if time < period / 2:
#                 samples[time] = amplitude
#             else:
#                 samples[time] = -amplitude
#         return samples
#
#
# def dot():
#     Note(440).play(-1, maxtime=150)
#     sleep(0.25)
#
# def line():
#     Note(440).play(-1, maxtime=150 * 3)
#     sleep(0.25 * 3)
#
# if __name__ == "__main__":
#     pre_init(44100, -16, 1, 1024)
#     pygame.init()
#     Note(440).play(-1, maxtime=150)
#     # CASA
#     line()
#     dot()
#     line()
#     dot()
#     sleep(150 * 3)
#
#     dot()
#     line()
#     sleep(150 * 3)
#
#     dot()
#     dot()
#     dot()
#     sleep(150 * 3)
#
#     dot()
#     line()
#     sleep(150 * 3)
