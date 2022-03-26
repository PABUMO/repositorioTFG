import soundfile
import matplotlib.pyplot as plt
from CalculosDeFFT import *

def graficarOndas(in_onda, in_frecuenciaDeMuestreo):
    
    print("---------Inicial graficarOndas---------")
    
    valoresDeTiempo = numpy.arange(0, len(in_onda))/frecuenciaDeMuestreo
    fig, ax = plt.subplots()
    ax.plot(valoresDeTiempo,in_onda)
    ax.set(xlabel='Tiempo(s)', ylabel='Amplitud (dB)')
    plt.show()

def calcularDuracionDelSonido(in_onda, in_frecuenciaDeMuestreo):
    
    print("---------Inicial el calcularDuracionDelSonido---------")
    
    longitudDeLaOnda = len(in_onda);
    in_onda = in_onda / max(abs(in_onda));

    contadorDeCantidadDeDatos = 0; ##cuántos valores del eje Y importan.
  
    for dato in in_onda:
        if (abs(dato) >= 0.05): #Umbral de inicio de sonido.
            contadorDeCantidadDeDatos+=1
    return(contadorDeCantidadDeDatos/in_frecuenciaDeMuestreo);
    
    #return abs(transformada)/len(valoresDeTiempo)

print("---------Inicial el Main---------")
onda, frecuenciaDeMuestreo = soundfile.read('../Sonidos/Pito de padre 1.ogg')

#duracionDelSonido = calcularDuracionDelSonido(onda, frecuenciaDeMuestreo)
listaResultante = calcularRangoPredominante(onda, frecuenciaDeMuestreo)
print("El rango predominante empieza en " + str(listaResultante[0]) + " y termina en " + str(listaResultante[1]))
#porcentajeDeConstanciaDeLaFormaDelSonido = calcularConstanciaDeLaFormaDelSonido(onda, frecuenciaDeMuestreo)
