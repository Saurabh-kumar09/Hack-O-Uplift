from kivy.app import App
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.core.window import Window

Window.size=(400,600)



class ConFeTalk(App):
    sound = SoundLoader.load('How To Talk_content-Audio.mp3')

    def build(self):
        return Label(text="Topic-How To Talk_Audio")

    if sound:
        sound.play()


ConFeTalk().run()
