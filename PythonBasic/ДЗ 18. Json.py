import json
user_data = {
    111111: ("Harry", 18),
    222222: ("Ron", 19),
    333333: ("Hermione", 17),
    444444: ("Draco", 21),
    555555: ("Marvolo", 45),
    666666: ("Severus", 40),
}
with open('ДЗ_18.json', 'w') as f:
    json.dump(user_data, f)

print("Словник було записано у файл ДЗ_18.json.")
