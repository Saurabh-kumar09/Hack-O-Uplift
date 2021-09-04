
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer


# An App running a video file

class ConFeTalk(App):

    def build(self):
        self.player = VideoPlayer(source='VID-20210904-WA0021.mp4', state='play',
                                  options={'allow_stretch': True})

        return (self.player)


# Start the Video App

if __name__ == '__main__':
    ConFeTalk().run()
