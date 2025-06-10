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
`"z"` → índice 2 → `"227"`

## 🎨 Personalización

### ¿Cómo funciona el cifrado?

Este encriptador utiliza una "base de datos" personalizable:  
Una lista (`lista1`) que contiene todos los caracteres permitidos, en un orden específico.  
Cada carácter de tu mensaje se convierte en un número según su posición en la lista.  
El número cifrado incluye un prefijo que indica cuántos dígitos tiene el índice, haciendo el cifrado dinámico y fácil de descifrar.

**Funcionamiento:**
1. El programa busca cada carácter del mensaje en la lista.
2. Obtiene su posición (índice) en la lista.
3. Añade la longitud del índice como prefijo.
4. Une todos los números para crear el mensaje cifrado.

### Lista de caracteres por defecto

Esta es la lista (`lista1`) utilizada en el código por defecto (69 caracteres):

```python
lista1 = [
    " ", "a", "b", "c", "d", "e", "f", "g", "h", "i",
    "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r",
    "s", "t", "u", "v", "w", "x", "y", "z", "!", '"',
    "#", "$", "%", "&", "'", "(", ")", "*", "+", ",",
    "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",
    "[", "\\", "]", "^", "_", "{", "|", "}", "~",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]
```

### ¿Cómo personalizar la lista?

1. Abre el archivo `encrypter.py` con cualquier editor de texto.
2. Modifica la lista `lista1` para agregar, quitar o reordenar caracteres.
3. Guarda el archivo y ejecuta el programa normalmente.

**Ejemplo:**  
Si quieres distinguir mayúsculas, podrías editar así:

```python
lista1 = [
    " ", "a", "b", ..., "z", "A", "B", ..., "Z", "0", ..., "9"
]
```

¡Listo! Ahora tu cifrador es completamente personalizado según tu lista de caracteres.

## 🛠️ Instalación

1. Asegúrate de tener Python 3 instalado. Puedes verificarlo ejecutando:

    ```bash
    python3 --version
    ```

2. Clona este repositorio o descarga el archivo `encrypter.py`:

    ```bash
    git clone https://github.com/EliahuMaira/Python-Encrypter.git
    cd Python-Encrypter
    ```

3. No se requieren dependencias adicionales. Todo el código utiliza únicamente la biblioteca estándar de Python.

---

## 🚀 Cómo usar

Ejecuta el programa desde la terminal:

```bash
python3 encrypter.py
```

Sigue las instrucciones en pantalla para cifrar o descifrar mensajes.

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

## 🧩 Desglose del Código

A continuación se explica la estructura básica de `encrypter.py` y el propósito de cada parte:

### 1. Definición de la lista de caracteres

```python
lista1 = [ ... ]
```
Esta lista contiene todos los caracteres permitidos para cifrar y descifrar. El orden define el índice numérico de cada carácter.

---

### 2. Función para cifrar mensajes

```python
def cifrar_mensaje(lista1):
    ...
```
- Solicita al usuario el mensaje a cifrar.
- Recorre cada letra, busca su posición en la lista y construye el mensaje cifrado añadiendo el prefijo de longitud y el índice.
- Si encuentra un carácter no permitido, muestra un error y detiene el proceso.

---

### 3. Función para descifrar mensajes

```python
def descifrar_mensaje(lista1):
    ...
```
- Solicita el mensaje cifrado.
- Lee el primer dígito (que indica la longitud del índice), extrae el índice correspondiente y lo convierte de nuevo en carácter usando la lista.
- Repite el proceso hasta reconstruir el mensaje original.
- Si encuentra un valor no válido, muestra un error y detiene el proceso.

---

### 4. Menú interactivo

```python
while True:
    ...
```
- Permite al usuario elegir entre cifrar, descifrar o salir.
- Llama a la función correspondiente según la opción seleccionada.

---

### 5. Validaciones

- El código verifica que todos los caracteres a cifrar estén en la lista.
- También valida que los índices extraídos durante el descifrado sean válidos y estén dentro del rango permitido.

---

**Resumen:**  
El flujo del programa es sencillo y está pensado para ser interactivo. Todo el cifrado y descifrado depende de la lista personalizada, lo que te permite adaptarlo fácilmente a tus necesidades.

**Autor:** Eliahu Maira  
**Fecha:** 06/06/2025  
**Contacto:** eliahu.en.maira@icloud.com
