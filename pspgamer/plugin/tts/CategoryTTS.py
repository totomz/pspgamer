import logging

from pspgamer.plugin.bose.SoundTouch import Plugin


class CategoryTTS(Plugin):
    """
    Raggruppa delle frasi in una o piu' categorie e permette di dire una frase con
    specificando una categoria

    Come funziona? con una struct
    [
        {struct}
    ]

    """

    def __init__(self):
        super().__init__()
        self.log = logging.getLogger("CategoryTTS")
        self.log.info("Loading class")

        # This stuff handles the list of pre-defined text messages
        # Struct contiene i messaggi delle categorie.
        # struct[0] Contiene il titolo della categoria
        # struct[1] Contiene l'elenco dei messaggi
        # struct[2] Contiene l'elenco dei messaggi che sto ciclando
        self.categories = list()
        self.categories_current = 0
        self.messages = {}

    def initialize(self, config: dict):
        self.log.info("Loading TTS messages")

        for category in config['categories']:
            print(category)
            self.categories.append(category)
            self.messages[category] = config['categories'][category]

    def handler(self, event):
        self.log.info("BOMBEEEER ")
        self.log.info(event)
