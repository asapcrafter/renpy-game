# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




# The game starts here.

label start:
    $ global tip
    $ global balance
    $ tip = 0
    $ balance = 0

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

            "The door chime rings again, pulling you from your thoughts. As you look up, your eyes widen in surprise."

            "{i}With a stack of ungraded papers under one arm and a weary smile on his face, it's Professor Lewis - the one who teaches your challenging, yet fascinating, Philosophy class.{/i}"

            "Professor Lewis" "Ah, what a pleasant surprise! It's nice to see one of my students outside of the classroom."

            "{i}You greet him with a smile, feeling a mix of surprise and a slight nervousness.{/i}"

            player "Hello, Professor Johnson. It's nice to see you too. What can I get you today?"

            label Professor_D1:
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
                $ tip += 2
                jump end
            
            label Professor_D1R31:
                p "Thanks."
                "Your professor thanks you for his coffee and leaves the coffee shop."
                $ tip += 4
                jump end

            label Professor_D1R32:
                "Your professor angrily takes his Americano from you and storms out of the coffee shop."
                jump end

            label end:
                "You check if the professor left anything extra"
                if tip == 0: 
                    "Looks like you didn't get anything."
                else:
                    $ tip
                    "Nice! Looks like you got an extra $%(tip)d"

        jump karen_one

        label karen_one:
            define k = Character("Karen", who_color="#c8ffc8")

            "As you stand behind the counter, the door chime rings, announcing the arrival of a new customer."

            "{i}Tightly curled hair, oversized sunglasses perched on her head, and an aura of entitlement - there's no mistaking it. This is a 'Karen'.{/i}"

            k "I'd like to place an order, but make sure it's exactly how I want it."

            "{i}You plaster on your best customer service smile, ready for the challenge.{/i}"

            player "Of course, ma'am. We aim to provide the best service. What can I get you today?"

            label Karen_D1:
                k "I'll have a venti Strawberry Frappuccino"
                menu:
                    "We actually don't serve Frappuccinos, but there is a Starbucks down the street that does.":
                        jump Karen_D1R1
                    "We actually don't serve Frappuccinos, and we've run out of Strawberry syrup. Is there anything else I can make you?":
                        jump Karen_D1R4
            
            label Karen_D1R1:
                k "That's not true! My friend told me that you served Frappuccinos here."
                menu:
                    "We do not. Your friend was wrong.":
                        jump Karen_D1R5
                    "I'm sorry, we do not serve Frappuccinos.":
                        jump Karen_D1R7

            label Karen_D1R4:
                k "Well, just make me a Frappuccino with blueberry syrup instead."
                menu:
                    "I've already told you we don't make Frappuccinos. We cannot serve you a bluberry Frappuccino.":
                        jump Karen_D1R10
                    "We can't make a Frappuccino, but we can make you a blueberry smoothie instead, with real blueberries.":
                        jump Karen_D1R9
            
            label Karen_D1R10:
                k "This is ridiculous. I'd like to speak to your manager."
                menu:
                    "I am the manager of this coffee shop.":
                        jump Karen_D1R11
                    "Ok. Let me go grab her for you.":
                        jump Karen_D1R17

            label Karen_D1R11:
                k "Stop lying to me and go get your manager."
                menu:
                    "I'm not lying. I am the manager and I'm telling you we can't serve your order.":
                        jump Karen_D1R16
                    "You're right, I'm sorry. Let me go grab her for you.":
                        jump Karen_D1R17

            label Karen_D1R5:
                k "You've never met my friend. You don't even know that."
                menu:
                    "Yes, I do. I work here and I know what we offer.":
                        jump Karen_D1R29
                    "I'm sorry, you're right. I've never met your friend. I don't know for sure if we serve Frappuccinos.":
                        jump Karen_D1R27
            
            label Karen_D1R27:
                k "I'm in a hurry. Just make me a latte now."
                menu:
                    "One latte coming up! Sorry for the delay.":
                        jump Karen_D1R28

            label Karen_D1R29:
                k "You're being very disrespectful. Let me speak to your manager."
                menu:
                    "No, I'm not. My manager is not available right now.":
                        jump Karen_D1R16
                    "You're right, I'm sorry. Let me speak to my manager.":
                        jump Karen_D1R17

            label Karen_D1R17:
                k "Thank you. I will be waiting."
                menu:
                    "I've just spoken to my manager, and it seems we can make you a Frappuccino. Sorry for the delay.":
                        jump Karen_D1R20

            label Karen_D1R9:
                k "Ok, that's good. Thank you"
                "You hand her the blueberry Frappuccino. She smiles, takes the drink from you, and leaves the coffee shop."
                jump end_karen
            
            label Karen_D1R16:
                k "This is the worst coffee shop I've ever been to. I'm leaving."
                "She storms out of the coffee shop angrily."
                jump end_karen

            label Karen_D1R28:
                "You hand her the latte. She gives you a disgruntled look, takes the drink from you, and leaves the coffee shop."
                jump end_karen

            label Karen_D1R20:
                k "Ok, that's wonderful."
                "You hand her the Frappuccino. She smiles, takes the drink from you, and leaves the coffee shop."
                jump end_karen

            label Karen_D1R7:
                "She gives you a disgruntled look and leaves the coffee shop."
                jump end_karen
            
    return


