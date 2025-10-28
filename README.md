# Cadenas con Funciones — Python

Este repositorio contiene tres programas en Python que trabajan con cadenas de texto utilizando funciones.  
Cada uno realiza una tarea diferente:

- Contar vocales, consonantes y espacios en una cadena.
- Verificar si una cadena es un palíndromo.
- Analizar un texto completo para contar palabras, frases y párrafos.

---

## Archivos incluidos

| Archivo | Descripción |
|--------|-------------|
| contar_caracteres.py | Cuenta vocales, consonantes y espacios en un texto ingresado. |
| palindromo.py | Determina si una palabra o frase es un palíndromo. |
| analizador_texto.py | Cuenta palabras, frases y párrafos en un texto. |

---

## 1) contar_caracteres.py

### Descripción
Este programa cuenta cuántas vocales, consonantes y espacios contiene una frase o palabra ingresada por el usuario.

### Funcionamiento
1. El usuario escribe un texto.
2. El programa recorre carácter por carácter.
3. Clasifica cada uno en vocal, consonante o espacio.
4. Muestra los totales.

### Ejemplo de ejecución
Escribe una cadena de texto: Hola Mundo
Cantidad de vocales: 4
Cantidad de consonantes: 5
Cantidad de espacios: 1


---

## 2) palindromo.py

### Descripción
Este programa verifica si un texto es un palíndromo: se lee igual de izquierda a derecha y de derecha a izquierda.

### Funcionamiento
1. Se ingresa una palabra o frase.
2. Se convierte el texto a minúsculas.
3. Se eliminan los espacios.
4. Se compara el texto con su versión invertida.
5. Se muestra si es palíndromo o no.

### Ejemplo de ejecución
Ingresa una palabra o frase: oso
La frase es un palíndromo.


---

## 3) analizador_texto.py

### Descripción
Analiza un texto para contar:
- Número total de palabras
- Número de frases
- Número de párrafos

### Funcionamiento
1. El usuario puede escribir el texto o leerlo desde un archivo .txt.
2. El programa procesa y separa el contenido.
3. Muestra los conteos correspondientes.

### Ejemplo de ejecución
Palabras: 12
Frases: 3
Párrafos: 1
