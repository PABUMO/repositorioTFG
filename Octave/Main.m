clear ; close all; clc;

sonidoAIdentificar = "../Sonidos/Pito de madre 1.ogg";
[onda,frecuenciaDeMuestreo] = audioread(sonidoAIdentificar);

##graficarOndas(onda, frecuenciaDeMuestreo, 0);
##
##duracionDelSonido = calcularDuracionDelSonido(onda, frecuenciaDeMuestreo)
##
##if(duracionDelSonido >= 1) %Evaluación de la duración del sonido.
##  disp("El sonido dura más de 1 segundo");
  [vectorFrecuencias, vectorEnergias] = calcularFFT(onda, frecuenciaDeMuestreo);
##  vectorEnergias = transpose(vectorEnergias); %Convertirla en un vector fila.
##  %Se calcula el rango de frecuencias con las energías más altas.
##  [valorInicialDelRangoPredominante, valorFinalDelRangoPredominante] = calcularRangoPredominante(vectorFrecuencias, vectorEnergias);
##
##  if(valorInicialDelRangoPredominante >= 2900 && valorFinalDelRangoPredominante <= 3150) %Evaluación de la frecuencia del sonido.
##  disp("La frecuencia fundamental de la onda se encuentra dentro del rango de las bocinas");
##    valorInicialDelRangoPredominante
##    valorFinalDelRangoPredominante
####    constanciaDeLaFormaDelSonido = calcularConstanciaDeLaFormaDelSonido(onda, frecuenciaDeMuestreo);
####    if (constanciaDeLaFormaDelSonido >= 0.6)
##      disp("El sonido es una bocina");
####    else
####      disp("El sonido no es una bocina");
####    endif
##  else
##    disp("El sonido no es una bocina");
##  endif
##else
##  disp("El sonido no es una bocina");
##endif
plot(vectorFrecuencias, vectorEnergias);
axis([0 4000]);
#calcularConstanciaDeLaFormaDelSonido(onda, frecuenciaDeMuestreo);
#calcularDuracionDelSonido(onda, frecuenciaDeMuestreo)