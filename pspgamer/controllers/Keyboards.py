
class KeyboardController:

    def __init__(self):
        self.handlers_up = dict()
        self.handlers_down = dict()

    def handle_event_key_down(self, event):
        pass

    def handle_event_key_up(self, event):
        pass

    def add_key_handler(self, keys: list, handler: callable = None, button_up=False):
        for key in keys:
            if button_up:
                handlers = self.handlers_up.get(key, list())
                handlers.append(handler)
                self.handlers_up[key] = handlers
            else:
                handlers = self.handlers_down.get(key, list())
                handlers.append(handler)
                self.handlers_down[key] = handlers


class ThreePedalKeyboard(KeyboardController):

    def __init__(self):
        super().__init__()

    def handle_event_key_down(self, event):
        print("DOWN DOWN DOWN")

    def handle_event_key_up(self, event):
        print("UP UP UP")
