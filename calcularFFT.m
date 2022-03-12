function [out_vectorResultante, out_espectroResultante] = calcularFFT(in_archivo)
  
  [sonido,frecuenciaMuestreo] = audioread(in_archivo); %Se carga la señal en la variable "sonido" y la frecuencia de muestreo en frecuenciaMuestreo.

  sonido =  sonido/max(abs(sonido)); %Se normaliza la señal.

  transformada = abs(fft(sonido)); %Se aplica la FFT. El absoluto es para obtener solamente la magnitud.
  longitudTransformada = length(transformada); %Longitud de la transformada.
  espectro = transformada(1:longitudTransformada/2); %Evita la repetición de la transformada en el eje X.
  %espectro = espectro/max(abs(espectro)); %Se normaliza el espectro.
  vectorFrecuencias = frecuenciaMuestreo*(1:(longitudTransformada/2))/longitudTransformada; %Vector de frecuencias

  longitudAudio = length(sonido); %Longitud del audio.
  duracionAudio =longitudAudio/frecuenciaMuestreo; %Tiempo total que dura el audio.
  periodoDeMuestreo=1/frecuenciaMuestreo; %Periodo de muestreo.
  tiempo = [0:periodoDeMuestreo:(duracionAudio-periodoDeMuestreo)]; %Vector de tiempo.

  out_vectorResultante = vectorFrecuencias;
  out_espectroResultante = espectro;

endfunction  
