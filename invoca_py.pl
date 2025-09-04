
:- use_module(library(py_shell)).

:- py_add_lib_dir('c:\users\virgi\onedrive\documents\prolog\').
:- py_import(mi_script).

saludar_desde_python(Nombre, Saludo):- py_call(mi_script(Nombre), Saludo).

ejemplo :- saludar_desde_python('Virgi', 'Hiii'), 
Write(Saludo),
sumar_numeros(8,12, Suma),
format('La suma es -w-n', [Suma]).

:-py_import(Ruta_campana).
xx :-py_call(Ruta_campana).
