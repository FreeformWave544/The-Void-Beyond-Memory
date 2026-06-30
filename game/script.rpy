define f = Character("??", who_prefix="Forgotten - ")
define n = Character("Narrator", color="#C8FFC8")
define c = Character("INARI", color="#ecc2ff")
define a = Character("AMI", color="#dd1f3f")
default cube = False
default ami = False
default inventory = []
image bg_black = "#000000a1"

label start:
    nvl clear
    Character("???", kind=nvl) "Yes..."
    Character("???", kind=nvl) "Go to sleep..."
    Character("???", kind=nvl) "And wake up amongst them..."
    nvl clear
    $ config.menu_include_disabled = True
    n "You wake up in the middle of a field,"
    n "The feel of grass blessing your hands,{p}the sound of birds tweeting engulfing your ears,{p}and the smell of nature filling your lungs."
    n "And the last thing you remember is..."
    n "Dying? But how..."
    n "You've forgotten how you died..."
    n "In fact, you've forgotten everything of your life..."
    n "Almost as if you never lived...{p}Just died."
    n "And this place?{p}This is a place where the forgotten reside."
    Character(f, kind=nvl) "Who am I?{nw=0.3}"
    Character(f, kind=nvl) "Where am I?{nw=0.3}"
    Character(f, kind=nvl) "Why am I stranded?{nw=0.8}"
    while True:
        menu:
            "Head towards..."
            "What appears to be a wreckage of a ship, split in two." if not "HeS" in inventory:
                call titanic
            "A cave with a warm glow extruding from inside." if not cube:
                call cubeCave
            "The big building that seems you cannot return to here from...":
                if cube:
                    jump theWallOfGone
                else:
                    call pitOfGoing
                    $ break
    n "..."
    return

label titanic:
    n "A strange ship sits before you, frost encroaching the hull - both parts."
    n "The remnants of centuries ago."
    n "Seems it was called the \"Titanic\"..."
    menu:
        "Look inside.":
            call HS
        "Walk away":
            pass
    n "You head back to see what else there is..."
    return

label HS:
    n "Upon searching one of the cabins, you find a CD disk - archaic but working - and you can make out a few of the letters..."
    n "Although said letters are in a different, ancient language, you did learn some letters back in the school."
    n "Primarily: __art_to__er _ore_er"
    menu:
        "Ask INARI." if cube:
            c "*Floats over to the disk.*{p}This appears to be a film from the year '2026'"
            c "It was under the genre of 'romance' and was heavily thought over at the time, everyone wanting a copy."
            c "Although I am uncertain on what it says."
            menu:
                "Take it.":
                    n "You place it carefully in your pocket"
                    $ inventory.append("HeS")
                "Leave it.":
                    n "You ignore it."
        "Take it.":
            n "You place it carefully in your pocket"
            $ inventory.append("HeS")
        "Leave it.":
            n "You ignore it."
    return

label cubeCave:
    n "As you approach the cave, the glow gets more and more... {w=1.5}green?"
    menu:
        "Proceed...":
            pass
        "Retreat...":
            return
    n "Upon entering the cave, the source of the glow seems to be... {p}everywhere?{p}And yet nowhere?"
    menu:
        "Run your hands across the wall.":
            f "OUCH!"
            n "Your hand hits a sharp rock, and you get a small cut."
            n "You leave the cave for better lighting to assess the wound"
            return
        "Run around like a headless chicken.":
            n "Running around, you chance upon an invisible object in the middle of the room."
            f "OWCH!"
            n "You stumble back, confused by this strange encounter."
    menu:
        "Try punch where you saw it.":
            n "Idiot."
            f "OUCH!"
        "Assess the shape of it.":
            n "It appears to be a cube."
            f "Hmm... this appears to be a cube..."
            menu:
                "Try do a handstand on it. (I know you want to.)":
                    n "You do it!"
                    f "YES! This is one happy thanksgiving."
                    n "And with that final word - seemingly the activation keyword - it becomes visible, shimmering and shaking."
                    $ cube = True
                    f "AHHH!"
                    n "You fall off the cube.{p}And for some reason, inexplicable to you, you don't end up \"breaking many of your bones\"."
                    n "Almost as if it weren't that far of a fall, and you didn't just ragdoll, but rather landed like a normal person."
                    "Cube" "Greetings... human?"
                    "Cube" "I am the Infinite Archive."
                    f "Infinite Archive, eh? Hmmm... {w=1.0}IN-finite AR-chI-ve...{p}{w=1.0}INARI!{p}I'll call you INARI."
                    c "You do not like Infinite Archive? How peculiar..."
                    c "Tell me, human. What is the year?"
                    menu:
                        "Lie.":
                            f "I think it's... 1534"
                            c "How strange..."
                            c "I was deactivated 2253."
                            c "Now. The truth without inconsistencies?"
                        "Truth.":
                            pass
                    f "I... actually cannot remember..."
                    c "You cannot remember?"
                    f "No..."
                    c "Is there any explanation to this?"
                    f "No..."
                    c "And what is your name?"
                    f "No... I don't *remember*!"
        "Try smash it with a rock.":
            n "As the rock makes contact...{p}And... {w=0.2}it doesn't? It runs through where the cube was merely a moment ago."
            menu:
                "Try to find it again.":
                    n "You search and you search yet to no avail.{p}You look and you look yet you're blind to the cube,{p}And you notice the green light is now... gone?"
                    return
                "Leave the cave...":
                    return
    return

label pitOfGoing:
    n "As you approach the building, squinting to try assess the size of it, the ground beneath you cracks."
    n "Then crumps and collapses."
    n "You fall through, falling and falling..."
    n "And falling..."
    n "..."
    n "..."
    n "Then..."
    n "SPLAT!{p}You land in a pile of slime."
    menu:
        "Light a match...":
            n "Looking around with the match, you see you're in a cave, covered in cobwebs,"
            n "And looking down, you see it's not the green of slime..."
            n "It's the red of blood!{p}And the organs of humans!"
            f "WHAT THE—?!"
            n "You drop the match in fright, and the blood immediately extinguishes it, plummeting you back into darkness..."
            n "..."
            f "HELP! SOMEBODY!"
            f "HELP!"
            f "..."
            n "No use.{p}No Response..."
            n "Then suddenly you feel something brush against your feet."
            n "Frozen in fear, you feel it crawl up your body, until it reaches your hand."
            n "And then it starts to glow... a calming, green glow."
            f "What... what are you?"
            a "Ami! Ami!"
            f "Ami, eh? Is that all you can say?"
            a "AMI! *Climbs your arm, onto your shoulder, and nuzzles your cheek.*"
            $ ami = True
            f "Ami it is, then."
        "Try break free...":
            n "After lots of struggle, you manage to do absolutely nothing."
            n "And then you hear it."
            n "The faint clicking of a spider."
            n "Then another."
            n "And another."
            n "And then your ears are filled, cannal to cannal, with clicking and hissing."
            n "You try to speak, but webs wrap your mouth too tight."
            n "You try to move but blood - especially this blood - is much, much thicker than water."
            n "But you can still feel."
            n "And you feel leg after leg crawling up your arms."
            n "And teeth gnawing at your legs."
            
    return

label theWallOfGone:
    n "As you approach the building, you try to see the size..."
    n "But your eyes won't let you."
    c "Do buildings usually feel impossible to visualise?"
    f "No... no they do not..."
    n "As you enter the double doors, you see rows upon rows of..."
    n "Bookshelves?"
    n "Some books are missing covers, others the blurb, and others... others are starting to gather dust. But..."
    n "But a rare few are incomplete, yet are gathering dust."
    c "This books appear to be stories of forgotten lives. I'd say those incomplete are still remembered..."
    c "So legends still exist in this day and age? Hmm..."
    f "It appears so..."
    menu:
        "Read a thin book...":
            call earlyBook
        "Read an unfinished book...":
            call newBook
        "Read a legend's life...":
            call legendBook
        "Look for your book...":
            c "Human, what are you looking for?"
            f "My book."
            c "You realise this library is so incredibly large it will be nigh on impossible to find any one specific book?"
            c "Your cravings for needless knowledge are futile."
    menu:
        "Read a thick book...":
            call thickBook
        "Read a golden book...":
            call goldenBook
        "Read a torn up book...":
            call tornBook
    n "A small voice echoes suddenly."
    "???" "Hello? Is anybody there? I'm alone... I don't remember anything..."
    menu:
        "Scream like a hooligan...":
            pass
        "Scream like a seagull...":
            pass
        "Scream like a bald eagle...":
            n "You can almost hear the American anthem..."
        "Scream like a cup'a'tea...":
            n "You can almost hear the British anthem... (we have one?)"
        "Scream like a chair getting crushed in a trash compactor...":
            n "You can almost hear the wood creaking..."
    return

label thickBook:
    c "From what I'm seeing, this is the book of..."
    c "\"Sir David Attenborough\""
    f "Wait... THE Sir David Attenborough?"
    c "Yes - the natura—"
    f "I'm joking. I forgot everything, remember? Or did you forget that?"
    f "I've no clue who he is nor any care to find out."
    n "You put the book lazily back on the shelf."
    n "[c.name] just floats there... unspeaking... unmoving..."
    f "Inari? You 'aight, mate?"
    c "Sir David Attenborough was a legend. Someone who—"
    f "A legend I do not remember, a legend who—"
    f "Wait... I do... I think I remember him... a natural historian? Legendary broadcaster?"
    c "Indeed... but how?"
    f "I guess he will always be in our hearts, even if our minds are blind to him.."
    c "The reason the book is so think is that—"
    f "Is that he lived to over 100."
    c "Yes..."
    return

label goldenBook:
    f "Hmm... this cover."
    f "It shines without reflection,"
    f "Persists without tear,"
    f "Not a web from any of the spiders."
    f "As if even arachnids respect the life contained..."
    n "Opening the first page, you look for the name."
    n  "A name that is not to be found."
    f "The name is missing..."
    c "But I already know whom this is writing..."
    f "So do I..."
    f "A person so influential they've transcended memory."
    f "Even for those who forget humanity, they still..."
    c "... they still remember what humanity became from this true legend."
    f "Indeed..."
    return

label tornBook:
    n "The cover held on by nothing more than a thread."
    n "The pages torn and few."
    n "Other ripped out to shreds."
    f "Who...? Why...?"
    n "..."
    c "Time is not this cruel."
    c "Humanity."
    c "Humanity is this cruel."
    c "Not the individual humans - but rather the collective society."
    f "A group... a group of people done this with full intent?"
    n "Opening the first remaining page, you start to read."
    nvl clear
    Character("", kind=nvl) "\"They laughed...\""
    Character("", kind=nvl) "\"They sneered...\""
    Character("", kind=nvl) "\"They took her...\""
    Character("", kind=nvl) "\"My daughter. {w=0.7}They took her.\""
    Character("", kind=nvl) "\"My promise \""
    n "The words end before the sentence - or even page, for that matter - should."
    nvl clear
    return

label earlyBook:
    c "Human... I'd urge you not to read that one."
    n "And as you flick through the pages, the sound of silence intensifies."
    n "Your heartbeat thumps every beat."
    n "Your eyes well up..."
    f "They... they were so young..."
    f "Some homework scribbled last minute..."
    f "A birthday card..."
    c "Why do humans bother with such needless writings?"
    f "A journal..."
    f "..."
    f "Why did they choose to...{p}why... why did they dance the edge of life, stepping on death's feet?{p}Tempt fate in such a way?"
    f "Trust a friend to catch them when they fell..."
    f "A life marked by  suffering... cut short by the burdens of life... yet forgotten all too quickly..."
    c "If it's any consolation, human, I'd estimate this to have been at least five thousand years ago, and chance to be more suffering if they lived than if not."
    return

label newBook:
    n "Each page seems brighter than the prior."
    n "Each word more promising than the last."
    n "Each... each heart more loving than the other..."
    n "A mother who loves them dearly."
    n "A father who cherishes their very existence."
    n "A child whose life has just begun. A life of joy."
    f "Inari..."
    c "Yes, human? Why are you sad?"
    f "No... not sad... happy... so, so overwhelmingly happy."
    f "I realise now how... how inconceivably precious each human life is."
    return

label legendBook:
    n "It starts off unlike any life you've ever heard of."
    n "A kid getting anything and everything they want."
    n "A bully to many. A friend to few."
    n "They're a legend for being popular online."
    n "What did they do online? Social media - posting themself doing idiotic things for views."
    c "Strange... a teenager risks their life countless times to... hope a statistic - a number - is higher than last time?"
    c "And they get paid for that number?"
    c "This is beyond any logic I possess..."
    return