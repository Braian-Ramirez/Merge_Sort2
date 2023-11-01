import random  # Importa el módulo random para generar números aleatorios y selecciones aleatorias.
import string  # Importa el módulo string para trabajar con cadenas de caracteres.

# Implementación del algoritmo de ordenamiento Merge Sort
def merge_sort(lista, inicio=0, fin=None):
    if fin is None:  # Si fin no está especificado, establece fin como la longitud de la lista. (O(1))
        fin = len(lista)

    if fin - inicio <= 1:  # Si la porción de la lista es de tamaño 0 o 1, está ordenada por definición. (O(1))
        return lista[inicio:fin]  # Devuelve la sublista. (O(1))

    # Divide la lista en dos mitades y ordena cada mitad recursivamente. (O(m * log(m)), donde 'm' es la longitud de la porción)
    mitad = (fin + inicio) // 2
    izquierda = merge_sort(lista, inicio, mitad)
    derecha = merge_sort(lista, mitad, fin)

    # Combina las dos mitades ordenadas. (O(n), donde 'n' es la suma de las longitudes de ambas listas)
    return merge(izquierda, derecha)

# Función para combinar dos listas ordenadas
def merge(izquierda, derecha):
    resultado = []  # Lista para almacenar el resultado combinado de las dos listas ordenadas. (O(1))

    # Combina las dos listas ordenadas seleccionando el elemento más pequeño en cada iteración. (O(n), donde 'n' es la suma de las longitudes de ambas listas)
    while (izquierda and derecha):
        if izquierda[0] < derecha[0]:
            resultado.append(izquierda[0])
            izquierda.pop(0)  # Elimina el elemento ya procesado de la lista izquierda. (O(1))
        else:
            resultado.append(derecha[0])
            derecha.pop(0)  # Elimina el elemento ya procesado de la lista derecha. (O(1))

    # Agrega los elementos restantes de izquierda y derecha. (O(n), donde 'n' es la suma de las longitudes de ambas listas)
    if izquierda:
        resultado += izquierda
    if derecha:
        resultado += derecha

    return resultado  # Devuelve la lista combinada y ordenada. (O(1))

# Punto de entrada del programa
if __name__ == "__main__":
    # Genera una lista de 500 documentos aleatorios, cada uno con 5 letras minúsculas aleatorias. (O(500))
    documentos = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(500)]

    # Ordena una porción de la lista de documentos (índices 100 a 199) usando Merge Sort. (O(m * log(m)), donde 'm' es la longitud de la porción)
    documentos_ordenados = merge_sort(documentos, 0, 499)

    # Imprime cada documento ordenado. (O(m), donde 'm' es la longitud de la porción)
    for documento in documentos_ordenados:
        print(documento)

    #La complejidad total del algoritmo en esta implementación es O(m * log(m))
