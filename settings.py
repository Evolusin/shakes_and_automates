import os

class Settings:
    def __init__(self):
            self.img_dir = 'img/'
            self.temp_names = []
            self.get_templates()

    def get_templates(self):
        for f in os.listdir(self.img_dir):
            self.temp_names.append(f)