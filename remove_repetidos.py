def remove_repetidos(lista):
    index = 0
    final = []
    for item in lista:
        if not item in lista[index + 1:]:
            final.append(item)
        index += 1
    final.sort()
    return final