# Greet the user and provide instructions
print(f"Hello,there! I have an exciting story about a girl who wants to become a racecar driver. I can't wait to tell the story.")
print(f"Before the story begins, I have a few questions I need you to answer.")
print(f"After typing your answer, make sure to press the enter key.")
input(f"\nPress the enter key to continue...")

keepPlaying ="yes"
while keepPlaying.lower() =="yes":
    
    name = input(f"\nWhat is the girl's name:  ")
    city = input(f"\nWhat is your favorite city:  ")
    car = input(f"\nWhat is your favorite car:  ")
    racecar = input(f"\nWhat is she interested in doing:  ")
    college = input(f"\nWhat test is she studying for:  ")
    
                