fires = input().split("#")
fires = " = ".join(fires)
fires = fires.split(" = ")
total_water = int(input())
total_used_water = 0
efford = 0
cells = []
for i in range(len(fires)):
    if i % 2 == 1:
        s = fires[i-1]
        n = fires[i]

        if s == "High" and 80 < int(n) < 126:
            if total_water - int(n) >= 0:
                efford += int(n) * 0.25
                total_used_water += int(n)
                total_water -= int(n)
                cells.append(n)

        elif s == "Medium" and 50 < int(n) < 81:
            if total_water - int(n) >= 0:
                efford += int(n) * 0.25
                total_used_water += int(n)
                total_water -= int(n)
                cells.append(n)

        elif s == "Low" and 0 < int(n) < 51:
            if total_water - int(n) >= 0:
                efford += int(n) * 0.25
                total_used_water += int(n)
                total_water -= int(n)
                cells.append(n)
print("Cells:")
for i in cells:
    print(f" - {i}")
print(f"Effort: {efford:.2f}")
print(f"Total Fire: {total_used_water}")