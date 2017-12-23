﻿#Variable declaration.

#Characters.
#define varname = Character("name")

define Annorexorcist = Character("Annorexorcist")
define Arceus = Character("Arceus3251")
define ArceusJew = Character("Arceus3251")
define Billy = Character("Billy Mays")
define BorderGuard = Character("BorderGuard")
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
define FatherDigBick = Character("Father Bick")
define Grrx = Character("Grrx")
define JoJUFO = Character("JoJ UFO")
define Linus = Character("Linus")
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

image Annorexorcist = "characters/Anno.png"
image Arceus = "characters/Arceus3251.png"
image ArceusJew = "characters/Arceus3251JewishForm.png"
image Billy = "characters/Billy_anime.png"
image BorderGuard = "characters/WithEyesGuard"
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
image FatherDigBick = "characters/DFigbick.png"
image Grrx = "characters/GrrxWorker.png"
image JoJUFO = "characters/jojufo.png"
image Linus = "characters/Linus.png"
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

"Chat Yeah, right. you just spent the week sleeping."

CS "I didn't just sleep away the week! Seriously, I can't even go through the shit that happened!"

"Chat Sure....."

CS "Okay, look. Why I was gone doesn't matter, Is there anything I can do as an apology CStream?"

"Chat Play Roblox! Play Roblox! Play Roblox! Play Roblox! Play Roblox!"

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

CS "Now let’s see, Chocola in heat? Oh yes, this is gonna be good!"

CS "Ooooooh…… "

CS "Oh yes yes yes yes yes yes yes yes! Yes yes yes yes yes yes! (CS rave)"

"{i}CS shoots his True Jizz Water all over his screen{/i}"

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

CS "Well of course I'm gonna go with the money, I can finally quit my shitty part time joj."

James "Okay, I'll transfer the first of the money to your account now"

menu:
    
    "Which option do you want?"

    "Improve the World":
        jump world 

    "Build a Statue":
        jump statue

######################################################################
label rename:

show CS at left

show Stream

CS “I’ll rename Mixer back to Beam!”

James “Are you sure you don’t have anything better you can do?”

CS “Yep, I wanna rename Mixer back to Beam!”

James “Okay, I guess…”

CS “So how long will this take?”

James “Not long at all actually, I have a program on my desktop to change Mixer back to Beam”

CS “Why do you have that?!”

James “Don’t question me!”

CS “Okay.”

return

######################################################################
label statue:

show CS at left

CS “I made this community on top of YTP’s, so maybe I should honor the source of my newfound riches.”

"{i}CS sets out to build statues of Billy Mays and Michael Rosen{/i}"

CS “This company looks good, Dig Bick’s Building Co.”

"{i}CS goes to Dig Bick Building Co’s HQ{/i}"

show Digbick at right

DigBick “Welcome! What would you like today?"

CS “I want to to build a custom statue of Billy Mays and Michael Rosen getting married.”

DigBick “Okay, that’s a weird order, how big do you want it?”

CS “As big as you can go!”

DigBick “I’ll get right on it!”

return

######################################################################  
label world:
show CS at left
CS “Well, I’ve always thought that rich people should spend their money on improving the world, so now that I’m rich I should do that!”
CS “But how should I improve the world?.....”
CS ”I could help people with medical expenses, but I already did that with the charity stream….”
CS “I know, I’ll make the ultimate contribution to the human race! Create real life Neko girls!”
{i}CS researches labs he can hire to make real life neko girls{/i}
CS “Ooh! This one looks good, Pakoo the Pervert’s Genetics Lab.” 
{i}CS picks up the phone and calls Pakoo’s the Pervert’s Genetics Lab{/i}
Pakoo “Pakoo the Pervert’s Genetics Lab, Dr. Pakoo speaking!”
CS “Wait.. You sound awfully like Pakoo from my stream…”
Pakoo “Huh? I don’t believe we’ve met before?”
CS “Oh? I could’ve sworn.”
Pakoo “Nope! Not at all!”
CS “In any case.. Do you think you could assist me in researching the creation of the Neko race?”
{i}The line goes quiet{/i}
shpw Pakoo at right
Pakoo (Appearing from nowhere) “Sunny D! Alright! Let’s do this!”
CS “How the hell did you find my house?!”
Pakoo “Traced your call. Anyways, you have the cash?”
CS “That depends, do you have the talent.” 
Pakoo “Yep, but no cash.”
CS hands over the cash
CS “I think this will be more than enough to support this cause.”
Pakoo “Holy shit, how did you come up with all this money?!”
CS “You were on the Stream when I got super partnership.”
Pakoo “You kidding me? I had you in the background, I was busy creating a fan-made game called CS Bounciness Volume 2.”
CS “That’s… oddly specific.”
Pakoo “Yeah.. Anyways, let me take you to my lab.”
{i}Pakoo takes CS to his Neko Genetics Research Lab after a bit of.. shopping{/i}
CS “Nice lab you got here.”
Pakoo “It’s about to get even better. Stand back.” 
{i}CS stands back and Pakoo begins installing the various gadgets and gizmos that were purchased on their shopping trip{/i}
CS “Are you sure this will work?”
Pakoo “Nope! But It’s not my money!”
CS “Well, damnit”
{i}Pakoo flips a switch, various machines begin to start up and whir{/i}
CS “Uhm…”
Pakoo “Almost there..”
{i}The machines begin to slow down to a halt, followed by a pleasant ding from a bell{/i}
CS “Well.. now I know what the bell we bought was for..”
Pakoo “What? Aesthetics Matter. I was gonna go for RGB RAM, but…. that was a bit expensive.”
CS “So.. Did it work?”
show Phil at right
Philsuki “IT EVEN WORKS UNDERWATER!”
{i}CS jumps{/i}
CS “Holy shit! What the hell are you?!”
show Pakoo at right
Pakoo “Damnit.. that Neko isn’t complete.. It’s got a penis.”
CS “So?”
Pakoo “Well, it’s meant to be a CatGIRL, not Catguy.”
show Phil at right
Philsuki “FLEX TAPE IS STUPID!”
show Pakoo at right
Pakoo “Yeah, so are you, back in the machine.”
{i}Pakoo shoves Philsuki back into the machine{/i}
show Phil at right
Philsuki “I SAWED THIS BOAT IN HA-
{i}His screams are drowned out by the machine{/i}
show Pakoo at right
Pakoo “Lemme fix some stuff….”
{i}Pakoo fiddles around in the back of the machine{/i}
Pakoo “You know what, I think I know what the problem is!”
{i}Pakoo ignores CS’ questions and goes out shopping again{/i}
Pakoo “I got the RGB!”
CS “I thought you said it was too expensive?”
Pakoo “It is a scientific fact, that you cannot achieve performance without…”
Pakoo “Mucho RGB!”
CS “So will it work now?”
Pakoo “Probably.”
{i}Pakoo turns on the machine again{/i}
Vanilla “Master!”
{i}Vanilla runs up to CS{/i}
CS “Well, I wanted Chocola, but Vanilla is good too.”

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
label deny:

show Interrogation

show CS at left

show Copguy at right

Copguy "So what did you see?"

CS "I don't know what happened! I just came to get a refund and he started shooting"

Copguy "Okay, I'm sorry you had to go through that sir."

jump home
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

return

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

show JailCell

Copguy "Alright, welcome to the slammer. How tough are ya?"
CS "How tough am I?! How, tough, am, I?! I beat Cuphead!"
Copguy "So?"
CS "In under 90 minutes!"
Copguy "Okay! You’re tough enough to get your choice of cellmate, which one do you want?"

menu:

     "Who do you want for your cellmate?"
     
     "Arceus":
        jump arceuscellmate

     "Annorexorcist":
        jump annorexorcellmate    

label arceuscellmate:
CS "I choose Arceus."
Copguy "Alright, but be warned. This person was arrested for cutting a tax collector with his nose."
CS "Alrighty then…."
CS "Hello, Arceus."
Arceus "Aye, Boss. .w."
CS "So what are you in for?"
Arceus "Didn’t you hear the cop? \ I’m in for cutting a tax collector with my nose."
CS "Well, I can see how. Your nose IS big enough."
Arceus "And from my recent playthrough of CSBounciness 1, I assume you’re in for killing workers at HoHSiS"
CS "I was 100 percent unsatisfied."
Arceus "As was I.. As was I.."
"{i}A brief moment of silence..{/i}"
Arceus "Welp, I’m bored of this place… Wanna break out? 3"
CS "Eh.. Sure, why not, I’ve played plenty of the Escapists, I should be able to figure it out."
CS "We should break out at least one other person though."
Arceus "Alright, who do ya wanna break out..?"
CS "Let’s just break out that guy next to us, I think his name was Annorexorcist-something…."
Arceus "Annorexorcist? Eh… He’s a bit of a stick in the mud, but sure. He may be of use to us."
CS "Alright then, let’s get going!"
jump breakout

label annorexorcellmate:
CS "I choose Annorexorcist"
Copguy "Okay" 
CS "Hey Annorexorcist."
Annorexorcist "Hey"
CS "So what’re you in for?"
Annorexorcist "..."
"{i}Annorexorcist begins to stare longingly at CS…{/i}"
CS "Well, you don’t talk much do you?"
Annorexorcist "Huh, sorry, I got lost in thought"
CS "About what?"
Annorexorcist "Breaking out of here."
CS "Wow, Am I that bad of a cellmate that you want to breakout as soon as I get here?"
Annorexorcist "No, I’ve been working with the prisoner in the next cell, Arceus, to breakout for 5 years now."
CS "Wow, can I come with?"
Annorexorcist "Only if you can figure out a way to escape, we’ve had no success, as you can tell given that we’re still here."
CS "I think I have some ideas, I’ve played a LOT of the escapists."
Annorexorcist "Works for me, let’s do this"
jump breakout


label breakout:
Arceus "So, what’s the plan? I’ve been tryna break outta here for 5 Years"
CS "Well, for a start. I need to get a feel of the routine here"
Arceus "Well, I’ll quickly describe that for you, cause I can’t stand another minute here." 
"{i}Arceus quickly describes the prison routine to CS{/i}"
CS "I think I got all that."
Arceus "So, what’s our plan, Boss?"
CS "I gotta grab a few plastic spoons from the mess hall, Cup of molten chocolate, a guard outfit, and a change of shorts."
Arceus "Why a change of shorts?"
CS "You kidding me? I’m gonna shit myself cause this is scary as hell."
Arceus "Fair enough."
"{i}The day ends, the next day progresses, CS and Arceus gather the required essentials for their escape. Along the way, they inform Annorexorcist, who more than happily complies with the plan.{/i}" 
"{i}The next evening....{/i}"
CS "Key, Check."
Arceus "Uniforms, Check."
Annorexorcist "Spoons, Check."
CS "Extra Shorts."
CS "Check."
CS "Alright men, let’s get the heck out of here!"
"{i}The plan goes off without a hitch, the three ditch their Prison Outfits, and put on their guard uniforms.{/i}" 
"{i}In the midst of them changing, Annorexorcist notices CS’s butt and compliments it.{/i}"
Annorexorcist "CS.. Nice Ass.."
CS "Thank you."
Arceus "Save it for later, love birds." 
"{i}The Three dig their way out of the cell and make a break into the dark of the evening.{/i}"
CS "Jeez.. I didn’t think that would actually work."
Arceus "You what?" 
Annorexorcist "Hey, CS.. You looked sexy runnin’ outta that prison.."
CS "Blush  Thank you.."
Arceus "Guys, save this for when we’re all safe, we need to get a car and get over the border."
Annorexorcist "How are we supposed to cross the border with the new wall?"
Arceus "Not the Mexican border, the Canadian border, we’re in New York, it’s way closer and they’re too polite to send us back."
CS"Works for me, free healthcare."
Arceus"Well, you have to live there for a few years before you get access to that, but you should last a few years without getting sick living on that healthy diet of Ritz and EZ cheese."
jump bordercrossing

label bordercrossing:
"{i}CS, Annorexorcist and Arceus get to the border crossing{/i}"
"{i}A border guard appears{/i}"
BorderGuard "I’m going to need proof of citizenship, eh."
Arceus "Color is spelled with a u, eh."
BorderGuard "Works for me, eh."
CS "Now that we’re over the border and can breathe easy, I wanted to ask you something Annorexorcist."
Annorexorcist "Yeah?"
CS "You made a couple passes at me on the trip here, was there anything behind that or were you joking around?"
Annorexorcist "Which one would you prefer?"
CS "The former, I mean, I’ve been single for a while I’ll take what I can get."
Annorexorcist "Well, I suppose I have good news for you then…."
Arceus "Are you lovebirds hungry? I’m gonna stop for food at Tim Horton’s."
"{i}At the Tim Horton’s, Annorexorcist and CS share a donut and make out{/i}"
CS "Wow, that was great!"
"{i}Annorexorcist blushes{/i}"
Annorexorcist "Thanks…."
CS "Oh, I was talking about the donut but the kiss was good too."
CS "About 88 percent as good as the donut."
Annorexorcist "I’ll take it."
Arceus "Sorry to interrupt you two, but we may have a problem, that donut cost me the last of my money, so we need to find a way to make some cash."
"{i}CS looks across the street to see Linus Media Group{/i}"
CS "I have a lot of video editing experience, maybe I can get a job there."
"{i}CS walks into the studio and asks for a job{/i}"
Linus "Sure, you can have a job, just show us proof of citizenship and you’re ready to go!"
CS "Color is spelled with a u, eh."
Linus "I need actual papers, the last time I hired someone who used that as proof of citizenship I got fined and had to sell one of my 1000s of GTX Titans."
CS "Ummmm, I’ll be right back."
"{i}CS leaves and talks to Annorexorcist{/i}"
CS "I need to get proof of citizenship, or at least fake proof of citizenship before I can get a joj here."
"{i}Annorexorcist gets an idea and begins to blush{/i}"
Annorexorcist "Trudeau is trying to make Canada more diverse by letting gay married couples get citizenship, we just have to get married and then you can work here."
CS "We don’t have money to get married!"
Annorexorcist "We can have a cheap wedding at one of your Canadian fan’s houses."
CS "Well, I know Nova lives around here, so we can have the wedding at his house."
jump wedding

label wedding:
"FatherDigBick “Do you, Annorexorcist, take NAME REDACTED to be your lawfully wedded husband?"
Annorexorcist "I do."
FatherDigBick "And do you, NAME REDACTED, take Annorexorcist, to be your lawfully wedded husband?"
CS "I do."
"{b}{i}True End CS marries Annorexorcist and lives in Canada working for LMG{/i}{/b}"

return
######################################################################
#   ___       _ _ 
#  |_  |     (_) |
#    | | __ _ _| |
#    | |/ _` | | |
#/\__/ / (_| | | |
#\____/ \__,_|_|_|
#
######################################################################   
