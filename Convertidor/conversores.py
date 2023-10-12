import os,json

#txt function
def txt_parser(files_path,res_path):
	'''Func que acepta txts de la forma estandar en la que guardo notas, los parsea y crea un diccionario guardandolo en un json'''
	
	#crea un archivo, separa las notas pescando las lineas en blanco como separador, guarda en un diccionario y dumpea a un json, y finalmente agregando cada resultado a la lista que puede, a gusto, ser printeada 
	dictio = {}
	with open(files_path) as new_files:
		new_files = new_files.read()
		lista = new_files.split('\n\n')
	for x in lista:
		marca = x.find('-')
		clave = x[:(marca - 1)]
		valor = x[marca + 2:]
		dictio[clave] = valor
	name = os.path.split(files_path)[1]
	name = name[:name.find('.')+1] + 'json'
	with open(res_path + os.sep + name,'w') as result:
		json.dump([dictio],result)
	return name
		
#json fixer
def json_parser(files_path,res_path):
		'''Func para parsear los viejos jsones que contenian muchos dictionarios con una sola clave para unirlos todos en un solo dict y guardarlo en un json'''
		
		#carga el json, le pasa un loop a la lista guardando el contenido(dicts)dentro de un diccionario, guardandolo en un json y añadiendo los resultados a una lista	
		dictio = {}
		with open(files_path) as new_file:
			paciente = json.load(new_file)
		for dic in paciente:
			for clave in dic:
				dictio[clave] = dic[clave]
		name = os.path.split(files_path)[1]
		with open(res_path + os.sep + name, 'w') as result:
			json.dump([dictio], result)
		return name