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
image csroom = "images/background/Cs_bedroom1.jpg"
image csroom_night = "images/background/Cs_bedroom3.jpg"
image csroom_window = "images/background/Cs_bedroom2.jpg"
image outside = "images/background/Cs_house.jpg"
image cscaroutside = "images/background/Car_Driveway.jpg"
image cscarinside = "images/background/Car_Inside.jpg"
image walmartinside = "images/background/Walmart_Inside.jpg"
image walmartcheckout = "images/background/Walmart_checkout.jpg"
image walmartoutside = "images/background/Walmart_Outside.jpg"
image walmartshelf = "images/background/Walmart_shelf.jpg"
image cardealer = "images/background/CarDealer.jpg"
image craptop1
image craptop2
image craptop3
image craptop4
image craptop5

#Character images.
image csdefault = "images/characters/Cshocola.png"
image cshappy = "images/characters/"
image csscared

image nova1
image carguy

#Sounds.
#Voices.


# The game starts here.

label start:

    scene csroom

    show csdefault

    cs "Welp, time to start up the ol' Craptop."

    scene craptop1
    
    ct "Your PC sux. lol."
    
    scene craptop2
    
    Character("Sticky Note") "Delete the CS Discord."
    cs "Eh, maybe tomorrow"
    
    scene craptop3
    
    ct "Downloading update 200/13."
    ct "Update complete"
    
    show cshappy
    
    cs "OoOoOoOoO yes!"
    
    scene craptop4

    cs "Hey guys!"
    d "Hihihihihihihihihihi"
    cs "Okay bedtime! Bye guys!"

    show nova1 at right

    n "But it's like 8:04AM and you just woke up."

    show csdefault at left
    
    cs "Bye!"
    
    scene craptop4

    d: "CS188 is now offline."
    
    show nova1
    
    n: "k bye"
	
	scene csroom

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
    
    scene craptop5
	
	show csdefault
    
    cs "Hmmm..."

    return
