# CONJUNTO CON FUNCION SET

# conjunto = set(["dato1","dato2","dato3"])

#DATOS MODIFICABLES DENTRO DE UN NO MODIFICABLE
# conjunto = set(["dato1","dato2",["datolist1","datonlis2"]])

# conjunto = set(["dato1","dato2",("datolist1","datonlis2")])

# METINEDO UN CONJUNTO DENTRO DEOTRO CONJUNTO

# conjunto1=frozenset({"dato1","dato2"})
# conjunto2 = {conjunto1,"dato3"}

# print(conjunto2)

# TEORIA DE CONJUUJNTOS 

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1
print(resultado)

# resultado2 = conjunto1.issuperset(conjunto2)
resultado2 = conjunto1 > conjunto2
print(resultado2)