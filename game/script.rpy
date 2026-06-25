define f = Character("??", who_prefix="Forgotten - ")
define n = Character("Narrator", color="#C8FFC8")

label start:
    n "You wake up in the middle of a field,"
    n "The feel of grass blessing your hands, the sound of birds tweeting engulfing your ears, and the smell of nature filling your lungs."
    n "And the last thing you remember is..."
    n "Dying? But how..."
    n "You've forgotten how you died..."
    n "In fact, you've forgotten everything of your life..."
    n "Almost as if you never lived...{p}Just died."
    n "And this place?{p}This is a place where the forgotten reside."
    menu:
        "Head towards..."
        "What appears to be a wreckage of a ship, split in two.":
            call titanic
        "A cave with a warm glow extruding from inside.":
            call cube
    return

label titanic:
    n "A strange ship sits before you, frost encroaching the hull - both parts."
    n "The reminants of centuries ago."
    n "Seems it was called the \"Titanic\"..."

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
            f "OWCH!"
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
            f "OWCH!"
        "Assess the shape of it.":
            n "It appears to be a cube."
            f "Hmm... this feels like a cube..."
            menu:
                "Try do a handstand on it. (I know you want to.)":
                    n "You do it!"
                    f "YES! This is one happy thanksgiving."
                    n "And with that final word, it becomes visible, shimmering and shaking."
                    f "AH!"
                    n "You fall off the cube."
