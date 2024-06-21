def analizar_archivo(input_file, output_file):
    conteo_letras = 0
    conteo_espacios = 0
    
    with open(input_file, 'r', encoding='utf-8') as file:
        contenido = file.read()
        
        for caracter in contenido:
            if caracter.isalpha():
                conteo_letras += 1
            elif caracter.isspace():
                conteo_espacios += 1
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"Resumen del archivo {input_file}:\n")
        file.write(f"Número de letras: {conteo_letras}\n")
        file.write(f"Número de espacios: {conteo_espacios}\n")

if __name__ == "__main__":
    archivo_entrada = 'alvaro.txt'
    archivo_salida = 'resumen.txt'
    
    analizar_archivo(archivo_entrada, archivo_salida)
