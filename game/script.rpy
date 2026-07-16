define f = Character("??", who_prefix="Forgotten - ")
define n = Character("Narrator", color="#C8FFC8")
define c = Character("INARI", color="#ecc2ff")
define a = Character("AMI", color="#dd1f3f")
default cube = False
default ami = False
default inventory = []

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
                    call theWallOfGone
                else:
                    call pitOfGoing
                    jump end_screen
    return

label titanic:
    n "A strange ship sits before you, frost encroaching the hull - both parts of it."
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
    n "Although said letters are in a different, ancient language, you do recognise some."
    n "Primarily: __art_to__er _ore_er"
    menu:
        "Ask INARI." if cube:
            c "*Floats over to the disk.*{p}This appears to be a film from the year '2026'"
            c "It was under the genre of 'romance' and was heavily fought over at the time, everyone wanting a copy."
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
            n "You leave the cave for better lighting to assess the wound."
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
    n "Then crumbles and collapses."
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
            n "No use.{p}No response..."
            n "Then suddenly you feel something brush against your feet."
            n "Frozen in fear, you feel it crawl up your body, until it reaches your hand."
            n "And then it starts to glow... {w=1.0}a calming, green glow."
            f "What... what are you?"
            a "Ami! Ami!"
            f "Ami, eh? Is that all you can say?"
            a "AMI!"
            n "The cute axolotl climbs your arm, onto your shoulder, and nuzzles your cheek."
            $ ami = True
            f "Ami it is, then."
            f "Ami the Axo."
            n "While you're distracted with Ami, their warmth seems to melt the blood beneath you."
            n "It gets thinner and thinner until you can step free."
            jump GoldenBloodOfAmber
        "Try break free...":
            n "After lots of struggle, you manage to do absolutely nothing."
            jump spider
    return

label spider:
    n "And then you hear it."
    n "The faint clicking of a spider."
    n "Then another."
    n "And another."
    n "And then your ears are filled, canal to canal, with clicking and hissing."
    n "You try to speak, but webs wrap your mouth too tight."
    n "You try to move but blood - especially this blood - is much, much thicker than water."
    n "But you can still feel."
    n "And you feel leg after leg crawling up your arms."
    n "And teeth gnawing at your legs."
    $ inventory.append("dead")
    n "One last scream escapes your throat.{p}Then is cut short."
    jump end_screen

label GoldenBloodOfAmber:
    n "Then suddenly..."
    n "Ami runs off further down the cave."
    menu:
        "Chase after Ami!":
            n "You run and you run — seemingly forever — until you enter a larger cave."
        "Call after Ami!":
            f "Ami! {p}Ami!"
            f "AMI!"
            f "Please!{p}Ami!{w=0.3}PLEASE!"
            n "Your voice echos off the walls of the cave.{p}And then gets called back to you."
            "???" "Ami?{p}Ami...{w=0.3} who's Ami??"
            n "And without thinking,{p}deprived of human contact,{p}You chase the voice."
            jump mysteryVoice
        "Stay where you are.":
            n "You stand still, staring where Ami ran.{p}Confused. {w=0.5}Worried."
            jump spider
    n "The walls veined in gold,{p}A pulsating glow that dazzles you each breath."
    menu:
        "Try scrape out some of the gold.":
            n "As you pull out handfuls of gold, you feel exhilarated."
            n "And it is not a powder of gold, nor solidity of gold."
            n "A greed so deeply rooted in your humanity for you to get blinded from what you're truly holding."
            n "Hundreds of insects and other organism that survived eternities of history, even beyond death."
            n "The blood of hundreds of beings preserved in the blood of trees!"
            n "And this lie of gold..."
            n "In your hands, it starts to burn.{p}The sheer pain is immeasurable."
            f "Oh damn."
            n "And that burning sensation courses through your veins."
            n "And you collapse into a pile of breathless greed."
            $ inventory.append("greed")
            jump end_screen
        "Look closely...":
            f "This is not gold... it is slightly transparent..."
            f "And insects from across time?"
            f "This must be amber... but why...?"
    a "Nips at your ankles, gesturing towards the center of the room where a big obelisk stands."
    f "What... what is that?"
    n "You feel an irresistible urge to approach the obelisk,{p}And as your hand rests on the rough casing you witness a black so deep it rivals that of obsidian."
    menu:
        a "Wiggling up to the obelisk, Ami nibbles at a crack in it running all the way up."
        "Try pry the obelisk open...":
            n "Fitting your fingers in the crack and using the physics of leverage, you manage to have the obelisk fall apart nicely into two pieces."
        "Try break the obelisk open...":
            n "After hours spent tirelessly chipping away at the stone structure, eventually you get it open..."
        "Do the Macarena...":
            f "Heeeyyyyyyyy...{nw=0.5}{p}Macarena!"
            n "And with that... the obelisk cracks open, falling into two near-perfect ovals."
            a "Ami!"
            n "You look down and realise that it was Ami who tore it apart."
            f "Oh...{p}Noooooooo... Macarena!"
        "Move on...":
            n "You slide to the left..."
            n "You slide to the right!"
            n "Criss-Cross!{p}Criss-Cross!"
            f "Cha-Cha real smooth!"
            f "Let's go to work!"
            n "And by vibing to the song, you accidentally head off to work."
            menu:
                n "While driving your car there, you find a fork in the road..."
                "To the left.":
                    n "That is the correct lyric to follow..."
                "Take it back now y'all.":
                    n "WRONG! You can never take it back.{p}You're doomed to forever do the Cha-Cha Slide!"
                "Hands on your knees.":
                    n "Wow. You look like an idiot."
                    n "..."
                    n "Idiot."
                "Get funky with it.":
                    n "You put your hands up in the air... like you just don't care..."
            n "You work tirelessly, throughout day and night. The coldest of colds and the hottest of heatwaves...{p}And then it all ends. You die..."
            n "You sold both your kidneys on the internet..."
            n "What a dumb way to die..."
            n "Idiot."
            jump end_screen
    n "The removal of the obelisk reveals a strange orb, no larger than a football, embedded in one of the halves."
    n "And what is so strange about this orb is that it is an absence of light — where light should be, it is instead absorbed."
    menu:
        "Pick it up...":
            n "Before you can do anything..."
        "Leave it be...":
            n "As you stare at it a moment too long..."
    a "Jumps at the orb, immediately disappearing into The Void Beyond Halves."
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
    c "These books appear to be stories of forgotten lives. I'd say those incomplete are still remembered..."
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
            f "OWOWOWOADSOKOHOWHOWOOHWO"
        "Scream like a seagull...":
            f "MINE! MINE!"
            n "Never do seagulls actually scream near beaches... no, always at random times away from beaches.{p}And you hold true to that pattern."
            f "MINE MINE MINE MINE!!!!"
        "Scream like a bald eagle...":
            f "Ameri{w=0.2}CAW{w=0.5}n!"
            f "CAW!"
            f "SCREEEEE"
            n "You can almost hear the American anthem..."
        "Scream like a cup'a'tea...":
            f "SLLLLLLRRRRRPPPPPPP"
            f "Oh dear, I am horribly sorry. I meant..."
            f "HHHHIISSSSSSSSSSSSSSSSSSSSSSSSSS{p}Other_kettle_sounds.png"
            n "You can almost hear the British anthem... {p}(we have one?)"
        "Scream like a chair getting crushed in a trash compactor...":
            f "CRRRREEEAAAA— {w=0.5}{p}Cracking.sfx{p}Smashing.sfx"
            n "You can almost hear the wood creaking..."
    n "..."
    n "Silence succeeds your unholy noise."
    n "Then..."
    "???" "AAAAAHHHHHHHHHHHHH"
    n "The voice screams, and grows distant."
    menu:
        "Put up chase...":
            jump mysteryVoice
        "Ignore the voice... (Requires no morals)" if False:
            n "How'd ya get here? Are you perhaps cheating?"
            $ renpy.full_restart()
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
    f "I guess he will always be in our hearts, even if our minds are blind to him..."
    c "The reason the book is so thick is that—"
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
    c "But I already know who this is writing..."
    f "So do I..."
    f "A person so influential they've transcended memory."
    f "Even for those who forget humanity, they still..."
    c "... they still remember what humanity became from this true legend."
    f "Indeed..."
    return

label tornBook:
    n "The cover held on by nothing more than a thread."
    n "The pages torn and few."
    n "Others ripped out to shreds."
    f "Who...? Why...?"
    n "..."
    c "Time is not this cruel."
    c "Humanity."
    c "Humanity is this cruel."
    c "Not the individual humans - but rather the collective society."
    f "A group... a group of people did this with full intent?"
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

label mysteryVoice:
    n "You chase the voice until you end up in..."
    n "In a strange room made of what seems to be obsidian..."
    if cube:
        n "And a cardboard box full of items sitting in the middle of it."
        c "This appears to be a primitive human 'Lost and Found' system. Before the invention of the Ever-Tracking."
        n "And there's the person you were chasing, looking through it."
        n "A girl, no older than 15, and eyes made of years of fear and urgency."
        f "What are... what are you doing?"
        "Girl" "Can't let them... can't let them become forgotten!"
        "Girl" "Can't have them end up like Daisy!"
        f "Who was Daisy? What happened to her?"
        n "The girl ignores, focusing on sorting the items."
        f "Too hard of a topic? Okay."
        f "What is this place?"
        "Girl" "This place?"
        "Girl" "This place..."
        "Girl" "Home."
        n "A warm, small smile steals her frantic expression for but a second"
        n "Then she goes back to sorting."
    elif ami:
        n "And a big nest full of items sitting in the middle of it."
        f "Is this... 'Lost and Found'?"
        a "Ami jumps into the nest and lays down next to the person you were just chasing.{P}Who's now sleeping in the nest, amongst toys."
        n "A girl, no older than 15, laying there, peacefully without any fear."

    else:
        n "Yet you're here alone. You decide to head back."
    jump end_screen

label end_screen:
    n "I forgot why you came here,{p}but let's see what you remember."
    $ gone = False
    while not gone:
        menu:
            "CD" if "HeS" in inventory:
                "It is an archaic CD in a language, where the title, partially translated is:{p}__art_to__er _ore_er"
            "Cube" if cube:
                "The \'Infinite Archive\' - a cube that bends the fabric of life as linear time."
            "Leave":
                $ gone = True
    if "dead" in inventory or "greed" in inventory:
        menu:
            "Choose your ending..."
            "Death." if "dead" in inventory:
                "No matter what happened, you died."
                "And in death, memories don't follow you."
                "You remember nothing."
            "Greed." if "greed" in inventory:
                "Your needless want for more of nothing was the doom of you."
                "Wasted for nothing."
        return
    menu:
        "Choose your ending..."
        "\"Content With Life\" ending..." if ami:
            a "Scales your arm and hugs your neck."
            "Peace... Calm...{w=1.0} Friendship."
            "Y'know, the silent "
        "\"The Meaning of Life\" ending..." if cube:
            c "Hmm."
            c "Understandable."
            c "Mortality is always the doom of humanity — no matter how good or safe the life lived."
    return
