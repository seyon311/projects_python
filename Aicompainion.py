import random
import datetime

def get_greeting():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning ☀️!"
    elif 12 <= current_hour < 18:
        return "Good afternoon 🌄!"
    elif 18 <= current_hour < 22:
        return "Good evening 🌆!"
    else:
        return "Good night! 🌙"

fun_facts = [
    "Did you know that Octopuses have three hearts and blue blood?",
    "Did you know that Australia is wider than the moon?",
    "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
    "Did you know that a day on Venus is longer than a year on Venus?",
    "Did you know that Scotland's national animal is the mythical unicorn?",
]

compliments = [
    "You have a great sense of humor! 😄",
    "You're a wonderful friend! 🤗",
    "You have a curious mind! 🧠",
    "Your creativity is inspiring! 🎨",
    "You have a heart of gold! 💛",
]

# Activities based on mood tracker
activities = {
    "good": [
        "Listen to your favorite happy song! 🎶",
        "Go for a walk in the park! 🌳",
        "Treat yourself to your favorite dessert! 🍰",
        "Talk to a friend and have some fun! 🗨️",
    ],
    "bad": [
        "Take a deep breath and relax. 🧘‍♂️",
        "Write down your thoughts in a journal. 📝",
        "Watch some cat memes to lift your spirits! 😂",
        "Call a friend or family member for support. 📞",
    ],
    "okay": [
        "Take a short break and stretch your legs. 🏃‍♂️",
        "Listen to some calming music. 🎵",
        "Do a small act of kindness for someone. 🤝",
        "Try learning a new hobby or activity! 🎨",
    ],
    "unclear": [
        "Take a deep breath and focus on the present moment. 🌬️",
        "Draw or doodle your feelings to express yourself. ✏️",
        "Go drink some water and take a short walk. 🚶‍♂️",
    ],
    "history": [
        "You can view your mood history by typing 'history' at any time. This will show you a list of all the moods you've shared with me during our conversations."
    ]
}

mood_history = [] # We will be storing the mood history here

""" This is a simple AI companion that provides greetings, fun facts, compliments, and activities based on the user's mood. """

name = input(f"{get_greeting()} I'm your AI companion! What's your name? ")
print(f"Nice to meet you, {name}!")

# Convo loop
while True:
    print("\nHow are you feeling today? (good/bad/okay/unclear) or type 'exit' to quit and 'history' to see your mood history:")
    mood = input().strip().lower()

    if mood == 'exit':
        print("Goodbye! Take care! 👋")
        break
    if mood not in activities:
        print("Sorry, I didn't understand that. Please enter 'good', 'bad', 'okay', or 'unclear'.")
        continue
    if mood in activities:
        if mood == "good":
            print("That's great to hear! Here is a fun activity you can do:")
            print(f"- {random.choice(activities[mood])}")
        if mood == "bad":
            print("I'm sorry to hear that. Here is a comforting activity you can try:")
            print(f"- {random.choice(activities[mood])}")
        if mood == "okay":
            print("Thanks for sharing! Here is a small activity you can do:")
            print(f"- {random.choice(activities[mood])}")
        if mood == "unclear":
            print("It's okay to not be able to put your feelings into words. Here is a gentle activity you can try:")
            print(f"- {random.choice(activities[mood])}")
        if mood == "history":
            if not mood_history:
                print("You haven't shared any moods with me yet.")
            else:
                print("Here's your mood history:")
                for i, m in enumerate(mood_history, 1):
                    print(f"{i}. {m}")
            continue
        print("Wanna hear a fun fact?")
        print(f"- {random.choice(fun_facts)}")
        print("And here's a compliment to make your day better:")
        print(f"- {random.choice(compliments)}")

        mood_history.append(mood)
