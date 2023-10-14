
def choice_1():
	print(""" 

Sobre que buscas:

1- Python
2- Html
3- Consola
4- PostgreSQL

Exit - termina el programa  
    
""")
	while 1:
		eleccion_1 = input("Escoja tema: ")
		eleccion_1 = eleccion_1.replace(" ", "")
		if eleccion_1.lower() == "exit":
		      exit()
		elif eleccion_1 in ['1','2','3','4']:
			if eleccion_1 == "1":
				eleccion_1 = "Python"
			elif eleccion_1 == "2":
				eleccion_1 = "Html"
			elif eleccion_1 == "3":
				eleccion_1 = "Consola"
			elif eleccion_1 == "4":
				eleccion_1 = "PostgreSQL"
			break
		else:
			print("Chama aclarate\n")
	return eleccion_1
           
def choice_2():
	print("""
    
Que vas a hacer:

1- Buscar
2- Agregar

Exit- termina el programa
    
""")

	while 1:
		eleccion_2 = input("Escoja tema: ")
		eleccion_2 = eleccion_2.replace(" ", "")
		if eleccion_2 in ['1','2']:
			break
		elif eleccion_2.lower() == "exit":
			exit()
		else:
			print("Chama aclarate\n")
	return eleccion_2

def choice_3(files):
 
	#Prompt
	print('\nSobre que tema vas a buscar:\n')
	for i,n in enumerate(files):
		print(str(i+1)+'-', n[:-5])
	print('\nExit - termina el programa\n')
	
	#main
	leer_todo = False
	while True:
	    eleccion_3 = input("Escoja tema: ")
	    eleccion_3 = eleccion_3.replace(" ", "")
	    if len(eleccion_3)==1 and eleccion_3.isnumeric() and int(eleccion_3) in range(1,len(files)+1):
	    	break
	    elif eleccion_3.lower() == "exit":
	    	exit()
	    elif eleccion_3.startswith("*") and len(eleccion_3) < 3 and eleccion_3[1].isnumeric() and int(eleccion_3[1]) in range(1,len(files)+1) :
	    	leer_todo = True
	    	eleccion_3 = eleccion_3[1]
	    	break
	    else:
	    	print("Chama aclarate\n")
	eleccion_3 = files[int(eleccion_3)- 1]
	return [eleccion_3, leer_todo]