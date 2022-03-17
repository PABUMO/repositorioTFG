import numpy
import pandas as pd
import matplotlib.pyplot as plt
import librosa as lr
from glob import glob
import soundfile

onda, frecuenciaDeMuestreo = soundfile.read('../Sonidos/Pito de padre 1.wav')

def graficarOndas(in_onda, in_frecuenciaDeMuestreo):
    valoresDeTiempo = numpy.arange(0, len(onda))/frecuenciaDeMuestreo
    fig, ax = plt.subplots()
    ax.plot(valoresDeTiempo,onda)
    ax.set(xlabel='Tiempo(s)', ylabel='Amplitud (dB)')
    plt.show()

def calcularDuracionDelSonido(in_onda, in_frecuenciaDeMuestreo):
    longitudDeLaOnda = len(in_onda);
    in_onda = in_onda / max(abs(in_onda));

    contadorDeCantidadDeDatos = 0; ##cuántos valores del eje Y importan.
  
    for dato = transpose(amplitudesDeLaOnda)
        if (abs(dato) >= 0.05) %Umbral de inicio de sonido.
        contadorDeCantidadDeDatos++;
        
    out_duracionDelSonido = contadorDeCantidadDeDatos/in_frecuenciaDeMuestreo;

graficarOndas(onda, frecuenciaDeMuestreo)
