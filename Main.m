clear ; close all; clc;

sonidoAIdentificar = "Sonidos/Peatonal.ogg";

duracionDelSonido = calcularDuracionDelSonido(sonidoAIdentificar);

if(duracionDelSonido >= 1) %Evaluación de la duración del sonido.

  [vectorFrecuencias, vectorEnergias] = calcularFFT(sonidoAIdentificar);
  vectorEnergias = transpose(vectorEnergias); %Convertirla en un vector fila.
  %Se calcula el rango de frecuencias con las energías más altas.
  [valorInicialDelRangoPredominante, valorFinalDelRangoPredominante] = calcularRangoPredominante(vectorFrecuencias, vectorEnergias);
  valorInicialDelRangoPredominante
  valorFinalDelRangoPredominante

  if(valorInicialDelRangoPredominante >= 2900 && valorFinalDelRangoPredominante <= 3150) %Evaluación de la frecuencia del sonido.
  
##    constanciaDeLaFormaDelSonido = calcularConstanciaDeLaFormaDelSonido(sonidoAIdentificar);
##    if (constanciaDeLaFormaDelSonido >= 0.6)
      disp("El sonido es una bocina");
##    else
##      disp("El sonido no es una bocina");
##    endif
  else
    disp("El sonido no es una bocina");
  endif
else
  disp("El sonido no es una bocina");
endif


















graficarOndas(sonidoAIdentificar, 0); %0, sin acotar los ejes; 1, acotados.