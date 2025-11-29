import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Himalayas", "Swiss Alps", "Rocky Mountains"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = {
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the docter? Because it had a virus!",
    "Why do travelers always feel warm? Because of their HOT SPOTS!"
}

def normalize_input(text)
    return re.sub(r"/s+", " ", text.strip().lower())

def reccomend():
    print(Fore.CYAN + "Travelbot: Beaches, Mountains or Cities?")
    preferance = input(Fore.YELLOW + "You:")
    preferance = normalize_input(preferance)

    if preferance in destinations:
        suggestion = random.choice (destinations[preferance])
        print(Fore.GREEN + f"Travelbot: How about {suggestion}?")
        print(Fore.CYAN + "Travelbot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"Travelbot: Glad you like it!")
        elif answer == "no":
            print(Fore.RED + "Travelbot: Sorry. Let's try another!")
            reccomend()
        else:
            print(Fore.RED + "Travelbot: I'll suggest again.")
            reccomend()
    
    else:
        print(Fore.RED + "Travelbot: Sorry I don't have that type of destination.")

    show_help()

def packing_tips():
    print(Fore.CYAN + "Travelbot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You:"))
    print(Fore.CYAN + "Travelbot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"Travelbot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes")
    print(Fore.GREEN + "- Bring chargers/adapters")
    print(Fore.GREEN + "- Check the weather forecast")

def tell_joke():
    print(Fore.YELLOW + f"Travelbot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can: ")
    print(Fore.GREEN + "- suggest travel spots (say: reccomendations)")
    print(Fore.GREEN + "- offer packing tips (say: packing)")
    print(Fore.GREEN + "- tell a joke (say: joke)")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end \n")

def chat():
    print(Fore.CYAN + "Hello! I'm Travel bot")
    name = input(Fore.YELLOW + "Your name?")
    print(Fore.GREEN + f"Nice to meet you {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}")
        user_input = normalize_input(user_input)

        if "reccomend" in user_input or "suggest" in user_input:
            reccomend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + f"Travelbot: Safe travels {name}, Goodbye!")
            break
        else:
            print(Fore.RED + "Travelbot: Could you rephrase?")

if __name__ == "__main__":
    chat()