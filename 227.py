tim = input()
rus = input()
tim_win = 'Тимур'
rus_win = 'Руслан'
draw = 'ничья'
stone = 'камень'
scissors = 'ножницы'
paper = 'бумага'
if tim == rus:
    print(draw)
elif tim == stone and rus == scissors:
    print(tim_win)
elif tim == stone and rus == paper:
    print(rus_win)
elif tim == scissors and rus == stone:
    print(rus_win)
elif tim == scissors and rus == paper:
    print(tim_win)
elif tim == paper and rus == scissors:
    print(rus_win)
elif tim == paper and rus == stone:
    print(tim_win)