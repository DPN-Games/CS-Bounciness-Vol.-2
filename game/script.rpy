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
image walmartoutside = "background/Walmart_Outside.png"
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

    show csdefault at left

    cs "Welp, time to start up the ol' Craptop."

    scene craptop1
    show csdefault at left
    ct "Your PC sux. lol."
    
    scene craptop2
    show csdefault at left
    Character("Sticky Note") "Delete the CS Discord."
    cs "Eh, maybe tomorrow"
    
    scene craptop3
    show csdefault at left
    ct "Downloading update 200/13."
    show csdefault at left
    ct "Update complete"
    hide csdefault at left
    show cshappy at left
    cs "OoOoOoOoO yes!"
    hide cshappy
    show csdefault at left
    #full windows sound
    ct "{i}please end my suffering{/i}"
    cs "no"
   
    scene craptop4
    show csdefault at left
    cs "Hey guys!"
    scene craptop2
    show discord
    d "Hihihihihihihihihihi"
    hide discord
    show csdefault at left
    cs "Okay bedtime! Bye guys!"
    hide csdefault
    show nova1 at right
    n "But it's like 8:04AM and you just woke up."
    hide nova1
    show csdefault at left
    cs "Bye!"
    hide csdefault

    scene craptop4
    show discord
    d "CS188 is now offline."
    hide discord
    show nova1 
    n "k bye"

    scene csroom
    show csdefault at truecenter
    cs "Okay, what to do now?"
    cs "I could go outside, look at some flowers..."
    
    scene csroom_window
    show csscared
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
    hide csdefault
    show csscared at left
    cs "OH GOD AN ADVERTISER!"
    cs "QUICK START THE CAR! START THE CAR!"

    scene cscarinside
    show csdefault
    cs "Whew, that was close."
    cs "Should I go get groceries?"

    menu grocerymenu:
        "Get groceries?"

        "Yes.":
            cs "Yeah, it's a good idea to get some stuff."
        "No.":
            cs "Screw you, I'm going anyway."

    scene walmartoutside
    show cshappy
    cs "Oh yes, CSMart is open!"

    scene walmartinside
    show csdefault
    cs "*pop* Noice! Genergy is on sale! I'll just grab them all."
    cs "2 for 1 on Capri Sus? Nah, not worth my time."


    return
