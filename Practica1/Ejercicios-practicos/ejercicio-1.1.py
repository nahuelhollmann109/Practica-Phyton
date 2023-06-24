# PROMEDIOS DE DURACION CURSOS

otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_promedio=4
dalto_curso=1.5

# PROMEDIO DE DURACION

diferencia_min=100-dalto_curso/otros_cursos_min*100

diferencia_max=100-dalto_curso*1000//otros_cursos_max/10

diferencia_promedio=100-dalto_curso/otros_cursos_promedio*100


print(f'diferencia minima {diferencia_min}')

print(f'diferencia maxima {diferencia_max}')

print(f'diferencia promedio {diferencia_promedio}')


# PROMEDIOS DE DURACION  EN CRUDO

crudo_promedio=5
crudo_datlo=3.5

tiempo_crudo=100-otros_cursos_promedio*1000//crudo_promedio/10

tiempo_crudo_dalto=100-dalto_curso*1000//crudo_datlo/10

print(f'tiempo crudo otros cursos {tiempo_crudo}')

print(f'tiempo crudo curso dalto {tiempo_crudo_dalto}')


# EQUIVALENCIA EN HORAS
print(f'ver 10 horas de cursos daltos equivale {otros_cursos_promedio*100//dalto_curso/10} horas')
print(f'ver 10 horas de otrso cursos equivale {dalto_curso*100//otros_cursos_promedio/10} horas de dalto')