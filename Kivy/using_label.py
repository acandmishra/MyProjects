import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyFirstApp(App):   # we used inheritance here   
	def build(self):
            return Label(text="hello world") 
MyFirstApp().run()
# To build the application, we have to return a widget on the build() function. 
# In the code above, we have returned a label with the text “Hello World”.
