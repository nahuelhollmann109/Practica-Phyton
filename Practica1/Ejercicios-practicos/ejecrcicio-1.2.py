# DATOS
frase= input("Decime una frase: ")

palabras_separadas= frase.split(" ")
cantidad_palabra=len(palabras_separadas)

print(f'dijiste {cantidad_palabra} y tardaste {cantidad_palabra/2} segundos')

print(f'dalto lo diria en {cantidad_palabra*100/2*1.3/100} segundos')

if cantidad_palabra >120:
    print("tampoco te pedi un testamento")
    