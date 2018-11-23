import kivy
kivy.require('1.0.7')

#The App itself
from kivy.app import App
#Connections to the KV file
from kivy.lang import Builder


#Manage JSON
import json

#.py file connections
import backend


#This class is used to define the app itself, and all its functions
class TestApp(App):

    


    #The build function is the app constructor
    def build(self):
        #Window Title
        self.title = "ACME MOVIE SEARCH"
        #Window contents
        self.root = Builder.load_file('pages_base.kv')
        return self.root


    #Find random movie function
    def findRandomMovie(self, button):
        a = backend.APIReqRandom("omdbapi")
        self.root.output_box.text = json.dumps(a, indent=4, separators=(',', ': '))
        print("I LIKE HOTDOGS!!")
        
        

    
    
    #Pass is a python command to identify stub functions
    pass





#This is the equivilant to the main function
if __name__ == '__main__':
    #This runs the application
    TestApp().run()









