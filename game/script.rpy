#Variable decleration.

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

    scene csroom

    show csdefault

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
