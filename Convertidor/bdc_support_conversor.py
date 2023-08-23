'''Programa frontend que importa la clase conversor, añadiendo la direccion de PyTools al path de python, y tomando los dos inputs basicos'''

import sys,os

def welcome():
		print('''
	
Welcome mi pana. A que vas a convertir:
	
1- Txt a Json
2- Fixear los jsones
	
	''')

def run():
	
	#presentacion
	welcome()
	
	#primera eleccion, decide con cual clase inicializar 
	while 1:
		type = input('Choose: ')
		#crea la instancia en la respectiva clase
		if type in ['1','2']:
			if type == '1':  
				conversor = files_parser_class.Txt(os.path.realpath(__file__))
			elif type == '2':
				conversor = files_parser_class.Json_Fixer(os.path.realpath(__file__))
			break
		else : print('Vamo a aclararnos.\n')
	
	#direccion del archivo o carpeta
	files_path = input('\nTirame direccion: ')
	
	#funcion principal
	conversor.main(files_path)
	print('\nDone\n')
	
	#opcional, para mostrar los resultados, de estar en la lista interna de la clase significa que se proceso correctamente
	print('Results:')
	for x in conversor.results:
		print(x)
		
		
if __name__ == '__main__':
	sys.path.append('/storage/emulated/0/APLP!!!!/Estudiar!!/PyTools')
	import files_parser_class
	run()
	
	