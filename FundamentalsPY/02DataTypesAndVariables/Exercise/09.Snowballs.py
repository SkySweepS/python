n = int(input())
ball_weight = -1
ball_time = -1
ball_quality = -1
ball_value = -1

for i in range(1, n + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight // time) ** quality
    if value > ball_value:
        ball_value = value
        ball_weight = weight
        ball_time = time
        ball_quality = quality

print(f"{ball_weight} : {ball_time} = {ball_value} ({ball_quality})")