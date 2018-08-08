#Quantitative Analysis Calculator - Connor Mattson
import re

periodTable = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U']
massNumbers = ['1.0079', '4.0026', '6.941', '9.0122', '10.811', '12.0107', '14.0067', '15.9994', '18.9984', '20.1797', '22.9897', '24.305', '26.9815', '28.0855', '30.9738', '32.065', '35.453', '39.948', '39.0983', '40.078', '44.9559', '47.867', '50.9415', '51.9961', '54.938', '55.845', '58.9332', '58.6934', '63.546', '65.39', '69.723', '72.64', '74.9216', '78.96', '79.904', '83.8', '85.4678', '87.62', '88.9059', '91.224', '92.9064', '95.94', '98', '101.07', '102.9055', '106.42', '107.8682', '112.411', '114.818', '118.71', '121.76', '127.6', '126.9045', '131.293', '132.9055', '137.327', '138.9055', '140.116', '140.9077', '144.24', '145', '150.36', '151.964', '157.25', '158.9253', '162.5', '164.9303', '167.259', '168.9342', '173.04', '174.967', '178.49', '180.9479', '183.84', '186.207', '190.23', '192.217', '195.078', '196.9665', '200.59', '204.3833', '207.2', '208.9804', '209', '210', '222', '223', '226', '227', '232.0381', '231.0359', '238.0289']


def molarMass():

	global compound
	global compound1
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	compound = input('Enter chemical compound: ')
	compound = list(compound)
	while compound == '0' or compound == '' or not any(_ in compound[0] for _ in alphabet):
		print('The compound must start with a letter and cannot contain any spaces')
		compound = input('Enter chemical compound: ')
		list(compound)
	
	compound = ''.join(compound)
	compound1 = compound
	compound = re.sub( r"([0-9])", r" \1", compound)
	compound = re.sub( r"([A-Z])", r" \1", compound)
	compound = compound.split(' ')
	if compound[0] == '' or compound[0] == ' ':
		del(compound[0])

	counter = 0
	while counter < len(compound):
		try:
			periodCounter = periodTable.index(compound[counter])
			compound[counter] = massNumbers[periodCounter]
			counter += 1
		except ValueError:
			compound[counter - 1] = float(compound[counter - 1]) * float(compound[counter])
			del(compound[counter])
	for _ in range(len(compound) - 1):
		compound[0] = float(compound[0]) + float(compound[1])
		del(compound[1])
		compound[0] = str(compound[0])
	global molarMassAnswer
	molarMassAnswer = (''.join(compound))

print('Note: This calculator does not work with americium (95 - Am) or any elements with a higher atomic number.')
toFind = input('What do you want to find [M, m, or n]? ')
toFind = list(toFind)
possibleStarts = ['M', 'm', 'n']

while len(toFind) == 0 or not any(_ in toFind[0] for _ in possibleStarts):
	print('Error: input must start with M, m or n.')
	toFind = input('What do you want to find [M, m, or n] ? ')


if toFind[0] == 'M':
	molarMass()
	print('M = ' + molarMassAnswer + ' g/mol')
else:

	if toFind[0] == 'm':
		molarMass()
		moles = input('How many moles of the substance do you have? ')
		molesIsNumber = 0
		while molesIsNumber == 0 or float(moles) < 0:
			if molesIsNumber == 0:
				try:
					float(moles)
					molesIsNumber = 1
				except ValueError:
					moles = input('How many moles of the substance do you have? (must be a positive number) ')
			else:
				moles = input('How many moles of the substance do you have? (must be a positive number) ')
	
		massAnswer = str(float(molarMassAnswer) * float(moles))
		print('m = ' + massAnswer + ' g')

	else:
		if toFind[0] == 'n':
			grams = input('How many grams of the substance do you have? ')
			molesIsNumber = 0
			while molesIsNumber == 0 or float(grams) < 0:
				if molesIsNumber == 0:
					try:
						float(grams)
						molesIsNumber = 1
					except ValueError:
						grams = input('How many grams of the substance do you have? (must be a positive number) ')
				else:
					grams = input('How many grams of the substance do you have? (must be a positive number) ')
		
			molarMass()
			molNumber = str(float(grams) / float(molarMassAnswer))
			print('n = ' + molNumber + ' mols of ' + ''.join(compound1))

		else:
			print('Error')