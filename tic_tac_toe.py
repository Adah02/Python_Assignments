import random;

tic_tac = [['-','-','-'],['-','-','-'],['-','-','-']];

for index in range(0,3):
  print(tic_tac[index])

win = 0;


random_number = random.randrange(1,3);
print(f'Player {random_number} starts')

print('player = X \nPlayer = O') 

# print('1 2 3 \n4 5 6 \n7 8 9')

counter = 0;
while counter != 9:
  row = int(input('row: '))
  column = int(input('column: '))
  choice = str(input('choice: '))
  tic_tac[row-1][column - 1] = choice
  counter += 1;
  for index in range(0,3):
    print(tic_tac[index])




