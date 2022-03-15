#  As a developer, I want to make at least three commits with descriptive messages.

#  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainments in their own separate lists.

#  As a user, I want a destination to be randomly selected for my day trip.

#  As a user, I want a restaurant to be randomly selected for my day trip.

#  As a user, I want a mode of transportation to be randomly selected for my day trip.

#  As a user, I want a form of entertainment to be randomly selected for my day trip.

#  As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if 
#  I don’t like one or more of those things.

#  As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.

#  As a user, I want to display my completed trip in the console.

#  As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!

import random


destinations = ["Key West, Florida" , "Ketchican, Alaska" , "Yellowstone Park, Colorado" , "Orlando, Florida" , "Las Vegas, Nevada"]
places_to_eat = ["The Square Grouper" , "Luigi's Noodle" , "Sake Asian Fusion" , "Red Rooster Bar and Grill" , "Sandinos Pub"]
transportation_options = ["Train" , "Yatch" , "Helicopter" , "Motorcycle" , "Party Bus"]
entertainment_options = ["Ice Fishing" , "Big Game Fishing" , "Geiser Tour" , "A Day with Goofy" , "Texas Hold em Poker Tournament"]

def welcome():
    greeting = "Welcome to the Day trip Generator! Where we will plan a trip for you, so you don't have to!! Let's get started. I'll choose a Destination for you, you tell me if you'd like to go there or not."
    print (greeting)
    return greeting
welcome()

def choose_destination(list_of_destinations):
    destination = random.choice(list_of_destinations)
    print (destination)
    user_input = input ("would you like to go to this destinantion?")
    lowered_input = user_input.lower()
    if user_input == ("yes"):
        print ("Great! That is an exciting place to travel!")
    while user_input == ("no"):
        print ("Understood, lets look at a different location.")
        destination = random.choice(list_of_destinations)
        print (destination)   
        user_input = input("would you like to go to this destinantion?")
    if user_input == ("yes"):
        print ("You aren't going to want to leave!")
    return destination
choose_destination(destinations)

def next_choice():
    statement = "Now, Let's move on to your next decision, your choice of where to eat!"
    print (statement)
    return statement
next_choice()

def pick_place_to_eat(list_of_places_to_eat):
    place_to_eat = random.choice(list_of_places_to_eat)
    print (place_to_eat)
    user_input = input ("Does this Restaraunt sound good?")
    lowered_input = user_input.lower()
    if user_input == ("yes"):
        print ("Great! It was my favorite restaraunt at your chosen location!!")
    while user_input == ("no"):
        print ("Okiedokie, let's find something a little more Tasty for you!")
        place_to_eat = random.choice(list_of_places_to_eat)
        print (place_to_eat)
        user_input = input ("Does this Restaraunt sound like a tastier option?")
    if user_input == ("yes"):
        print ("You're going to love their food!!")  
    return place_to_eat      
pick_place_to_eat(places_to_eat)

def next_choice():
    statement1 = "Now, Let's move on to your next decision, choosing your mode of travel!"
    print (statement1)
    return statement1
next_choice()

def choose_your_mode_of_travel(list_of_transportation_options):
    mode_of_travel = random.choice(list_of_transportation_options)
    print (mode_of_travel)
    user_input= input("Is this how you would like to travel?")
    lowered_input = user_input.lower()
    if user_input == ("yes"):
        print ("That is a fun way to travel!!")
    while user_input == ("no"):
        print ("No worrries, we can also get you there this way!")
        mode_of_travel= random.choice(list_of_transportation_options)
        print (mode_of_travel)
        user_input = input ("Does this sound like a better way to travel?")
    if user_input == ("yes"):
        print ("Awesomesauce! You are almost on vacation!")
        return mode_of_travel
choose_your_mode_of_travel(transportation_options)

def next_choice():
    statement2 = "Now you have one final choice and you can get off the computer and into the World! Let's figure out what you want to do for some entertainment!"
    print (statement2)
    return statement2
next_choice()

def pick_type_of_entertainment(list_of_entertainment_options):
    type_of_entertainment = random.choice(list_of_entertainment_options)
    print (type_of_entertainment)
    user_input = input("Does this sound like something fun to do?")
    lowered_input = user_input.lower()
    if user_input == ("yes"):
        print ("That's a great choice of activities!")
    while user_input == ("no"):
        print ("Didn't sound like fun, huh? That's OK, how about this for some entertainment?")
        type_of_entertainment= random.choice(list_of_entertainment_options)
        print (type_of_entertainment)
        user_input = input ("Would you like to do this instead?")
    if user_input == ("yes"):
        print ("Superb! I'm so glad we found something you want to do on your 'Daycation', HaHa!")
    return type_of_entertainment
pick_type_of_entertainment(entertainment_options)


def last_decision():
    final_statement = "We have finalized your choices and have a 'Daycation' plan just for you! Let's review your decision and make sure this is what you want to do with your day."
    print (final_statement)
    return final_statement
last_decision()

def confirmation():
    ready_to_go= "Well what are you waiting for? Get going!"
    changed_your_mind= "Let's plan a different 'Daycation' for you!"
    user_input= ("Are you excited about your 'Daycation'?")
    if user_input == "yes":
        print (ready_to_go)
    elif user_input == "no":
        print (changed_your_mind)
confirmation()



def randomizer(list_of_any):
    all_lists= list_of_any
    any_of_my_lists = random.choices(all_lists)
    print (any_of_my_lists)
    return any_of_my_lists 
randomizer(list_options)  #figure this out.....





