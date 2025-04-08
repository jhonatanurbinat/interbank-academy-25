
### Código Documentado

# Importa la librería CSV para manejar archivos CSV y unicodedata para normalizar cadenas


import csv
import unicodedata

def leer_transacciones(archivo):
    """
    Lee un archivo CSV con transacciones y las devuelve como una lista de diccionarios.

    :param archivo: Nombre del archivo CSV que contiene las transacciones.
    :return: Lista de diccionarios con las transacciones procesadas.
    """
    transacciones = []  # Lista donde se guardarán las transacciones procesadas
    with open(archivo, mode='r') as file:
        reader = csv.DictReader(file)  # Lee el archivo CSV como un diccionario
        for row in reader:
            transacciones.append({
                'id': int(row['id']),  # Convierte el ID a entero
                'tipo': normalize_string(row['tipo']),  # Normaliza el tipo de transacción
                'monto': float(row['monto'])  # Convierte el monto a flotante
            })
    return transacciones


def normalize_string(texto):
    """
    Normaliza una cadena de texto eliminando acentos y convirtiéndola a minúsculas.

    Se tuvo que realizar por las tildes en el archivo csv

    :param texto: Cadena de texto a normalizar.
    :return: Cadena de texto normalizada, en minúsculas y sin acentos.
    """
    # Eliminar acentos y convertir a minúsculas
    texto_normalizado = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    return texto_normalizado.strip().lower()  # Elimina espacios y convierte a minúsculas


def reporte_transacciones(transacciones):
    """
    Genera un reporte con el balance final, la transacción de mayor monto y el conteo de transacciones.

    :param transacciones: Lista de transacciones a procesar.
    """
    balance_final = 0  # Inicializa el balance
    transaccion_mayor_monto = 0  # Inicializa el monto de la transacción mayor
    conteo_credito = 0  # Contador de transacciones de tipo crédito
    conteo_debito = 0  # Contador de transacciones de tipo débito
    id_transaccion_mayor_monto = 0  # ID de la transacción con mayor monto

    # Procesar cada transacción
    for trans in transacciones:
        # Si la transacción es de tipo crédito, aumenta el balance
        if trans['tipo'] == 'cradito': 
            balance_final += trans['monto']
            conteo_credito += 1
        # Si la transacción es de tipo débito, disminuye el balance
        elif trans['tipo'] == 'dabito':
            balance_final -= trans['monto']
            conteo_debito += 1

        # Actualiza la transacción de mayor monto
        if trans['monto'] > transaccion_mayor_monto: 
            transaccion_mayor_monto = trans['monto']
            id_transaccion_mayor_monto = trans['id']

    # Imprime el reporte con los resultados
    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance_final:.2f}")
    print(f"Transaccion de Mayor Monto: ID {id_transaccion_mayor_monto} - {transaccion_mayor_monto:.2f}")
    print(f"Conteo de Transacciones: Credito: {conteo_credito} Debito: {conteo_debito}")


# Ejecución principal del script
if __name__ == "__main__":
    archivo = 'data.csv'  # Nombre del archivo CSV con las transacciones
    transacciones = leer_transacciones(archivo)  # Lee las transacciones del archivo
    reporte_transacciones(transacciones)  # Genera y muestra el reporte
