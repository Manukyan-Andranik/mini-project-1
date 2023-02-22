import os
import random

start = True
while(start):
    os.system("clear")
    
    number_of_template = input("Input the number of template(1 - 3): ")
    num_of_try = 0
    while  not number_of_template in ["1", "2", "3"] and num_of_try < 3 :
        os.system("clear")
        number_of_template = input("Input the number of template(1 - 3): ")
        num_of_try += 1
    if num_of_try == 3:
        number_of_template = ["1", "2", "3"][random.randint(0, 3)]
        os.system("clear")
        print("I will tell a random story from my story base․", end = "\n" * 2)
    else:
        os.system("clear")
   


    if(number_of_template == "1"):
        number = input("Input a number: ")
        measure_of_time = input("Measure of time: ")
        mode_of_transportation = input("Input mode of transportation: ")    
        adjective = input("Input adjective: ")
        adjective2 = input("Input adjective: ")
        noun = input("Input noun: ") 
        color = input("Input a color: ")   
        part_of_the_body = input("Input part of the body: ")
        verb = input("Input verb: ")
        number2 = input("Input a number: ")
        noun2 = input("Input noun: ")
        noun3 = input("Input noun: ")
        part_of_the_body_2 = input("Input part of the body:")
        noun4 = input("Input noun: ")
        adjective3 = input("Input adjective: ")
        silly_word = input("Input a silly word: ")
        os.system("clear")
        template =  f"""\n\n\t\tIt was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}.
            The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here.
            There are nurses here who have {color} {part_of_the_body}.
            If someone wants to come into my room I told them that they have to {verb} first.
            I’ve decorated my room with {number2} {noun2}. 
            Today I talked to a doctor and they were wearing a {noun3} on their {part_of_the_body_2}.
            I heard that all doctors {verb} {noun4} every day for breakfast.
            The most {adjective3} thing about being in the hospital is the {silly_word} {noun} !"""


    elif number_of_template == "2":
        Proper_Noun_Persons_Name = input("Input person name: ") 
        Noun = input("Input noun: ")
        Adjective_Feeling = input("Input adjective(feeling): ")
        Verb = input("Input verb: ")
        Adjective_Feeling_2 = input("Input adjective(feeling): ")
        Animal = input("Input an animal: ")
        Verb2 = input("Input a verb : ")
        Color = input("Input a color: ")
        Verb_ending_in_ing = input("Input a verb (ending in ing): ")
        Adverb_ending_in_ly = input("Input adverb (ending in ly): ")
        Number = input("Input a number: ")
        Measure_of_Time = input("Measure of time: ")
        Silly_Word = input("Input a silly word: ") 
        Noun2 = input("Input noun: ")
        os.system("clear")
        template =   f"""\n\n\t\tThis weekend I am going camping with {Proper_Noun_Persons_Name}.
            I packed my lantern, sleeping bag, and {Noun}. I am so {Adjective_Feeling} to {Verb} in a tent.
            I am {Adjective_Feeling_2} we might see a {Animal}, I hear they’re kind of dangerous.
            While we’re camping, we are going to hike, fish, and {Verb2}.
            I have heard that the {Color} lake is great for {Verb_ending_in_ing}.
            Then we will {Adverb_ending_in_ly} hike through the forest for {Number} {Measure_of_Time}.
            If I see a {Color} {Animal} while hiking, 
            I am going to bring it home as a pet! 
            At night we will tell {Number} {Silly_Word} stories and roast {Noun2} around the campfire!!
            """


    elif number_of_template == "3":
        Proper_Noun_Persons_Name = input("Input person name: ")
        Adjective = input("Input adjective: ")
        Color = input("Input a color: ")
        Animal = input("Input an animal: ")
        Place = input("Input place: ")
        Adjective2 = input("Input adjective: ")
        Magical_Creature_Plural = input("Input magical creature(plural): ")
        Adjective3 = input("Input adjective: ")
        Magical_Creature_Plural2 = input("Input magical creature(plural): ")
        Room_in_a_House = input("Input room in a house: ")
        Noun = input("Input noun: ")
        Noun2 = input("Input noun : ")
        Noun_Plural_3 = input("Input noun(plural): ")
        Adjective4 = input("Input adjective: ")
        Noun_Plural_4 = input("Input noun(plural): ")
        Number = input("Input a  number: ")
        Measure_of_time = input("Measure of time: ")
        Verb_ending_in_ing = input("Input verb (ending in ing): ")
        Adjective5 = input("Input adjective: ")
        Noun5 = input("Input noun: ")
        os.system("clear")
        template = f"""\n\n\t    Dear {Proper_Noun_Persons_Name},
            I am writing to you from a {Adjective} castle in an enchanted forest.
            I found myself here one day after going for a ride on a {Color} {Animal} in {Place}.
            There are {Adjective2} {Magical_Creature_Plural} and {Adjective3} {Magical_Creature_Plural} here!
            In the { Room_in_a_House} there is a pool full of {Noun}. 
            I fall asleep each night on a {Noun2} of {Noun_Plural_3} and dream of {Adjective4} {Noun_Plural_4}. 
            It feels as though I have lived here for {Number} { Measure_of_time}. I hope one day you can visit, 
            although the only way to get here now is {Verb_ending_in_ing} on a {Adjective5} {Noun5}!!"""

    print(template, end = "\n" * 3)
    inputed = input("Play again?(Y/N): ").lower() 
    start = (inputed == "y")
    

os.system("clear")
