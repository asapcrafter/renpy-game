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

        # The first customer of the day
        label professor_one:
            
            define t = Character("Professor", who_color="#c8ffc8")

            "The door chime rings again, pulling you from your thoughts. As you look up, your eyes widen in surprise."

            "{i}With a stack of ungraded papers under one arm and a weary smile on his face, it's Professor Lewis - the one who teaches your challenging, yet fascinating, Philosophy class.{/i}"

            "Professor Lewis" "Ah, what a pleasant surprise! It's nice to see one of my students outside of the classroom."

            "{i}You greet him with a smile, feeling a mix of surprise and a slight nervousness.{/i}"

            player "Hello, Professor Johnson. It's nice to see you too. What can I get you today?"

            label Professor_D1:
                menu:
                    t "Americano. Splash of oat milk."
                    "How's your day been? I took your midterm earlier and it was pretty hard.":
                        jump Professor_D1R4
                    "Coming right up. Should be about 5 minutes.":
                        jump Professor_D1R33
            
            label Professor_D1R4:
                menu:
                    t "Oh yeah, I remember just grading yours before coming here."
                    "How did I do?":
                        jump Professor_D1R9
                    "Oh really?":
                        jump Professor_D1R7
            
            label Professor_D1R7:
                menu:
                    t "Yeah. I'll give them back tomorrow. How much longer for the coffee?"
                    "Coming up right now.":
                        jump Professor_D1R30
            
            label Professor_D1R9:
                menu:
                    t "You did alright. I'm not going to curve it, and it seemed like you grasped the material sufficiently."
                    "Could you tell me what letter grade I got?":
                        jump Professor_D1R12
                    "Oh, okay. Were the rest of the tests generally ok?":
                        jump Professor_D1R11

            label Professor_D1R11:
                menu:
                    t "I pride myself on having a difficult class, where only the best get an A."
                    "I look forward to seeing if I'm one of the best.":
                        jump Professor_D1R15
                    "That seems a little harsh and unfair.":
                        jump Professor_D1R19
            
            label Professor_D1R15:
                menu:
                    t "That's a good attitude to have."
                    "Here's your coffee.":
                        jump Professor_D1R31
            
            label Professor_D1R19:
                menu:
                    t "You are the embodiment of the classic entitled student. Always asking for an A and not working for it."
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
                menu:
                    t "You're not allowed to ask me for your grade before I hand the tests back to everyone. How much longer on the coffee?"
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

            label Professor_D1R33:
                "Your professor takes his Americano from you and leaves the coffee shop."
                "{i}He looked unamused. Perhap you should have tried starting a conversation with him.{/i}"
                jump end

            label end:
                "You check if the professor left anything extra"
                if tip == 0: 
                    "Looks like you didn't get anything."
                else:
                    $ tip
                    "Nice! Looks like you got an extra $%(tip)d"
                    "You now have a balance of $%(balance)d" 
                $ balance += tip
                $ tip = 0

        jump karen_one

        label karen_one:
            define k = Character("Karen", who_color="#c8ffc8")

            "As you stand behind the counter, the door chime rings, announcing the arrival of a new customer."

            "{i}Tightly curled hair, oversized sunglasses perched on her head, and an aura of entitlement - there's no mistaking it. This is a 'Karen'.{/i}"

            k "I'd like to place an order, but make sure it's exactly how I want it."

            "{i}You plaster on your best customer service smile, ready for the challenge.{/i}"

            player "Of course, ma'am. We aim to provide the best service. What can I get you today?"

            label Karen_D1:
                menu:
                    k "I'll have a venti Strawberry Frappuccino"
                    "We actually don't serve Frappuccinos, but there is a Starbucks down the street that does.":
                        jump Karen_D1R1
                    "We actually don't serve Frappuccinos, and we've run out of Strawberry syrup. Is there anything else I can make you?":
                        jump Karen_D1R4
            
            label Karen_D1R1:
                menu:
                    k "That's not true! My friend told me that you served Frappuccinos here."
                    "We do not. Your friend was wrong.":
                        jump Karen_D1R5
                    "I'm sorry, we do not serve Frappuccinos.":
                        jump Karen_D1R7

            label Karen_D1R4:
                menu:
                    k "Well, just make me a Frappuccino with blueberry syrup instead."
                    "I've already told you we don't make Frappuccinos. We cannot serve you a bluberry Frappuccino.":
                        jump Karen_D1R10
                    "We can't make a Frappuccino, but we can make you a blueberry smoothie instead, with real blueberries.":
                        jump Karen_D1R9
            
            label Karen_D1R10:
                menu:
                    k "This is ridiculous. I'd like to speak to your manager."
                    "I am the manager of this coffee shop.":
                        jump Karen_D1R11
                    "Ok. Let me go grab her for you.":
                        jump Karen_D1R17

            label Karen_D1R11:
                menu:
                    k "Stop lying to me and go get your manager."
                    "I'm not lying. I am the manager and I'm telling you we can't serve your order.":
                        jump Karen_D1R16
                    "You're right, I'm sorry. Let me go grab her for you.":
                        jump Karen_D1R17

            label Karen_D1R5:
                menu:
                    k "You've never met my friend. You don't even know that."
                    "Yes, I do. I work here and I know what we offer.":
                        jump Karen_D1R29
                    "I'm sorry, you're right. I've never met your friend. I don't know for sure if we serve Frappuccinos.":
                        jump Karen_D1R27
            
            label Karen_D1R27:
                menu:
                    k "I'm in a hurry. Just make me a latte now."
                    "One latte coming up! Sorry for the delay.":
                        jump Karen_D1R28

            label Karen_D1R29:
                menu:
                    k "You're being very disrespectful. Let me speak to your manager."
                    "No, I'm not. My manager is not available right now.":
                        jump Karen_D1R16
                    "You're right, I'm sorry. Let me speak to my manager.":
                        jump Karen_D1R17

            label Karen_D1R17:
                menu:
                    k "Thank you. I will be waiting."
                    "I've just spoken to my manager, and it seems we can make you a Frappuccino. Sorry for the delay.":
                        jump Karen_D1R20

            label Karen_D1R9:
                k "Ok, that's good. Thank you"
                "You hand her the blueberry Frappuccino. She smiles, takes the drink from you, and leaves the coffee shop."
                $ tip += 2
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
                $ tip += 3.50
                jump end_karen

            label Karen_D1R7:
                "She gives you a disgruntled look and leaves the coffee shop."
                jump end_karen

            label end_karen:
                "You feel relieved now that she's gone."
                "You check if the lady left anything extra"
                if tip == 0: 
                    "Looks like you didn't get anything."
                else:
                    $ tip
                    "Nice! Looks like you got an extra $%(tip)d. Perhaps she's not as bad as you thought."
                    "You now have a balance of $%(balance)d" 
                $ balance += tip
                $ tip = 0


        jump parent
        
        label parent:
            define p = Character("Parent", who_color="#c8ffc8")

            label Parent_D1:
                menu:
                    p "Hi, can I get a small black coffee? How are you?"
                    "I'm good, how are you?":
                        jump Parent_D1R4
                    "Of course. I'm alright, thanks for asking.":
                        jump Parent_D1R5
            
            label Parent_D1R4:
                p "Good, thanks."
                menu:
                    "Here's your black coffee. Thanks for stopping by.":
                        jump Parent_D1R40
            
            label Parent_D1R5:
                menu:
                    p "Yeah, I'm glad that you're pulling through. My son hasn't been too happy here. He's a Freshman."
                    "Oh, I'm sorry to hear that.":
                        jump Parent_D1R7
                    "Oh, that sucks. I'm surprised he feels that way.":
                        jump Parent_D1R9

            label Parent_D1R7:
                menu:
                    p "It's alright, it's just tough to see him be so upset."
                    "Yeah, I know the feeling. College can be difficult. There are some resources at the school if he every needs any help.":
                        jump Parent_D1R13
                    "He should just cheer up. UCSB is a beautiful place to be at.":
                        jump Parent_D1R11

            label Parent_D1R9:
                p "Why is that?"
                menu:
                    "UCSB is like the most pleasant place in the world. It would be hard to feel depressed here.":
                        jump Parent_D1R11
                    "There are a lot of resources for him that UCSB provides, that's all.":
                        jump Parent_D1R13
            
            label Parent_D1R11:
                p "That's a really ignorant way of thinking about mental health."
                menu:
                    "Nah, I know about mental health. I've dealt with my own anxiety issues.":
                        jump Parent_D1R15
                    "Yeah, you're right. I'm sorry. I hope your son feels better soon.":
                        jump Parent_D1R21
            
            label Parent_D1R13:
                p "That's good to hear. Can you point me to some of those resources?"
                menu:
                    "Yes, I'd love to. Let me write down the UCSB conseling services number. Hopefully this can help your son.":
                        jump Parent_D1R23
                    "Uh, sure, but they kinda suck.":
                        jump Parent_D1R25

            label Parent_D1R23:
                p "Thanks for all your help. This was a wonderful service."
                jump Parent_D1R42
            
            label Parent_D1R25:
                p "What do you mean?"
                menu:
                    "Nothing. Regardless, I can give you their contact anyways to see if your son finds them more useful than I did.":
                        jump Parent_D1R28
                    "They tend to ignore the students' mental health needs.":
                        jump Parent_D1R29
                
            label Parent_D1R28:
                p "Thank you."
                jump Parent_D1R40

            label Parent_D1R29:
                p "Well, if the mental health support system is that terrible, I might as well pull my son from UCSB. Thanks for the coffee."
                jump Parent_D1R41

            label Parent_D1R15:
                p "Well, I'm sorry to hear that, but you don't know more about my son's mental issues than I do."
                menu:
                    "Uh, ok. Here's your coffee. I'm sure your son is doing fine.":
                        jump Parent_D1R20
                    "You're right. I'm sorry about your son. I hope he can feel better soon.":
                        jump Parent_D1R21

            label Parent_D1R20:
                p "You are really inconsiderate. I have no idea how you got accepted here."
                "The parent quickly pays and doesn't leave anything extra"
                jump Parent_D1R41

            label Parent_D1R21:
                p "It's ok. Thanks for the coffee. It was nice to at least talk to someone, even though it seems you can be a little inconsiderate at times."
                tip += 1
                jump Parent_D1R40

            label Parent_D1R41:
                "The parent quickly pays and doesn't leave anything extra"
                "She angrily takes the coffee from you and leaves the coffee shop in a hurry."
                jump end_parent

            label Parent_D1R40:
                "She takes the coffee from you and exits the coffee shop."
                tip += 2
                jump end_parent
            
            label Parent_D1R42:
                "She takes the coffee from you while giving you a smile and leaves the coffee shop feeling a little better than before."
                tip += 5
                jump end_parent

            label end_parent:
                if tip == 0: 
                    "It would have been nice if you received something extra"
                else:
                    $ tip
                    "Nice! Looks like you got an extra $%(tip)d."
                    "You now have a balance of $%(balance)d" 
                $ balance += tip
                $ tip = 0

    return


