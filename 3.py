mano = [
    {"valor": 10, "palo": "Picas"},
    {"valor": "A", "palo": "Corazones"},
    {"valor": 5, "palo": "Tréboles"},
    {"valor": "J", "palo": "Diamantes"},
    {"valor": 7, "palo": "Corazones"}
]

# Función lambda para calcular el valor numérico de una carta
calcular_valor_carta = lambda carta: (10 if carta["valor"] in ("J", "Q", "K") else
                                    1 if carta["valor"] == "A" else
                                    int(carta["valor"]))

# Calcular el valor total de la mano de cartas
valor_total = sum(map(calcular_valor_carta, mano))

# Imprimir el valor total de la mano
print("Valor total de la mano:", valor_total)