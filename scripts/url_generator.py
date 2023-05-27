for x in range(1000000):
    with open('urls_caib.txt', 'a', encoding='utf-8') as f:
        url = f"https://www.caib.es/sites/fp/f/{x}\n"
        f.write(url)
