import kivy 
from kivy.app import App
from kivy.properties import StringProperty , BooleanProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout


class WidgetsExample(GridLayout):
    count = 1
    # my_text3 = StringProperty("Slide")
    my_text = StringProperty("Hello!")
    my_text2 = StringProperty("Toggle")
    status = BooleanProperty(False)
    string = StringProperty(" ")
    

    def On_Toggle_Button(self,widget):
        print("state of the button is:"+ widget.state)
        if(widget.state == "down"):
            self.my_text2 = "ON"
            self.status = True
        else:
            self.my_text2 = "OFF"
            self.status = False
        
    def On_Button_Press(self):
        if(self.status == True):
            print("Button Clicked !!")
            self.my_text = str(self.count)
            self.count += 1

    def On_Switch(self,widget):
        print("Switch:"+str(widget.active))
    
    def On_Slider_Movement(self,widget):
        print("slider value:"+str(int(widget.value)))
        # self.my_text3=str(int(widget.value))

    def on_text_validate(self,widget):
        self.string = widget.text
            
  

    
class StackLayoutEample(StackLayout):
    pass
# Pls understand stack layout !!

class GridLayoutExample(GridLayout):    # Read the note in kivy file !!
    pass
class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self,**kwargs):        # Here kwargs is not used but is required for internal working of the kivy
    #     super().__init__(**kwargs)
    #     # self.orientation = "vertical"
    #     b1=Button(text="hello")
    #     b2=Button(text="bye")
    #     b3=Button(text="Tata")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
        
class MainWidget(Widget):
    pass 
class TheLabApp(App): 
    pass
class CanvasExample1(Widget):
    pass
class CanvasExample2(Widget):
    pass
class CanvasExample3(Widget):
    pass
class CanvasExample4(Widget):
    pass
TheLabApp().run()