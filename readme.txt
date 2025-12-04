Cambios a Version 1.5:

.Creada carpeta Modulo y Tools, para agrupar tanto los modulos y las herraminetas
como el updater y los conversores.
.Eliminado la separacion de procesos en threads debido a su poco uso.
.Agregada funcion que agiliza las selecciones.
.Agregado un nuevo menu al inicio donde se decida utilizar alguna de las herramientas como
si levantar el gui del buscador de comandos, actualizar los modulos(mediante fetcheo web, 
mas adelante version github desde window), abrir el conversor o directamente la version de consola del bdc.
.Se elimino el script de las funciones por aparte y se integro al main.
.La core_function ahora solo fetchea los resultados o agrega contenido, se elimino que maneje inputs del usuario.
.Agregada funcionalidad del testeo, que devuelve 10 claves aleatorias sobre el tema escogido.
.Agregada funcionalidad de sugerencias a la hora de buscar, donde se muestran resultados 
encontrados en los valores tambien y se mejoro la calidad a la hora de buscar.
.Modulo 'DF and S methods(DataAnalysis expansion)' paso a llmarse 'DA_expansion'.