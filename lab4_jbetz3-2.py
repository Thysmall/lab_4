"""
Name: Guess the Number, Keep the Kids
Author: Jordan Betz
Description: Guess the number game where as you guess incorrect your wife builds the car and takes the kids.
Date: 2/4/26
Credits: ASCII car art from: https://www.asciiart.eu/art/5e3d4e6de976abac
"""

import random

number: int = random.randint(1,15)
stage: int = 0
names: list[str] = ["Jimmy", "Timmy", "Jacob", "Tobias", "Gerard", "Nathan", "Steve", "Lucy", "Carmen", "Stacy", "Alex", "Jenny"]
kid_1: str = names.pop(random.randint(0,len(names)))
kid_2: str = names.pop(random.randint(0,len(names)))
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
    """,
    f"""
    {kid_1} & {kid_2}
         \\O/   
      \\o/ | \\o/
       |  |  |
       ^  ^  ^
    """    
]

print("Welcome to Guess the Number, Keep the Kids! Your wife is on her way out, but you want to keep your kids and they want to stay with you. She said if you can guess the right number, one through fifteen, you can keep them. Otherwise, they are gone.")

playing: bool = True
while playing:
    try:
        guess: int = int(input("Enter your guess: "))
        
        if guess == number:
            print("You guessed correct! You get to keep the kids!")
            print(art[6])
            playing = False
            break
        if guess < number:
            print(f"Thats not it. ({kid_1} says its higher)")
            print(art[stage])
        if guess > number:
            print(f"Thats not it. ({kid_2} says its lower)")
            print(art[stage])
        stage += 1
        if stage > 5:
            print("You lost! Your wife took the kids.")
            playing = False
        
    except:
        if ValueError: print("You must guess an integer.")      
    
    