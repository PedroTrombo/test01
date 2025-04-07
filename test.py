
# #sum puede sumar todos los valores de una lista
# lista=[1,2,3,4,5,6,7,8]

# resultado=sum(lista)

# print(f'El resultado es: {resultado}')

# #sum puede sumar todos los valores de una lista comenzando desde un valor inicial

# resultado02=sum(lista, 20)

# print(f'El resultado es: {resultado02}')


# #funcion next() devuelve el siguente calor de un elemento interable cada vez que se ejecuta

# lista_iterador=iter(lista)


# print(f'El resultado es: {next(lista_iterador)}') #devuelve 1
# print(f'El resultado es: {next(lista_iterador)}') #devuelve 2

#Tratamiento de excepciones

def division(numerador,divisor):

    try:
        resultado=numerador/divisor
        return resultado
    # except ZeroDivisionError:
    #     print('Error: división por cero')
    except Exception as e:
        print(f'Ocurrio un error: {e}') #captura cualquier error


division(2,0)