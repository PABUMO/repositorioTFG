function [out_duracionDelSonido] = calcularDuracionDelSonido(in_sonidoAIdentificar)
  [onda,frecuenciaDeMuestreo] = audioread(in_sonidoAIdentificar);
  
  longitudDeLaOnda = length(onda);
  amplitudesDeLaOnda = onda(1:longitudDeLaOnda); %Valores Y de la gráfica.
  amplitudesDeLaOnda = amplitudesDeLaOnda / max(abs(amplitudesDeLaOnda)); %Se normaliza para estandarizar el umbral.
  
  contadorDeCantidadDeDatos = 0; %Cuántos valores del eje Y importan.
  %for dato = transpose(amplitudesDeLaOnda)
  for dato = transpose(amplitudesDeLaOnda)
    if (abs(dato) >= 0.05) %Umbral de inicio de sonido.
      contadorDeCantidadDeDatos++;
    endif
  endfor
  out_duracionDelSonido = contadorDeCantidadDeDatos/frecuenciaDeMuestreo;

endfunction