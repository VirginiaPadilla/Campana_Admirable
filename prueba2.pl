

:-use_module(library(janus)).
 
initialize


% Ejemplo 1: Ejecutar código Python simple     ejecutar_p :-    py_call(print('Hola desde Python')).

 

% Ejemplo 3: Ejecutar script

campana :-  py_call('Ruta_campana').

batalla :- py_call('Sitio_Batallas').

