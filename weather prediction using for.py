for _ in range(1):
    t = int(input("Enter value for t: "))
    h = int(input("Enter value for h: "))
    w = int(input("Enter value for w: "))
    W = (0.5 * t * t) - (0.2 * h) + (0.1 * w)

    if W > 300:
        print("Sunny")
    elif 200 < W <= 300:
        print("Cloudy")
    elif 100 < W <= 200:
        print("Rainy")
    elif W <= 100:
        print("Stormy")
