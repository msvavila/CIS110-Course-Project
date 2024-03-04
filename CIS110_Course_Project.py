# Greet the user and provide instructions
print(f"Hello,there! I have an exciting story about a girl who wants to become a racecar driver. I can't wait to tell the story.")
print(f"Before the story begins, I have a few questions I need you to answer.")
print(f"After typing your answer, make sure to press the enter key.")
input(f"\nPress the enter key to continue...")

keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    #5 Questions Before the story begins
    name = input(f"\nWhat is the girl's name:  ")
    while len(name) == 0:
        name = input(f"Please enter a girls name:  ")
    
    city = input(f"\nWhat is your favorite city:  ") 
    while len(city) == 0:
        city = input(f"Please enter a city:  ")
    
    carName = input(f"\nWhat is your favorite car:  ")   
    while len(carName) == 0:
        carName = input (f"Please enter a car name:  ")
    
    hobby = input(f"\nWhat is your favorite car hobby:  ")
    while len(hobby) == 0:
        hobby = input(f"Please enter a car hobby:  ")
    
    college = input(f"\nWhat would you like to study in college:  ")
    while len(college) == 0:
        college = input(f"Please enter a field of study:  ")

    
    #Story Starts
    print(f"\nLET'S BEGIN!!!")
    print(f"\nOnce upon a time there was a young girl named {name} who was very smart who loved cars and wanted to become a racecar driver.  ")
    print(f"{name} was from {city}, where she began to love {hobby}.  ")
    print(f"One day {name} was preparing to study for {college}. She had the opportunity to drive her favorite car that is a {carName}.  ")
    print(f"Instead of preparing for college {name} snuck out of the house to go to a racetrack to see the races which was her favoite thing to do.  ")

    #Decision 1
    sneaksOutHouse = input(f"\nShould {name} sneak out of the house or stay home? Type yes or no:  ")
    while sneaksOutHouse.lower() != "yes" and sneaksOutHouse.lower() != "no":
        sneaksOutHouse = input("Please type yes or no:  ")
    
    if sneaksOutHouse == "yes":
        print(f"\n{name} sneaks out of her bedroom window.  ")
        print(f"After {name} sneaks out she goes to the races and watches her friends drive on a racetrack. ")
        print(f"Once she gets to the racetrack. {name} got to drive her favorite car that is a {carName} on the track.  ")
        print(f"After racing her favorite car, {name} soon realize how late it was and got in trouble when she came back home.  ")
    else:
        print(f"{name} decides it is too risky to sneak out of her house.  ")
        print(f"Instead of sneaking out she prepares for {college} entrance exam. so she can start going to college next term.  ")
        print(f"Although {name} missed out on her favorite thing to do.")
        print(f"{name} realized that it is best she studies for {college} entrance exam and not get in trouble.  ")
    
    #Decision 2
    goesToRacetrack = input(f"\nShould {name} go to the racetrack?  Type yes or no:  ")
    while goesToRacetrack.lower() != "yes" and goesToRacetrack.lower() != "no":
        goesToRacetrack = input(f"Please type yes or no:  ")
    
    if goesToRacetrack == "yes":
        print(f"{name} goes out to enjoy the {hobby} with her friends.  ")
        print(f"When {name} arrives at the racetrack she enjoys her time with her friends watching them race. ")
        print(f"While {name} is watching her friends, she got the chance to race in her favorite car that is a {carName}.  ")
        print(f"During the race {name} set her highest record in first place.  ")
        print(f"After the race {name} got a sponsorship with {carName} to become a famous racecar driver.  ")
    else:
        print(f"She goes to the racetrack, and decides to watch the races only.  ")
        print(f"While being to afraid of getting in trouble, {name} does not stay long.  ")
        print(f"{name} goes home before she gets caught and starts to study for her college entrance exam for {college}.  ")
    
    #Alernate Endings
    if sneaksOutHouse == "yes" and goesToRacetrack == "yes":
        print(f"\nAfter sneaking out and going to {city}, and spending the day enjoying the {hobby}.  ")
        print(f"{name} drives her favorite car that is a {carName} on the track and wins first place.  ")
        print(f"After winning first place, {name} gets offered a sponsorship to become a racecar driver.  ")
        print(f"Lukily when she left {city} and got home {name} did not get caught.  ")
        print(f"{name} went home just on time to study for {college} entrance exam to get accepted into college.  ")
    elif sneaksOutHouse == "no" and goesToRacetrack == "no": 
        print(f"\nAfter sneaking out and going to {city}, and spending the day enjoying the {hobby}.  ")
        print(f"{name} drives her favorite car that is a {carName} on the track and wins first place.  ")
        print(f"After winning first place, {name} gets offered a sponsorship to become a racecar driver.  ")
        print(f"Lukily when she left {city} and got home {name} did not get caught.  ")
        print(f"{name} went home just on time to study for {college} entrance exam to get accepted into college.  ")
    else:
        print(f"\nAfter sneaking out and going to {city}, and spending the day enjoying the {hobby}.  ")
        print(f"{name} drives her favorite car that is a {carName} on the track and wins first place.  ")
        print(f"After winning first place, {name} gets offered a sponsorship to become a racecar driver.  ")
        print(f"Lukily when she left {city} and got home {name} did not get caught.  ")
        print(f"{name} went home just on time to study for {college} field to get accepted into college.  ")
    print(f"\nThe End")
    keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "np":
        keepPlaying = input(f"Please type yes or no:  ")
        
    
      