#Variable decleration.

#Characters.
define cs = Character("CS188")
define ct = Character("Craptop")
define d = Character("Discord")
define n = Character("Nova")
define ycs = Character("Young CS")
define mr = Character("Micheal Rosen")
define cg = Character("Car Guy")

#Backgrounds.
image csroom
image csroom_window
image outside
image cscaroutside
image cscarinside
image walmartinside
image walmartoutside

#Character images.
image csdefault
image cshappy
image csscared
image craptop1
image craptop2
image craptop3
image craptop4
image craptop5
image nova1
image carguy

#Sounds.
#Voices.


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
    
    cs: "Okay, what to do now?"
    cs: "I could go outside, look at some flowers..."
    
    scene csroom_window
    
    cs: "Oh, look out the window, there's a Micheal Rosen!"
    cs: "Yeah, let's go outside."
    
    scene outside
    
    show cshappy
    
    cs: "Nice day!"
    cs: "Well, I guess it's car time."
    
    scene cscaroutside
    
    show carguy at right
    
    cg: "*walks up* Nice car!"
    
    show csdefault at left
    
    cs: "It's pretty nice, but it's got some scratches."
    
    show carguy at right
    
    cg: "Nooot so nice scratch..."
    cg: "You should try Crotch Doctor!"
    
    show csscared at left
    
    cs: "OH GOD AN ADVERTISER!"
    cs: "QUICK START THE CAR! START THE CAR!"

    scene cscarinside
    
    show csdefault
    
    
    
    cs "Alright, what source now?"
    
    show craptop5
    
    cs "Hmmm..."

    return
