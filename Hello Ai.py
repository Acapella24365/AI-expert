print("Hello! My name is AI Bot! What's yours?")

name = input()
print(f"Nice to meet you {name}")

print("How are you feeling today (eg: Good, Bad..)")

mood = input().lower

if mood == "good" :
    print("Glad to hear that!")
elif mood == "bad" :
    print("I'm sorry to hear that! Hope you feel good soon.")
else :
    print("I see, sometimes i'ts hard to put your feelings into words.")

print(f"It was nice chatting with you {name}, goodbye!")