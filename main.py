import random


Player_1 = input('Игрок 1. Введите ваше имя : ')
Player_2 = input('Игрок 2. Введите ваше имя : ')

Player_1_score = 0
Player_2_score = 0

dice_1 = [1, 2, 3, 4, 5, 6]
dice_2 = [1, 2, 3, 4, 5, 6]


def random_dice():
    for i in range(5):
        random.shuffle(dice_1)
        random.shuffle(dice_2)
        random_dice_1 = random.choice(dice_1)
        random_dice_2 = random.choice(dice_2)
        return random_dice_1 + random_dice_2


for i in range(3):
    random_player = [Player_1, Player_2]
    First_random_player = random.choice(random_player)

    if First_random_player == Player_1:
        print('\n', 'Первым играет : ', Player_1)
        Player_1_score = random_dice()
        Player_2_score = random_dice()
    else:
        print('\n', 'Первым играет : ', Player_2)
        Player_2_score = random_dice()
        Player_1_score = random_dice()

    if Player_1_score > Player_2_score:
        print('Победил', Player_1, ', счёт игрока', Player_1, ':',
              Player_1_score, ', а счёт игрока', Player_2, ':', Player_2_score, '\n')
    elif Player_2_score > Player_1_score:
        print('Победил', Player_2, ', счёт игрока', Player_2, ':',
              Player_2_score, ', а счёт игрока', Player_1, ':', Player_1_score, '\n')
    else:
        print('Ничья, счёт игрока', Player_1, ':', Player_1_score,
              ', а счёт игрока', Player_2, ':', Player_2_score, '\n')
