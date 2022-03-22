function [out_vectorFrecuencias, out_vectorEnergias] = calcularFFT(in_onda, in_frecuenciaDeMuestreo)

  in_onda =  in_onda/max(abs(in_onda)); %Se normaliza la señal.

  transformada = abs(fft(in_onda)); %Se aplica la FFT. El absoluto es para obtener solamente la magnitud.
  longitudTransformada = length(transformada); %Longitud de la transformada.
  #vectorFrecuencias = in_frecuenciaDeMuestreo*(1:(longitudTransformada/2))/longitudTransformada; %Vector de frecuencias
  vectorFrecuencias = in_frecuenciaDeMuestreo*(linspace(1,longitudTransformada/2, longitudTransformada/2))/longitudTransformada;
  vectorEnergias = transformada(linspace(1,longitudTransformada/2, longitudTransformada/2)); %Evita la repetición de la transformada en el eje X.
  %espectro = espectro/max(abs(espectro)); %Se normaliza el espectro.

  vectorPrueba = zeros(longitudTransformada/2,1);
  
  for i = 1:(longitudTransformada/2)
    vectorPrueba(i) = transformada(i);
  endfor
  
  out_vectorFrecuencias = vectorFrecuencias;
  out_vectorEnergias = vectorPrueba;

endfunction  
