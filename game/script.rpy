#Variable decleration.

#Characters.
define cs = Character("CS188")
define ct = Character("Craptop")
define d = Character("Discord")
define n = Character("Nova")
define ycs = Character("Young CS")
define mr = Character("Micheal Rosen")
define cg = Character("Car Guy")
define ed = Character("Ed")
define rich = Character("Richard")
define wes = Character("Wesley")
define bill = Character("Billy Mays")

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
image craptopsad = "background/Craptop_sad.jpg"
image doorclosed = "background/Door_closed.jpg"
image dooropen = "background/Door_open.jpg"
image office1 = "background/Office_1.jpg"
image rosenhouse = "background/rosenhouse.jpg"


#Character images.
image csdefault = "characters/Cshocola.png"
image cshappy = "characters/csocola_happy.png"
image csscared = "characters/cs-ocola suprised.png"
image nova1 = "characters/Anime nova.png"
image carguy = "characters/Carguy_anime.png"
image discord = "characters/discord.png"
image youngcs = "characters/Csocola_young(chibi).png"
image wesley = "characters/wesley-chan.png"
image edimg = "characters/Ed.png"
image richard = "characters/Richard.png"
image digi = "characters/DuncanBig.png"
image billy = "characters/Billy_anime.png"
image michael = "characters/Michael.png"
image csphone = "characters/CshocolaPhone.png"


# The game starts here.

label start:
    scene csroom
    
    $ renpy.movie_cutscene("introHD.ogv")
    
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
    scene craptop
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
    show csdefault at left
    cs "Okay, what to do now?"
    cs "I could go outside, look at some flowers..."
    
    scene csroom_window
    show csscared
    cs "Oh, look out the window, there's a Micheal Rosen!"
    cs "Yeah, let's go outside."
    
    scene outside
    show cshappy at left
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
    show csdefault at left
    cs "Whew, that was close."
    cs "Should I go get groceries?"

    menu grocerymenu:
        "Get groceries?"

        "Yes.":
            cs "Yeah, it's a good idea to get some stuff."
        "No.":
            cs "Screw you, I'm going anyway."

    scene walmartoutside
    show cshappy at right
    cs "Oh yes, CSMart is open!"

    scene walmartshelf
    show csdefault at left
    cs "*pop* Noice! Genergy is on sale! I'll just grab them all."
    cs "2 for 1 on Capri Sus? Nah, not worth my time."

    scene csroom
    
    show text "1 HOUR LATER" at truecenter
    
    show csdefault at left
    cs "Computer time!"

    scene craptop5
    show csdefault at left
    cs "*sigh* I guess it's YTP time. What source now?"
    cs "*scrolls through youtube*"
    cs "Hmm, 'We WiLl AlL DiE EvEnTuAlLy LoL BY ohmanmycontent'..."
    cs "k"
    cs "I guess that works."
    cs "Time for ClipConverter.cs!"
    cs "Now for Premiere. Man, it was so easy back then, just WMM and some effects. If only that was now."
    cs "Oh look, a flashback. What a coincidence..."
    hide csdefault
    "hey flashback time"
    
    scene csroom with irisin
    show youngcs
    ycs "Hey guys, Young CS here. Today I'm gonna be editing a new craAaAaAaAaAaAazy video!"
    "*keyboard tapping*"
    ycs "Ohhhhhh YeEeEeEeEess! This is lookin' good!"
    hide youngcs
    
    scene csroom with irisout
    show csdefault at left
    cs "Oh. Flashback over."
    cs "Oh wow, hahahaha, this is funny already, hahaha, I have no friends."
    show csdefault at right
    cs "Woah. This house has felt like it was sitting with a giant rock on the side of the house."
    cs "I really need to get some foundation repair on this house."
    cs "Better call HoH SiS!"
    cs "They are really good at giving me the JoJ!"
    hide csdefault
    show csphone at left
    cs "{i} Dials 1-188-HOH-SISS{/i}"
    cs "Hello, can you give me the JoJ?"
    
    Character("HoH SiS Operator") "Is this a prank caller on the line?"
    cs "No! My house really needs foundation repair and I need help!"
    "HoH SiS operator" "Alright, that will be 200 CStars. You can pay us afterwards."
    "HoH SiS operator" "{i}hangs up{/i}"
    show text "..." at truecenter
    cs "Well, that is one thing taken care of."
    cs "I guess I'll work on my new YTP while I wait."
    "{i}Time Passes{/i}"
    "{i}Doorbell Rings{/i}"
    cs "Oh! They're here!"
    cs "Lemme go get the door"
    scene dooropen
    show csdefault at left
    cs "Hello! I am CS188, and I-"
    show edimg at right
    ed "Alright, that will be 200 cstars."
    cs "Alright, lemme get my wallet."
    cs "Here you go"
    ed "You want the JoJ!"
    hide csdefault
    "{i}CS leaves{/i}"
    ed "Come on in guys. CS left."
    hide edimg
    show richard at right
    rich "JoJ!"
    show wesley at left
    hide richard
    wes "Do we have to do this all over again?"
    show edimg at right
    ed "So now we are here, what should we do to him?"
    "Ed, Wesley and Richard" "Hmmm..."
    ed "Let's go check his room"
    "{i} The three HoH SiS workers go upstairs {/i}"
    scene csroom
    show wesley at right
    wes "Wow, I didn't know CS plays nekopara"
    show edimg at left
    ed "CS surrrre loves those cute catgirls~ <3"
    wes "Alright, but now what should we do?"
    hide edimg
    show richard at right
    rich "What about his laptop?"
    hide richard
    show edimg at left
    ed "Ehh..."
    wes "Wow, he even has a JoJ Ufo of his stupid HoH SiS series, the on that humiliated us."
    ed "Alright, how about we sabotage his computer?"
    "{i}Ed launches up the craptop{/i}"
    ed "Hehe... He won't know what hit him."
    #play sound "sounds/secret/eastereggquite.mp3"
    ed "Alrighty, It's done!"
    wes "Quick, Let's get out of here before he comes back"
    scene dooropen
    show wesley
    wes "Hurry up!"
    scene doorclosed
    "..."
    scene outside
    show richard at right
    rich "Lemme call our JoJ Ufo."
    show edimg at left
    ed "Ready?"
    "Ed, Wesley and Richard" "I'm beaming up!"
    scene csroom
    show csdefault at left
    cs "What should I do?"
    cs "Things sure are boooooring around here."
    cs "Hey, I got an idea!"
    cs "Let's go to Michael Rosen's house!"
    scene rosenhouse
    show michael at right
    mr "Hallo!"
    show csdefault at left
    cs "What's up Michael!"
    mr "I am feeling *pop* Noice."
    cs "Same here"
    cs "How are the poems coming along"
    mr "Ummm, actually they are rather noice."
    cs "That's good"
    cs "What if you put me in on of your poems?"
    mr "Horrible."
    cs "Yeah, that would be a mad idea."
    cs "Lemme call Billy Mays to come over."
    hide michael
    cs "{i}Dials Billy's number{/i}"
    show billy at right
    cs "Hey billy!"
    bill "Hi, it's Billy!"
    bill "What are you doing in my car?"
    cs "I'm not! I'm at Michael Rosen's house!"
    bill "Be there in two minutes!"
    "{i}Call ends{/i}"
    hide billy
    cs "Billy is so weird sometimes."
    show michael at right
    mr "Actually, that's not very noice."
    "{i}Billy arrives{/i}"
    hide michael
    show billy at right
    bill "Hi, it's Billy!"
    bill "Who wants some big city sliders?"
    cs "Sure!"
    hide billy
    show michael at right
    mr "Right into the mouth... Mmmmmmmm.... Noice."
    hide michael
    show billy at right
    bill "Here, take my Oxi Clean!"
    cs "Ummmm... Thanks?"
    hide billy
    show michael at right
    mr "Oohh there it is!"
    cs "Michael! That's not chocolate cake!"
    mr "And I had loads to eat! *Omm Nomm Nomm...*"
    mr "Blarrughhh!"
    mr "Worst chocolate cake I've ever had."
    cs "Yep. I'm gonna go now."
    scene cscarinside
    show csdefault
    cs "Well that was a waste of time."
    cs "Oh well, let's go work on my YTP at home."
return