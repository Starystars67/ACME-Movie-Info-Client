import kivy

from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.scatter import Scatter

from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

import json

import backend

if __name__ == '__main__':
    root = FloatLayout()

    # Variables
    # This is the position of the top row of elements.
    topPosition = 0.9

    # Functions
    # Find a random movie
    def find_random_movie(*l):
        db = "omdbapi"
        a = backend.APIReqRandom(db)
        outputText.text = json.dumps(a, indent=4, separators=(',', ': '))

    # Goes through the database and finds all movies with the keywords entered.
    def find_movie(*l):
        db = "omdbapi"
        search_type = "s"  # s stands for search
        search_value = inputBox.text
        a = backend.APIReq(db, search_value, search_type)
        print(len(a))
        outputText.text = json.dumps(a, indent=4, separators=(',', ': '))

    # Elements
    # Find Random Movie Button
    rndButton = Button(
        text='Find random \nmovie',
        size_hint=(.16, .075),
        pos_hint={'x': 0.02, 'y': topPosition},
        halign='center',
        valign='center'
    )
    # Call Random Movie Button Function
    rndButton.bind(
        on_release=find_random_movie
    )

    # Top Search Bar
    inputBox = TextInput(
        size_hint=(0.5, 0.075),
        pos_hint={'x': .2, 'y': topPosition},
        height=100,
        font_size='22'
    )

    # Search Button - next to the Search Bar
    searchButton = Button(
        text='SEARCH',
        size_hint=(.1, .075),
        pos_hint={'x': .705, 'y': topPosition}
    )
    # Call Search button Function
    searchButton.bind(
        on_release=find_movie
    )

    # My List Button
    listButton = Button(
        text='MY LIST',
        size_hint=(.16, 0.075),
        pos_hint={'x': .82, 'y': topPosition}
    )

    # Output Text - this displays the searched information
    outputText = Label(
        text='Output here',
        size_hint_y=None,
        height=100,
        pos_hint={'top': .5},
        color=(0, 1, 0, 1),
        halign='center',
        valign='center'
    )

    root.add_widget(rndButton)
    root.add_widget(inputBox)
    root.add_widget(searchButton)
    root.add_widget(listButton)
    root.add_widget(outputText)

    runTouchApp(root)

# Useful Code

# # Find a random movie                 HERE JAMES CREATED THE 6 OBJECTS
# def findRandomMovie(*l):
#     for x in range(6):
#         ads = Button(
#             text='here',
#             size_hint=(.16, 0.075),
#             pos_hint={'x': (x/10), 'y': 1 - topPadding}
#         )
#         root.add_widget(ads)
