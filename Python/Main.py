import numpy
import pandas as pd
import matplotlib.pyplot as plt
import librosa as lr
from glob import glob
import soundfile

onda, frecuenciaDeMuestreo = soundfile.read('../Sonidos/Pito de padre 1.ogg')

def graficarOndas(in_onda, in_frecuenciaDeMuestreo):
    valoresDeTiempo = numpy.arange(0, len(in_onda))/frecuenciaDeMuestreo
    fig, ax = plt.subplots()
    ax.plot(valoresDeTiempo,in_onda)
    ax.set(xlabel='Tiempo(s)', ylabel='Amplitud (dB)')
    plt.show()

def calcularDuracionDelSonido(in_onda, in_frecuenciaDeMuestreo):
    longitudDeLaOnda = len(in_onda);
    in_onda = in_onda / max(abs(in_onda));

    contadorDeCantidadDeDatos = 0; ##cuántos valores del eje Y importan.
  
    for dato in in_onda:
        if (abs(dato) >= 0.05): #Umbral de inicio de sonido.
            contadorDeCantidadDeDatos+=1
    return(contadorDeCantidadDeDatos/in_frecuenciaDeMuestreo);

def calcularFFT(in_onda, in_frecuenciaDeMuestreo):
    in_onda /= max(abs(in_onda))
    
    transformada = abs(numpy.fft.fft(in_onda))
    longitudTransformada = len(transformada)
    
    f_plot = in_onda[0:int(longitudTransformada/2+1)]
    x_mag_plot = 2 * transformada[0]/2
    
##    espectro = transformada[1:longitudTransformada/2]
##    vectorFrecuencias = in_frecuenciaDeMuestreo[1:longitudTransformada/2]/longitudTransformada
##
##    longitudAudio = len(in_onda)
##    duracionAudio =longitudAudio/in_frecuenciaDeMuestreo
##    periodoDeMuestreo=1/in_frecuenciaDeMuestreo;
    
    fig, ax = plt.subplots()
    ax.plot(f_plot,x_mag_plot)
    ax.set(xlabel='Tiempo(s)', ylabel='Amplitud (dB)')
    plt.show()
    #return numpy.abs(transformada)/len(valoresDeTiempo)

calcularFFT(onda, frecuenciaDeMuestreo)
#duracionDelSonido = calcularDuracionDelSonido(onda, frecuenciaDeMuestreo)
