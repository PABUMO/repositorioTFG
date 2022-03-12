function [out_promedioDeEnergias] = calcularPromedioDeEnergiasEnUnRango(in_vectorFrecuencias, in_vectorEnergias, in_valorInicialDelRango, in_valorFinalDelRango)
  
  contadorInicialDeFrecuencias = 0; %Para saber cu�ntas frecuencias hay antes del primer valor medido.
  contadorDeFrecuencias = 0; %Cuenta la cantidad de frecuencias en un rango espec�fico.
  for frecuencia = in_vectorFrecuencias
    if (frecuencia >= in_valorInicialDelRango && frecuencia < in_valorFinalDelRango) %Si est� dentro del rango, incrementa contadorDeFrecuencias
      contadorDeFrecuencias = contadorDeFrecuencias + 1;
    elseif (frecuencia < in_valorInicialDelRango) %Si no est� dentro del rango, incrementa el contadorInicialDeFrecuencias
      contadorInicialDeFrecuencias = contadorInicialDeFrecuencias + 1;
    endif
  endfor

  sumaDeEnergiasDelSegmento = 0; %Acumulador de la cantidad de energ�as en el rango.
  contadorDeEnergias = 0; %Iterador para comparar con el de las frecuencias.
  contadorInicialDeEnergias = 0; %Para poder empezar a contar desde el punto correcto.
  for energiaActual = in_vectorEnergias
    if (contadorDeEnergias == contadorDeFrecuencias) %Si ya se evaluaron todos los puntos, se sale.
      break;
    else
      if (contadorInicialDeEnergias < contadorInicialDeFrecuencias) %Todav�a no se ha alcanzado el punto inicial de inter�s.
        contadorInicialDeEnergias = contadorInicialDeEnergias + 1;
      else
        sumaDeEnergiasDelSegmento = sumaDeEnergiasDelSegmento + energiaActual;
        contadorDeEnergias = contadorDeEnergias + 1;
      endif
    endif
  endfor
  out_promedioDeEnergias = (sumaDeEnergiasDelSegmento / contadorDeEnergias)*100;

endfunction