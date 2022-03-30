import pyfirmata
import time

board = pyfirmata.ArduinoMega('COM3')
led = board.get_pin('d:10:o')

contador = 1

while contador <= 10:
    print(contador)
    led.write(1)
    time.sleep(contador)
    led.write(0)
    time.sleep(contador)
    contador+=1
