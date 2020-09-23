import logging
import pygame


def noop(event):
    pass


class JoypadController:

    def handle_event_button_down(self, event):
        pass

    def handle_event_button_up(self, event):
        pass

    def handle_event_axis_motion(self, event):
        pass


class MarsJoypad(JoypadController):

    def __init__(self):
        self.log = logging.getLogger("MarsJoypad")

        self.log.debug("Initializing MARS Joypad")
        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        self.joystick = joysticks[0]
        self.joystick.init()

        self.log.info(f"Found Joypad: {self.joystick.get_name()}")

        self.handlers_up = dict()
        self.handlers_down = dict()

    def add_button_handler(self, buttons: list, handler: callable = None, button_up=False):
        for button in buttons:
            if button_up:
                handlers = self.handlers_up.get(button, list())
                handlers.append(handler)
                self.handlers_up[button] = handler
            else:
                self.handlers_down[button] = handler

    def handle_event_button_down(self, event):
        func = self.handlers_down.get(event.button, noop)
        func(event)

    def handle_event_button_up(self, event):
        func = self.handlers_up.get(event.button, noop)
        func(event)

    def handle_event_axis_motion(self, event):
        print("TODO")

