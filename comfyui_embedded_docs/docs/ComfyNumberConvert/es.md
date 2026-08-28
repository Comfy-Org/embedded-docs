# Conversión de número

El nodo Number Convert transforma varios tipos de datos de entrada en valores numéricos. Acepta una única entrada de tipo entero, flotante, cadena de texto o booleano y produce dos salidas: un número flotante y un entero. Esto es útil para convertir valores de texto o lógicos en un formato que pueda ser utilizado por otros nodos matemáticos o de procesamiento en su flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `valor` | El valor que se convertirá en salidas numéricas. Acepta un entero, un número flotante, una cadena de texto o un booleano verdadero/falso. | INT, FLOAT, STRING, BOOLEAN | Sí | N/A |

**Nota:** Cuando la entrada es una cadena, esta no debe estar vacía y debe contener una representación válida de un número (por ejemplo, `"123"`, `"3.14"`). El nodo generará un error para cadenas vacías, texto que no pueda interpretarse como número o valores que no sean finitos (como `"inf"` o `"nan"`). Para entradas booleanas, `true` se convierte en 1.0 (FLOAT) y 1 (INT), mientras que `false` se convierte en 0.0 (FLOAT) y 0 (INT). Para entradas flotantes y para cadenas que contienen un número decimal, la salida entera se obtiene truncando la parte decimal.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `FLOAT` | El valor de entrada convertido a un número flotante. | FLOAT |
| `INT` | El valor de entrada convertido a un entero. Para entradas flotantes, esto realiza un truncamiento. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/es.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`
