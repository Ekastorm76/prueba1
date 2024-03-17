meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "Algo aterrador o sinietro",
            "AGROO": "Ponerse agresivo o enojado(al añadirle una N al final es un Pokemon)",
            }
for i in range(4):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
       print(meme_dict[word])
    else:
        print("Ups, no lo sabemos")
