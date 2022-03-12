function [] = graficarOndas(in_sonidoAIdentificar)
  [s1,fp1] = audioread(in_sonidoAIdentificar); %Importación y lectura de los archivos.
  
  t_length1 = length(s1); %Cálculo de la longitud de cada uno.

  t1 = linspace(0, t_length1/fp1, length(s1));

  %Gráfica del archivo.
  plot(t1, s1(1:t_length1), 'r');
  %axis([1.55 1.57 -1 1]); Por si se quiere acotar el eje X.
  title(in_sonidoAIdentificar);
  xlabel("Tiempo (s)");
  ylabel("Intensdad");
  grid on;

endfunction