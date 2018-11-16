from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.scatter import Scatter

from kivy.properties import StringProperty

from kivy.lang import Builder
from kivy.base import runTouchApp

import json

import backend

Builder.load_string('''
<RootWidget>:
    Button:
        pos: root.width * 0.5, root.height * 0.8
        size: root.width * 0.1, root.height * 0.08
        text: 'Find Random Movie'
        font_size: 12
        text_size: self.size
        text_align: 'center'
    rndButton:
        text: 'Find random \nmovie'
        size_hint: (.16, .075)
        pos_hint: {'x': 0.02, 'y': topPosition}
        align: 'center'
    inputBox:
        size_hint:(0.5, 0.075)
        pos_hint: {'x': .2, 'y': topPosition}
        height: 100
        font_size: '22'
    searchButton:
        text: 'SEARCH',
        size_hint: (.1, .075),
        pos_hint: {'x': .705, 'y': topPosition}
    listButton:
        text: 'MY LIST',
        size_hint: (.16, 0.075),
        pos_hint: {'x': .82, 'y': topPosition}
    outputText:
        text: 'Output here'
        size_hint_y: None
        height: 100
        pos_hint: {'top': .5}
        color: (0, 1, 0, 1)
        align: 'center'
''')


class RootWidget(FloatLayout):
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
    rndButton = Button()
    # Call Random Movie Button Function
    rndButton.bind(on_release=find_random_movie)

    # Top Search Bar
    inputBox = TextInput()

    # Search Button - next to the Search Bar
    searchButton = Button()
    # Call Search button Function
    searchButton.bind(on_release=find_movie)

    # My List Button
    listButton = Button()

    # Output Text - this displays the searched information
    outputText = Label()


runTouchApp(RootWidget())

# Useful Code

# In Class Widget
# def do_layout(self, *args):
#     number_of_children = len(self.children)
#     width = self.width
#     width_per_child = int(width / number_of_children)
#
#     positions = range(0, width, width_per_child)
#     for position, child in zip(positions, self.children):
#         child.height = self.height
#         child.x = self.x + position
#         child.y = self.y
#         child.width = width_per_child
#
#
# def on_size(self, *args):
#     self.do_layout()
#
#
# def on_pos(self, *args):
#     self.do_layout()
#
#
# def add_widget(self, widget):
#     super(RootWidget, self).add_widget(widget)
#     self.do_layout()
#
#
# def remove_widget(self, widget):
#     super(RootWidget, self).remove_widget(widget)
#     self.do_layout()

# Image:
# pos: root.width * 0.5, root.height * 0.8
# size: root.width * 0.08, root.height * 0.06
# source: 'colours.png'
# allow_stretch: False
# keep_ratio: False

