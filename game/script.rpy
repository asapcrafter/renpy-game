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
        "Start working":
            jump day_one
        
    label day_one:
        init:
            image arbor_outside = "arbor.jpg"
        define alex = Character("Alex", who_color="#c8ffc8")
        define player = Character("Player", who_color="#3340fd")


        scene arbor_outside with fade:
        
        "The Arbor cafe is located in the middle of the campus. It's a small, but it gets busy during the day."
        "You arrive at the campus coffee shop, the aroma of fresh coffee beans filling the air."

        alex "Hey there! You must be the new recruit. Welcome to the team!"
        "{i}The voice is warm and friendly, matching the bright smile on the coworker's face.{/i}"
        
        alex "I'm Alex, by the way. I'll be showing you the ropes today."
        
        player "Nice to meet you, Alex."

        alex "Nice to meet you too! Alright, so your main job here will be taking orders from customers. Just take their order, pass it onto the barista, and keep things moving."

        alex "And remember, a friendly smile can go a long way. We rely on tips, after all. The friendlier you are, the more tips you're likely to get. Don't be afraid to strike up a conversation, just keep it light and professional."

        "{i}You nod, taking in the advice.{/i}"

        alex "Great! You'll do just fine. Let's get started then, shall we?"

        "Your first customer of the day arrives"

        jump professor_one

        label professor_one:
            define t = Character("Professor", who_color="#c8ffc8")
            label Professor_D1:
                player "Hello, what can I get for you?"
                t "Americano. Splash of oat milk."
                menu:
                    t "Americano. Splash of oat milk."
                    "How's your day been? I took your midterm earlier and it was pretty hard.":
                        jump Professor_D1R4
                    "Coming right up. Should be about 5 minutes.":
                        jump Professor_D1R30
            
            label Professor_D1R4:
                menu:
                    t "Oh yeah, I remember just grading yours before coming here."
                    "How did I do?":
                        jump Professor_D1R9
                    "Oh really?":
                        jump Professor_D1R7
            
            label Professor_D1R7:
                t "Yeah. I'll give them back tomorrow. How much longer for the coffee?"
                menu:
                    "Coming up right now.":
                        jump Professor_D1R30
            
            label Professor_D1R9:
                t "You did alright. I'm not going to curve it, and it seemed like you grasped the material sufficiently."
                menu:
                    "Could you tell me what letter grade I got?":
                        jump Professor_D1R12
                    "Oh, okay. Were the rest of the tests generally ok?":
                        jump Professor_D1R11

            label Professor_D1R11:
                t "I pride myself on having a difficult class, where only the best get an A."
                menu:
                    "I look forward to seeing if I'm one of the best.":
                        jump Professor_D1R15
                    "That seems a little harsh and unfair.":
                        jump Professor_D1R19
            
            label Professor_D1R15:
                t "That's a good attitude to have."
                menu:
                    "Here's your coffee.":
                        jump Professor_D1R31
            
            label Professor_D1R19:
                t "You are the embodiment of the classic entitled student. Always asking for an A and not working for it."
                menu:
                    "I'm willing to work for it. I'd just like to know about the grading distributions beforehand.":
                        jump Professor_D1R24
                    "I'm not unmotivated. This is just an irrational system on which to grade your class.":
                        jump Professor_D1R23

            label Professor_D1R24:
                t "Good, I'm glad you're willing to put in the work."
                jump Professor_D1R30
            
            label Professor_D1R23:
                t "You know what's irrational. The awful grade you're going to receive on your test tomorrow."
                jump Professor_D1R32

            label Professor_D1R12:
                t "You're not allowed to ask me for your grade before I hand the tests back to everyone. How much longer on the coffee?"
                menu:
                    "Coming up right now. Here you go.":
                        jump Professor_D1R30

            label Professor_D1R30:
                "Your professor takes his Americano from you and leaves the coffee shop."
                jump end
            
            label Professor_D1R31:
                p "Thanks."
                "Your professor thanks you for his coffee and leaves the coffee shop."
                jump end

            label Professor_D1R32:
                "Your professor angrily takes his Americano from you and storms out of the coffee shop."
                jump end

            label end:
                return

            return


    return


