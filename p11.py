palabras = ("pixel", "civil", "paco", "hijo", "toxico", "Camion", "Clave", "Ximena", "Damian", "Lili", "Claudia", "Medallon", "Clima")
romanos = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}

for palabra in palabras:
    numeroRomano = ""
    letras = []

    letras = [letra for letra in palabra.lower() if letra in romanos]
    
    
    numeroRomano= "".join(letras)

    if numeroRomano:
        print(f"La palabra '{palabra}' contiene el numero romano: {numeroRomano}")
