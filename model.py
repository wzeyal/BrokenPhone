import random


class Model:
    def __init__(self):
        self.text = ""
        self.image = None

    def update_text(self, text):
        self.text = text

    def update_image(self, image):
        self.image = image
