weather = (0, 1, 0, 0, 1, 0, 1, 0, 0, 1)

def predict_weather(weather):
    sunny = 0
    rainy = 0
    for i in weather:
        if i == 0:
            rainy += 1
        else:
            sunny += 1
    if sunny > rainy:
        return "Good weather ahead!"
    elif rainy > sunny:
        return "Rainy days are coming!"
    else:
        return "Weather is unpredictable!"

print(predict_weather(weather))            