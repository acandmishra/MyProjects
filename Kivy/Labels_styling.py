import kivy
from  kivy.app import App
from kivy.uix.label import Label

class MyLabel(App):
    def build(self):
        label = Label(text="[u][b][i][color=ff0066]Hello World!![/color][/i][/b][/u]",markup=True,font_size="30")
        
        return label
MyLabel().run()