function [out_valorInicialDelRango, out_valorFinalDelRango] = calcularRangoPredominante(in_vectorFrecuencias, in_vectorEnergias)
  
  valorInicialDeIteracion = 0; %Con estos valores se iterará en el algoritmo.
  valorFinalDeIteracion = 50;
  promedioDeEnergiasDeIteracion = 0;
  
  valorInicialDeComparacion = 0; %Con estos valores se comparará y en caso de ser menores, se reemplazarán.
  valorFinalDeComparacion = 50;
  promedioDeEnergiasDeComparacion = 0;
  
  while(valorFinalDeIteracion < 4000) %La gráfica la estoy definiendo hasta los 4000 Hz.
    promedioDeEnergiasDeIteracion = calcularPromedioDeEnergiasEnUnRango(in_vectorFrecuencias, in_vectorEnergias, valorInicialDeIteracion, valorFinalDeIteracion);
    if (promedioDeEnergiasDeIteracion > promedioDeEnergiasDeComparacion) %Si el promedio es mayor que el anterior se reemplaza.
      promedioDeEnergiasDeComparacion = promedioDeEnergiasDeIteracion;
      valorInicialDeComparacion = valorInicialDeIteracion;
      valorFinalDeComparacion = valorFinalDeIteracion;
    endif
    valorInicialDeIteracion += 50;
    valorFinalDeIteracion += 50;
  endwhile
  out_valorInicialDelRango = valorInicialDeComparacion;
  out_valorFinalDelRango = valorFinalDeComparacion;
endfunction