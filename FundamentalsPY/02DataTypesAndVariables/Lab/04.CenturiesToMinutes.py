cent = int(input())
year = cent * 100
days = int(year * 365.2422)
hours = days * 24
min = hours * 60
print(f"{cent} centuries = {year} years = {days} days = {hours} hours = {min} minutes")