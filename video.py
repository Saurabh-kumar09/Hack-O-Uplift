#Content-->Video Tutorial-->How to introduce yourself
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer


class ConFeTalk(App):

    def build(self):
        self.player = VideoPlayer(source='How To Introduce Yourself_Content- video.mp4', state='play',
                                  options={'allow_stretch': True})

        return (self.player)


# Start the Video tutorial

if __name__ == '__main__':
    ConFeTalk().run()
