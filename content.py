from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, OneLineListItem, TwoLineListItem
from kivy.lang import Builder
from info import content_section
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Window.size = (400, 600)


class ConFeTalk(MDApp):
    def build(self):
        return Builder.load_string(content_section)


ConFeTalk().run()
