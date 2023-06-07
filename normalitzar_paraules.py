def normalitzar(s):
    canvia = (
        ("á", "a"),
        ("à", "a"),
        ("é", "e"),
        ("è", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ò", "o"),
        ("ú", "u"),
    )
    for a, b in canvia:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

print(normalitzar("¡Hólá, múndó!"))
print(normalitzar("¡HÓLÁ, MÚNDÓ!"))