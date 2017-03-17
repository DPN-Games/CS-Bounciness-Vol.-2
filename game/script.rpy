# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cs = Character("CS188")
define ct = Character("Craptop")
define d = Character("Discord")
define n = Character("Nova")
define ycs = Character("Young CS")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg csroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show cs default

    # These display lines of dialogue.

    cs "Welp, time to start up the ol' Craptop."

	show craptop1
	
	ct "Your PC sux. LOL."

    return
