"""
Luke Russell
Prove: Adventure Story 
2/13/2021
""" 
start = input('Please type START to begin: ')
print('Welcome to The Forest of Bär, enter at your own risk.')
print('Your goal is to make it through The Forest of Bär without dying...')
print("Good luck, you'll need it.")
being = input('Type BEGIN to continue. ')
print('Welcome to The Forest of Bär, your task, should you choose to accept it is to cross through the forest and make it back to your base camp.')
item_1 = input('You are now walking through the forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up? ')


if item_1 == "match":
    action_1 = input('You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree? ')
else: 
    action_2 = input('You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ')


#If you picked MATCH
if action_1 == 'hide':
    print('You hear branched breaking and leaves crunching as the bear draws near to where you are at.')
    s2_action = input('Do you want to CLIMB the tree or PLAY DEAD? ')
    if s2_action == 'play dead':
        print('The bear comes up to you as you lay perfectly still, hardly breathing.')
        print('After what feels like an eternity; she leaves you alone and you stay still for a few more minutes for good measure.') 
        print('You slowly rise to your feet and continue walking, as you’re walking you kick something...')
        s2_reaction = input('Do you PICK IT UP or KEEP GOING? ')
        if s2_reaction == 'pick it up':
                print('You pick up the large stick, it’s slightly heavy and you know it could do some serious damage.')
                print('You see the bear coming towards you. Jumping to your feet you start swinging.')
                print()
                print('You make contact with something, and it growls loudly. Finding your mark, you keep swinging with all your might until you successfully fend off the hungry bear.')
                dog = input('You keep walking until you find a dog Do you PET IT or LET IT GO? ')
                if dog == 'pet it':
                        print('You approach dog slowly, getting lower and reaching out your hand, the dog trots over and sniffs your hand as you pet him on the head.')
                        print('The dog then notices your stick and you let him take it.')
                        

        else: 
                print('As you look around, you see two beady eyes staring back at you from about 50 yards away.')
                print('Thinking quickly, you run in the opposite direction, but end up tripping on something, it’s a large stick!')
                s3_reaction = input('Do you PICK IT UP or KEEP RUNNING? ')
                if s3_reaction == 'keep running':
                    print('You turn around and notice that nothing is following you. Catching your breath. You slow down and see a pond in the distance. Seeing the pond puts your mind at ease, for a pond means your close to your base camp.')
                    print('As you draw near to the pond you hear an unmistakable noise. You get closer and find a little frog on a log.')     
                    print('Observing your surroundings, you pick up the little frog and rub its head. Suddenly it jumps out of your hand and before your eyes is a beautiful maiden “follow me” she says, “I know the way.”')
                    print('The maiden takes your and together you exit the forest and return to your base camp. The End.')
                    print('Congradulations! You made all the right choices and survived the Forst of Bär!')
                else: 
                    print('You pick up the large stick, it’s slightly heavy and you know it could do some serious damage.')
                    print('You see the bear coming towards you. Jumping to your feet you start swinging.')
                    print()
                    print('You make contact with something, and it growls loudly. Finding your mark, you keep swinging with all your might until you successfully fend off the hungry bear.')
                    s4_reaction = input('You keep walking until you find a dog Do you PET IT or LET IT GO? ')
                    if s4_reaction == 'pet it':
                        print('You approach dog slowly, getting lower and reaching out your hand, the dog trots over and sniffs your hand as you pet him on the head.')
                        print('The dog then notices your stick and you let him take it.')
                        
    else:
        print('Silly player, bears are amazing climbers, should have played dead. GAME OVER')
else: 
    print('You hear the bear chasing after you!') 
    s2_action_1 = input('Knowing you can’t out run her do you TURN AND FIGHT or PLAY DEAD? ')
    if s2_action_1 == 'play dead':
        print('The bear comes up to you as you lay perfectly still, hardly breathing.')
        print('After what feels like an eternity; she leaves you alone and you stay still for a few more minutes for good measure.') 
        print('You slowly rise to your feet and continue walking, as you’re walking you kick something...')
        s2_reaction_1 = input('Do you PICK IT UP or KEEP GOING? ')    
        if s2_reaction_1 == 'pick it up':
                print('You pick up the large stick, it’s slightly heavy and you know it could do some serious damage.')
                print('You see the bear coming towards you. Jumping to your feet you start swinging.')
                print()
                print('You make contact with something, and it growls loudly. Finding your mark, you keep swinging with all your might until you successfully fend off the hungry bear.')
                s4_reaction_1 = input('You keep walking until you find a dog Do you PET IT or LET IT GO? ')
                if s4_reaction_1 == 'pet it':
                    print('You approach dog slowly, getting lower and reaching out your hand, the dog trots over and sniffs your hand as you pet him on the head.')
                    print('The dog then notices your stick and you let him take it.')
                    print('Suddenly, the dog takes off! Trusting its instincts, you decide to follow it. It leads you to a pond.')
                    print('As you draw near to the pond you hear an unmistakable noise. You get closer and find a little frog on a log.')
                    print('Observing your surroundings, you pick up the little frog and rub its head. Suddenly it jumps out of your hand and before your eyes is a beautiful maiden “follow me” she says, “I know the way.”')
                
        
        
        
        else: 
                print('As you look around, you see two beady eyes staring back at you from about 50 yards away.')
                print('Thinking quickly, you run in the opposite direction, but end up tripping on something, it’s a large stick!')
                if s2_reaction_1 == 'keep going' :
                    print('You turn around and notice that nothing is following you. Catching your breath. You slow down and see a pond in the distance. Seeing the pond puts your mind at ease, for a pond means your close to your base camp.')
                    print('As you draw near to the pond you hear an unmistakable noise. You get closer and find a little frog on a log.')     
                    print('Observing your surroundings, you pick up the little frog and rub its head. Suddenly it jumps out of your hand and before your eyes is a beautiful maiden “follow me” she says, “I know the way.”')
                    print('The maiden takes your and together you exit the forest and return to your base camp. The End.')
                    print('Congradulations! You made all the right choices and survived the Forst of Bär!')
                
    else: 
        print('Silly player, you cannot out run a hungry bear, should have played dead. GAME OVER')



#If you picked FLASHLIGHT
if action_2 == 'follow':
    print('You see a path through the forest.')
    action_s3 = input('Do you FOLLOW the path or LOOK around? ')
    if action_s3 == 'follow':
        print('You start down the path, illuminated by your flashlight, and hear something following you.')
        reaction_s3 = input('Will you LOOK AT what it is, or KEEP WALKING down the path? ')
        if reaction_s3 == 'LOOK AT':
            print('As you look around, you see two beady eyes staring back at you from about 50 yards away.')
            print('Thinking quickly, you run in the opposite direction, but end up tripping on something, it’s a large stick!')
            s3_reaction_2 = input('Do you PICK IT UP or KEEP RUNNING? ')
            if s3_reaction_2 == 'keep running':
                    print('You turn around and notice that nothing is following you. Catching your breath. You slow down and see a pond in the distance. Seeing the pond puts your mind at ease, for a pond means your close to your base camp.')
                    print('As you draw near to the pond you hear an unmistakable noise. You get closer and find a little frog on a log.')     
                    print('Observing your surroundings, you pick up the little frog and rub its head. Suddenly it jumps out of your hand and before your eyes is a beautiful maiden “follow me” she says, “I know the way.”')
                    print('The maiden takes your and together you exit the forest and return to your base camp. The End.')
                    print('Congradulations! You made all the right choices and survived the Forst of Bär!')
            else:
                    s4_reaction_2 = input('You keep walking until you find a dog Do you PET IT or LET IT GO? ')
            if s4_reaction_2 == 'pet it':
                    print('You approach dog slowly, getting lower and reaching out your hand, the dog trots over and sniffs your hand as you pet him on the head.')
                    print('The dog then notices your stick and you let him take it.')
                    print('Suddenly, the dog takes off! Trusting its instincts, you decide to follow it. It leads you to a pond.')
                    print('As you draw near to the pond you hear an unmistakable noise. You get closer and find a little frog on a log.')
                    print('Observing your surroundings, you pick up the little frog and rub its head. Suddenly it jumps out of your hand and before your eyes is a beautiful maiden “follow me” she says, “I know the way.”')
                    print('The maiden takes your and together you exit the forest and return to your base camp. The End. ')
                    print('Congradulations! You made all the right choices and survived the Forst of Bär!')
            else:
                    print('You keep walking alone into the night…')
                    print('Will you ever find your way?')
                    print('Did you make the right decisions?')
    else:  
          s4_reaction_3 = input('You keep walking until you find a dog Do you PET IT or LET IT GO? ')
    if s4_reaction_3 == 'pet it':
                print('You approach dog slowly, getting lower and reaching out your hand, the dog trots over and sniffs your hand as you pet him on the head.')
                print('The dog then notices your stick and you let him take it.')
                print('Suddenly, the dog takes off! Trusting its instincts, you decide to follow it. It leads you to a pond.')
                print('As you draw near to the pond you hear an unmistakable noise. You get closer and find a little frog on a log.')
                print('Observing your surroundings, you pick up the little frog and rub its head. Suddenly it jumps out of your hand and before your eyes is a beautiful maiden “follow me” she says, “I know the way.”')
                print('The maiden takes your and together you exit the forest and return to your base camp. The End. ')
                print('Congradulations! You made all the right choices and survived the Forst of Bär!')
    else:
                print('You keep walking alone into the night…')
                print('Will you ever find your way?')
                print('Did you make the right decisions?')  
else:
    print('You keep walking the same way you were, leaving the path behind; when suddenly you trip on something!')
    reaction_s2 = input('It is a very large metal pole, will you PICK IT UP or KEEP WALKING? ')
    if reaction_s2 == 'pick it up':
         print('You approach dog slowly, getting lower and reaching out your hand, the dog trots over and sniffs your hand as you pet him on the head.')
print('The dog then notices your stick and you let him take it.')
print('Suddenly, the dog takes off! Trusting its instincts, you decide to follow it. It leads you to a pond.')
print('As you draw near to the pond you hear an unmistakable noise. You get closer and find a little frog on a log.')
print('Observing your surroundings, you pick up the little frog and rub its head. Suddenly it jumps out of your hand and before your eyes is a beautiful maiden “follow me” she says, “I know the way.”')
print('The maiden takes your and together you exit the forest and return to your base camp. The End. ')
print('Congradulations! You made all the right choices and survived the Forst of Bär!')
