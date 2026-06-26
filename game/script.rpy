define f = Character("??", who_prefix="Forgotten - ")
define n = Character("Narrator", color="#C8FFC8")
define c = Character("INARI", color="#ecc2ff")
default cube = False
default inventory = []

label start:
    $ config.menu_include_disabled = True
    n "You wake up in the middle of a field,"
    n "The feel of grass blessing your hands, the sound of birds tweeting engulfing your ears, and the smell of nature filling your lungs."
    n "And the last thing you remember is..."
    n "Dying? But how..."
    n "You've forgotten how you died..."
    n "In fact, you've forgotten everything of your life..."
    n "Almost as if you never lived...{p}Just died."
    n "And this place?{p}This is a place where the forgotten reside."
    f "Who am I?{nw=0.3}"
    f "Where am I?{nw=0.3}"
    f "Why am I stranded?{nw=0.5}"
    while True:
        menu:
            "Head towards..."
            "What appears to be a wreckage of a ship, split in two." if not "HeS" in inventory:
                call titanic
            "A cave with a warm glow extruding from inside." if not cube:
                call cube
            "The big building that seems you cannot return to here from...":
                jump theWallOfGone
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

label cube:
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
                            c "Now, the truth?"
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
    return

label earlyBook:
    c "Human... I'd urge you not to read that one."
    n "And as you flick through the pages, the sound of silence intensifies."
    n "Your heartbeat thumps every beat."
    n "Your eyes well up..."
    f "They... they were so young..."
    f "Why did they choose to... why... why did they dance the edge of life, stepping on death's feet?{p}Tempt fate in such a way?{p}Trust a friend to catch them when they fell..."
    f "A life of pain and suffering... cut short by the pains of life... yet forgotten all too quickly..."
    c "If it's any consolation, human, I'd estimate this to have been at least five thousand years ago, and chance to be more suffering if they lived than if not."
    return

label newBook:
    n "Each page seems brighter than the prior."
    n "Each word more promising than the last."
    n "Each... each heart more loving than the other..."
    n "A mother who loves them dearly."
    n "A father who cherishes their very existence."
    n "A child who's life has just begun. A life of joy."
    f "Inari..."
    c "Yes, human? Why are you sad?"
    f "No... not sad... happy... so, so overwhelmingly happy."
    f "I realise now how... how inconceivably precious each human life is."
    return

label legendBook:
    pass