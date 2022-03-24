import numpy
import matplotlib.pyplot as plt

def calcularPromedioDeEnergiasEnUnRango(in_vectorFrecuencias, in_vectorEnergias, in_valorInicialDelRango, in_valorFinalDelRango):

    print("---------Inicia calcularPromedioDeEnergiasEnUnRango---------")

    contadorInicialDeFrecuencias = 0 #Para saber cuántas frecuencias hay antes del primer valor medido.
    contadorDeFrecuencias = 0 #Cuenta la cantidad de frecuencias en un rango específico.
    for frecuencia in in_vectorFrecuencias: #El método identifica la cantidad de frecuencias presentes en un rango específico.
        if (frecuencia >= in_valorInicialDelRango && frecuencia < in_valorFinalDelRango): #Si la frecuencia está dentro del rango, se incrementa el contadorDeFrecuencias
            contadorDeFrecuencias += 1
        elif (frecuencia < in_valorInicialDelRango) #Si la frecuencia está antes del rango, incrementa el contadorInicialDeFrecuencias para saber cuántas hay antes.
            contadorInicialDeFrecuencias += 1

    sumaDeEnergiasDelSegmento = 0 #Acumulador de la cantidad de energías en el rango.
    contadorDeEnergias = 0 #Iterador para comparar con el de las frecuencias.
    contadorInicialDeEnergias = 0 #Para poder empezar a contar desde el punto correcto.
    for energiaActual in in_vectorEnergias:
        if (contadorDeEnergias == contadorDeFrecuencias) #Si ya se evaluaron todos los puntos, se sale.
            break
        else:
            if (contadorInicialDeEnergias < contadorInicialDeFrecuencias): #Todavía no se ha alcanzado el punto inicial de interés.
                contadorInicialDeEnergias += 1
            else:
                sumaDeEnergiasDelSegmento += energiaActual
                contadorDeEnergias += 1

  out_promedioDeEnergias = (sumaDeEnergiasDelSegmento / contadorDeEnergias)*100   

def calcularFFT(in_onda, in_frecuenciaDeMuestreo):
    
    print("---------Inicia calcularFFT---------")

    in_onda /= max(abs(in_onda))

    transformada = abs(numpy.fft.fft(in_onda))

    vectorEnergias = transformada.tolist()

    contador = 0

    while(contador != len(transformada)/2):
        vectorEnergias.pop()
        contador += 1

    longitudTransformada = len(transformada)

    vectorFrecuencias = in_frecuenciaDeMuestreo*(numpy.linspace(1,longitudTransformada/2, int(longitudTransformada/2)))/longitudTransformada

    out_listaResultante = [vectorFrecuencias, vectorEnergias]

    return out_listaResultante

def calcularRangoPredominante(in_onda, in_frecuenciaDeMuestreo):
    
    print("---------Inicia calcularRangoPredominante---------")

    listaResultante = calcularFFT(in_onda, in_frecuenciaDeMuestreo)

    vectorFrecuencias = listaResultante[0]

    vectorEnergias = listaResultante[1]

    valorInicialDeIteracion = 0 #Con estos valores se iterará en el algoritmo.
    valorFinalDeIteracion = 50
    promedioDeEnergiasDeIteracion = 0
      
    valorInicialDeComparacion = 0 #Con estos valores se comparará y en caso de ser menores, se reemplazarán.
    valorFinalDeComparacion = 50;
    promedioDeEnergiasDeComparacion = 0;
      
    while(valorFinalDeIteracion < 4000) #La gráfica la estoy definiendo hasta los 4000 Hz.
        promedioDeEnergiasDeIteracion = calcularPromedioDeEnergiasEnUnRango(vectorFrecuencias, vectorEnergias, valorInicialDeIteracion, valorFinalDeIteracion);
        if (promedioDeEnergiasDeIteracion > promedioDeEnergiasDeComparacion) #Si el promedio es mayor que el anterior se reemplaza.
            promedioDeEnergiasDeComparacion = promedioDeEnergiasDeIteracion;
            valorInicialDeComparacion = valorInicialDeIteracion;
            valorFinalDeComparacion = valorFinalDeIteracion;
        valorInicialDeIteracion += 50;
        valorFinalDeIteracion += 50;

    out_listaResultante = [valorInicialDeComparacion, valorFinalDeComparacion]

##    fig, ax = plt.subplots()
##    ax.set(xlim=(0, 4000), ylim=(0, 10000))
##    ax.plot(out_listaResultante[0],out_listaResultante[1])
##    ax.set(xlabel='Tiempo(s)', ylabel='Amplitud (dB)')
##    plt.show()

    #return out_listaResultante
