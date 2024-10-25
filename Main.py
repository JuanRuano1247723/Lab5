import os

from Lab5.LZWcompressor import LZWCompressor

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
    compressor = LZWCompressor()
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
            compressed_data = compressor.compress_file(ruta)
            if compressed_data:
                print(f"\nDatos comprimidos: {compressed_data}")
        elif opcion == '2':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()