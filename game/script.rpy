# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:
    init:
        image you = "stick.png" 
        image campus = "rsz_ucsb2.jpg"

    scene campus with fade:
    "The sky is a soft blue, the sun peeking over the impressive edifice of the college buildings. Students amble to and fro, textbooks under their arms, laptops in their bags. There's an energy in the air, the promise of possibility."

    "The University of California, Santa Barbara. A sea of knowledge nestled between the ocean and lush, green hills. Every day brings something new - a lecture that changes your perspective, a conversation that challenges your beliefs"

    show stick at center with dissolve
    "And at the heart of it all, there's you. A regular college student with dreams bigger than the campus itself. Juggling between lectures, assignments, and a part-time job at the campus coffee shop."

    "You may be just a speck in the grand scheme of the university life, but who knows? Perhaps the aroma of coffee and late-night cram sessions will lead you to experiences that are anything but ordinary."

    "Welcome to the Arbor cafe. Let's see what brews up!"

    menu:
        "Goto the green room":
            jump green_room
        
        "Goto the red room":    
            jump red_room

    label green_room:
        "You've entered the green room"

    label red_room:
        "You've entered the red room"

    return
