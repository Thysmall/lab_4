"""
Name: Guess the Number, Keep the Kids
Author: Jordan Betz
Description: Guess the number game where as you guess incorrect your wife builds the car and takes the kids.
Date: 2/4/26
Credits: ASCII art from: https://www.asciiart.eu/art/5e3d4e6de976abac
"""

import random

number: int = random.randint(1,15)
stage: int = -1
art: list[str] = [
    """
    
    
    
            (_)
    """,
    """
    
    
    
       (_)--(_) 
    """,  
    """
      
     ___________
    (   _    _ _\\
    =`-(_)--(_)-' 
    """,  
    """
      ______
     /|_||_\\`.__
    (   _    _ _\\
    =`-(_)--(_)-' 
    """,  
    """
      ______
     /|_||0\\`.__
    (   _    _ _\\
    =`-(_)--(_)-' 
    """,  
    """
      ______
     /|o||0\\`.__
    (   _    _ _\\
    =`-(_)--(_)-' 
    """    
]

print("Welcome to Guess the Number, Keep the Kids! Your wife is on her way out, but you want to keep your kids and they want to stay with you. She said if you can guess the right number, one through fifteen, you can keep them. Otherwise, they are gone.")

playing: bool = True
while playing:
    try:
        guess: int = int(input("Enter your guess: "))
        
        playing = False
    except:
        if ValueError: print("You must guess an integer.")      
    
    