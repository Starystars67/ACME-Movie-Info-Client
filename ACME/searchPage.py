import kivy
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.graphics import Color, Rectangle
from kivy.uix.scatter import Scatter
import json

import backend

if __name__ == '__main__':
    root = FloatLayout()





    # # Find a random movie                 HERE JAMES CREATED THE 6 OBJECTS
    # def findRandomMovie(*l):
    #     for x in range(6):
    #         ads = Button(
    #             text='here',
    #             size_hint=(.16, 0.075),
    #             pos_hint={'x': (x/10), 'y': 1 - topPadding}
    #         )
    #         root.add_widget(ads)








    # Find a random movie
    def findRandomMovie(*l):
        db = "omdbapi"
        a = backend.APIReqRandom(db)
        # print(json.dumps(a, sort_keys=True, indent=4, separators=(',', ': ')))
        label.text = json.dumps(a, indent=4, separators=(',', ': '))

    # Define a button object and attach a script
    topPadding = .1  # just test here with the padding
    rndButton = Button(
        text='Find random \nmovie',
        size_hint=(.16, .075),
        pos_hint={'x': .02, 'y': 1-topPadding}
    )
    rndButton.bind(
        on_release=findRandomMovie
    )
    root.add_widget(rndButton)

    # Search label
    def findMovie(*l):
        db = "omdbapi"
        searchtype = "s"# s stands for search
        searchval = inputBox.text
        a = backend.APIReq(db, searchval, searchtype)
        print(len(a))
        label.text = json.dumps(a, indent=4, separators=(',', ': '))
        #print(json.dumps(a, sort_keys=True, indent=4, separators=(',', ': ')))



    # Define Input box in top middle of screen , this is for the search label
    inputBox = TextInput(
        size_hint=(0.5, 0.075),
        pos_hint={'x': .2, 'y': 1-topPadding},
        height=100,
        font_size='22'
    )
    root.add_widget(inputBox)

    # Define a button object and attach a script, this searches through OMDBapi
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
    # listButton.bind(
    #     on_release=findRandomMovie   # add function to open mylist page
    # )
    root.add_widget(listButton)

    # Define Textbox at top of Window
    labelText = 'Output here' # this displays the searched information
    label = Label(
        text=labelText,
        size_hint_y=None,
        height=100,
        pos_hint={'top': .5},
        color=(0, 1, 0, 1),
        halign='center',
        valign='center'
    )
    root.add_widget(label)
    runTouchApp(root)


