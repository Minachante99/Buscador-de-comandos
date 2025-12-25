"""Script que contiene la core_function, la cual es usada por el main o el gui."""

import json,random

def core_function(accion,full_path,**kargs):      
	"""Funcion principal. Le pasa las elecciones anteriores para elegir carpeta y tema donde buscar, 
carga el Json y busca dentro de las claves del diccionario o agrega datos"""
    #abriendo j_sones
	try:
		with open(full_path) as file:
			subject = json.load(file)[0] #subject es un diccionario
	except FileNotFoundError:
		print("Chama no encuentro los J_sones.\n")
		exit()

	#agregar datos
	if accion == 'Agregar':
		#kargs
		agg_key,agg_value = kargs['clave'].strip(),kargs['valor'].strip()
		subject[agg_key] = agg_value
		#agregando lo nuevo
		with open(full_path, "w") as file_new:
			json.dump([subject], file_new,indent=2)
	
	#testeo
	elif accion == 'Testear':
		randoms_keys,all_keys = [], list(subject.keys())
		#si tiene 10 o menos claves lo devuelve directamente
		if len(all_keys)<=10:
			return all_keys
		#else itera pickeando random
		while len(randoms_keys)!=10:
			key = random.choice(all_keys)
			if key not in randoms_keys:
				randoms_keys.append(key)
		return randoms_keys,subject

	#la buscacion
	else:
		word = kargs['word'].replace(' ','').lower()
		main_results,suggestions= {},{}
        #parseandolo
		for key,value in subject.items():
			if word in key.lower():
				main_results[key] = value
			elif word in value.lower():
				suggestions[key]=value
		return main_results,suggestions

	
	