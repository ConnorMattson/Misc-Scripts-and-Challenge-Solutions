# Problem E 2009 - Connor Mattson

data = input("1 2 3   X X X\n4 5 6     O O\n7 8 9   O   X\nEnter the starting letter followed by a list of moves e.g. 'X 1 5 9 7 3 6 2' for the game above: ").split(" ")
table = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}
for i in range(len(data)): table[data[i]] = ['X', 'O'][::1 - 2*(data[0]=='X')][i % 2]
if (table['1'] == table['2'] == table['3'])  or  (table['1'] == table['4'] == table['7'])  or  (table['1'] == table['5'] == table['9']): winner = table['1']
elif (table['2'] == table['5'] == table['8'])  or  (table['4'] == table['5'] == table['6'])  or  (table['7'] == table['5'] == table['3']): winner = table['5']
elif (table['7'] == table['8'] == table['9'])  or  (table['3'] == table['6'] == table['9']): winner = table['9']
else: winner = "Draw"

print("Your game was:\n" + table['1'], table['2'], table['3'] + '\n' + table['4'], table['5'], table['6'] + '\n' + table['7'], table['8'], table['9'])
print("The game was won by:", winner)