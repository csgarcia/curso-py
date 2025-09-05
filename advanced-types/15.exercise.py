# 1- Eliminar los espacios en blanco de un string y
# devolver una lista con los caracteres restantes

def remove_spaces(string) -> list:
    letters = [char.upper() for char in string if char != ' ']
    return letters

# 2- Contar en un diccionario cuanto se repiten
# los caracteres de un string


def count_characters_in_dictionary(string):
    dictionary = {}
    for char in string:
        char = char.upper()
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary

# 3- Ordenar las llaves de un diccionario por el valor
# que tienen y devolver una lista que contiene tuplas
# ej. [("a", 3), ("b", 2), ("c", 4), ("d", 4)]


def sort_dictionary_by_value(dictionary) -> tuple:
    # transform the dictionary into a list of tuples
    tuples_list = dictionary.items()
    # sort the list of tuples by the second element (value)
    # using second element of the tuple as key to sort
    sorted_tuples = sorted(tuples_list, key=lambda item: item[1], reverse=True)
    return sorted_tuples


# 4- De un listado de tuplas, devolver las tuplas que tengan
# el mayor valor. ej:
# [("a", 3), ("b", 2), ("c", 4), ("d", 4)] -> [("c", 4), ("d", 4)]
def get_max_value_tuples(tuples_list):
    if not tuples_list:
        return []
    # get the max value of the list of tuples
    tuple_with_max_value = max(tuples_list, key=lambda item: item[1])
    max_value = tuple_with_max_value[1]
    # filter the list of tuples to get only the tuples with the max value
    # not an elegant way
    # max_value_tuples = []
    # for item in tuples_list:
    #     if (item[1] == max_value):
    #         max_value_tuples.append(item)
    # return max_value_tuples
    max_value_tuples = [
        max_value_tuple for max_value_tuple in tuples_list if max_value_tuple[1] == max_value
    ]
    return max_value_tuples


# 5- Crear un mensaje que diga:
# Los caracteres que más se repiten con 4 repeticiones son:
# - C (En mayúscula)
# - D (En mayúscula)
def create_message(max_value_tuples):
    if not max_value_tuples:
        return "No hay caracteres que se repitan."
    for char in max_value_tuples:
        print(f"El caracter {char[0]} se repite {char[1]} veces.")


# 6- Juntar la solución de los ejercicios anteriores
# para encontrar los caracteres que más se repiten en un string
def main():
    string_to_analyze = 'Hola mundo este es mi stringe'
    string_no_spaces = remove_spaces(string_to_analyze)
    string_dictionary = count_characters_in_dictionary(string_no_spaces)
    sorted_characters = sort_dictionary_by_value(string_dictionary)
    max_value_tuples = get_max_value_tuples(sorted_characters)
    print(f"String sin espacios: {string_no_spaces}")
    print(f"Diccionario de caracteres: {string_dictionary}")
    print(f"Caracteres ordenados por valor: {sorted_characters}")
    print(f"Caracteres con mayor frecuencia: {max_value_tuples}")
    create_message(max_value_tuples)


main()


# string_to_analyze = 'Oportunidad Mejora'

# string_no_spaces = remove_spaces(string_to_analyze)
# string_dictionary = count_characters_in_dictionary(string_no_spaces)
# sorted_characters = sort_dictionary_by_value(string_dictionary)
# max_value_tuples = get_max_value_tuples(sorted_characters)
# print(f"String sin espacios: {string_no_spaces}")
# print(f"Diccionario de caracteres: {string_dictionary}")
# print(f"Caracteres ordenados por valor: {sorted_characters}")
# print(f"Caracteres con mayor frecuencia: {max_value_tuples}")
# create_message(max_value_tuples)
