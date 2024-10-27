import os

class Log:
    def __init__(self, log_file_path="compression_log.txt"):
        # Inicializa la clase Log con el nombre del archivo de log, usando un valor predeterminado.
        self.log_file_path = log_file_path

    def log_compression(self, file_path, compressed_size, time, total_time, max_code):
        # Registra los detalles de la compresión en el archivo de log.
        
        with open(self.log_file_path, 'a') as log_file:
            # Calcula el tamaño original del archivo en bits.
            original_size = os.path.getsize(file_path) * 8
            # Determina la ruta del archivo comprimido cambiando la extensión a .lzw.
            compressed_file_path = file_path.replace(".txt", ".lzw")
             # Calcula la tasa de compresión como la relación entre el tamaño original y el comprimido.
            tasa = (original_size/compressed_size) 
            # Escribe los detalles de la compresión en el archivo de log.
            log_file.write("=== COMPRESION ===\n")
            log_file.write(f"Arhivo original: {file_path}\n")
            log_file.write(f"Archivo comprimido: {compressed_file_path}\n")
            log_file.write(f"Tamanio original (bits): {original_size}\n")
            log_file.write(f"Tamanio comprimido (bits): {compressed_size}\n")
            log_file.write(f"Tasa de compresion: {tasa:.2f}\n")
            log_file.write(f"Tiempo de operacion: {time:.2f}  micro-segundos\n")
            log_file.write(f"Tiempo total de operacion (desde compresion hasta creacion de archivo): {total_time:.2f}  micro-segundos\n")
            log_file.write(f"Dictionary Max Index Used: {max_code}\n")
            log_file.write("\n")

    def log_decompression(self, compressed_file, decompressed_file, time, max_code):
        # Registra los detalles de la descompresión en el archivo de log.
        
        with open(self.log_file_path, 'a') as log_file:
            log_file.write("=== DECOMPRESION ===\n")
             # Escribe los detalles de la descompresión en el archivo de log.
            log_file.write(f"Archivo ingresado: {compressed_file}\n")
            log_file.write(f"Archivo descomprimido: {decompressed_file}\n")
            log_file.write(f"Tiempo de operacion: {time:.2f} micro-segundos\n")
            log_file.write(f"Dictionary Max Index Used: {max_code}\n")
            log_file.write("\n")






