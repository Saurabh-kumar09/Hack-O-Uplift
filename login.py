from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRoundFlatButton
from kivy.lang import Builder
from kivymd.uix.list import MDList, OneLineListItem
from kivy.core.window import Window
from info import username,user_Email,user_contact,set_password,confirm_password,label,idea,btn_v

Window.size = (400, 600)


class ConFeTalk(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        display = Screen()

        # icon_label = MDIcon(icon="android", halign="right")

        self.contact = Builder.load_string(user_contact)
        self.email = Builder.load_string(user_Email)
        self.pasd = Builder.load_string(set_password)
        self.cnpasd = Builder.load_string(confirm_password)
        self.naam = Builder.load_string(username)
        self.head = Builder.load_string(label)
        self.think = Builder.load_string(idea)
        self.click = Builder.load_string(btn_v)

        display.add_widget(self.click)
        display.add_widget(self.naam)
        display.add_widget(self.contact)
        display.add_widget(self.email)
        display.add_widget(self.pasd)
        display.add_widget(self.cnpasd)

        # display.add_widget(icon_label)
        display.add_widget(self.head)
        display.add_widget(self.think)

        return display

    def show_data(self, obj):
        print(self.naam.text)
        print(self.contact.text)
        print(self.email.text)
        print(self.pasd.text)
        print(self.cnpasd.text)


ConFeTalk().run()
