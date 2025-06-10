# 🔐 Cifrador Personalizado en Python

Sistema de **cifrado y descifrado** usando índices numéricos con prefijos de longitud.

## 🧠 Concepto del Cifrado

### Características:
- **Lista personalizada** de 69 caracteres
- **Prefijos dinámicos** indicando longitud del índice
- **Resistente** a análisis de frecuencia básico

### Proceso:
1. Buscar índice del carácter en `lista1`
2. Calcular dígitos del índice (1-2 dígitos)
3. Concatenar: `[longitud][índice]`

**Ejemplo:**  
`"a"` → índice 1 → `"11"`  
`"z"` → índice 27 → `"227"`

## 📋 Índice de Caracteres

| Rango  | Tipo          | Ejemplos          |
|--------|---------------|-------------------|
| 0      | Espacio       | ` `               |
| 1-27   | Letras (a-z,ñ)| a=1, ñ=15, z=27   |
| 28-57  | Especiales    | !=28, ?=49, ~=57  |
| 58-68  | Dígitos (0-9) | 0=58, 9=68        |

## 🛠 Uso

### Comandos:
```bash
python cifrador.py
```

### Opciones:
- `c`: Cifrar mensaje
- `d`: Descifrar mensaje
- `salir`: Terminar programa

### Ejemplos:

**Cifrado:**
```
Mensaje: hola
Cifrado: 1812711312
```

**Descifrado:**
```
Cifrado: 1812711312
Mensaje: hola
```

## ⚠️ Limitaciones

- No soporta mayúsculas
- Caracteres no listados causan error
- Máximo 99 caracteres en lista

## 📦 Estructura

```python
lista1 = [" ", "a", "b", ..., "9"] # 69 elementos

def cifrar_mensaje():
    # texto → número con prefijos

def descifrar_mensaje():
    # número → texto original
```

**Autor:** Eliahu Maira  
**Fecha:** 06/06/2025  
**Contacto:** eliahu.en.maira@icloud.com