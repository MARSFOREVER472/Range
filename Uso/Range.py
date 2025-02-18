# USO DEL RANGE:

# Uno de las iteraciones mas comunes que se realizan, es la de iterar un número entre por ejemplo 0 y n. 
# Si ya programas, estoy seguro de que estas cansado de escribir esto, aunque sea en otro lenguaje. 
# Pongamos que queremos iterar una variable i de 0 a 5. 
# Haciendo uso de lo que hemos visto anteriormente, podríamos hacer lo siguiente:

# EJEMPLO PRÁCTICO:

# DATOS DE ENTRADA:

for i in (0, 1, 2, 3, 4, 5):
    print(i)

# DATOS DE SALIDA:

# 0
# 1
# 2
# 3
# 4
# 5

# Se trata de una solución que cumple con nuestro requisito. 
# El contenido después del in se trata de una clase que como ya hemos visto antes, es iterable, y es de hecho una tupla. 
# Sin embargo, hay otras formas de hacer esto en Python, haciendo uso del range().

# EJEMPLO:

# DATOS DE ENTRADA:

for i in range(6):
    print(i)

# DATOS DE SALIDA:

# 0
# 1
# 2
# 3
# 4
# 5

# El range() genera una secuencia de números que van desde 0 por defecto hasta el número que se pasa como parámetro menos 1. 
# En realidad, se pueden pasar hasta tres parámetros separados por coma, donde el primer es el inicio de la secuencia, el segundo el final y el tercero el salto que se desea entre números. 
# Por defecto se empieza en 0 y el salto es de 1.

# EJEMPLO:

# range(inicio, fin, salto)

# Por lo tanto, si llamamos a range() con (5,20,2), se generarán números de 5 a 20 de dos en dos. 
# Un truco es que el range() se puede convertir en list.

# EJEMPLO:

# DATOS DE ENTRADA:

for i in range(5, 20, 2):
    print(i)

# DATOS DE SALIDA:

# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19