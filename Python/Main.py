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
    ax.set(xlabel='Time(s)', ylabel='Sound Amplitud')
    plt.show()

graficarOndas(onda, frecuenciaDeMuestreo)
