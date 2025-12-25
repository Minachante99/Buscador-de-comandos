"""Script para actualizar los elementos de una carpeta desde el github mediante descarga directa.
A futuro que la aplicacion determine OS y si es window que lo haga desde git."""

import os
for modulo in ['wget','requests']:
    try:
        exec(f'import {modulo}')
    except ModuleNotFoundError:
        print(f'\nNo se encontro el modulo {modulo}, voy a intentar instalarlo.Revisa que tengas internet.')
        input('Presiona algo para continuar: ')
        try:
            os.system('pip install ' + modulo)
            exec(f'import {modulo}')
            print('Instalado!')
        except:
            print('Algo salio mal al intentar instalar, rechecka de nuevo fijate si tienes internet.')
            exit()

def main(base_path,base_url):
    """Funcion que transeversa una carpeta y va actualizando del link de github"""
    #definiendo headers y modulos
    headers = {
		'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0',
        'Accept-Language' : 'es-419,es;q=0.9,en-US;q=0.8,en;q=0.7',
		'Accept-Encoding' : 'gzip, br'
}
    modulos = os.listdir(base_path) + ['All']
    #mostrando modulos
    print('\nModulos:\n')
    for ind,obj in enumerate(modulos): 
        print(f'{ind+1}- {obj}')
    rango = range(len(modulos))
    #seleccion de modulo
    while 1:
        eleccion = input('\nSeleccione modulo: ')
        try:
            eleccion = int(eleccion) - 1 
            if (eleccion) in rango: break
            else :
                print('\nAclarate papi.\n')
                continue
        except ValueError:
            if eleccion.lower() == 'exit' : exit()
            else:
                print('Tiene que ser un entero o la palabra "Exit" para salir.\n')
    #si se selecciono all que sea a traves de todos los modulos.
    modulos = modulos[:-1] if modulos[eleccion]=='All' else [modulos[eleccion]]
    #iterando a traves de los modulos, paths y github
    for mod in modulos:
        #obteniendo temas y moviendose a carpeta
        os.chdir(base_path + os.sep + mod)
        temas = os.listdir('.')
        #segundo iter para descargar 
        for subj in temas:
            link = base_url + mod + '/' + subj
            print(link)
            try:
                call = requests.get(link,headers=headers,timeout=15)
            except:
                print('Probablemente tengas un problema de internet. Rechecka e intentalo de nuevo.')
                exit()
            if call.status_code==200:
                print(f'\n{subj}: OK')
                os.remove(subj)
                wget.download(url=link,out='.')
            #en mantenimiento,para dar mas informacion sobre el error
            elif call.status_code>=500:
                print(f'\nSomething went wrong with the server:( with {link}')
            else :
                print(f'\nSomething went wrong:( with {link}')


if __name__ == '__main__':
    base_url = 'https://raw.githubusercontent.com/Minachante99/Buscador-de-comandos/main/Modulos/'
    base_path = 'D:\Programacion\Proyectos\Test_spot\Modulos'
    main(base_path,base_url)