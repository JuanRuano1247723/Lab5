class LZWCompressor:
    def __init__(self):
        # Inicializamos el diccionario con los caracteres únicos
        self.max_dict_size = 256  # Tamaño inicial del diccionario
        self.dictionary = {chr(i): i for i in range(self.max_dict_size)}

    def compress(self, input_string):
        dict_size = self.max_dict_size
        compressed_data = []
        current_string = ""
        
        for symbol in input_string:
            new_string = current_string + symbol
            if new_string in self.dictionary:
                current_string = new_string
            else:
                compressed_data.append(self.dictionary[current_string])
                if dict_size < 4096:  # Tamaño máximo del diccionario
                    self.dictionary[new_string] = dict_size
                    dict_size += 1
                current_string = symbol

        if current_string:
            compressed_data.append(self.dictionary[current_string])
        
        return compressed_data

    def compress_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                input_data = file.read()
                compressed_output = self.compress(input_data)
                return compressed_output
        except FileNotFoundError:
            print("Error: Archivo no encontrado.")
        except Exception as e:
            print(f"Error al comprimir el archivo: {e}")