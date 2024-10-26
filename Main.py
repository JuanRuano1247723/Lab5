import os
import time
from LZWcompressor import LZWcompressor
from log import Log

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

    while True:
        print("\n--- Menú ---")
        print("1. Leer archivo .txt")
        print("2. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == '1':
            ruta = input("\nIngresa la ruta completa del archivo .txt: ")
            if os.path.exists(ruta) and ruta.endswith('.txt'):
                leer_archivo(ruta)
            else:
                print("\nError: Ruta inválida o el archivo no es un .txt.")
            #Compresión
            start_time = time.perf_counter()
            compressed_data = compressor.lzw_compressn_from_file(ruta)
            time_us = (time.perf_counter() - start_time) * 1_000_000  # Tiempo en microsegundos
            
            if compressed_data is not None:
                
                compressed_size = len(compressed_data) * 9  
                
                # Guardar el archivo comprimido y capturar el índice máximo usado en el diccionario
                start_total_time = time.perf_counter()
                max_code = compressor.save_compressed_to_lzw(compressed_data, ruta)
                total_time_us = ((time_us/1_000_000) + (time.perf_counter() - start_time)) * 1_000_000  # Tiempo en microsegundos
                
                logger.log_compression(ruta, compressed_size, time_us, total_time_us, max_code)
                
            elif opcion == '2':
                print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()