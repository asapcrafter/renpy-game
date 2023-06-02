# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




# The game starts here.

label start:
    $ global tip
    $ global balance
    $ global professor_rate
    $ global karen_rate
    $ global love_rate
    $ global parent_rate
    $ global nerd_rate
    $ global athlete_rate
    $ global day
    $ global total_tip
    $ global rent_paid
    $ global food_paid
    $ global electric_paid
    $ tip = 0
    $ balance = 0
    $ professor_rate = 0
    $ karen_rate = 0
    $ love_rate = 0
    $ parent_rate = 0
    $ nerd_rate = 0
    $ athlete_rate = 0
    $ day = 1
    $ total_tip = 0
    $ rent_paid = 0
    $ food_paid = 0
    $ electric_paid = 0

    screen Day:
        text "{color=#ffffff}Day: [day]{/color}" xpos 0.1 ypos 0.1

    screen Savings:
        text "{color=#ffffff}Savings: $[balance]{/color}" xpos 0.1 ypos 0.2

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

        "Day 1"
        
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

            player "Hello, Professor Lewis. It's nice to see you too. What can I get you today?"

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
                        jump Professor_D1R33

            label Professor_D1R30:
                "Your professor takes his Americano from you and leaves the coffee shop."
                $ professor_rate += 1
                jump end
            
            label Professor_D1R31:
                p "Thanks."
                "Your professor thanks you for his coffee and leaves the coffee shop."
                $ professor_rate += 2
                jump end

            label Professor_D1R32:
                "Your professor angrily takes his Americano from you and storms out of the coffee shop."
                $ professor_rate -= 1
                jump end

            label Professor_D1R33:
                "Your professor takes his Americano from you and leaves the coffee shop."
                "{i}He looked unamused. Perhap you should have tried starting a conversation with him.{/i}"
                jump end

            label end:
                "You check if the professor left anything extra"
                if (professor_rate > 0):
                    $ tip = professor_rate * 5
                if tip == 0: 
                    "Looks like you didn't get anything."
                else:
                    $ tip
                    "Nice! Looks like you got an extra $%(tip)d"
                $ balance += tip
                $ total_tip += tip
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
                $ karen_rate += 1
                jump end_karen
            
            label Karen_D1R16:
                k "This is the worst coffee shop I've ever been to. I'm leaving."
                "She storms out of the coffee shop angrily."
                $ karen_rate -= 2
                jump end_karen

            label Karen_D1R28:
                "You hand her the latte. She gives you a disgruntled look, takes the drink from you, and leaves the coffee shop."
                jump end_karen

            label Karen_D1R20:
                k "Ok, that's wonderful."
                "You hand her the Frappuccino. She smiles, takes the drink from you, and leaves the coffee shop."
                $ karen_rate += 2
                jump end_karen

            label Karen_D1R7:
                "She gives you a disgruntled look and leaves the coffee shop."
                $ karen_rate -= 1
                jump end_karen

            label end_karen:
                "You feel relieved now that she's gone."
                "You check if the lady left anything extra"
                if (karen_rate > 0):
                    $ tip = karen_rate * 5
                if tip == 0: 
                    "Looks like you didn't get anything."
                else:
                    $ tip
                    "Nice! Looks like you got an extra $%(tip)d. Perhaps she's not as bad as you thought."
                $ balance += tip
                $ total_tip += tip
                $ tip = 0

    label night_one:
        scene black

        $ balance += 20
        show screen Day
        show screen Savings

        "You received $20 from your salary. You received $%(total_tip)d in tips. You now have $%(balance)d in savings."

        label one_all_three:
            menu:
                "Rent: -$10":
                    $ balance -= 10
                    $ rent_paid = 1
                    jump one_no_rent
                "Food: -$5":
                    $ balance -= 5
                    $ food_paid = 1
                    jump one_no_food
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump one_no_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_two
        
        label one_no_rent:
            menu:
                "Food: -$5":
                    $ balance -= 5
                    $ food_paid = 1
                    jump one_no_rent_food
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump one_no_rent_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_two

        label one_no_food:
            menu:
                "Rent: -$10":
                    $ balance -= 10
                    $ rent_paid = 1
                    jump one_no_rent_food
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump one_no_food_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_two
        
        label one_no_electric:
            menu:
                "Rent: -$10":
                    $ balance -= 10
                    $ rent_paid = 1
                    jump one_no_rent_electric
                "Food: -$5":
                    $ balance -= 5
                    $ food_paid = 1
                    jump one_no_food_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_two
        
        label one_no_rent_food:
            menu:
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump one_next_day
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_two
    
        label one_no_rent_electric:
            menu:
                "Food: -$5":
                    $ balance -= 5
                    $ food_paid = 1
                    jump one_next_day
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_two

        label one_no_food_electric:
            menu:
                "Rent: -$10":
                    $ balance -= 10
                    $ rent_paid = 1
                    jump one_next_day
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_two
        
        label one_next_day:
            menu:
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_two


    label day_two:
        hide screen Day
        hide screen Savings

        if (rent_paid == 0):
            "You have received a warning from the apartment to pay rent."
            $ rent_paid = -1
        elif (rent_paid == -1):
            "You have been evicted by the apartment for not paying rent."
            return
        else:
            $ rent_paid = 0

        if (food_paid == 0):
            "You feel hungry from not eating last night."
            $ food_paid = -1
        elif (food_paid == -1):
            "You have succumbed to your hunger."
            return
        else:
            $ food_paid = 0

        if (electric_paid == 0):
            "You feel sick from a lack of heat last night."
            $ electric_paid = -1
        elif (electric_paid == -1):
            "You have succumbed to sickness."
            return
        else:
            $ electric_paid = 0

        init:
            image arbor_outside = "arbor.jpg"
        define alex = Character("Alex", who_color="#c8ffc8")
        define player = Character("Player", who_color="#3340fd")
        
        scene arbor_outside with fade:

        "Day 2"

        "You arrive at the campus coffee shop, the aroma of fresh coffee beans filling the air."
        "Alex greets you when you get behind the counter."

        alex "Hey again! Great job yesterday. How did you feel working your first day here?"

        menu:
            "It felt alright. Some of the customers were a bit rude.":
                jump Alex_D2R1
            "It was great! The customers here leave a lot of tips.":
                jump Alex_D2R2

        label Alex_D2R1:
            alex "That's unfortunate to hear. I'm sure our future customers will be nicer. Make sure to watch what you say to some of these customers."
            jump parent_one

        label Alex_D2R2:
            alex "Awesome! It seems like the customers enjoy talking with you. Stay on their good side and I'm sure they'll keep leaving tips."
            jump parent_one
        
        label parent_one:
            define p = Character("Parent", who_color="#c8ffc8")

            "As you stand behind the counter, the door chime rings, announcing the arrival of a new customer."

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
                $ parent_rate += 1
                jump Parent_D1R40

            label Parent_D1R41:
                "The parent quickly pays and doesn't leave anything extra"
                "She angrily takes the coffee from you and leaves the coffee shop in a hurry."
                $ parent_rate -= 2
                jump end_parent

            label Parent_D1R40:
                "She takes the coffee from you and exits the coffee shop."
                jump end_parent
            
            label Parent_D1R42:
                "She takes the coffee from you while giving you a smile and leaves the coffee shop feeling a little better than before."
                $ parent_rate += 2
                jump end_parent

            label end_parent:
                if (parent_rate > 0):
                    $ tip = parent_rate * 5
                if tip == 0: 
                    "It would have been nice if you received something extra"
                else:
                    $ tip
                    "Nice! Looks like you got an extra $%(tip)d."
                $ balance += tip
                $ total_tip += tip
                $ tip = 0

            
        jump love_one

        label love_one:
            define l = Character("Love Interest", who_color="#c8ffc8")

            "As you stand behind the counter, the door chime rings, announcing the arrival of a new customer."

            label Love_D1:
                l "Can I get an iced vanilla latte?"
                menu:
                    "Sure, absolutely. One vanilla latte coming up.":
                        jump Love_D1R4

            label Love_D1R4:
                l "Thanks a bunch!"
                menu:
                    "You're so beautiful, by the way.":
                        jump Love_D1R7
                    "I love your outfit, by the way.":
                        jump Love_D1R8
                    
            label Love_D1R7:
                l "Stop being creepy. I'm just going to take my drink and leave."
                jump Love_D1R28
            
            label Love_D1R8:
                l "Thank you! I thrifted it."
                menu:
                    "It looks great on you.":
                        jump Love_D1R11
                    "Would you like to go thrifting with me sometime? Maybe you can help me pick out some clothes as well.":
                        jump Love_D1R12

            label Love_D1R12:
                l "I'd love that."
                menu:
                    "What's your number? I've written mine on your coffee cup.":
                        jump Love_D1R17
            
            label Love_D1R17:
                l "That's perfect! I'll text you. I'm free Friday."
                jump Love_D1R29
            
            label Love_D1R11:
                l "Uh, thanks."
                menu:
                    "So, uh, can I get your number?":
                        jump Love_D1R15
                    "So, how's your day been?":
                        jump Love_D1R18

            label Love_D1R18:
                l "Uh, pretty good. Been studying a lot."
                menu:
                    "Ahaha, wanna study together sometime?":
                        jump Love_D1R15
                    "Sounds like you're pretty busy.":
                        jump Love_D1R21
            
            label Love_D1R21:
                l "Yeah, I am. Hence why I need the latte."
                menu:
                    "Here's your coffee. I gave you a double shot for the trouble.":
                        jump Love_D1R24
                    "Sounds like you also need my number.":
                        jump Love_D1R15
                
            label Love_D1R24:
                l "Thank you! You're too sweet."
                menu:
                    "I wrote my number on there, in case you'd ever want to hang out.":
                        jump Love_D1R17
                    "Yea thanks. I try to be.":
                        jump Love_D1R27

            label Love_D1R27:
                l "Appreciate you ~ I'm sure Ill see you soon."
                jump Love_D1R29

            label Love_D1R15:
                l "No. Just give me my coffee."
                jump Love_D1R28

            label Love_D1R28:
                "She takes her drink from you and quickly exits the coffee shop."
                jump love_end
            
            label Love_D1R29:
                "She takes her drink from you and gives you a smile. You watch her leave the coffee shop."
                $ love_rate += 1
                jump love_end

            label love_end:
                if (love_rate> 0):
                    $ tip = love_rate * 5
                if tip == 0: 
                    "It would have been nice if you received something extra"
                else:
                    $ tip
                    "Nice! Looks like you got an extra $%(tip)d."
                $ balance += tip
                $ total_tip += tip
                $ tip = 0

    label night_two:
        scene black

        $ balance += 20
        show screen Day
        show screen Savings

        "You received $20 from your salary. You received $%(total_tip)d in tips. You now have $%(balance)d in savings."
        "Your apartment has increased the daily rent by $5."

        label two_all_three:
            menu:
                "Rent: -$15":
                    $ balance -= 15
                    $ rent_paid = 1
                    jump two_no_rent
                "Food: -$5":
                    $ balance -= 5
                    $ food_paid = 1
                    jump two_no_food
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump two_no_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_three
        
        label two_no_rent:
            menu:
                "Food: -$5":
                    $ balance -= 5
                    $ food_paid = 1
                    jump two_no_rent_food
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump two_no_rent_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_three

        label two_no_food:
            menu:
                "Rent: -$15":
                    $ balance -= 15
                    $ rent_paid = 1
                    jump two_no_rent_food
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump two_no_food_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_three
        
        label two_no_electric:
            menu:
                "Rent: -$15":
                    $ balance -= 15
                    $ rent_paid = 1
                    jump two_no_rent_electric
                "Food: -$5":
                    $ balance -= 5
                    $ food_paid = 1
                    jump two_no_food_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_three
        
        label two_no_rent_food:
            menu:
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump two_next_day
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_three
    
        label two_no_rent_electric:
            menu:
                "Food: -$5":
                    $ balance -= 5
                    $ food_paid = 1
                    jump two_next_day
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_three

        label two_no_food_electric:
            menu:
                "Rent: -$15":
                    $ balance -= 15
                    $ rent_paid = 1
                    jump two_next_day
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_three
        
        label two_next_day:
            menu:
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_three

    label day_three:
        hide screen Day
        hide screen Savings

        if (rent_paid == 0):
            "You have received a warning from the apartment to pay rent."
            $ rent_paid = -1
        elif (rent_paid == -1):
            "You have been evicted by the apartment for not paying rent."
            return
        else:
            $ rent_paid = 0

        if (food_paid == 0):
            "You feel hungry from not eating last night."
            $ food_paid = -1
        elif (food_paid == -1):
            "You have succumbed to your hunger."
            return
        else:
            $ food_paid = 0

        if (electric_paid == 0):
            "You feel sick from a lack of heat last night."
            $ electric_paid = -1
        elif (electric_paid == -1):
            "You have succumbed to sickness."
            return
        else:
            $ electric_paid = 0

        init:
            image arbor_outside = "arbor.jpg"
        define alex = Character("Alex", who_color="#c8ffc8")
        define player = Character("Player", who_color="#3340fd")
        
        scene arbor_outside with fade:

        "Day 3"

        "You take your position behind the counter and wait for the day's customers."

        "As you stand behind the counter, the door chime rings, announcing the arrival of a new customer."

        jump nerd_one

        label nerd_one:
            define n = Character("Nerd", who_color="#c8ffc8")

            label Nerd_D1:
                n "Um, I'll have a venti caramel frappe with whipped cream and a splash of chai."
                menu:
                    "Certainly. Coming right up.":
                        jump Nerd_D1R4
            
            label Nerd_D1R4:
                n "Sounds good, but can you make it quickly. I haven't slept at all because I've been studying for an exam. It is in 10 minutes."
                menu:
                    "Oh sounds stressful. I'll see what I can do.":
                        jump athlete_one
                    "Ok I'll keep that in mind.":
                        jump athlete_one

        label athlete_one:
            define a = Character("Athlete", who_color="#c8ffc8")

            label Athlete_D1:
                a "I'll have a black coffee, extra shot of expresso. But I need it now, I have a game today and I'm going to miss the bus."
                menu:
                    "Hey, I'm sorry but you will have to wait until after I complete another order.":
                        jump Athlete_D1R5
                    "Oh hey, aren't you the star player on our soccer team. Yeah dude, I can prioritize making yours. Just don't tell that nerd over there.":
                        jump Athlete_D1R4

            label Athlete_D1R4:
                a "Thanks, bro. I appreciate you. Our win today is going to be because of you."
                menu:
                    "Here is your coffee.":
                        jump Athlete_D1R29
            
            label Athlete_D1R5:
                a "Look, I need it now. I can't miss the bus. This is the final game of the season."
                menu:
                    "We can't rush your order. I'm sorry.":
                        jump Athlete_D1R7
                    "I guess I can bump your order up. Just don't tell that nerd waiting behind you.":
                        jump Athlete_D1R10
            
            label Athlete_D1R7:
                a "Then the whole school is going to hate you and know you were the dumb barista that made us lose the final game of the season."
                menu:
                    "Hey, look. Maybe I can make an exception for you. That nerd behind you ordered a fancy drink that will take a while so I'll make your order first real quick.":
                        jump Athlete_D1R10
                    "I don't care who you are or what the school will think. You have to wait in line like everyone else.":
                        jump Athlete_D1R23
            
            label Athlete_D1R10:
                a "Yeah, I'm sure they have nowhere to be. Thanks."
                menu:
                    "Actually I've changed my mind. I can't do that to one of our customers.":
                        jump Athlete_D1R13
                    "True that. They're probably on their way to the library or something. Can't be as important as the final soccer game of the season.":
                        jump Athlete_D1R30

            label Athlete_D1R30:
                a "Yeah, my priorities are the most important obviously."
                menu:
                    "Here is your coffee.":
                        jump Athlete_D1R29

            label Athlete_D1R29:
                a "Pleasure doing business with you. And thanks for putting my order in front of that other customer's. Sports are more important than school anyways."
                $ athlete_rate += 2
                jump Athlete_not_nerd

            label Athlete_D1R23:
                a "Shut up. I'm just going to leave. I don't have time for this."
                menu:
                    "That's great. You won't be late to your game anymore.":
                        jump Athlete_D1R26
                    "Wait no I'm sorry. I'll make your drink first. Just don't leave.":
                        jump Athlete_D1R27

            label Athlete_D1R27:
                a "Whatever, dude. At least now the whole school won't hate you."
                jump Athlete_not_nerd
            
            label Athlete_D1R13:
                a "You serious? I'm going to miss my bus at this rate."
                menu:
                    "I'm just messing with you. Here is your coffee.":
                        jump Athlete_D1R16
                    "That's not my problem. You have to wait like everybody else.":
                        jump Athlete_D1R23
            
            label Athlete_D1R16:
                a "Thanks a bunch man. You saved my day."
                $ athlete_rate += 1
                jump Athlete_not_nerd
            
            label Athlete_D1R26:
                a "Whatever. You've just lost a customer. If we lose this game, the whole school will know its on you."
                $ athlete_rate -= 2
                jump nerd_grateful

        label nerd_grateful:
            "The nerd walks back up to the counter after the athlete leaves."
            n "Hey thanks for choosing not to make that athlete's order before mine. I really appreciate it."
            menu:
                "Of course. Good luck on your exam today. Do you mind me asking what the subject is?":
                    jump Nerd_D1R12
                "I didn't do it for you specifically. I just don't like his attitude.":
                    jump Nerd_D1R30

            label Nerd_D1R12:
                n "It's for an this coding project class I'm taking. I love coding so I'm pretty excited for the exam. I won't bore you with the details."
                menu:
                    "I totally understand. Here is your coffee.":
                        jump Nerd_D1R14

            label Nerd_D1R14:
                n "Thank you! Thanks again for making my drink first."
                "He takes his drink from you and leaves hurriedly in the direction of the lecture hall."
                $ nerd_rate += 2
                jump nerd_end

            label Nerd_D1R30:
                n "Oh ok. Thanks anyways I guess."
                "He hesitantly takes his drink from you and leaves the coffee shop."
                $ nerd_rate += 1
                jump nerd_end
            
        label Athlete_not_nerd:
            "You feel happy helping that athlete win his game."
            "You check if he left behind anything."
            if (athlete_rate > 0):
                $ tip = athlete_rate * 5
            if tip == 0: 
                "He left no tip behind. I guess he was too rushed to give me a tip."
            else:
                $ tip
                "Nice! Looks like he left behind an extra $%(tip)d."
            $ balance += tip
            $ total_tip += tip
            $ tip = 0

            "The nerd walks back up to the counter after the athlete leaves."

            n "Did you just make his order before mine. I have to go take an exam in a few minutes!"
            menu:
                "Yea sorry about that his bus was about to leave. I'll be able to make your drink in time still.":
                    jump Nerd_D1R18
                "The athlete's game was way more important than your exam. It's the final game of the season and they're representing our school.":
                    jump Nerd_D1R19
            
            label Nerd_D1R18:
                n "Oh ok I guess I understand. Hopefully I'll still be able to make it to my exam and perform well."
                menu:
                    "Good luck on your exam. Here is your drink.":
                        jump Nerd_D1R21
                    "School isn't that important anyways. Stop taking everything so seriously. Here's your drink.":
                        jump Nerd_D1R22

            label Nerd_D1R19:
                n "My exam is also important! It's my last chance to guarantee I get a good grade in the class. At this rate, I might be late and get a bad grade."
                menu:
                    "Sorry about that. I hope you still do well on your exam. Here is your drink.":
                        jump Nerd_D1R21
                    "School isn't that important anyways. Stop taking everything so seriously. Here is your drink":
                        jump Nerd_D1R22

            label Nerd_D1R21:
                n "Thanks I guess."
                "He takes his drink from you, giving you a disgruntled look and leaving quickly to his lecture hall."
                jump nerd_end
            
            label Nerd_D1R22:
                n "How can you say that! How we do in school will determine how we do for the rest of our lives."
                "He angrily takes the drink from your hands and storms out of the coffee shop towards his lecture hall."
                $ nerd_rate -= 2
                jump nerd_end


            jump night_three

        label nerd_end:
            "You check if he left behind any tip."
            if (nerd_rate > 0):
                $ tip = nerd_rate * 5
            if tip == 0: 
                "He left no tip on the counter. Seems like he's too busy thinking about his exam."
            else:
                $ tip
                "Nice! Looks like he left behind an extra $%(tip)d."
            $ balance += tip
            $ total_tip += tip
            $ tip = 0
            
            jump night_three

    label night_three:
        scene black

        $ balance += 20
        show screen Day
        show screen Savings

        "You received $20 from your salary. You received $%(total_tip)d in tips. You now have $%(balance)d in savings."
        "The cost of living in Santa Barbara has gone up."

        label three_all_three:
            menu:
                "Rent: -$15":
                    $ balance -= 15
                    $ rent_paid = 1
                    jump three_no_rent
                "Food: -$10":
                    $ balance -= 10
                    $ food_paid = 1
                    jump three_no_food
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump three_no_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_four
        
        label three_no_rent:
            menu:
                "Food: -$10":
                    $ balance -= 10
                    $ food_paid = 1
                    jump three_no_rent_food
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump three_no_rent_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_four

        label three_no_food:
            menu:
                "Rent: -$15":
                    $ balance -= 15
                    $ rent_paid = 1
                    jump three_no_rent_food
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump three_no_food_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_four
        
        label three_no_electric:
            menu:
                "Rent: -$15":
                    $ balance -= 15
                    $ rent_paid = 1
                    jump three_no_rent_electric
                "Food: -$10":
                    $ balance -= 10
                    $ food_paid = 1
                    jump three_no_food_electric
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_four
        
        label three_no_rent_food:
            menu:
                "Electricity: -$5":
                    $ balance -= 5
                    $ electric_paid = 1
                    jump three_next_day
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_four
    
        label three_no_rent_electric:
            menu:
                "Food: -$10":
                    $ balance -= 10
                    $ food_paid = 1
                    jump three_next_day
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_four

        label three_no_food_electric:
            menu:
                "Rent: -$15":
                    $ balance -= 15
                    $ rent_paid = 1
                    jump three_next_day
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_four
        
        label three_next_day:
            menu:
                "Next Day":
                    $ total_tip = 0
                    $ day += 1
                    jump day_four
        
    label day_four:
        hide screen Day
        hide screen Savings

        init:
            image arbor_outside = "arbor.jpg"
        define alex = Character("Alex", who_color="#c8ffc8")
        define player = Character("Player", who_color="#3340fd")
        
        scene arbor_outside with fade:

        if (rent_paid == 0):
            "You have been evicted by the apartment for not paying rent."
            return
        elif (rent_paid == -1):
            "You have been evicted by the apartment for not paying rent."
            return
        else:
            $ rent_paid = 0

        if (food_paid == 0):
            "You have succumbed to your hunger."
            return
        elif (food_paid == -1):
            "You have succumbed to your hunger."
            return
        else:
            $ food_paid = 0

        if (electric_paid == 0):
            "You have succumbed to sickness because of a lack of heat last night."
            return
        elif (electric_paid == -1):
            "You have succumbed to sickness because of a lack of heat last night."
            return
        else:
            $ electric_paid = 0

        "Congratulations! You have successfully navigated through the game."

            

            


    return


