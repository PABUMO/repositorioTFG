import soundfile
import matplotlib.pyplot as plt
from CalculosDeFFT import *
from calcularConstanciaDeLaFormaDelSonido import *

def graficarOndas(in_onda, in_frecuenciaDeMuestreo):
    
    print("---------Inicia graficarOndas---------")
    
    valoresDeTiempo = numpy.arange(0, len(in_onda))/frecuenciaDeMuestreo
    fig, ax = plt.subplots()
    ax.plot(valoresDeTiempo,in_onda)
    ax.set(xlabel='Tiempo(s)', ylabel='Amplitud (dB)')
    plt.show()

def calcularDuracionDelSonido(in_onda, in_frecuenciaDeMuestreo):
    
    print("---------Inicia el calcularDuracionDelSonido---------")
    
    longitudDeLaOnda = len(in_onda);
    in_onda = in_onda / max(abs(in_onda));

    contadorDeCantidadDeDatos = 0; ##cuántos valores del eje Y importan.
  
    for dato in in_onda:
        if (abs(dato) >= 0.05): #Umbral de inicio de sonido.
            contadorDeCantidadDeDatos+=1
    
    return(contadorDeCantidadDeDatos/in_frecuenciaDeMuestreo);
    
print("---------Inicia el Main---------")

onda, frecuenciaDeMuestreo = soundfile.read('../Sonidos/200 Hz.ogg')

duracionDelSonido = calcularDuracionDelSonido(onda, frecuenciaDeMuestreo)

if(duracionDelSonido >= 1): #Evaluación de la duración del sonido.
    
    print("El sonido dura más de 1 segundo. Específicamente ", duracionDelSonido, " segundos.")
    listaResultante = calcularRangoPredominante(onda, frecuenciaDeMuestreo)
    valorInicialDelRangoPredominante = listaResultante[0]
    valorFinalDelRangoPredominante = listaResultante[1]

    if(valorInicialDelRangoPredominante >= 2900 and valorFinalDelRangoPredominante <= 3150): #Evaluación de la frecuencia del sonido.
        print("La frecuencia fundamental de la onda se encuentra dentro del rango de las bocinas")
        constanciaDeLaFormaDelSonido = calcularConstanciaDeLaFormaDelSonido(onda, frecuenciaDeMuestreo)
        if (constanciaDeLaFormaDelSonido >= 70):
            print("El sonido es una bocina.")
        else:
            print("El sonido no es una bocina, no tiene la constancia requerida.")
    else:
        print("El sonido no es una bocina, la frecuencia fundamental no se encuentra dentro del rango.")
else:
  print("El sonido no es una bocina, la duración del sonido es menor a la establecida.")
