# juego-matriz

 TMini video juego con la Raspberry Pi Pico y una Matriz 8x8, programado con Micropython.
 
 Video:
https://www.youtube.com/watch?v=tTS1omT62Jg

Para generar las imagenes que se muestran en la Matriz vamos a ir a la pagina:

http://xlr8.at/8x8hexbin/	

seleccionamos los leds para formar la imagen

![image](https://user-images.githubusercontent.com/85527788/164893602-c3fc3d9d-f708-453f-88b1-f69311d659bd.png)

copiamos los valores que estan en "Dec"

https://www.programiz.com/python-programming/online-compiler/

from array import array
print("Hello world")
a=array("B",[36, 126, 255, 255, 255, 195, 129])
print(a.tostring())
