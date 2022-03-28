import numpy
import matplotlib.pyplot as plt

def calcularPromedioDeEnergiasEnUnRango(in_vectorFrecuencias, in_vectorEnergias, in_valorInicialDelRango, in_valorFinalDelRango):

    contadorInicialDeFrecuencias = 0 #Para saber cuántas frecuencias hay antes del primer valor medido.
    contadorDeFrecuencias = 0 #Cuenta la cantidad de frecuencias en un rango específico.
    for frecuencia in in_vectorFrecuencias: #El método identifica la cantidad de frecuencias presentes en un rango específico.
        if (frecuencia >= in_valorInicialDelRango and frecuencia < in_valorFinalDelRango): #Si la frecuencia está dentro del rango, se incrementa el contadorDeFrecuencias
            contadorDeFrecuencias += 1
        elif (frecuencia < in_valorInicialDelRango): #Si la frecuencia está antes del rango, incrementa el contadorInicialDeFrecuencias para saber cuántas hay antes.
            contadorInicialDeFrecuencias += 1

    sumaDeEnergiasDelSegmento = 0 #Acumulador de la cantidad de energías en el rango.
    contadorDeEnergias = 0 #Iterador para comparar con el de las frecuencias.
    contadorInicialDeEnergias = 0 #Para poder empezar a contar desde el punto correcto.
    for energiaActual in in_vectorEnergias:
        if (contadorDeEnergias == contadorDeFrecuencias): #Si ya se evaluaron todos los puntos, se sale.
            break
        else:
            if (contadorInicialDeEnergias < contadorInicialDeFrecuencias): #Todavía no se ha alcanzado el punto inicial de interés.
                contadorInicialDeEnergias += 1
            else:
                sumaDeEnergiasDelSegmento += energiaActual
                contadorDeEnergias += 1

    out_promedioDeEnergias = (sumaDeEnergiasDelSegmento / contadorDeEnergias)*100
    return out_promedioDeEnergias

def calcularFFT(in_onda, in_frecuenciaDeMuestreo):
    
    print("//////// Inicia calcularFFT ////////")

    in_onda /= max(abs(in_onda))

    transformada = abs(numpy.fft.fft(in_onda)) #Cálculo de la FFT.

    vectorEnergias = transformada.tolist()

    contador = 0

    while(contador != len(transformada)/2): #Se divide a la mitad la FFT para evitar la repetición del espectro.
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

    valorInicialDeReferencia = 0 #Con estos valores se iterará en el algoritmo.
    valorFinalDeReferencia = 50
    promedioDeEnergiasDeReferencia = 0
      
    valorInicialDeComparacion = 0 #Con estos valores se comparará y en caso de ser menores, se reemplazarán.
    valorFinalDeComparacion = 50
    promedioDeEnergiasDeComparacion = 0

    print("//////// Inicia calcularPromedioDeEnergiasEnUnRango ////////")
    
    while(valorFinalDeReferencia < 4000): #La gráfica la estoy definiendo hasta los 4000 Hz.
        promedioDeEnergiasDeReferencia = calcularPromedioDeEnergiasEnUnRango(vectorFrecuencias, vectorEnergias, valorInicialDeReferencia, valorFinalDeReferencia)
        if (promedioDeEnergiasDeReferencia > promedioDeEnergiasDeComparacion): #Si el promedio es mayor que el anterior se reemplaza.
            promedioDeEnergiasDeComparacion = promedioDeEnergiasDeReferencia
            valorInicialDeComparacion = valorInicialDeReferencia
            valorFinalDeComparacion = valorFinalDeReferencia
        valorInicialDeReferencia += 50
        valorFinalDeReferencia += 50

    out_listaResultante = [valorInicialDeComparacion, valorFinalDeComparacion]

    return out_listaResultante
