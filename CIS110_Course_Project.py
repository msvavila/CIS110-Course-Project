# Greet the user and provide instructions
print(f"Hello,there! I have an exciting story about a girl who wants to become a racecar driver. I can't wait to tell the story.")
print(f"Before the story begins, I have a few questions I need you to answer.")
print(f"After typing your answer, make sure to press the enter key.")
input(f"\nPress the enter key to continue...")

#5 Questions Before the story begins
name = input(f"\nWhat is the girl's name:  ")
city = input(f"\nWhat is your favorite city:  ")
car = input(f"\nWhat is your favorite car:  ")
hobby = input(f"\nWhat is your favorite car hobby:  ")
college = input(f"\nWhat would you like to study in college:  ")
    
#Story Starts
print(f"\nLET'S BEGIN!!!")
print(f"\nOnce upon a time there was a young girl named {name} who was very smart who loved cars and wanted to become a racecar driver.  ")
print(f"{name} was from {city}, where she began to love {hobby}.  ")
print(f"One day {name} was preparing to study for {college}. She had the opportunity to drive her favorite {car}.  ")
print(f"Instead of preparing for college {name} snuck out of the house to go to a racetrack to see the races which was her favoite thing to do.  ")

#Decision 1
sneaksOutHouse = input(f"\nShould {name} sneak out of the house or stay home? Type yes or no:  ")
if sneaksOutHouse == "yes":
    print(f"\n{name} sneaks out of her bedroom window.  ")
    print(f"After {name} sneaks out she goes to the races and watches her friends drive on a racetrack. ")
    print(f"Once she gets to the racetrack. {name} got to drive her favorite {car} on the track.  ")
    print(f"After racing her favorite {car} she soon realize how late it was and got in trouble when she came back home.  ")
else:
    print(f"{name} decides it is too risky to sneak out of her house.  ")
    print(f"instead of sneaking out she prepares for {college}. so she can start going to college next term.  ")
    print(f"although {name} missed out on her favorite thing to do.")
    print(f"{name} realized that it is best she studies for {college} and not get in trouble.  ")
    
    