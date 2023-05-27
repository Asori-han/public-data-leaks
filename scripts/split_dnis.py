import sys
import dni_matcher

name = sys.argv[1]

with open(f"{name}.txt", 'r') as f:
    lines = f.readlines()

sorted_lines = sorted(lines)

# Remove duplicated entries
sorted_lines = list(dict.fromkeys(sorted_lines))

# Splits DNIs between anonymized and complete on two files
with open(f"{name}_complete.txt", 'w') as f:
    with open(f"{name}_anonymized.txt", 'w') as g:
        for line in sorted_lines:
            if line.find('*') == -1:
                if dni_matcher.calculate_dni_letter(int(line[:8])) == line[8]:
                    f.write(line.upper())
                else:
                    print(f"Invalid DNI: {line}")
            else:
                g.write(line)
