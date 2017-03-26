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
image csroom = "background/Cs_bedroom1.jpg"
image csroom_night = "background/Cs_bedroom3.jpg"
image csroom_window = "background/Cs_bedroom2.jpg"
image outside = "background/Cs_house.jpg"
image cscaroutside = "background/Car_Driveway.jpg"
image cscarinside = "background/Car_Inside.jpg"
image walmartinside = "background/Walmart_Inside.jpg"
image walmartcheckout = "background/Walmart_checkout.jpg"
image walmartoutside = "background/Walmart_Outside.jpg"
image walmartshelf = "background/Walmart_shelf.jpg"
image cardealer = "background/CarDealer.jpg"
image craptop1 = "background/Craptop_error.jpg"
image craptop2 = "background/Craptop_Desktop.png"
image craptop3 = "background/Craptop_Updating.jpg"
image craptop4 = "background/Craptop_Desktop.png"
image craptop5 = "background/Craptop_Youtube.jpg"

#Character images.
image csdefault = "characters/Cshocola.png"
image cshappy = "characters/csocola_happy.png"
image csscared = "characters/cs-ocola suprised.png"
image nova1 = "characters/Anime nova.png"
image carguy = "characters/Carguy_anime.png"
image discord = "characters/discord.png"

#Sounds.
#Voices.


# The game starts here.

label start:

    scene csroom

    show csdefault

    cs "Welp, time to start up the ol' Craptop."

    scene craptop1
    show csdefault
    ct "Your PC sux. lol."
    
    scene craptop2
    show csdefault
    Character("Sticky Note") "Delete the CS Discord."
    cs "Eh, maybe tomorrow"
    
    scene craptop3
    
    show csdefault
    ct "Downloading update 200/13."
    show csdefault
    ct "Update complete"
    hide csdefault
    show cshappy
    
    cs "OoOoOoOoO yes!"
    
    scene craptop4

    cs "Hey guys!"
    
    show discord
    d "Hihihihihihihihihihi"
    hide discord
    show csdefault
    cs "Okay bedtime! Bye guys!"
    hide csdefault
    show nova1 at right

    n "But it's like 804AM and you just woke up."

    show csdefault at left
    
    cs "Bye!"
    
    scene craptop4
    
    show discord
    d "CS188 is now offline."
    
    show nova1 
    
    n "k bye"

    scene csroom

    show csdefault at truecenter
    
    cs "Okay, what to do now?"
    cs "I could go outside, look at some flowers..."
    
    scene csroom_window
    
    cs "Oh, look out the window, there's a Micheal Rosen!"
    cs "Yeah, let's go outside."
    
    scene outside
    
    show cshappy
    
    cs "Nice day!"
    cs "Well, I guess it's car time."
    
    scene cscaroutside
    
    show carguy at right
    
    cg "*walks up* Nice car!"
    
    show csdefault at left
    
    cs "It's pretty nice, but it's got some scratches."
    
    show carguy at right
    
    cg "Nooot so nice scratch..."
    cg "You should try Crotch Doctor!"
    
    show csscared at left
    
    cs "OH GOD AN ADVERTISER!"
    cs "QUICK START THE CAR! START THE CAR!"

    scene cscarinside
    
    show csdefault at ycenter
    
    
    
    cs "Alright, what source now?"
    
    scene craptop5

    show csdefault
    
    cs "Hmmm..."

    return
