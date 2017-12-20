#Variable declaration.

#Characters.
#define varname = Character("name")

define Arceus = Character("Arceus3251")
define ArceusJew = Character("Arceus3251")
define Billy = Character("Billy Mays")
define CS = Character("CS188")
define CSPhone = Character("CS188")
define CSInsane = Character("CS188")
define CSSurprised = Character("CS188")
define CSHappy = Character("CS188")
define CSThink = Character("CS188")
define CSYoung = Character("CS188")
define Carguy = Character("Carguy")
define Copguy = Character("Copguy")
define CSGuard = Character("CSGod")
define CorndogGuy = Character("Corndog Worker")
define Digi = Character("DigiDuncan")
define Discord = Character("Discord")
define Ed = Character("Ed")
define Grrx = Character("Grrx")
define JoJUFO = Character("JoJ UFO")
define Michael = Character("Michael")
define Pakoo = Character("Pakoo")
define Phil = Character("Phil Swift")
define Rich = Character("Richard")
define Wesley = Character("Wesley")
define James = Placeholder("boy")

#Backgrounds.
#image name = "dir/file.filetype"

image Asylum = "background/Asylum.jpg"
image Asylum2 = "background/Asylum2.jpg"
image Black = "background/black.jpg"
image CarDriveway = "background/Car_Driveway.jpg"
image CarInside = "background/Car_Inside.jpg"
image Elevator = "background/elevator.jpg"
image Helipad = "background/Heli_pad.jpg"
image JailCell = "background/JailCell.jpg"
image Nekopara = "background/Laptop_nekopara.png"
image Roblox = "background/Laptop_roblox.png"
image Stream = "background/Laptop_stream.png"
image Store = "background/microcenter.png"
image WeddingStatue = "background/MichaelRosenBillyMaysWedding.png"
image Office = "background/Office.jpg"
image OfficeOutside = "background/Officeoutside.png"
image Interrogation = "background/PoliceInterrogation.jpg"
image SmallHouse = "background/Smallhouse.jpg"
image TVBilly = "background/TV_Billy.png"
image TVBars = "background/TV_SMPTE.png"
image BadEnd = "background/badend.png"


#Character images.
#image name = "dir/file.filetype"

image Arceus = "characters/Arceus3251.png"
image ArceusJew = "characters/Arceus3251JewishForm.png"
image Billy = "characters/Billy_anime.png"
image Carguy = "characters/Carguy_anime.png"
image Copguy = "characters/Copguy_anime.png"
image CorndogGuy = "characters/CornWorker.png"
image CS = "characters/Cshocola.png"
image CSPhone = "characters/CshocolaPhone.png"
image CSInsane = "characters/Cs-ocolaInsane.png"
image CSSurprised = "characters/Cs-ocolasuprised.png"
image CSHappy = "characters/csocola_happy.png"
image CSThink = "characters/Csocola_think.png"
image CSYoung = "characters/CsocolaYoung.png"
image CSGuard = "characters/CSgod-ocola.png"
image Discord = "characters/discord.png"
image Digi = "characters/DuncanBig.png"
image Ed = "characters/Ed.png"
image Grrx = "characters/GrrxWorker.png"
image JoJUFO = "characters/jojufo.png"
image Michael = "characters/Michael.png"
image Pakoo = "characters/Pakoo.png"
image Phil = "characters/Phil.jpg"
image Rich = "characters/Richard.png"
image Wesley = "characters/wesley-chan.png"

# The game starts here.
label start:

show Helipad
with fade

show CS at left
show Wesley at right

CS "You'll pay for what you did!"

Wesley "Do you want a refund?"

CS "I'll refund your face to the floor!"

######################################################################

menu:

        "What attack would you like to use?"

        "Use Punch":

            jump punch

        "Use Chop.":

            jump chop

        "Use Kick":
            jump kick
        
        "Use Special":
            jump special    

######################################################################

label punch:

show CS at left

show Wesley at right

CS "Take this!"

"{i}CS punches Wesley and knocks him out{/i}"

hide Wesley

CS "That'll teach you not to miss with a nerd's computer!"

show Ed at right

Ed "Hello, 911? My boss just got knocked out by a disgruntled customer and appears to be dying! Send help!"

CS "Dammit! Ed's calling the police! I gotta go after him!"

Ed "911! Come quickly! He's chasing after me!"

"{i}The police arrive and CS runs away.{/i}"

hide Ed
show Copguy at right

Copguy "Hey! Get back here!"

CS "You can't catch me, I'm the speedy Michael Rosen!"

"{i}As CS is not actually the speedy Michael Rosen, he goes to jail.{/i}"

jump jail

######################################################################

label chop:

show CS at left

show Wesley at right

CS "Take this!"

"{i}CS chops Wesley and a fight ensues.{/i}"

Wesley "You'll pay for that!"

CS "Like hell I will!"

hide CS

hide Wesley

show Ed at center

Ed "911? Help! My boss just got attacked by a customer and now they're fighting right here in the office!"

hide Ed

show CS at left

CS "Dammit! Ed's calling the police! I need to finish this fast!"

"{i}The fight continues and the police arrive{/i}"

"{i}CS runs away{/i}"

show Copguy at right

Copguy "Get back here!"

CS "You can't catch me, I'm the speedy Michael Rosen"

"{i}As CS is not actually the speedy Michael Rosen, he gets caught by the police{/i}"

jump jail

######################################################################

label kick:

show CS at left

show Wesley at right

CS "This is CraAaAazy Saturday!"

"{i}CS kicks Wesley off of the building.{/i}"

hide Wesley

Wesley "AHHHHHH!"

CS "Well, that was satisfying. Time to go home!"

jump home

######################################################################

label special:

show CS at left

show Wesley at right

CS "Take this!"

hide CS

hide Wesley

show Office
with fade

"{i}CS uses the magic of YTP to make Wesley shoot his employees.{/i}"

show CS at left

"{i}CS calls the police.{/i}"

CS "Hello, 911! Come quickly, this guy is shooting up his office!"

"{i}CS hides under a desk until the police come and arrest Wesley{/i}"

show Copguy at right

Copguy "Sir, would you come with us? We'll need you to ask you a few questions"

CS "Of course, Officer."

jump questioning

######################################################################
#_   _                      
#| | | |                     
#| |_| | ___  _ __ ___   ___ 
#|  _  |/ _ \| '_ ` _ \ / _ \
#| | | | (_) | | | | | |  __/
#\_| |_/\___/|_| |_| |_|\___|
#                                                     
######################################################################

label home:

show CarInside

show CS at left

CS "Ahh almost home"

show SmallHouse

"{i}CS comes home to find his house drastically smaller.{/i}"

CS "This is what happens when you don't get quality foundation repair"

CS "Whatever, at least I'm finally home...."

"CS goes inside"

show InsideHouse

CS "Man, I need to relax after that shit, what should I do?"

menu:
    
    "What do you want to do?"

    "Watch TV":
    
        jump motorolatv
    
    "Go to the store and buy a new craptop":
    
        jump notsocraptop

label motorolatv:

show CS at left

CS "I may as well watch TV and get my mind off of things..."

"CS Fiddle diddles with the knobs on his Motorola TV"

show TVBilly

"Hi! Billy Mays here for the Noooot So Craptop, the easy way to get a better computer for FREE, that's right FREE! We can do that because this is being broudcast on analog signal from beyond the grave!"

"To get this offer, you'd need an old analog tv with the capability to pick up signal from super heaven, where only Billy Mays resides! This is a pointless ad, as nobody can ever see it!"

CS "Well, this is a good deal, not sure about all that stuff about interdimensional TV is about, but whatever, free computer."

"CS calls the number on the screen and BIlly Mays picks up."

"How did you get this number, it was only broadcast on Super Heaven TV"

CS "Idfk, I just fiddle diddled with the knobs on my Motorola TV and you showed up"

"Whatever, just take the computer....."

CS "Sweet"

jump newcomputer

######################################################################

label notsocraptop:

show CS at left

CS "I should probably go buy a new computer since HoH SiS destroyed my last one......"

show CarInside

"CS drives to MicroCenter to buy a new computer"

show bg MicroCenter

CS "Ooh this one looks good, the LenOwO dQw4w9WgXcQ. It's got a Sexy T.I.T.S graphics card or I can get one with an Nvidia Jesusforce 188! And it only costs 1 Dimick donation! I gotta get this!"

show ArceusJew at right

ArceusJew "Oh boy! Good deals, I gotta get one too!"

hide ArceusJew

"CS returns home with his brand new computer"

jump newcomputer

######################################################################

label newcomputer:

"Now that I have my new computer What should I do?"

menu:

    "What should I do with my new computer?"

    "Stream":
        jump stream

    "{i}Research{/i} Nekopara":
        jump cshappyfappytime

######################################################################  

label stream:

show CS at left

CS "I should probably stream since it's been over a week since I've streamed"

CS "Hey guys! CS here! Sorry I've been gone so long. Some crazy shit happened to me, I'm not even gonna TRY to explain it all."

"Chat: Yeah, right. you just spent the week sleeping."

CS "I didn't just sleep away the week! Seriously, I can't even go through the shit that happened!"

"Chat: Sure....."

CS "Okay, look. Why I was gone doesn't matter, Is there anything I can do as an apology CStream?"

"Chat: Play Roblox! Play Roblox! Play Roblox! Play Roblox! Play Roblox!"

CS "Well, I agreed to a apology CStream......"

CS "Okay, but only once!"

show Roblox

"{i}James and Matt show up to the CStream{/i}"

CS "Holy shit! Both founders in my stream at once?! Has this ever happened to any Mixer streamer before?"

James "Well, when I saw your Roblox stream I had to watch and it was so funny that I had to get Matt."

CS "Wow! I'm honored you think my stream is that funny!"

James "That's not all, Matt and I have decided to make you the Mixer Super Partner"

CS "What's a super partner? I've never heard of that before"

James "You've never heard of it because it's exclusive to you. You get to choose between half of all of Mixer's profits or renaming Mixer back to Beam."

menu:
    
    "Which option do you want?"

    "Half of Mixer's Profits":
        jump profits 

    "Rename Mixer to Beam":
        jump rename
######################################################################

label cshappyfappytime:

show Nekopara

show CS at left

CS "Well, I mean I was kinda getting hard for Chocola, and Pakoo always does it everyday…"

CS "As long as he doesn’t find out about it, then I don’t have to worry."

"{i}opens an extra tab up and types in Porno.com{/i}"

CS "This is a site your dad will love!"

CS "Now let’s see, “Chocola in heat”? Oh yes, this is gonna be good!"

CS "Ooooooh…… "

CS "Oh yes yes yes yes yes yes yes yes! Yes yes yes yes yes yes! (CS rave)"

"{i}CS shoots his “True Jizz Water” all over his screen{/i}"

"{i}then notices that he left OBS open and was streaming{/i}"

CS "OH SHIT!!!!!!"

"{i} CS tries to stop the stream and close the tab still playing the hentai, but his computer freezes.{/i}"

CS "DAMNIT!!! Now I will get my partnership taken away, and everyone will know that I fapped to this!"

"{i}Just as CS is going to delete his Mixer account, he sees the founders, James and Matt.{/i}"

"{i}James and Matt show up to the CStream{/i}"

CS "Holy shit! Both founders saw me accidentally fapping on stream! Now I definitely need to delete my account?"

James "Don't be so quick to act, CS"

CS "What do you mean, I'm in violation of like every rule in the TOS right now"

James "That's true, but you've introduced me to a whole new world."

CS "You mean you never heard of Nekopara before?"

James "Nope! I just found out about it and my eyes have been opened, so I decided to reward you."

CS "Reward me? What do you mean?"

James "I've decided to make you a super partner!"

CS "What's a super partner? I've never heard of that before"

James "You've never heard of it because it's exclusive to you. You get to choose between half of all of Mixer's profits or renaming Mixer back to Beam."

menu:
    
    "Which option do you want?"

    "Half of Mixer's Profits":
        jump profits 

    "Rename Mixer to Beam":
        jump rename

######################################################################
label profits:

show CS at left

show Stream




######################################################################  
# _   _                      
#| | | |                     
#| |_| | ___  _ __ ___   ___ 
#|  _  |/ _ \| '_ ` _ \ / _ \
#| | | | (_) | | | | | |  __/
#\_| |_/\___/|_| |_| |_|\___|
#
######################################################################

######################################################################
#  ___            _                 
# / _ \          | |                
#/ /_\ \___ _   _| |_   _ _ __ ___  
#|  _  / __| | | | | | | | '_ ` _ \ 
#| | | \__ \ |_| | | |_| | | | | | |
#\_| |_/___/\__, |_|\__,_|_| |_| |_|
#            __/ |                  
#           |___/                            
######################################################################

label questioning:

show Interrogation

show CS at left

show Copguy at right

Copguy "So what did you see?"

menu:
 "What did you see?"

 "I used YTP Magic":

     jump admit

 "He was crazy":

     jump deny

######################################################################

label admit:

show Interrogation

show CS at left

show Copguy at right

CS "I made him do it using the power of YTP."

Copguy "No joking around, this is a serious situation."

CS "No, I really did!"

Copguy "Yeah, you're obviously deranged, I'm calling the insane asylum!"

CS "I really did!"

Copguy "Sure ya did....."

jump asylum

######################################################################

label asylum:

show Asylum

show CSInsane at left

CSInsane "Let me out! I'm not crazy!"

show CSGuard at right

CSGuard "Quiet down! I can't let you out!"

hide CSInsane

hide CSGuard

"{i}A few days pass and the guard comes back{/i}"

show CSInsane at left

CSInsane "Have you come to let me out?"

CSGuard "I already told you, I can’t let you out. I came because we have an overflow of patients right now" 

CSGuard "Due to lack of space, we need to pair you with one of our less dangerous patients."

CSGuard "He's a schizo and he sees money everywhere, but other than that he's fine"

hide CSGuard

show ArceusJew at right

Arceus "Money Money Money Money Money Money Money Money Money Money"

CSInsane "Great, now I have to deal with this shit"

hide ArceusJew

hide CSInsane

"After a few days of listening to Arceus, CS was starting to think he may need to be in this insane asylum soon, but then, a new face came."

show CSInsane at left

show Digi at right

CSInsane "You don't look like just a guard... Are you the owner?"

Digi "Indeed I am, I've come to get your cellmate here. One of the patients killed a guard, and the other guards had to take him down. So now we have an open cell and a staff shortage, hence why I'm getting him myself."

CSInsane "Since you're the owner, you’ll be able to let me out! Please let me out I’m not insane!"

Digi "Alright, give me something I want and I’ll let you go."

menu:
     "What should you bribe Digi with?"

     "Powerade.":

         jump powerade

     "Insulin.":

         jump insulin

     "Promise to be on time for streams.":
         
         jump ontime

######################################################################

label insulin: 

show CSInsane at left

show Digi at right

CSInsane "I'll give you some insulin."

Digi "I'll take it!"

jump home

######################################################################

label powerade:

show CSInsane at left

show Digi at right

CSInsane "I'll give you a 36 pack of powerade."

Digi "I'll take it."

jump home

######################################################################

label ontime:

show CSInsane at left

show Digi at right

CSInsane "I'll actually be on time for streams."

Digi "Wow, you really think you can do that? You must need to be in an Insane Asylum! C'mon Arceus, let's get you into your new cell."

hide CSInsane

hide Digi

show BadEnd

"{b}Digi leaves and CS is stuck in the insane asylum. Bad End{/b}"
######################################################################
#  ___            _                 
# / _ \          | |                
#/ /_\ \___ _   _| |_   _ _ __ ___  
#|  _  / __| | | | | | | | '_ ` _ \ 
#| | | \__ \ |_| | | |_| | | | | | |
#\_| |_/___/\__, |_|\__,_|_| |_| |_|
#            __/ |                  
#           |___/                            
######################################################################

######################################################################
#   ___       _ _ 
#  |_  |     (_) |
#    | | __ _ _| |
#    | |/ _` | | |
#/\__/ / (_| | | |
#\____/ \__,_|_|_|
#
######################################################################                 
                 
label jail:

######################################################################
#   ___       _ _ 
#  |_  |     (_) |
#    | | __ _ _| |
#    | |/ _` | | |
#/\__/ / (_| | | |
#\____/ \__,_|_|_|
#
######################################################################   
