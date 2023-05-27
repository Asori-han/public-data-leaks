import argparse
import json
import dni_matcher

# Read the JSON file and store its content in a variable
with open('scripts/regions.json', encoding='utf-8') as f:
    regions = json.load(f)['regions']

# Define the command line arguments
parser = argparse.ArgumentParser(description='Interactive menu')
parser.add_argument('-r', '--region', type=int, help='Select a region from the menu')
parser.add_argument('-d', '--dni', type=str, help='Enter a DNI from the menu')
parser.add_argument('-p', '--prefix', type=str, help='Enter a prefix from the menu')

# Read the command line arguments
args = parser.parse_args()

# If the user passed an option argument, use that option number
# Otherwise, prompt the user to select an option from the menu
if args.region:
    selected_region = args.region
elif not args.prefix:
    # Show the menu options to the user
    print("Select an option from the menu:")
    print('0. No region')
    for i, region in enumerate(regions):
        print(f"{i+1}. {region['name']}")

    # Prompt the user to select an option and validate their input
    selected_region = input("Enter the number of the option you want to select: ")
    try:
        selected_region = int(selected_region)
        if selected_region < 0 or selected_region > len(regions):
            raise ValueError
    except ValueError:
        print("Error: invalid selection. Enter a number between 0 and", len(regions))

# If the user's selection is valid, show the details of the selected option
if  not args.prefix and selected_region != 0:
    region = regions[selected_region-1]
    prefixes = list(region['codes'])
    if not args.region:
        print(f"You have selected option {region['name']}.")
        print('Prefixes for selected region:')
        for prefix in prefixes:
            print(prefix, end=' ')
        print()
elif args.prefix:
    prefixes = []
    prefixes.append(args.prefix)
else:
    prefixes = []

valid_dni = False
while not valid_dni:
    if args.dni:
        dni = args.dni
    else:
        # Prompt the user to enter a DNI
        dni = input("Enter a DNI: (Ex: ***0000**)\n")
    # Validate the DNI format
    if len(dni) != 9:
        print("Error: invalid DNI format. The DNI should have 9 digits and a letter at the end.")
    elif not dni[:-1].replace('*', '0').isdigit():
        print("Error: invalid DNI format. The first 8 characters of the DNI should be digits.")
    elif dni[-1].upper() not in "*TRWAGMYFPDXBNJZSQVHLCKE":
        print("Error: invalid DNI format.")
    else:
        valid_dni = True

dni_arr = []

# Prints all DNI candidates from anonymized one
if len(prefixes) > 0:
    for prefix in prefixes:
        dni_arr.extend(dni_matcher.list_dni(prefix + dni[len(prefix):-1]))
else:
    dni_arr = dni_matcher.list_dni(dni[:-1])
for dni in dni_arr:
    print(dni)
