class LZWdescompressor():
    def descomprimir(self, compressed_file, descompressed_file):
        with open(compressed_file, 'rb') as file:
            byte_data = file.read()

        # Configuración de variables
        dict_size = 256
        compressed_data = []
        bit_length = 9  # Tamaño inicial de los códigos en bits
        max_bit_length = 9  # Máximo tamaño en bits permitido

        # Convertir los bytes en una secuencia continua de bits
        bits = []
        for byte in byte_data:
            for i in range(8):
                bit = (byte >> (7 - i)) & 1
                bits.append(bit)

        # Convertir la secuencia de bits en códigos de tamaño `bit_length`
        current_code = 0
        bits_filled = 0

        for bit in bits:
            current_code = (current_code << 1) | bit
            bits_filled += 1

            if bits_filled == bit_length:
                compressed_data.append(current_code)
                current_code = 0
                bits_filled = 0

                # Aumentar `bit_length` sin exceder el máximo
                if dict_size < (1 << max_bit_length) and dict_size >= (1 << bit_length):
                    bit_length += 1


        # Inicializar el diccionario con caracteres ASCII
        dictionary = {i: chr(i) for i in range(dict_size)}
        result = []

        # Procesar el primer código
        if compressed_data:
            prev_code = compressed_data.pop(0)
            result.append(dictionary[prev_code])

        # Procesar los códigos restantes
        for code in compressed_data:
            if code in dictionary:
                entry = dictionary[code]
            elif code == dict_size:
                entry = dictionary[prev_code] + dictionary[prev_code][0]
            else:
                print(f"Error: Código {code} no encontrado en el diccionario.")
                raise ValueError(f"Código LZW inválido: {code}")

            result.append(entry)

            # Agregar nuevo código al diccionario, sin pasar el límite de 9 bits
            if dict_size < (1 << max_bit_length):
                dictionary[dict_size] = dictionary[prev_code] + entry[0]
                dict_size += 1

            prev_code = code

        # Unir el resultado y escribirlo en el archivo de salida
        descompressed_content = ''.join(result)
        max_code_used = max(compressed_data) if compressed_data else 0
        
        return max_code_used
        

        with open(descompressed_file, 'w', encoding='utf-8') as output:
            output.write(descompressed_content)
            
