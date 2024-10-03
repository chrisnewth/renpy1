# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    $ refuse_drink = False
    $ drank_tea = False

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Would you like a drink?"

    

    # test branching

menu:

    "What shall I choose"

    "option 1":

        "You chose option 1"


    "option 2":
        "You chose option 2"



menu:
     "What should I do (testing commits 2)?"

     "Drink coffee.":
         "I drink the coffee, and it's good to the last drop, but I sense it was the wrong choice."

     "Drink tea.":
         $ drank_tea = True
         "I drink the tea, trying not to be smug that I've chosen the correct drink."

     "Refuse to drink.":
         $ refuse_drink = True
         jump ending

label after_menu:

     "After having my drink, I got on with my morning but couldn't decide where to go."
menu:
    "Go left.":
        "You chose the wrong direction and/or the wrong drink'"
        
    "Go right.":
        "You chose the wrong direction and/or the wrong drink"
        
    "Go down the stairs." if drank_tea:
        "Drinking tea and heading down the stairs is correct - Well done '"

label ending:
    if refuse_drink:
        "As you refused to drink, you are dehydrated and must exit the game - Bye"
    else:
        "The end."
return
