import os
import time
from LZWcompressor import LZWcompressor
from log import Log
from LZWdescompressor import LZWdescompressor

def leer_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            print("\nContenido del archivo:\n")
            print(contenido)
    except FileNotFoundError:
        print("\nError: Archivo no encontrado.")
    except Exception as e:
        print(f"\nError al leer el archivo: {e}")

def menu():
    compressor = LZWcompressor()
    logger = Log()
    descompressor = LZWdescompressor()

    while True:
        print("\n--- Menú ---")
        print("1. Leer archivo .txt")
        print("2. Descomprimir archivo .txt")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            ruta = input("\nIngresa la ruta completa del archivo .txt: ")
            if os.path.exists(ruta) and ruta.endswith('.txt'):
                leer_archivo(ruta)
            else:
                print("\nError: Ruta inválida o el archivo no es un .txt.")
            #Compresión
            # Incio del tiempo     
            start_time = time.perf_counter()
            compressed_data = compressor.lzw_compressn_from_file(ruta)
            # Finalización del tiempo y calculo en microsegundos
            time_us = (time.perf_counter() - start_time) * 1_000_000  
            
            if compressed_data is not None:
                compressed_size = len(compressed_data) * 9 
                # Incio del tiempo     
                start_total_time = time.perf_counter()
                # Guardar el archivo comprimido y capturar el índice máximo usado en el diccionario
                max_code = compressor.save_compressed_to_lzw(compressed_data, ruta)
                # Finalización del tiempo y calculo en microsegundos
                total_time_us = ((time_us/1_000_000) + (time.perf_counter() - start_time)) * 1_000_000 
                # Log de compresión
                logger.log_compression(ruta, compressed_size, time_us, total_time_us, max_code)
                compressor.save_compressed_to_lzw(compressed_data, ruta)

        elif opcion == '2':
            archivo_lzw = input("Ingrese la ruta del archivo .lzw: ")

            if os.path.isfile(archivo_lzw) and archivo_lzw.endswith('.lzw'):

                nombre_del_archivo = os.path.splitext(archivo_lzw)[0]

                output_file = nombre_del_archivo + 'descomprimido.txt'

                descompressor.descomprimir(archivo_lzw, output_file)
                print(f"Archivo descomprimido guardado como: {output_file}")

            else:
                print("Error: El archivo debe existir y tener la extensión .lzw.")

        elif opcion == '3':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()