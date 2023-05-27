# Returns letter from DNI number
def calculate_dni_letter(dni_number):
    dni_letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    index = dni_number % 23
    letter = dni_letters[index]
    return letter

# Returns a list with all DNI candidates from anonymized one
def list_dni(str, start = 0, dni_arr = None):
    if dni_arr is None:
        dni_arr = []
    if start < len(str) and str[start] == '*':
        for x in range(10):
            list_dni(f"{str[:start]}{x}{str[(start+1):]}", start+1, dni_arr)
    elif start == len(str):
        dni = f"{str}{calculate_dni_letter(int(str))}"
        dni_arr.append(dni)
    else:
        list_dni(str, start+1, dni_arr)
    return dni_arr

# Returns if a DNI matches with anonymized one
def dni_match(dni1, dni2):
    if dni1 == dni2:
        return True
    for i in range(len(dni1)):
        if not (dni1[i] == dni2[i] or dni1[i] == '*' or dni2[i] == '*'):
            return False
    return True
