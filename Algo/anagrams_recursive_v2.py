#author: Marcello Mora

def anagrammi(parola):
    set_anagrammi = set()
    parziale = ""
    anagrammi_ricorsivo(parola, parziale, set_anagrammi)
    return list(set_anagrammi)


def anagrammi_ricorsivo(source, destination, results):
    if len(source) == 0:
        results.add(destination)
    else:
        for letter in source:
            anagrammi_ricorsivo(source.replace(letter, "", 1), destination + letter, results)
            # in questa soluzione non c'è bisogno di fare backtraking:
            #   - nè per destination (che tiene traccia della soluzione "parziale")
            #   - nè per source (che tiene traccia delle lettere ancora disponibili)
            # perché vengono create nuove ogni volta, al volo, passandole come parametro alla funzione
            # in sostanza, quando la funzione anagrammi_ricorsivo chiamata ritornerà, la funzione
            # chiamante vedrà ancora le versioni "vecchie" di destination e source


mia_parola = "dog"
print(anagrammi(mia_parola))
