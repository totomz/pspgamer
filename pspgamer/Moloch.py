import os

# os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame.transform
import pygame.display
# pygame.display.init()
# screen = pygame.display.set_mode((1, 1))

import pygame
import logging
from pynput.keyboard import Key, Listener
from pydoc import locate
from pspgamer.Configuration import Configuration
from pspgamer.controllers.Joypad import JoypadController, MarsJoypad
from pspgamer.controllers.Keyboards import ThreePedalKeyboard, KeyboardController
from pspgamer.plugin.Plugin import BasePlugin
from pspgamer.test.Speecher import Speecher


class Main:
    def __init__(self, joypad: JoypadController, keyboard: KeyboardController):
        self.joypad = joypad
        self.keyboard = keyboard
        self.log = logging.getLogger("Main")

    def run(self):
        self.log.info("Staring...")

        pygame.init()
        self.log.debug("pygame init()")

        ###################
        # Main Event Loop #
        ###################
        #adas
        #
        # def on_press(key):
        #     print('{0} pressed'.format(key))
        #
        # def on_release(key):
        #     print('{0} release'.format(key))
        #     if key == Key.esc:
        #         # Stop listener
        #         return False
        #
        # # Collect events until released
        # print("BOMBAAAAA")
        # with Listener(
        #         on_press=on_press,
        #         on_release=on_release) as listener:
        #     listener.join()
        #
        # print("zio")
        done = False
        while not done:
            event = pygame.event.wait()
            # event = pygame.event.get()

            self.log.debug(f"PING {event.type}")

            if event.type == pygame.QUIT: # If user clicked close.
                done = True # Flag that we are done so we exit this loop.

            elif event.type == pygame.JOYBUTTONDOWN:
                self.joypad.handle_event_button_down(event=event)

            elif event.type == pygame.JOYBUTTONUP:
                self.joypad.handle_event_button_up(event=event)

            elif event.type == pygame.JOYAXISMOTION:
                self.joypad.handle_event_axis_motion(event=event)

            elif event.type == pygame.KEYUP:
                self.keyboard.handle_event_key_up(event=event)

            elif event.type == pygame.KEYUP:
                self.keyboard.handle_event_key_down(event=event)


if __name__ == "__main__":
    #############
    # Internals #
    #############
    def load_plugin(item: dict):
        log.info(f"Loading {item['type']}")
        my_class = locate(item['type'])
        instance: BasePlugin = my_class()
        instance.initialize(item)
        return instance

    ########
    # Main #
    ########
    log = logging.getLogger("main")
    conf = Configuration().as_dict()

    # Initialize controllers
    try:
        joypad = MarsJoypad()
    except Exception:
        log.info("No Joypad controller found")
        joypad = None

    keyboard: KeyboardController = ThreePedalKeyboard()
    # tts = Speecher()
    # def click_struct_ctts(voice):
    #     def handler(event):
    #         last_category = struct[-1]
    #         button = event.button
    #
    #         if button != last_category:
    #             # Ho premuto questo pulsante per la prima volta
    #             # Il messaggio e' il primo elemento della prima lista.
    #             # Copio la lista originale nella seconda posizione, che li la ciclero'
    #             message = struct[button][0]
    #             struct[button][2] = struct[button][1].copy()
    #         else:
    #             # Sto ciclando la lista
    #             message = struct[button][2].pop(0)
    #             struct[button][2].append(message)
    #
    #         tts.say(message=message, voice=voice)
    #         struct[-1] = button
    #     return handler

    # def say_struct(btn, voice):
    #
    #     def inner(evnt):
    #         message = struct[btn][2][-1]
    #         # tts.say(message=f"DICO: {message}", voice=voice)
    #     return inner

    plugins = {}    # Temporary map for registered plugins

    ############################
    log.info("Loading Plugins")
    ############################
    for name, item in conf['plugins'].items():
        print(name)
        pconf = conf['plugins'][name]
        plugin = load_plugin(pconf)
        plugins[name] = plugin

    #########################
    log.info("Loading Keys")
    #########################
    for keypressed, item in conf['keyboard'].items():
        keycode = getattr(pygame, f"K_{keypressed}")
        plugin = plugins[conf['keyboard'][keypressed]['handler']]

        keyboard.add_key_handler(
            keys=[keycode],
            button_up=True,
            handler=plugin.handler
        )

    # for name, item in conf['buttons'].items():
    #
    #     button = int(name)

    app = Main(
        joypad=joypad,
        keyboard=keyboard
    )
    log.info("Starting...")
    app.run()


