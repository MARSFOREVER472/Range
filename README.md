# **_Range en Python_**

### **_Uso del range_**

- **_Una de las iteraciones más comunes que se realizan, es la de iterar un número entre por ejemplo ```0``` y ```n```._**
  
- **_Si ya programas, estoy seguro de que estas cansado de escribir esto, aunque sea en otro lenguaje._**
  
- **_Pongamos que queremos iterar una variable i de 0 a 5. Haciendo uso de lo que hemos visto anteriormente, podríamos hacer lo siguiente._**
  
```  
for i in (0, 1, 2, 3, 4, 5):
    print(i) #0, 1, 2, 3, 4, 5
```

- **_Se trata de una solución que cumple con nuestro requisito._**
  
- **_El contenido después del ```in``` se trata de una clase que como ya hemos visto antes, es iterable, y es de hecho una tupla._**
  
- **_Sin embargo, hay otras formas de hacer esto en Python, haciendo uso del ```range()```._**
for i in range(6):
    print(i) #0, 1, 2, 3, 4, 5
