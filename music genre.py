#!/usr/bin/env python

import webbrowser
from random import choice
random_page_generator = ("https://youtu.be/xWqWxfMdqCQ","https://youtu.be/MMP5ao1KlZg","https://youtu.be/djYYb5y4aXA","https://youtu.be/djYYb5y4aXA")
webbrowser.open (choice(random_page_generator), new=3)

def main ():
    """ Start guessing a music genre."""
    print("Guess the music")

    x= ("kpop")
   
    guess = None

    while x != guess :
   
       guess =str(input("Guess music that you think:"))

       if x == guess :
          print("You genius!")

main ()