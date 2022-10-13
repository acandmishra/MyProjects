from webbrowser import BackgroundBrowser
import kivy
from kivy.app import App
from kivy.uix.button import Button

class MyFirstbutton(App):
    def build(self):
        return (Button(text="Enter",size_hint=(0.2,0.2),font_size="20sp",
        pos_hint={"center_x":0.5,"center_y":0.5},
        background_color=(3,2,1,1)))
MyFirstbutton().run()