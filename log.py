import os

class Log:
    def __init__(self, log_file_path="compression_log.txt"):
        self.log_file_path = log_file_path

    def log_compression(self, file_path, compressed_size, time, total_time, max_code):

        
        with open(self.log_file_path, 'a', encoding='utf-8') as log_file:
            
            original_size = os.path.getsize(file_path) * 8
            compressed_file_path = file_path.replace(".txt", ".lzw")
            tasa = (original_size/compressed_size) 
            
            log_file.write("=== COMPRESION ===\n")
            log_file.write(f"Arhivo original: {file_path}\n")
            log_file.write(f"Archivo comprimido: {compressed_file_path}\n")
            log_file.write(f"Tamanio original (bits): {original_size}\n")
            log_file.write(f"Tamanio comprimido (bits): {compressed_size}\n")
            log_file.write(f"Tasa de compresion: {tasa:.2f}\n")
            log_file.write(f"Tiempo de operacion: {time:.2f}  micro-segundos\n")
            log_file.write(f"Tiempo total de operacion (crear archivo): {total_time:.2f}  micro-segundos\n")
            log_file.write(f"Dictionary Max Index Used: {max_code}\n")
            log_file.write("\n")

    def log_decompression(self, compressed_file, decompressed_file, time, max_code):
        with open(self.log_file_path, 'a') as log_file:
            log_file.write("=== DECOMPRESION ===\n")
            log_file.write(f"Archivo ingresado: {compressed_file}\n")
            log_file.write(f"Archivo descomprimido: {decompressed_file}\n")
            log_file.write(f"Tiempo de operacion: {time:.2f} micro-segundos\n")
            log_file.write(f"Dictionary Max Index Used: {max_code}\n")
            log_file.write("\n")






