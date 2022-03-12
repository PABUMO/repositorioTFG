clear ; close all; clc;

sonidoAIdentificar = "Sonidos/400 Hz.ogg";

%%%%%%%%%%%%%%%% Cálculo de la duración %%%%%%%%%%%%%%%%

duracionDelSonido = calcularDuracionDelSonido(sonidoAIdentificar)

##if(duracionDelSonido < 1)
##  disp("El sonido no es una bocina");
##else
##  [vectorFrecuencias, vectorEnergias] = calcularFFT(sonidoAIdentificar);
##  vectorEnergias = transpose(vectorEnergias); %Convertirla en un vector fila.
##  Se calcula el rango de frecuencias con las energías más altas.
##  [valorInicialDelRangoPredominante, valorFinalDelRangoPredominante, promedioDeEnergiaDelRangoPredominante] = calcularRangoPredominante(vectorFrecuencias, vectorEnergias);
##  if(valorInicialDelRangoPredominante >= 2900 && valorFinalDelRangoPredominante <= 3100)
##    disp("El sonido es una bocina");
##  else
##    disp("El sonido no es una bocina");
##    endif
##endif

%%%%%%%%%%%%%%%% Cálculo de Fourier %%%%%%%%%%%%%%%%
%[vectorFrecuencias, vectorEnergias] = calcularFFT(sonidoAIdentificar); %Se calcula la FFT.

%Se grafica la FFT.
##plot(vectorFrecuencias, vectorEnergias);
##axis([0,4000]);
##title("Frecuencias del sonido de la bocina del Suzuki Baleno");
##xlabel("Frecuencia (Hz)");
##ylabel("Cantidad de energía");
##grid on;

%vectorEnergias = transpose(vectorEnergias); %Convertirla en un vector fila.

%Se calcula el rango de frecuencias con las energías más altas.
%[valorInicialDelRangoPredominante, valorFinalDelRangoPredominante, promedioDeEnergiaDelRangoPredominante] = calcularRangoPredominante(vectorFrecuencias, vectorEnergias);
##disp("El rango con las frecuencias más elevadas está entre:");
##valorInicialDelRangoPredominante
##valorFinalDelRangoPredominante
##disp("El promedio de las energías en dicho rango es de:");
##promedioDeEnergiaDelRangoPredominante