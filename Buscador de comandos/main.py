""""Un buscador de comandos dentro de mis apuntes. Llama las elecciones y le pasa los resultados a la core_function."""

import firsts_choices,_thread as thread,queue
import core_function as cf

dipocket = queue.Queue()

def subjects(carpeta):
	import os
	way = os.path.split(os.path.realpath(__file__))[0]
	dipocket.put(os.listdir(way+os.sep+carpeta))
	
def run():
    while 1:
    	#primeras elecciones
    	eleccion_1 = firsts_choices.choice_1()
    	#lanza un thread para que escanee la carpeta de fondo
    	thread.start_new_thread(subjects,(eleccion_1,))
    	eleccion_2 = firsts_choices.choice_2()
    	#lee el dipocket y le pasa el resultado a la proxima eleccion
    	while 1:
    		try:
    			lista = dipocket.get(block=False)
    		except queue.Empty:
    			import time
    			time.sleep(0.25)
    		else: break
    	eleccion_3 = firsts_choices.choice_3(lista)
    	#funcion de parseo
    	cf.core_function(eleccion_1, eleccion_2, eleccion_3)
    	#empezar de nuevo o no
    	x = input('\nDo you wanna start again?(Y or N): ') 
    	if x in ['y','Y'] : pass
    	else: break      

if __name__ == "__main__":
	run()
 