import logging
import sys

from pspgamer.controllers.Joypad import MarsJoypad
from pspgamer.Moloch import Main

logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler(sys.stdout)])

log = logging.getLogger("JoypadTester")

struct = {}

struct[4] = ["Bottone 4", ["4 uno", "4 due"], ["4 uno", "4 due"]]
struct[6] = ["Bottone 6", ["6 uno", "6 due"], ["6 uno", "6 due"]]
struct[-1] = 0


def printmsg(event):
    # log.info(f"{event.button} pressed and released")
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

    print(f"message: {message}")
    struct[-1] = button


# Initialize the  Joypad Controller


joypad = MarsJoypad()
joypad.add_button_handler(
    buttons=list(range(0, 50)),
    button_up=True,
    handler=printmsg
)


app = Main(
    joypad=joypad
)

log.info("Inizio")
print(" ")
print(" ")
print(" ")
app.run()


