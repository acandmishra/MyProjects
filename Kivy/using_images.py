import kivy
from kivy.app import App
from kivy.uix.image import Image

class MyFirstImage (App):
    def build(self):
        return (Image(source="D:\Computer Practice\Programming\Kivy\Lovebirds.jpg"))

MyFirstImage().run()