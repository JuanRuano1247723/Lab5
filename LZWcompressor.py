class LZWcompressor():
    def lzw_compressn_from_file(self, file_path):
        try:
            # Abrir y leer el archivo .txt
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()  # Leer todo el contenido del archivo

            # Crear el diccionario inicial con todos los caracteres únicos
            diccionario = {chr(i): i for i in range(256)}  # Códigos de 0 a 255 para caracteres ASCII
            código_actual = 256  # Siguiente código disponible
            max_codigos = 512

            # Variables de estado
            W = ""
            resultado = []  # Lista para almacenar los códigos comprimidos

            # Iterar sobre cada símbolo en la entrada
            for C in data:
                WC = W + C
                if WC in diccionario:
                    W = WC  # Si W + C está en el diccionario, expandir W
                else:
                    # Emitir el código de W
                    resultado.append(diccionario[W])

                    # Agregar W + C al diccionario
                    if código_actual < max_codigos:
                        diccionario[WC] = código_actual
                        código_actual += 1

                    # Establecer W como el nuevo símbolo actual
                    W = C

            # Emitir el último código de W
            if W:
                resultado.append(diccionario[W])
            
            # Retornar los códigos comprimidos
            return resultado

        except FileNotFoundError:
            print(f"Error: El archivo '{file_path}' no fue encontrado.")
            return None
        except Exception as e:
            print(f"Error al comprimir el archivo: {e}")
            return None

    def save_compressed_to_lzw(self, compressed_data, original_file_path):
            try:
                # Determinar la cantidad mínima de bits necesarios para representar los códigos
                bit_length = 9  # Número de bits necesarios

                # Crear el nuevo nombre de archivo con extensión .lzw
                new_file_path = original_file_path.replace(".txt", ".lzw")

                # Abrir el archivo en modo binario para escritura
                with open(new_file_path, 'wb') as file:
                    current_byte = 0  # Byte temporal que estamos llenando
                    bits_filled = 0   # Cantidad de bits usados en el byte actual

                    # Recorrer cada código comprimido
                    for code in compressed_data:
                        # Convertir el código a su representación binaria con la longitud mínima
                        code_bits = format(code, f'0{bit_length}b')
                        

                        # Añadir cada bit al byte actual
                        for bit in code_bits:
                            current_byte = (current_byte << 1) | int(bit)  # Añadir el bit al byte actual
                            bits_filled += 1

                            # Si el byte está lleno (8 bits), escribirlo en el archivo
                            if bits_filled == 8:
                                file.write(bytes([current_byte]))  # Escribir el byte al archivo
                                current_byte = 0  # Reiniciar el byte temporal
                                bits_filled = 0

                    # Si quedan bits que no llenaron un byte completo, escribir el byte restante
                    if bits_filled > 0:
                        # Rellenar con ceros los bits restantes para completar el byte
                        current_byte <<= (8 - bits_filled)
                        file.write(bytes([current_byte]))  # Escribir el último byte


                # Mostrar los códigos binarios generados
                print(f"Archivo comprimido guardado como {new_file_path}")
                

            except Exception as e:
                print(f"Error al guardar el archivo comprimido: {e}")

   