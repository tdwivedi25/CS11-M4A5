# Two ASCII art pieces stored as multiline strings

cat_art = """
 /\_/\  
( o.o ) 
 > ^ <
"""

dragon_art = """
           / \\  //\\
     |\\___/|      \\
    /       \\     //
   |  /\\ /\\  |   //
   \\_\\ ° °  /_//
     /   *   \\
     \\__\\_/__/
"""

# Ask the user which art they want to see
choice = input("Type 'cat' or 'dragon' to see some ASCII art: ").strip().lower()

if choice == "cat":
    print(cat_art)
else:
    print(dragon_art)

