/* Vebot Brain:  Campana Admirable, Venezuela 1813 */
/* 1.Concepto constante y relaciones con un solo argumento */ 
objetivo('liberar a Venezuela de los Realistas').
comandante('Simon Bolivar').
comandante('Jose Felix Rivas').
comandante('Atanasio Girardot').
comandante('Domingo Monteverde').
comandante('Manuel Canas').
comandante('Jose Marti').
comandante('Francisco Oberto').
comandante('Julian Izquierdo').
/* 2. Relaciones binarias. fecha inicio y fin de la Campana Admirable*/ 
fecha_inicio('Cucuta', '6 de mayo 1813').
fecha_fin('Caracas', '6 de agosto 1813').
/* jefe  Comandante A de comandante B, */
jefe('Simon Bolivar','Atanasio Girardot').
jefe('Simon Bolivar','Jose Felix Rivas').
jefe('Domingo Monteverde','Manuel Canas').
jefe('Domingo Monteverde','Jose Marti').
jefe('Domingo Monteverde','Francisco Oberto').
jefe('Domingo Monteverde','Julian Izquierdo').
/* comandante lider del ejercito*/
lider('Simon Bolivar','Ejercito Patriota').
lider('Domingo Monteverde','Ejercito Realista').
 /* lugar, batalla */
lugar('Cucuta','Cucuta').
lugar('Barquisimeto','Horcones').
lugar('Bocono','Niquitao').
lugar('Trujillo','Agua de Obispo').
lugar('Trujillo','Decreto Guerra a Muerte').
lugar('Cojedes','Taguanes').
/* Rol de Simon Bolivar*/
titulo('Simon Bolivar', 'Libertador').
jefe_campana('Simon Bolivar', 'Campana Admirable').
/*conecta un sitio a con sitio b*/
conecta('Cucuta','San Cristobal').
conecta('San Cristobal','Merida').
conecta('Merida','Trujillo').
conecta('Trujillo','Bocono').
conecta('Bocono','Barquisimeto').
conecta('Barquisimeto','Cojedes').
conecta('Cojedes','Valencia').
conecta('Valencia','Caracas').
/* batalla y fecha */
batalla('Cucuta', '28 de febrero 1813').
batalla('Agua de Obispo', '18 de jumio 1813').
batalla('Niquitao', '2 de julio 1813').
batalla('Horcones', '22 de julio 1813').
batalla('Taguanes', '31 de julio 1813').
 /* Relaciones entre mas de dos. */
  /* Enfrenta comandante ganador a comandante perdedor en batalla */
enfrenta('Atanasio Girardot', 'Manuel Canas', 'Agua de Obispo').
enfrenta('Jose Felix Rivas', 'Jose Marti', 'Niquitao').
enfrenta('Jose Felix Rivas', 'Francisco Oberto', 'Horcones').
enfrenta('Simon Bolivar', 'Julian Izquierdo', 'Taguanes').
/* Causas de Campana Admirable y */
causa('Perdida de la Primera Republica').
 /* Amenazas de Monteverde de invasion  a Nueva Granada*/
amenaza('Domingo Monteverde','Invasion a Nueva Granada ').
/* Deseos de fuerzas patriotas de restaurar la independencia */
deseos('restaurar la independencia').
/* Consecuencias de Campana Admirable y */
consecuencia('Decreto Guerra a Muerte', '15 de junio 1813').
 /* ciudades liberadas*/
liberada('Merida').
liberada('Barinas').
liberada('Trujillo').
/* Perdida del ejercito realista de 6000 efectivos*/
perdida('ejercito realista', 6000).

/* 3. Consultas atómicas */
/* jefe('Simon Bolivar','Jose Felix Rivas')*/
/*jefe('Domingo Monteverde','Atanasio Girardot'). */
/*comandante('Simon Bolivar'). */
 /*Comandante('Manuel Canas'). */
/* liberada('Barinas').*/
/*liberada('Cucuta').*/
/* 4. Consultas atomicas con variables. Cual es la fecha de ocurrencia de la Batalla de Taguanes*/
batalla('Taguanes', X).
/* Donde ocurre la batalla de Niquitao*/
lugar(X,'Niquitao').
/* 5. Consultas Conjuntivas. */
/* Lider del Ejercito Patriota y Jefe de la Campana Admirable */
jefe_campana(X, 'Campana Admirable'),lider(X,'Ejercito Patriota').
 /* Donde se firmo el Decreto de Guerra a Muerte? */
consecuencia('Decreto Guerra a Muerte', '15 de junio 1813'),lugar(X,'Decreto Guerra a Muerte').
/* Rutas a sitio de ocurrencia de la Batalla de Niquitao */
lugar(X,'Niquitao'), ruta(X,Y).
/* Rutas a sitio de ocurrencia de la Batalla de Horcones */
lugar(X,'Horcones'), ruta(X,Y).
/* Rutas a sitio de ocurrencia de la Batalla de Agua de Obispos */
lugar(X,'Agua de Obispo'), ruta(X,Y).
/* Rutas a sitio de ocurrencia de la Batalla de Taguanes */
lugar(X,'Taguanes'), ruta(X,Y).
 /* */

/* 6. Reglas. */
/* Forman parte del ejercito patriota: si son comandantes y su jefe es Simon Bolivar */
efectivo_patriota(X):- comandante(X),jefe('Simon Bolivar',X).
 /* forman parte del ejercito realista: si son comandante y su jefe es Domingo Monteverde*/
efectivo_realista(X):- comandante(X),jefe('Domingo Monteverde',X).
/* Comandante ganadores de Batallas).*/
ganador(X):- enfrenta(X,Y,Z).
perdedor(Y):- enfrenta(X,Y,Z).
 /* Causas de la Campana Admirable*/                                                            
  causa_campana(X,Y,W,Z):- causa(X), amenaza(Y,W), deseos(Z).                                                            
/*  Conexion entre sitios. Recursion  */ 
ruta(X,Y) :- conecta(X,Y).
ruta(X,Z) :- conecta(X,Y), ruta(Y,Z).

# 
 


  