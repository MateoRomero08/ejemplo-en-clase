Hola :D
# Proyecto ELT con Python

Este proyecto implementa un flujo **ELT (Extract, Load, Transform)** para limpiar un dataset de Kaggle.

## Pasos
1. **Extract** → Se lee un CSV con pandas (`extract/`).
2. **Load** → Se cargan los datos crudos en una base SQLite (`load/`).
3. **Transform** → Se limpian los datos (nulos, duplicados, columnas) (`transform/`).

## Ejecución
```bash
python main.py