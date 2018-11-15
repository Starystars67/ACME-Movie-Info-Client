import kivy
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.graphics import Color, Rectangle
import json

import backend

if __name__ == '__main__':

    root = FloatLayout()

    # Find a random movie
    def findRandomMovie(*l):
        db = "omdbapi"
        a = backend.APIReqRandom(db)
        #print(json.dumps(a, sort_keys=True, indent=4, separators=(',', ': ')))
        label.text = json.dumps(a, indent=4, separators=(',', ': '))


    # Find a movie
    def findMovie(*l):
        db = "omdbapi"
        searchtype = "s"
        searchval = inputBox.text
        a = backend.APIReq(db, searchval, searchtype)
        print(len(a))
        label.text = json.dumps(a, indent=4, separators=(',', ': '))
        #print(json.dumps(a, sort_keys=True, indent=4, separators=(',', ': ')))

    topPadding = .1




    # Define a button object and attach a script
    rndButton = Button(
        text='Find random \nmovie',
        size_hint=(.16, .075),
        pos_hint={'x': .02, 'y': 1-topPadding}
    )
    rndButton.bind(
        on_release=findRandomMovie
    )
    root.add_widget(rndButton)






    # Define Input box in top middle of screen
    inputBox = TextInput(
        size_hint=(0.5, 0.075),
        pos_hint={'x': .2, 'y': 1-topPadding},
        height=100,
        font_size='22'
    )
    root.add_widget(inputBox)




    # Define a button object and attach a script
    searchButton = Button(
        text='SEARCH',
        size_hint=(.1, .075),
        pos_hint={'x': .7, 'y': 1-topPadding}
    )
    searchButton.bind(
        on_release=findMovie
    )
    root.add_widget(searchButton)




    # Define a button object and attach a script
    listButton = Button(
        text='MY LIST',
        size_hint=(.16, 0.075),
        pos_hint={'x': .82, 'y': 1-topPadding}
    )
    listButton.bind(
        on_release=findRandomMovie
    )
    root.add_widget(listButton)





    # Define Textbox at top of Window
    labelText = 'Search for Output'
    label = Label(
        text=labelText,
        size_hint_y=None,
        height=100,
        pos_hint={'top': .5},
        color=(0, 1, 0, 1),
        halign = 'center',
        valign = 'center'
    )
    root.add_widget(label)

    runTouchApp(root)

