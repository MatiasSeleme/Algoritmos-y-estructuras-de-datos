def contar_palabra(vector, palabra, index=0):
    if index >= len(vector):
        return 0

    count = 1 if vector[index] == palabra else 0

    return count + contar_palabra(vector, palabra, index + 1)
vector_palabras = ["Hola", "mesa", "Hola", "gato", "Sebastian", "Hola"]
palabra_a_contar = "Hola"
resultado = contar_palabra(vector_palabras, palabra_a_contar)
print(f"La palabra '{palabra_a_contar}' aparece {resultado} veces.")
