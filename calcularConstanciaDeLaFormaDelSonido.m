function [out_valorDeConstanciaDeLaFormaDelSonido] = calcularConstanciaDeLaFormaDelSonido(in_onda, in_frecuenciaDeMuestreo)
  
  longitudDeLaOnda = length(in_onda)
  
  unidadesDeTiempo = linspace(0, longitudDeLaOnda/in_frecuenciaDeMuestreo, longitudDeLaOnda);
  unidadesDeAmplitud = in_onda(1:longitudDeLaOnda);

  valorPromedio = sum(unidadesDeAmplitud)/longitudDeLaOnda
  umbral = valorPromedio*0.5
  limiteSuperior = valorPromedio + umbral
  limiteInferior = valorPromedio - umbral
  
  cantidadDeDatosEnElRango = 0;
  for dato = unidadesDeAmplitud
    if (limiteInferior <= dato && limiteSuperior >= dato)
      cantidadDeDatosEnElRango++;
    endif
  endfor
  cantidadDeDatosEnElRango
  (cantidadDeDatosEnElRango/longitudDeLaOnda) * 100
endfunction