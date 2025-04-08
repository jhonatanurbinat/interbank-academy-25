# Proyecto de Análisis de Transacciones

## Introducción

Este proyecto tiene como objetivo leer un archivo CSV que contiene transacciones financieras, procesar los datos y generar un reporte con el balance final, la transacción de mayor monto y el conteo de transacciones de tipo crédito y débito.

## Instrucciones de Ejecución

### Requisitos
- Python 3.x
- Librerías: `csv`, `unicodedata` (incluidas en la biblioteca estándar de Python)

### Instalación
1. Clona este repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>


cd <CARPETA_DEL_PROYECTO>


python scriptv.py


El reporte será impreso en la consola con el balance final, la transacción de mayor monto y el conteo de transacciones de crédito y débito.

Enfoque y Solución
El script sigue estos pasos:

Lee las transacciones desde un archivo CSV usando el módulo csv.

Normaliza las cadenas de texto eliminando acentos y convirtiéndolas a minúsculas con la función normalize_string.

Calcula el balance final basado en las transacciones de tipo crédito y débito.

Determina la transacción de mayor monto y el conteo de transacciones de tipo crédito y débito.

Imprime el reporte con los resultados.

Estructura del Proyecto
bash
Copiar

```
├── main.py                # Archivo principal con el código
├── data.csv               # Archivo CSV con las transacciones (ejemplo)
└── README.md              # Este archivo
Documentación y Calidad del Código
El código está documentado con comentarios para explicar los pasos clave en cada función. Además, se siguen buenas prácticas para la legibilidad y mantenimiento del código.


### Detalle de la ejecucion

$ python scriptv.py
Reporte de Transacciones
---------------------------------------------
Balance Final: 10985.85
Transaccion de Mayor Monto: ID 222 - 499.69
Conteo de Transacciones: Credito: 508 Debito: 492
