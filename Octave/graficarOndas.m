function [] = graficarOndas(in_onda, in_frecuenciaDeMuestreo, in_tipoDeVisualizacion)
  %El par�metro in_tipoDeVisualizacion determina si se quiere ver la onda m�s de cerca o de lejos.
  
  longitudDeLaOnda = length(in_onda); %C�lculo de la longitud de cada uno.

  unidadesDeTiempo = linspace(0, longitudDeLaOnda/in_frecuenciaDeMuestreo, longitudDeLaOnda);
  
  %Gr�fica del archivo.
  plot(unidadesDeTiempo, in_onda, 'r');
  if in_tipoDeVisualizacion == 1
    axis([1.55 1.57 -1 1]); %Por si se quiere acotar el eje X.
  endif
  xlabel("Tiempo (s)");
  ylabel("Intensdad");
  grid on;

endfunction