import logging

import pygame

from pspgamer.plugin.bose.SoundTouch import Plugin


class CategoryTTS(Plugin):

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

        self.k_select = "None"
        self.k_action = "None"

    def initialize(self, config: dict):
        self.log.info("Loading TTS messages")

        self.k_select = config['k_select']
        self.k_action = config['k_action']

        for category in config['categories']:
            print(category)
            self.categories.append(category)
            self.messages[category] = config['categories'][category]

            # self.categorykey = getattr(pygame, self.k_select)

    def handler(self, event):
        if event.key == getattr(pygame, self.k_select):
            '''
            self.categories is a list of categories. 
            The "currently selected category" is always at self.categories[0]
            When I need ot cycle over the categories, we just pop the first item and push it at the bottom of the list
            '''
            next_category = self.categories.pop(0)
            self.categories.append(next_category)
            self.say(self.categories[0])

        elif event.key == getattr(pygame, self.k_action):
            print("Dico qualcosa")

    def say(self, message, ):
        print(f"===> ${message}")

