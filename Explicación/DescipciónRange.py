# El range() genera una secuencia de números que van desde 0 por defecto hasta el número que se pasa como parámetro menos 1. 
# En realidad, se pueden pasar hasta tres parámetros separados por coma, en 
# donde el primer es el inicio de la secuencia, el segundo el final y el tercero el salto que se desea entre números. 
# Por defecto se empieza en 0 y el salto es de 1.

# EJEMPLO:

# range(inicio, fin, salto)

# Por lo tanto, si llamamos a range() con (5,20,2), se generarán números de 5 a 20 de dos en dos. 
# Un truco es que el range() se puede convertir en list.

# DATOS DE ENTRADA:

print(list(range(5, 20, 2)))

# DATOS DE SALIDA:

# [5, 7, 9, 11, 13, 15, 17, 19]