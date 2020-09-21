import logging

import boto3
import boto3
from dotenv import load_dotenv
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import pygame
import subprocess
from tempfile import gettempdir
import base64
import pathlib

load_dotenv()

logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])


class Speecher:
    def __init__(self):
        self.polly = boto3.client('polly')
        self.speachdir = "/Users/totomz/Documents/totomz/pspgamer/speech"
        self.log = logging.getLogger("Speecher")

    def message_to_file(self, language="it-IT", message="", voice="Giorgio"):
        filename = base64.b32encode(f"{voice}-{message}".encode()).decode("ascii")
        filepath = os.path.join(self.speachdir, filename)
        return filename, filepath

    def preload(self, message, voice="Giorgio",  lang="it-IT"):

        filename, filepath = self.message_to_file(message=message, voice=voice)
        p = pathlib.Path(filepath)

        if p.is_file():
            self.log.info("File already loaded")
            return filepath

        response = self.polly.synthesize_speech(
            Engine="standard",
            LanguageCode=lang,
            OutputFormat="ogg_vorbis",
            Text=message,
            VoiceId=voice   # Giorgio, Bianca, Carla
        )

        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                try:
                    with open(filepath, "wb") as file:
                        file.write(stream.read())
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)

        return filepath

    def say(self, message="", voice="Giorgio", lang="it-IT"):
        filepath = self.preload(message=message, voice=voice)
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()
        pygame.event.wait()


# polly = Speecher()
# polly.preload(message="Ciao Daria, come stai?")
#
# print("fine")
