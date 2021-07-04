"""
Código creado por Electro de Una
Youtube: Electronica de Una
2021
"""
import max7219
from machine import Pin, SPI
import framebuf
from time import sleep
import random

spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3))
ss = Pin(5, Pin.OUT)
botonI=Pin(14, Pin.IN, Pin.PULL_DOWN)
botonD=Pin(15, Pin.IN, Pin.PULL_DOWN)

display = max7219.Matrix8x8(spi, ss, 1)

start = bytearray(b"\x00\x00\xee\x8a\xaa\xee\x00\x00")
auto = bytearray(b"@\xe0@\xa0")
pared = bytearray(b"\x80\x80\x00\x80\x80\x00\x80\x80")
fin = bytearray(b"\xaaU\xaaU\xaaU\xaaU")
fin2 = bytearray(b"U\xaaU\xaaU\xaaU\xaa")
autoBuff = framebuf.FrameBuffer(auto, 3, 4, framebuf.MONO_HLSB)
paredBuff = framebuf.FrameBuffer(pared, 8, 8, framebuf.MONO_HLSB)
finBuff = framebuf.FrameBuffer(fin, 8, 8, framebuf.MONO_HLSB)
fin2Buff = framebuf.FrameBuffer(fin2, 8, 8, framebuf.MONO_HLSB)
startBuff = framebuf.FrameBuffer(start, 8, 8, framebuf.MONO_HLSB)

def fin():
    for i in range(6):
        display.blit(finBuff,0,0)
        display.show()
        sleep(0.1)
        display.blit(fin2Buff,0,0)
        display.show()
        sleep(0.1)

display.brightness(1)   # ajustar brillo 1 a 15
display.fill(1)
display.show()
sleep(0.5)
display.fill(0)
display.show()
sleep(0.2)

for i in range(9):
    display.fill(0)
    display.blit(startBuff,8-i,0) #muestro mensaje GO
    display.show()
    sleep(0.1)
    
sleep(0.2)
numbers = {
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6"}

loop = 0
posAuto2x=4
posAuto2y=0
posicion=1
timer=0
dificultad=6 #6 lento, 1 rapido
nivel=1
contNivel=0
start=False

while True:
    display.fill(0)
    if start == False:
        if botonI.value() == 1 or botonD.value() == 1: #Hasta que no aprete un botón no inicia
            start=True
            loop = 0
            posAuto2x=4
            posAuto2y=0
            posicion=1
            timer=0
            dificultad=6
            nivel=1
            contNivel=0
    else:
        if contNivel == 200: #Cuando llega a 200 pasa de nivel
            dificultad -= 1
            timer=0
            contNivel = 0
            display.text(numbers[nivel],0,0) #Muestro el numero del nivel
            nivel +=1
            display.show()
            sleep(1)
        if timer == dificultad:
            timer=0
            loop += 1
            posAuto2y += 1
        if loop == 2:
            loop = -1
    
        if posAuto2y > nivel+11:
            posAuto2y=0
            autoRan = random.randrange(1, 3, 1)
            if autoRan == 1:
                posAuto2x=4
            else:
                posAuto2x=1
        
        if botonI.value() == 1: #Si apreto el botón de la izquierda, se mueve a la izquierda
            if posicion > 1:
                posicion-=1
        
        if botonD.value() == 1:
            if posicion < 4:
                posicion+=1
    
        if posAuto2x == 1 and posAuto2y > 4 and posicion < 4: #Si esta en la misma posicion que los autos, chocan
            fin()
            start=False
        elif posAuto2x == 4 and posAuto2y > 4 and posicion > 1:
            fin()
            start=False
        else:
            display.blit(paredBuff,0,loop)
            display.blit(autoBuff,posicion,4)
            display.blit(autoBuff,posAuto2x,posAuto2y-4)
            display.blit(paredBuff,7,loop)
        display.show()
        timer += 1
        contNivel += 1
        sleep(0.05)
