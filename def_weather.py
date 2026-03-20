def weather(season, goodbad):
    if season == "summer" and goodbad == "good":
        print("It's a great time to go to the beach!")
    elif season == "summer" and goodbad == "bad":
        print("It's too hot outside, better stay indoors.")
    elif season == "winter" and goodbad == "good":
        print("It's a perfect time for skiing!")
    elif season == "winter" and goodbad == "bad":
        print("It's too cold outside, better stay indoors.")
    elif season == "spring" and goodbad == "good":
        print("The flowers are blooming, it's a beautiful time of year!")
    elif season == "spring" and goodbad == "bad":
        print("It's raining, better stay indoors.")
    elif season == "fall" and goodbad == "good":
        print("The leaves are changing colors, it's a lovely time of year!")
    elif season == "fall" and goodbad == "bad":
        print("It's too windy outside, better stay indoors.")

input_season = input("Enter the season (summer, winter, spring, fall): ")
input_goodbad = input("Is the weather good or bad? (good/bad): ")

weather(input_season, input_goodbad)