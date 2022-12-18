import kivy
from kivy.app import App
from kivy.uix.button import Button


class Button1(App):
    def build(self):
        button = Button(text="print",size_hint=(0.2,0.2),font_size="30sp",
                        background_color=(2,5,2,1),pos_hint={"x":0.5,"y":0.5})
        button.bind(on_press=self.click)
        return button
    def click(self,event):
        print("hello world!!")
        
        
Button1().run()