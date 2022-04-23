# Video juego matriz

Mini video juego con la Raspberry Pi Pico y una Matriz 8x8, programado con Micropython.
 
Video:
https://www.youtube.com/watch?v=tTS1omT62Jg

Para generar las imagenes que se muestran en la Matriz vamos a ir a la pagina:

http://xlr8.at/8x8hexbin/	

Seleccionamos los leds para formar la imagen

![image](https://user-images.githubusercontent.com/85527788/164893689-45d801f5-3d05-460b-8af6-bf7212acb98b.png)

copiamos los valores que estan en "Dec"

Vamos a la pagina:

https://www.programiz.com/python-programming/online-compiler/

 y pegamos el siguiente codigo:
 
from array import array
print("Hello world")
a=array("B",[64, 224, 64, 160])
print(a.tostring())

![image](https://user-images.githubusercontent.com/85527788/164893967-e6e0c67f-a814-425a-b4c4-24d558adef0b.png)

Dentro del array reemplazamos los valores con los copiados anteriormente, borrando los 0 (ceros)

![image](https://user-images.githubusercontent.com/85527788/164894002-ddaca2a9-96dd-4a52-9e9c-4024eb6b65ab.png)

Click en "Run" y copiamos los valores que están en la ventanda "Shell"

![image](https://user-images.githubusercontent.com/85527788/164893820-fec197ff-414c-4a33-b7d7-331716b312ae.png)

