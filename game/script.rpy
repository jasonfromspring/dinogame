# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define u = Character(_("You"), color="#aaaaaa", what_slow_cps=50)
#Pentaceratops 
define tr = DynamicCharacter("rexName", color="#984a4a", what_slow_cps=50)
define ti = DynamicCharacter("triName", color="#bb650a", what_slow_cps=50)
define v1 = DynamicCharacter("v1Name", color="#aaaaaa", what_slow_cps=50)
define v2 = DynamicCharacter("v2Name", color="#aaaaaa", what_slow_cps=50)
define s = DynamicCharacter("stegName", color="#aaaaaa", what_slow_cps=50)
define d = DynamicCharacter("diloName", color="#aaaaaa", what_slow_cps=50)
define p = DynamicCharacter("paraName", color="#aaaaaa", what_slow_cps=50)

define n = Character(what_slow_cps=50)

default tmp = False

# The game starts here.

label start:
    $ rexName = "Tyrannosaurus Rex"
    $ triName = "Triceratops"
    $ v1Name = "The Loud Velociraptor"
    $ v2Name = "The Quiet Velociraptor"
    $ stegName = "Stegosaurus"
    $ diloName = "Dilophosaurus"
    $ paraName = "Parasaurolophus"


    #play music?

    scene black

    n "The lapping of water is a gentle awakening to your rest beside the spring waters."

    scene bg forest with fade

    n "The sun shines at the peak of its height, producing a perfect cover of shade directly upon you."
    n "A faint squacking is heard in the distance.  You instincitvely glance the skies for any aerial predators, or for another unfortunate pterodactyl excrement incident."
    n "Once again, a reminder that the life of a herbivore is one of constant annoyances, despite your fierce horns."

    ti "Another late nap?"

    show triceratops
    with dissolve

    n "From a nearby thicket emerges the familiar face of your fastest friend and fellow foliage-eater."
    ti "I knew I'd find you here."

    u "Hey, Trip."
    $ triName = "Trip"

    ti "I always find you in the same spot, at the same time of day, taking the same nap.  Is this like the special spot of Pentaceratops?"

    menu:

        "What a strange question.  You decide..."

        "\"It's a nice spot\"":
            
            u  "It's comfortable."
            ti "I would hope it is."
            #show trex test with dissolve


        "\"Actually, this is the perfect spot at this time of day for an optimal casting of shade for maximum quality of rest\"":
            
            u "At this exact moment, the sun rises to the very middle of the sky. Because of the angle between the trees overhead and the sun--"

            #show triceratops annoyed with dissolve

            ti "Okay."
            ti "I'm cutting you off there.  I'm sure it's a perfect spot, but it'll be perfect any day.  Not every day is Steggy's birthday!"

            n "Steggy?  Birthday?  The words were vaguely familiar."
            $ tmp = True
            ti "Why do you look so confused?"
        
        "Say nothing, and begin to doze off again":

            show triceratops #shock
            ti "..."
            scene black
            with dissolve
            
            n "You deliberately snore."

            ti "You're about to catch these horns right now."
            with vpunch
            scene bg forest
            show triceratops #annoyed
            pause(1)
    
    ti "DId you forget what we're supposed to do today?"

    u "..."

    ti "Please don't tell me you did."

    menu:
        "You decide that..."

        "You remember.  Definitely":
            u "Hold up, I defini--{nw}"

        "Better to tell the truth: you forgot":
            u "You know me too w--{nw}"


    #show triceratops shock with vpunch
    pause(1)

    #show triceratops anger with dissolve
    n "The Earth shook."
    with vpunch
    pause(1)

    n "Consuctive tremors announced the sudden presence of the apex predator to the world."
    with vpunch
    pause(1)
    
    hide triceratops with dissolve
    n "The rising intensity of the quakes was the only warning to the grand approach of the all-powerful king."
    with vpunch
    pause(1)

    n "Before you knew it, you found yourself staring into the eyes of a Tyrannosaurus Rex."
    with vpunch
    show trex with dissolve
    pause(1)
    tr "Hey guys."

    n "The mild-mannered Rexxi emerged from the forest."
    $ rexName = "Rexxi"

    show triceratops at right with dissolve

    ti "Oh, it's just you, Rexxi.  What are you doing here?"

    tr "I have arrived to retrieve you two.  We have been searching."

    tr "Especially for you.  For what reason have you been missing?  Do not tell me that you have forgotten."

    n "You rack your brain for an answer.  You don't want to let down Rexxi, forgotten knowledge or not."

    menu:

        "You decide to say..."

        "\"Forgot what?\"":

            # show triceratops bruh at right with dissolve

            tr "..."

            u "Sorry, I don't remember a thing."

            # show trex exasperated with dissolve

            n "A sigh escapes the great jaw of the T-Rex.  Amidst the awkwardness, you wonder how that's even possible."

            ti "It's Steggy's birthday."

            u "Oh."

            n "You wondered who that was again..."

            ti "Your adoptive brother."

            u "Oh."

            tr "Whose birthday is the day before your own date of birth."

            u "..."

            u "I think I have some amensia."

            pause(1)

            tr "Maybe a rock fell on your head as you were napping."

            u "Yeah..."

        "\"I didn't forget anything.\"":

            tr "That is reassuring.  It would be quite the feat to forget the date of birth of your own kin."

            n "You pointedly ignore Trip's conspicuous stare."

            tr "It really is such an exciting idea, to celerbrate one's date of birth."

        "\"I was napping...\"":
        
            tr "..."

            tr "I suppose that is just like you.  Napping as always, even during the date of birth of your brother."

        "\"I couldn't forget about Steggy's birthday today.\"" if tmp:

            #show trex shocked
            tr "Of course.  You wouldn't forget about the birthday of your kin, especially when it resides on the day before your own anniversary."
            #show trex solemn with dissolve
            tr "It would be a strange if you truly had forgotten.  I suppose you were just resting before the celebrations?"

            u "Yup.  I was just waiting."
            n "A pretty convenient lie, and it seemed to have worked perfectly."


    ti "Anyway... Rexxi.  You said you were looking for us?"

    tr "Oh, that is right.  Everyone else is currently at our volcano."
    tr "Come, let me escort you two. We are already late."


label next:

    scene bg volcano with dissolve

    n "Due to the time restraints, this is the end of the presentation game."

label end:

    return
