time = input().split()

h = time[0].split(":")

if h[0].isdigit() and h[1].isdigit():

    hour = []
    for i in h:
        hour.append(int(i))

    if time[1] == "AM":
        if hour[0] == 12 or 0 < hour[0] < 3 and 0 <= hour[1] <= 59:
            print("beer time")
        elif hour[0] >= 3 and hour[0] <= 11 and 0 <= hour[1] <= 59:
            print("non-beer time")
        if hour[0] > 12 or hour[0]<= 0:
            print("invalid time")
        elif hour[1] < 0 or hour[1] > 59:
            print("invalid time")
    elif time[1] == "PM":
        if hour[0] >= 1 and hour[0] <= 11 and 0 <= hour[1] <= 59:
            print("beer time")
        elif hour[0] == 12 and 0 <= hour[1] <= 59:
            print("non-beer time")
        elif hour[0] > 12 or hour[0] <= 0:
            print("invalid time")
        elif hour[1] < 0 or hour[1] > 59:
            print("invalid time")
    else:
        print("invalid time")
else:
    print("invalid time")
