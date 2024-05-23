def boyer_moore_search(text, pattern):
    n = len(text)
    m = len(pattern)

    # Costruzione della tabella di skip per i caratteri cattivi
    skip_table = {}
    for i in range(m):
        skip_table[pattern[i]] = i

    # Inizializzazione della posizione di inizio nel testo
    pos = 0
    while pos <= n - m:
        # Verifica del pattern dal fondo verso l'inizio
        i = m - 1
        while i >= 0 and pattern[i] == text[pos + i]:
            i -= 1

        # Se il pattern viene trovato, ritorna la posizione
        if i == -1:
            return pos

        # Altrimenti, calcola lo spostamento in base al carattere non corrispondente
        if text[pos + i] in skip_table:
            pos += max(1, i - skip_table[text[pos + i]])
        else:
            pos += i + 1

    # Pattern non trovato
    return -1


# Esempio di utilizzo
text = "abbacabbacababacababc"
pattern = "ababac"
result = boyer_moore_search(text, pattern)
if result != -1:
    print("Il pattern è stato trovato in posizione:", result)
else:
    print("Il pattern non è stato trovato nel testo.")
