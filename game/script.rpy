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
define p = Character("Pakoo")
define di = Character("Digi")
define policeoff1 = Character("Police Officer #1")

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
image factory = "background/Factory.jpg"
image elevator = "background/elevator.jpg"
image helipad = "background/Heli_pad.jpg"
image black = "background/black.jpg"
image interrogate = "background/PoliceInterrogation.jpg"
image smallhouse = "background/Smallhouse.jpg"

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
image pakoo = "characters/Pakoo.png"
image corndog = "characters/CornWorker.png"
image diabeetus = "characters/DiaBeetusWorker.png"
image grrx = "characters/GrrxWorker.png"
image copguy = "characters/Copguy_anime.png"
image csgod = "characters/Image7.png"

# The game starts here.

label start:
    scene black
    
    centered "{size=+40}PREVIOUSLY ON CS BOUNCINESS{/size}"

    scene csroom
    
    show csdefault at left

    cs "I'm so mad at HoH SiS. I was told they would do a great JoJ, but they hacked my computer!"
    cs "I'm gonna go to HoH SiS HeHdQuarters and show them who's boss."
    scene cscarinside
    show csdefault at left
    "..."
    scene office1
    show csdefault at left
    show corndog at right
    cs "Alright, where's the head JoJites?!"
    "Worker 1" "I don't know!"
    cs "BullShisH!"
    cs "{i}Punches worker.{/i}"
    hide corndog
    show grrx at right
    "Worker 2" "They-- They're on the roof!"
    cs "Good!"
    scene elevator
    show csdefault at left
    "..."
    scene helipad
    show csdefault at left
    show richard at right
    cs "You!"
    rich "Uh-oh."
    cs "You'll pay for what you did!"
    hide richard
    show wesley at right
    wes "Do you want a refund?"
    cs "I'll refund your face to the floor!"
    $ renpy.movie_cutscene("introplaceholder.mpg")
    centered "{size=+40}CHAPTER 1 - THE FIGHT{/size}"
    menu punch_menu:
        "Attack Wesley and Richard"
        "Punch them!":
            cs "{i}Punches!{/i}"
            jump taken_to_police
        "Kick them!":
            cs "This is..."
            cs "CrAaAaAaAaAaAaZY SATURDAY!"
            cs "{i}Kicks!{/i}"
            cs "Whoops, looks like he fell off the edge."
            jump return_home
        "Chop them!":
            cs "{i}Chops!{/i}"
        "Special Attack":
            cs "{i}Uses the power of YTP"
            jump police_station
            
    
    label return_home:
        cs "Well time to go home!"
        scene smallhouse
        show csdefault at left
        cs "This is what happens when you don't get quality foundation repair. {i}sigh.{/i}"
        scene csroom
        show csdefault at left
        cs "What should I do now that my house is different."
        menu:
            "What to do?"
            "Watch TV":
                "TV" "HI BILLY MAYS HERE FOR AN AMAZING NEW OFFER, A NEW COMPUTER CALLED THE NOOOT SO CRAPTOP, IT'S FUUFING FREE! WE CAN DO THAT BECAUSE NOBODY WILL SEE THIS AD SINCE NOBODY WATCHES TV ANYMORE!"
                "{i}Random Noise.{/i}"
                cs "Oh whats this? The noooot so craptop?"
            "Go to store and buy a new Craptop.":
                scene walmartinside
                show csdefault at left
                cs "Oh man! A noooot so craptop! What a steal!"
        scene csroom
        show csdefault at left
    return
    
    label taken_to_police:
        scene helipad
        show wesley at right
        wes "OH GOD WHY WOULD YOU DO THIS!?!?!?!?"
    return
    
    label police_station:
        scene helipad
        show csdefault at left
        show wesley at right
        wes "{i}The power of YTP gives Wesley a SuS gun and he starts shooting his co-workers with SuS"
        scene office1
        show wesley at left
        show edimg at right
        ed "OH GOD WESLEY DON'T SHOOT ME!"
        hide edimg
        ed "{i}is dedified{/i}"
        show copguy at right
        policeoff1 "WHAT THE NAME OF CROTCH DOCTOR IS HAPPENIN' HERE?!"
        wes "{i}Shoots officer{/i}"
        policeoff1 "Ha! Jokes on you, I'm wearing a SuS-proof vest!"
        wes "{i}{size=-8}aww{/size}{/i}"
        hide wesley
        show csdefault at left
        cs "Oh nice job wesley!"
        policeoff1 "EXCUSE ME!?!?!"
        cs "Oh shish."
        policeoff1 "You two are coming with me."
        scene cscarinside
        show csdefault at left
        show wesley at right
        cs "{i}{size=-4}Psst, hey, can I get my SuS gun back?{/size}{/i}"
        wes "{i}Hands CS his SuS gun.{/i}"
        cs "{i}{size=-4}Thanks man.{/size}{/i}"
        scene interrogate
        show csdefault at left
        show copguy at right
        policeoff1 "Now do you have any idea what the fuuf happened to wesley?"
        menu:
            "What caused wesley to go beserk?"
            "He was deranged.":
                cs "He was deranged, I came to get a refund because he hacked my computer when he was supposed to be fixing my completely oversized house!"
            "I came to get a refund.":
                cs "No officer, I came to request a refund because I didn't get the good JoJ I was promised, and he just started shooting SuS at everyone!"
                policeoff1 "Okay sir, thanks for your time!"
                scene cscarinside
                show csdefault at left
                jump return_home
            "I made him.":
                cs "I made him do it using the power of YTP."
                jump insane_asylum
            
        
    label insane_asylum:
        scene interrogate
        show csdefault at left
        show copguy at right
        policeoff1 "Bullshish! {i}Wait what's a YTP? Oh nevermind.{/i} I don't believe you!"
    return