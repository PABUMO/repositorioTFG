function [out_vectorResultante, out_espectroResultante] = calcularFFT(in_onda, in_frecuenciaDeMuestreo)

  in_onda =  in_onda/max(abs(in_onda)); %Se normaliza la señal.

  transformada = abs(fft(in_onda)); %Se aplica la FFT. El absoluto es para obtener solamente la magnitud.
  longitudTransformada = length(transformada); %Longitud de la transformada.
  espectro = transformada(1:longitudTransformada/2); %Evita la repetición de la transformada en el eje X.
  %espectro = espectro/max(abs(espectro)); %Se normaliza el espectro.
  vectorFrecuencias = in_frecuenciaDeMuestreo*(1:(longitudTransformada/2))/longitudTransformada; %Vector de frecuencias

  longitudAudio = length(in_onda); %Longitud del audio.
  duracionAudio =longitudAudio/in_frecuenciaDeMuestreo; %Tiempo total que dura el audio.
  periodoDeMuestreo=1/in_frecuenciaDeMuestreo; %Periodo de muestreo.
  %tiempo = [0:periodoDeMuestreo:(duracionAudio-periodoDeMuestreo)]; %Vector de tiempo.

  out_vectorResultante = vectorFrecuencias;
  out_espectroResultante = espectro;

endfunction  
