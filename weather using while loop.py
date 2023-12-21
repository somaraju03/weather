def predict_weather(t, h, ws):
    return 0.5 * t**2 - 0.2 * h + 0.1 * ws - 15

while True:
    t = int(input("Enter the temperature: "))
    h = int(input("Enter the humidity: "))
    ws = int(input("Enter the wind speed: "))
    
    weather_score = predict_weather(t, h, ws)
    
    if weather_score > 300:
        print("Sunny")
    elif 200 < weather_score <= 300:
        print("Cloudy")
    elif 100 < weather_score <= 200:
        print("Rainy")
    elif weather_score <= 100:
        print("Stormy")
    
    another_input = input("Do you want to predict weather again? (yes/no): ")
    if another_input.lower() != 'yes':
        break
