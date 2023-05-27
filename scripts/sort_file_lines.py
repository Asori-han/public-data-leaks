with open('docs/dni.txt', 'r') as f:
    lines = f.readlines()

sorted_lines = sorted(lines)

with open('docs/sorted_dni.txt', 'w') as f:
    f.writelines(sorted_lines)
