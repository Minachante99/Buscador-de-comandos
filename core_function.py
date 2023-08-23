"""Funcion principal. Le pasa las elecciones anteriores para elegir carpeta y tema donde buscar, carga el Json y busca dentro de las claves del diccionario mediante una expresion regular o agrega datos"""

import json,os

def core_function(eleccion_1, eleccion_2, seleccion_0):  
	
	new_file,el_boleano = seleccion_0[0],seleccion_0[1]      
 
    #abriendo j_sones
	way = os.path.split(os.path.realpath(__file__))[0]
	way = way+os.sep+eleccion_1 + os.sep + new_file
	try:
		with open(way) as file:
		  subject = json.load(file)[0]
	except FileNotFoundError:
	       print("Chama no encuentro los J_sones.\n")
	       exit()
	       
	#mostrar todo si se usa " * "
	if eleccion_2 == "1" and el_boleano == True:
		for key in subject:
        		print("\n" + key,":", subject[key])
    
    #buscar algo
	elif eleccion_2 == "1" and el_boleano == False:
		searcher = input("Introduzca expresion: ")
		searcher = searcher.replace(" ", "")
		counts = 0
        #parseandolo
		for key in subject:
				if searcher in key:
					counts += 1
					print("\n" + key + " :" + subject[key])
		if counts == 0:
			print("\nNada chama, o lo escribiste mal o google con eso")
		else: 
			print("\nResultados encontrados: " + str(counts))
    
    #agregar datos
	elif eleccion_2 == "2" and el_boleano == False:
		agrega_key = input("Agrega clave: ")
		agrega_value = input ("Agrega descripcion: ")
		subject[agrega_key] = agrega_value 
		subject = [subject]
		#agregando lo nuevo
		with open(way, "w") as file_new:
			json.dump(subject, file_new)
		print("Hecho chama")

	else:
		print("\nChama aclarate, o agregas o ves algo")
		exit()
		
if __name__ == '__main__':
	core_function('Python','1',['Funciones.json',False])
	
	