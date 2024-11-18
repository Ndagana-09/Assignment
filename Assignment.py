print('''
For pressure press A
For power press B
For density press C
For potential_energy press D
For force press E
''')

def calculate_pressure():
    force = float(input('Enter force: '))
    area = float(input('Enter area: '))
    pressure = force / area
    print(f"pressure: {pressure} units")


def calculate_power():
    work = float(input('Enter work: '))
    time = float(input('Enter time: '))
    power = work / time
    print(f"power: {power} units")


def calculate_density():
    mass = float(input('Enter mass: '))
    volume = float(input('Enter volume: '))
    density = mass / volume
    print(f"density: {density} units")


def calculate_potential_energy():
    mass = float(input('Enter mass: '))
    gravity = float(input('Enter gravity: '))
    height = float(input('Enter height: '))
    potential_energy = mass * gravity * height
    print(f"potential_energy: {potential_energy} units")

def calculate_force():
    mass = float(input('Enter mass: '))
    acceleration = float(input('Enter acceleration: '))
    force = mass * acceleration
    print(f"force: {force} units")

# Main code to prompt the user for a choice
choice= input ("What do you need (A/B/C/D/E)? ").strip().upper()

if choice == 'A':
    calculate_pressure()
elif choice == 'B':
    calculate_power()
elif choice == 'C':
    calculate_density()
elif choice == 'D':
    calculate_potential_energy()
elif choice ==  'E':
    calculate_force()
else:
    print('Invalid choice. Please enter an alphabet between A to E')




