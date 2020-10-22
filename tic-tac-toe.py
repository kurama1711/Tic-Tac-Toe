cross = True
step = 1
moves = {}

for i in range(0, 3):
  for j in range(0, 3):
    moves[(i, j)] = '-'

def print_field():
  print("  0 1 2")

  for i in range(0, 3):
    row = str(i)
    for j in range(0, 3):
      if (j, i) in moves:
        row += " " + moves[(j, i)]
      else:
        row += " -"
    print(row)

def game_check():
  print_field()

  for i in range(0, 3):
    x_counter_Ox = x_counter_Oy = o_counter_Ox = o_counter_Oy = 0

    for m in moves:
      if m[0] == i and moves[m] == 'X':
        x_counter_Ox += 1

      if m[1] == i and moves[m] == 'X':
        x_counter_Oy += 1

      if m[0] == i and moves[m] == 'O':
        o_counter_Ox += 1

      if m[1] == i and moves[m] == 'O':
        o_counter_Oy += 1

  if any([x_counter_Ox == 3, x_counter_Oy == 3,
        moves[(0, 0)] == moves[(1, 1)] == moves[(2, 2)] == 'X',
        moves[(0, 2)] == moves[(1, 1)] == moves[(2, 0)] == 'X']):
    print("\nИгра окончена!\nПобедил Игрок 1 (крестики)!")
    return 1

  if any([o_counter_Ox == 3, o_counter_Oy == 3,
        moves[(0, 0)] == moves[(1, 1)] == moves[(2, 2)] == 'O',
        moves[(0, 2)] == moves[(1, 1)] == moves[(2, 0)] == 'O']):
    print("\nИгра окончена!\nПобедил Игрок 2 (нолики)!")
    return 2

  if step == 9:
    print("\nИгра окончена.\nВышла ничья.")
    return 0

  print("\nИгра продолжается.")
  return 3

print("Добро пожаловать в игру Крестики-Нолики!\n\n1) Двое Игроков ходят по очереди.\n2) Игра всегда начинается с хода крестиком.\n3) Чтобы сделать ход, нужно ввести координаты клетки через пробел: X Y\n")
print_field()

while step <= 9:
  if cross == True:
    print("\nСейчас ходит Игрок 1 (крестики)")
  else:
    print("\nСейчас ходит Игрок 2 (нолики)")

  x_y = tuple(map(int, input("Введите координаты клетки: ").split(' ')))

  if 0 <= x_y[0] <= 2 and 0 <= x_y[1] <= 2:
    if moves[x_y] != '-':
      print("Эта клетка уже занята. Введите другие координаты.")
      continue
    else:
      if cross == True:
        moves[x_y] = 'X'
      else:
        moves[x_y] = 'O'

      print("Ход сделан.\n")
  else:
    print("Введены недопустимые координаты. Введите другие.")
    continue

  if cross == True:
    cross = False
  else:
    cross = True

  game_check()
  step += 1
