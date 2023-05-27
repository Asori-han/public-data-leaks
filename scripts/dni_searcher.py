import dni_matcher

dnis_complete = []
dnis_anonymized = []

file_complete = 'dnis_complete.txt'
file_anonymized = 'dnis_anonymized.txt'

with open(file_complete, 'r') as f:
    dnis_complete = f.readlines()

with open(file_anonymized, 'r') as f:
    dnis_anonymized = f.readlines()

# Prints which DNIs matches from each DNI in file_complete and each
# anonymized DNI in dnis_anonymized
for dni_complete in dnis_complete:
    for dni_anonymized in dnis_anonymized:
        if dni_matcher.dni_match(dni_complete, dni_anonymized):
            print(f"{dni_anonymized[:-1]} matches with {dni_complete[:-1]}")
