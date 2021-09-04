from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRaisedButton
from kivy.core.audio import SoundLoader
from link import bvc

Window.size = (400, 600)


class ConFeTalk(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightBlue"
        return Builder.load_string(bvc)


ConFeTalk().run()
