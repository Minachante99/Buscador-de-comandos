'''Programa frontend que importa la clase files_parser, añadiendo la direccion de PyTools al path de python y le pasa funciones.'''

import sys,os,conversores

def welcome():
		print('''
	
Welcome mi pana. A que vas a convertir:
	
1- Txt a Json
2- Fixear los jsones
3- Json a Txt
	
	''')

def run():
	
	#presentacion
	welcome()
	
	#primera eleccion, decide con cual clase inicializar 
	while 1:
		opt = input('Choose: ')
		#crea la instancia en la respectiva clase
		if opt in ['1','2','3']:
			if opt == '1':  
				conversor = files_parser_class.FilesParser(os.path.realpath(__file__))
				func,type = conversores.txt_parser,'txt'
			elif opt == '2':
				conversor = files_parser_class.FilesParser(os.path.realpath(__file__))
				func,type = conversores.json_parser,'json'
			elif opt=='3':
				conversor=files_parser_class.FilesParser(os.path.realpath(__file__))
				func,type=conversores.json_txt,'json'
			break
		else : print('Vamo a aclararnos.\n')
	
	#direccion del archivo o carpeta
	files_path = input('\nTirame direccion: ')
	
	#funcion principal
	conversor.main(func,files_path,type)
	print('\nDone\n')
	
	#opcional, para mostrar los resultados, de estar en la lista interna de la clase significa que se proceso correctamente
	conversor.show_results()
		
		
if __name__ == '__main__':
	sys.path.append('D:\\Programacion\\Proyectos\\Tools')
	import files_parser_class
	run()
	
	