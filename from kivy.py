from kivy.app import App
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        btn=Button(text="click me!")
        btn.bind(on_press=self.on_button_click)
        return btn   
    def on_button_click(self,instance):
        instance.text="clicked" 
if __name__=="__main__":
        MyApp().run()