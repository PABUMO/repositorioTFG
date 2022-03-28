import numpy

def calcularConstanciaDeLaFormaDelSonido(in_onda, in_frecuenciaDeMuestreo):

    print("---------Inicia calcularConstanciaDeLaFormaDelSonido ---------")
  
    longitudDeLaOnda = len(in_onda)

    in_onda /= max(abs(in_onda))
    
    limiteSuperior = max(in_onda)/2
    limiteInferior = min(in_onda)/2
      
    cantidadDeDatosEnElRango = 0
    for dato in in_onda:
        if (limiteInferior <= dato and limiteSuperior >= dato):
            cantidadDeDatosEnElRango += 1

    porcentajeDeValoresEnElRango = (cantidadDeDatosEnElRango/longitudDeLaOnda) * 100
    print("El límite superior es de ", limiteSuperior, ", el inferior de ", limiteInferior, " y el ", porcentajeDeValoresEnElRango, "% de los datos están en el rango")
    return porcentajeDeValoresEnElRango
