import numpy
import matplotlib.pyplot as plt

def calcularRangoPredominante(vectorFrecuencias, vectorEnergias):
    print("---------Inicial calcularRangoPredominante---------")

def calcularFFT(in_onda, in_frecuenciaDeMuestreo):
    print("---------Inicial calcularFFT---------")

    in_onda /= max(abs(in_onda))

    transformada = abs(numpy.fft.fft(in_onda))

    vectorEnergias = transformada.tolist()

    contador = 0

    while(contador != len(transformada)/2):
        vectorEnergias.pop()
        contador += 1

    longitudTransformada = len(transformada)

    vectorFrecuencias = in_frecuenciaDeMuestreo*(numpy.linspace(1,longitudTransformada/2, int(longitudTransformada/2)))/longitudTransformada
    fig, ax = plt.subplots()
    ax.set(xlim=(0, 4000), ylim=(0, 10000))
    ax.plot(vectorFrecuencias,vectorEnergias)
    ax.set(xlabel='Tiempo(s)', ylabel='Amplitud (dB)')
    plt.show()
