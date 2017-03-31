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
    show text "{i}Time Passes{/i}" at truecenter
    "{i}Doorbell Rings{/i}"
    cs "Oh! They're here!"
    cs "Lemme go get the door"
    
    scene dooropen
    show csdefault at left
    cs "Hello! I am CS188, and I-"
    show edimg at right
    ed "Alright, that will be 200 cstars."
    cs "Alright, lemme get my wallet."
    cs "Here you go."
    show edimg
    ed "You want the JoJ!"
    hide csdefault
    "{i}CS leaves.{/i}"
    show edimg
    ed "Come on in guys. CS left."
    show richard at right
    rich "JoJ!"
    hide richard
    show wesley at left
    wes "Do we have to do this all over again?"
    show edimg at right
    ed "So now that we're here, what should we do to him?"
    "Ed, Wesley and Richard" "Hmmm..."
    ed "Let's go check his room"
    "{i} The three HoH SiS workers go upstairs. {/i}"
    
    scene csroom
    show wesley at right
    wes "Wow, I didn't know CS plays nekopara!"
    show edimg at left
    ed "CS surrrre loves those cute catgirls~ <3"
    show wesley at left
    wes "Alright, but now what should we do?"
    show richard at right
    rich "What about his laptop?"
    hide richard
    show edimg at left
    ed "Ehh..."
    show wesley
    wes "Wow, he even has a JoJ Ufo of his stupid HoH SiS series, the on that humiliated us."
    show edimg
    ed "Alright, how about we sabotage his computer?"
    "{i}Ed launches up the craptop.{/i}"
    ed "Hehe... He won't know what hit him."
    #play sound "sounds/secret/eastereggquite.mp3"
    ed "Alrighty, It's done!"
    show wesley
    wes "Quick, Let's get out of here before he comes back"
    
    scene dooropen
    show wesley
    wes "Hurry up!"
    
    scene doorclosed
    "..."
    
    scene outside
    show richard at right
    rich "Lemme call our JoJ UFO."
    show edimg at left
    ed "Ready?"
    "Ed, Wesley and Richard" "I'm beaming up!"
    #show jojufo
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
    cs "Same here."
    cs "How are the poems coming along."
    mr "Ummm, actually they are rather noice."
    cs "That's good."
    cs "What if you put me in on of your poems?"
    mr "Horrible."
    cs "Yeah, that would be a bad idea."
    cs "Lemme call Billy Mays to come over."
    hide michael
    hide csdefault
    show csphone at left
    cs "{i}Dials Billy's number.{/i}"
    cs "Hey billy!"
    show billy at right
    bill "Hi, it's Billy!"
    bill "What are you doing in my car?"
    cs "I'm not! I'm at Michael Rosen's house!"
    bill "Be there in two minutes!"
    "{i}Call ends{/i}"
    hide billy
    hide csphone
    show csdefault
    cs "Billy is so weird sometimes."
    show michael at right
    mr "Actually, that's not very noice."
    "{i}Billy arrives{/i}"
    hide michael
    show billy at right
    bill "Hi, it's Billy!"
    bill "Who wants some big city sliders?"
    hide csdefault
    show cshappy
    cs "Sure!"
    hide cshappy
    show csdefault
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
    
    scene dooropen
    show csdefault
    cs "Wow. What a day!"
    show edimg
    ed "Your house is all fixed up!"
    cs "Oh yay!"
    cs "Thank you!"
    ed "Remember : If you need foundation repair, just call HoH SiS."
    hide edimg
    ed "{i}Leaves.{/i}"
    scene csroom
    show csdefault at left
    cs "Alright time to work on my YTP."
    cs "Time to start up the ol' craptop again"
    scene craptop1
    show csdefault at left
    cs "Hmm... That's odd..."
    ct "Startup complete! Launching Totally_Not_Virus.exe...."
    cs "Hmm... What's this?"
    ct "{i}Random errors and noises{/i}"
    cs "Wait... what?"
    cs "Lemme try this again."
    ct "{i}Same errors and noises{/i}"
    cs "Okay, this is a problem."
    cs "I need help..."
    cs "{i}Looks at ground.{/i}"
    cs "What's this?"
    cs "'Pakoo's Novedits : Hire Novedits to help work for you! Just call 10101010010100101001'"
    cs "Let's see what they have there."
    scene factory
    show csdefault at left
    cs "Wow... this place gives me the creeps...."
    show pakoo at right
    p "Welcome to Pakoo's Novedit Factory! How can I help ya?"
    cs "Ummm... What are novedits anyway?"
    p "Whhhaaaat? Why are you even here?"
    p "Ever seen one of these?"
    p "{i}Pulls out a Novedit{/i}"
    cs "Perfect! I will buy 3, please."
    p "Ummm... Alright... {i}1,2,3, that will be.... hmm....{/i} That'll be 3000 CStars"
    cs "Oh wow okay.... I think I got that..."
    cs "Alright here you go!"
    p "Alright, here are the 3 little numbskulls you ordered."
    hide csdefault
    show nova1 at left
    "Nova 1" "Nova?"
    p "Yep, this freak is your owner now."
    "Nova 3" "Novvv... Novvaaa..."
    p "I bet he also enjoys playing Nekopara."
    "{i}All novas snicker{/i}"
    hide nova1
    show csdefault at left
    cs "Hey! Shut up! {i}dangit{/i}"
    p "Well have fun with those guys."
    cs "Alrighty, nice doing business with you."
    p "You too."
    hide csdefault
    p "Whew! That was close."
    "{i}Faint neko voices from the back of the factory.{/i}"
    p "SHUT UP VANILLA!!!"
    scene csroom 
    show csdefault at left
    show nova1 at right
    cs "Alright, I'm gonna go for a bit, see if you can fix my craptop."
    cs "Thanks"
    hide csdefault
    "Nova 1" "Nova!"
    "Nova 2" "Nova Nova Nova?"
    "Nova 3" "Nova Nova, Nova Nova Nova."
    "Nova 3" "{i}Opens up Craptop{/i}"
    ct "{i}Bluescreen of death.{/i}"
    "Nova 3" "Nooooo... va."
    "Nova 2" "Nova Nova Nova."
    ct "{i}Bluescreen again.{/i}"
    "Nova 3" "Nova Nova."
    ct "{i}Another bluescreen.{/i}"
    "Nova 3" "F***"
    show csdefault at left
    cs "Hey guys, CS He-"
    cs "Get. Out."
    scene factory
    show csdefault at left
    show pakoo at right
    cs "Here. Take these back."
    p "I expected this."
    p "You do know what you got into, right?"
    cs "Noooo...."
    p "Hehe... I thought so."
    p "Do you want your money back?"
    cs "Just, keep it."
    p "Alrighhhhht..."
    p "If that's fine with you."
    scene csroom
    show csdefault at left
    cs "{i}Crying noises{/i}"
    show digi at right
    di "What's wrong?"
    cs "{i}sniff{/i} My craptop doesn't work..."
    cs "I need to check my YouTube, my fans are yelling at me right now probably."
    di "Ahh... Yes.. I can fix this."
    di "Let's look at the craptop."
    ct "{i}Bluescreens.{/i}"
    di "Hmm..."
    di "{i}Types furiously.{i}"
    di "Ahh yes..."
    di "Move this... and this..."
    di "Open 'nekopics' and..."
    di "Done!"
    di "HoH SiS sabotaged your craptop, that's why."
    cs "Oh really?"
    cs "{i}Calls HoH SiS.{/i}"
    hide digi
    show edimg at right
    ed "Do you need foundat--"
    cs "No, and screw you! I no longer need the JoJ!"
    hide edimg
    cs "{i}Hangs up.{/i}"
    show digi at right
    cs "Now that that is over, does my Craptop work?"
    di "Yep, it should."
    cs "Alright, thanks! I owe you."
    di "No problem, cya!"
    hide digi
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
    show csdefault
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
    "..."
    scene black
    $ renpy.movie_cutscene("credits.ogv")
    show wesley
    wes "Now do it all over again."
    wes "In fact, do it 15 times over again."
return