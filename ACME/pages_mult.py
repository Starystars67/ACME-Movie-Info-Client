import kivy
kivy.require('1.8.0')

#The App itself
from kivy.app import App
#Connections to the KV file
from kivy.lang import Builder
#Multiple page management systems
from kivy.uix.screenmanager import ScreenManager, Screen

#Manage JSON
import json

#.py file connections
import backend


#Load the KV file
Builder.load_file('pages_mult.kv')



class MainScreen(Screen):
    pass

class WishList(Screen):
    pass



sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(WishList(name='wishlist'))



#This class is used to define the app itself, and all its functions
class TestApp(App):


    #The build function is the app constructor
    def build(self):
        return sm

    #Find random movie function
    def findRandomMovie(self, button):
        a = backend.APIReqRandom("omdbapi")
        #self.root.output_box.text = json.dumps(a, indent=4, separators=(',', ': '))
        print(sm.current) 
        #sm.switch_to(wishlist, direction='left')
        print("I LIKE HOTDOGS!!")





#This is the equivilant to the main function
if __name__ == '__main__':
    #This runs the application
    TestApp().run()









