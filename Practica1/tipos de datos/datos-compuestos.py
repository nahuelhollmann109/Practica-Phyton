# LISTA se pueden modificar
lista = ["lucas","Nahuel",True,1.50]
# TUPLA no se puede modificar el elemento 
# pero si se puede redefinir
tupla = ("lucas","Nahuel",True,1.50)
# CONJUNTO (SET) no podemos modificar el valor 
# del elemento pero si podemos redefinir el contenido
# no se puede acceder a los datos desde el indice
# no permite duplicado de datos
# son datos desordenados
conjunto = {"lucas","Nahuel",True,1.50}
# DICCIONARIO parecido a un JSON
diccionario = {
    'nombre':"Nahuel",
    'apellido':"hollmann"
}
print(diccionario['nombre'])