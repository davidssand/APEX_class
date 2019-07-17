scenario = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1]
            ]

car = [3, 0]

def boundry_restrictions(coordinates):
  pass

def move_sequence(car, directions):
  pass

def move(car, direction):
  if direction == 'N':
    car[0] -= 1
  elif direction == 'S':
    car[0] += 1
  elif direction == 'L':
    car[1] += 1
  elif direction == 'O':
    car[1] -= 1
  else
    Warning('Invalid Direction')
  print(car)
  return car

move(car,'NNLL')

move(car, 'K')
print(car)


print(move_sequence(car, "NNLLNNO") == [0, 1])

print("done")