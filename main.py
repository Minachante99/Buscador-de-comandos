""""Un buscador de comandos dentro de mis apuntes. Segun las elecciones busca,testea,agrega contenido,actualiza o convierte nuevos json 
la core_function."""
#  hello

from core_function import core_function as cf
import os


def seleccionador(opciones,isFolder=0):
	"""Funcion que agiliza las selecciones.En caso de ser una carpeta 
	le pasa listdir y toma eso como opciones"""
	#en caso de ser una carpeta le pasa listdir y le limpia las extensiones(asume que todo tiene extension)
	if isFolder:
		try:
			contenido = os.listdir(os.path.realpath('.') + os.sep + opciones)
			opciones = [file.split('.')[0] for file in contenido]
			if not opciones:
				print('Something went wrong.No archivos en esa carpeta.')
				exit()
		except FileNotFoundError:
			print('No encuentro esa direccion.')
			exit()
	#printea las opciones y se encarga de que sea correcta la seleccion
	for i,opt in enumerate(opciones):
		print(f'{i+1}- {opt}')
	while 1:
		eleccion = input('\nSeleccione: ')
		try:
			eleccion = int(eleccion) - 1
			if eleccion<0:
				raise IndexError
			return opciones[eleccion]
		except ValueError:
			if eleccion.lower() == 'exit' : exit()
			else:
				print('Tiene que ser un entero o la palabra "Exit" para salir.\n')
		except IndexError:
			print('\nAclarate papi.\n')


def main():
	"""Funcion principal de la version de consola,donde se hacen las elecciones para luego llamar
	a la funcion core.Printea los resultados de las busquedas"""
	#primera eleccion, modulo
	print('\nSobre que modulo buscas:\n')
	full_path = 'Modulos' #variable que se va construyendo hasta que tiene la direccion del archivo
	modulo = seleccionador(full_path,isFolder=1)
	#segunda eleccion, action
	print('\nQue vas a hacer:\n')
	actions = ['Buscar','Testear','Agregar']
	accion = seleccionador(actions)
	#ultima eleccion,eligiendo tema segun modulo
	print('\nSobre que tema:\n')
	full_path+= os.sep + modulo
	tema = seleccionador(full_path,isFolder=1)
	full_path+= os.sep + tema + '.json'
	
	#recopilando ultima informacion y llamando la cf
	if accion=='Agregar':
		#si se eligio agregar
		agrega_key = input("\nAgrega clave: ")
		agrega_value = input ("Agrega descripcion: ")
		cf(accion,full_path,clave=agrega_key,valor=agrega_value)
		print("\nHecho chama")
	elif accion=='Buscar':
		#si se eligio buscar
		expresion = input("\nIntroduzca expresion: ")
		results,sugg = cf(accion,full_path,word=expresion)
		for clave,valor in results.items():
			print(f'\n{clave} : {valor}')
		#printe sugerencias
		if len(sugg)!=0:
			print('\n\nTambien podria interesarte: ')
			for clave,valor in sugg.items():
				print(f'\n{clave} : {valor}')
		print(f'\nResultados encontrados: {len(results)}.\nSugerencias encontradas: {len(sugg)}.')
	else:
		#testear, 10 claves randoms y luego muestra todo el contenido
		commands = cf(accion,full_path)
		for com in commands[0]:
			print('\n' + com)
		input('\n\nYa? ')
		print('\n')
		for clave,valor in commands[1].items():
			print(f'\n{clave} : {valor}')


if __name__ == "__main__":
	#algo parecido a un menu, desde donde se puede lanzar el gui u otro tool, o proseguir con el bdc
	options = ['Buscador de Comandos','Version GUI','Update','Conversor']
	print('A que vienes: \n')
	menu = seleccionador(options)
	if menu == 'Conversor':
		#anade el path del convertidor al sys.path y lo inicia
		from sys import path as sys_path
		conv_path = os.path.abspath('.') + os.sep + 'Tools' + os.sep + 'Convertidor'  
		sys_path.append(conv_path)
		import bdc_support_conversor as bdc
		bdc.run()
	elif menu == 'Update':
		from Tools.Updater import updater
		mods_path = os.path.realpath('.') + os.sep + 'Modulos'
		updater.main(mods_path,'https://raw.githubusercontent.com/Minachante99/Buscador-de-comandos/main/Modulos/')
	elif menu == 'Version GUI':
		print('En mantenimiento papiiiiiiii.Comiiiiiiiiiing Sooooooooooon')
		exit()
	elif menu == 'Buscador de Comandos':
		while 1:
			main()
			if input('\nDo you want to continue(y\\n): ') not in ['Y','y']: break

			
 