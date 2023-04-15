print("--------------------------------------------------")
print("Hola ingeniero, bienvenido al programa")
print("--------------------------------------------------")

#Creacion de datos (paises/humanos y animales)

# Variables de pais 
pais1 = 'El Salvador'
pais2 = 'Colombia'
pais3 = 'Argentina'
pais4 = 'Bolivia'
pais5 = 'Alemania'
pais6 = 'India'
pais7 = 'Republica Dominicana'
pais8 = 'Francia'
pais9 = 'China'
pais10 = 'Brasil'

# Variables de nacionalidad
nac1 = 'Salvadoreño'
nac2 = 'Colombiano'
nac3 = 'Argentino'
nac4 = 'Boliviano'
nac5 = 'Aleman'
nac6 = 'Indio'
nac7 = 'Dominicano'
nac8 = 'Frances'
nac9 = 'Chino'
nac10 = 'Brasileño'

# Variables de especie
especie1 = 'Canino'
especie2 = 'Felino'
especie3 = 'Porcino'
especie4 = 'Aviar'
especie5 = 'Reptil'
especie6 = 'Mamifero'
especie7 = 'Anfibio'
especie8 = 'Insecto'
especie9 = 'Roedor'
especie10 = 'Aracnido'

# Variables de animal
animal1 = 'Perro'
animal2 = 'Gato'
animal3 = 'Cerdo'
animal4 = 'Paloma'
animal5 = 'Vibora'
animal6 = 'Elefante'
animal7 = 'Sapo'
animal8 = 'Mariposa'
animal9 = 'Raton'
animal10 = 'Araña'

# Capturar nombre desde teclado
nombre = str(input('\nIngrese su nombre: '))

#Menu de opciones
print('''Menu de opciones
         1. Humanos
         2. Animales''')

menu = int(input('¿Cual es la opción que desea seleccionar?'))

if menu == 1:

    print(f'''\nLista de los paises almacenados en el programa:
    1. {pais1}
    2. {pais2}
    3. {pais3}
    4. {pais4}
    5. {pais5}
    6. {pais6}
    7. {pais7}
    8. {pais8}
    9. {pais9}
    10. {pais10}''')
    
    opcionHumano = input('Ingrese el nombre o numero de lista de un pais: ''')
    
    if opcionHumano == '1' or opcionHumano == pais1:
        print(nombre, f'su país es {pais1} y su nacionalidad es: {nac1}')
    elif opcionHumano == '2' or opcionHumano == pais2:
        print(nombre, f'su país es {pais2} y su nacionalidad es: {nac2}')
    elif opcionHumano == '3' or opcionHumano == pais3:
        print(nombre, f'su país es {pais3} y su nacionalidad es: {nac3}')
    elif opcionHumano == '4' or opcionHumano == pais4:
        print(nombre, f'su país es {pais4} y su nacionalidad es: {nac4}')
    elif opcionHumano == '5' or opcionHumano == pais5:
        print(nombre, f'su país es {pais5} y su nacionalidad es: {nac5}')
    elif opcionHumano == '6' or opcionHumano == pais6:
        print(nombre, f'su país es {pais6} y su nacionalidad es: {nac6}')
    elif opcionHumano == '7' or opcionHumano == pais7:
        print(nombre, f'su país es {pais7} y su nacionalidad es: {nac7}')
    elif opcionHumano == '8' or opcionHumano == pais8:
        print(nombre, f'su país es {pais8} y su nacionalidad es: {nac8}')
    elif opcionHumano == '9' or opcionHumano == pais9:
        print(nombre, f'su país es {pais9} y su nacionalidad es: {nac9}')
    elif opcionHumano == '10' or opcionHumano == pais10:
        print(nombre, f'su país es {pais10} y su nacionalidad es: {nac10}')
    else:
        print('La opción ingresada no es válida')
    
# elif menu == 2:
#     opcionAnimal = str(input('Ingrese el nombre de una especie: '))
    
#     if opcionAnimal == 'Canino':
#         print('El tipo de animal que pertenece a esa especie es: ', animal1)
#     elif opcionAnimal == 'Felino':
#         print('El tipo de animal que pertenece a esa especie es: ', animal2)
#     elif opcionAnimal == 'Porcino':
#         print('El tipo de animal que pertenece a esa especie es: ', animal3)
#     elif opcionAnimal == 'Aviar':
#         print('El tipo de animal que pertenece a esa especie es: ', animal4)
#     elif opcionAnimal == 'Reptil':
#         print('El tipo de animal que pertenece a esa especie es: ', animal5)
#     elif opcionAnimal == 'Mamifero':
#         print('El tipo de animal que pertenece a esa especie es: ', animal6)
#     elif opcionAnimal == 'Anfibio':
#         print('El tipo de animal que pertenece a esa especie es: ', animal7)
#     elif opcionAnimal == 'Insecto':
#         print('El tipo de animal que pertenece a esa especie es: ', animal8)
#     elif opcionAnimal == 'Dictioptero':
#         print('El tipo de animal que pertenece a esa especie es: ', animal9)
#     elif opcionAnimal == 'Aracnido':
#         print('El tipo de animal que pertenece a esa especie es: ', animal10)
#     else:
#         print('La opción ingresada no es válida')
    
else:
    print('\nLa opción seleccionada no es válida')
    
print('\nFIN')


