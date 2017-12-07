#Variable declaration.

#Characters.
#define varname = Character("name")

define Arceus = Character("Arceus3251")
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
image WeddingStatue = "background/MichaelRosenBillyMaysWedding.png"
image Office = "background/Office.jpg"
image OfficeOutside = "background/Officeoutside.png"
image Interrogation = "background/PoliceInterrogation.jpg"
image SmallHouse = "background/Smallhouse.jpg"
image TVBilly = "background/TV_Billy.png"
image TVBars = "background/TV_SMPTE.png"

#Character images.
#image name = "dir/file.filetype"

image Arceus = "characters/Arceus3251JewishForm.png"
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
show Copguy at left

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

label jail:

######################################################################

label home:

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

show Arceus at right

Arceus "Money Money Money Money Money Money Money Money Money Money"

CSInsane "Great, now I have to deal with this shit"

hide Arceus

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