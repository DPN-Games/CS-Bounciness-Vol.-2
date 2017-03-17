# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cs = Character("CS188")
define ct = Character("Craptop")
define d = Character("Discord")
define n = Character("Nova")
define ycs = Character("Young CS")

image csroom
image csdefault
image cshappy
image craptop1
image craptop2
image craptop3
image craptop4
image craptop5
image nova1


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg csroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show csdefault

    # These display lines of dialogue.

    cs "Welp, time to start up the ol' Craptop."

    show craptop1
	
    ct "Your PC sux. LOL."
    
    show craptop2
    
    Character("Sticky Note") "Delete the CS Discord."

    cs "Eh, maybe tomorrow"
    
    show craptop3
    
    ct "Downloading update 200/13."
    ct "Update complete"
    
    show cshappy
    
    cs "OoOoOoOoO yes!"
    
    show craptop4

    cs "Hey guys!"
    
    d "Hihihihihihihihihihi"
    
    cs "Okay bedtime! Bye guys!"

    show nova1 at right

    n "But it's like 8:04AM and you just woke up."

    show csdefault at left
    
    cs "Bye!"
    
    show craptop4

    d: "CS188 is now offline."
    
    show nova1
    
    n: "k bye"

    show csdefault
    
    cs "Alright, what source now?"
    
    show craptop5
    
    cs "Hmmm..."

    return
