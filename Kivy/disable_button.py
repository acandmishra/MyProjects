import kivy
from kivy.app import App
from kivy.uix.button import Button
from functools import partial

class MyApp (App):
    def disable(self,obj,xyz):
        obj.disabled =True
    def update(self,obj,xyz):
        obj.text="diabled"
    def build(self):
        button = Button(text="Print",size_hint=(0.2,0.2),
        font_size="20sp",pos_hint={"x":0.4 , "y":0.4}) # herde self refers to the class in the the method the defined
        button.bind(on_press=self.click) #bind() is used to bind to bind button with functon
        button.bind(on_press=partial(self.disable,button)) #partial is used to pass the args to the function written inside it 
        button.bind(on_press=partial(self.update,button))
        return button
    def click(self,element):
        print("hello World!!")
MyApp().run()