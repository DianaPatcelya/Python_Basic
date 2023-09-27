chess_players = {

    "Carlsen, Magnus": 1865,

    "Firouzja, Alireza": 2804,

    "Ding, Liren": 2799,

    "Caruana, Fabiano": 1792,

    "Nepomniachtchi, Ian": 2773

}
du_car = [{value: k} for k, value in chess_players.items()]
tu_car = {key[0]: value for key, value in du_car if int(value) >= 2000}

print(*[value[0] for value in du_car.values()])
print(*du_car, sep="\n")
print(*fri_car, sep="\n")

list_car = [[key[0:1], key[0:1]] for key in tu_car]
print(list_car)
