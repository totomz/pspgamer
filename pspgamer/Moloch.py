import pygame
import logging
import toml
from pspgamer.controllers.Joypad import JoypadController, MarsJoypad
from pspgamer.test.Speecher import Speecher


class Main:
    def __init__(self, joypad: JoypadController):
        self.joypad = joypad
        self.log = logging.getLogger("Main")

    def run(self):
        self.log.info("Staring...")
        pygame.init()

        ###################
        # Main Event Loop #
        ###################
        done = False
        while not done:
            # for event in pygame.event.get():
            event = pygame.event.wait()

            if event.type == pygame.QUIT: # If user clicked close.
                done = True # Flag that we are done so we exit this loop.

            elif event.type == pygame.JOYBUTTONDOWN:
                self.joypad.handle_event_button_down(event=event)

            elif event.type == pygame.JOYBUTTONUP:
                self.joypad.handle_event_button_up(event=event)

            elif event.type == pygame.JOYAXISMOTION:
                self.joypad.handle_event_axis_motion(event=event)


if __name__ == "__main__":

    log = logging.getLogger("main")

    conf = toml.load('./default.toml')
    print(conf)

    # Initializing controllers
    joypad = MarsJoypad()
    tts = Speecher()

    # This stuff handles the list of pre-defined text messages
    # Struct contiene i messaggi delle categorie.
    # struct[0] Contiene il titolo della categoria
    # struct[1] Contiene l'elenco dei messaggi
    # struct[2] Contiene l'elenco dei messaggi che sto ciclando
    struct = {-1: -1}

    def click_struct_ctts(voice):
        def handler(event):
            last_category = struct[-1]
            button = event.button

            if button != last_category:
                # Ho premuto questo pulsante per la prima volta
                # Il messaggio e' il primo elemento della prima lista.
                # Copio la lista originale nella seconda posizione, che li la ciclero'
                message = struct[button][0]
                struct[button][2] = struct[button][1].copy()
            else:
                # Sto ciclando la lista
                message = struct[button][2].pop(0)
                struct[button][2].append(message)

            tts.say(message=message, voice=voice)
            struct[-1] = button
        return handler

    def say_struct(btn, voice):

        def inner(evnt):
            message = struct[btn][2][-1]
            tts.say(message=f"DICO: {message}", voice=voice)
        return inner

    ############################
    log.info("Loading Buttons")
    ############################

    for name, item in conf['buttons'].items():

        button = int(name)

        if item['type'] == "tts":
            struct[button] = [item['name'], item['options'], item['name']]
            joypad.add_button_handler(
                buttons=[button],
                button_up=True,
                handler=click_struct_ctts(voice=conf['language']['voice'])
            )

            joypad.add_button_handler(
                buttons=[int(item['activator'])],
                button_up=True,
                handler=say_struct(btn=button, voice=conf['language']['voice'])
            )

        elif item['type'].startswith("pspgamer.plugin."):
            print("dio")
            module_name = item['type']
            class_name = "Plugin"

            log.info(f"Loading {module_name}.{class_name}")

            module = __import__(module_name, fromlist=[class_name])
            my_class = getattr(module, class_name)
            instance = my_class()

            log.info("E mo che bindo allinstance?")

        else:
            log.warning(f"Invalid type [{item['type']} for button {button} - ignoring")
            continue

    app = Main(joypad=joypad)
    log.info("Inizio")
    app.run()


