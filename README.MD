Hola :D
# Proyecto ELT con Python

Este proyecto implementa un flujo **ELT (Extract, Load, Transform)** para limpiar un dataset de Kaggle.

## Pasos
1. **Extract** → Se lee un CSV con pandas (`extract/`).
2. **Transform** → Se limpian los datos (nulos, duplicados, columnas) (`transform/`).
3. **Load** → Se cargan los datos limpios en una base SQLite (`load/`).

-La funcionalidad del codigo esta en que el ETL sea generico es decir la idea es que pueda leer cualquier base de datos ubicada en la ruta que se le indique
para el caso practico se especifico la ruta data /raw/dataset.csv

-El dataset seleccionado fue de Kaggle es un dataset de videojuegos enfocado a las compras InApp

-Extract recibira los datos que posteriormente seran convertidos a dataframe de pandas, y se guardaran en una tabla de almacenamiento en crudo "raw_table"

-Transform limpiara los datos donde especificamente elimnara los NA, Nulos, y transformara los titulos de las columnas (teniendo encuenta eliminar espacios, reemplzarlos por guiones bajos, y convertir todo a minusculas)
EJ: si tenemos " Nombre Tabla" quedara ----> "nombre_tabla"

-Load "recibira los datos limpios de transform y se asegurara de cargarlo en una nueva tabla "clean_table"

-Finalmente main ejecuta todas las funciones creadas de cada proceso y se encarga del correcto flujo del ETL para mostrar una db completamente limpia.

## para la Ejecución
```bash
python main.py
