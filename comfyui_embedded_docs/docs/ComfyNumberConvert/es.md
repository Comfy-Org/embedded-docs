> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/es.md)

El nodo Convertir Número transforma varios tipos de datos de entrada en valores numéricos. Acepta una única entrada de tipo entero, flotante, cadena de texto o booleano y produce dos salidas: un número de punto flotante y un número entero. Esto es útil para convertir valores de texto o lógicos en un formato que pueda ser utilizado por otros nodos matemáticos o de procesamiento en tu flujo de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `valor` | INT, FLOAT, STRING, BOOLEAN | Sí | N/A | El valor que se convertirá en salidas numéricas. Acepta un número entero, un número de punto flotante, una cadena de texto o un valor booleano verdadero/falso. |

**Nota:** Cuando la entrada es una cadena de texto, no debe estar vacía y debe contener una representación válida de un número (por ejemplo, `"123"`, `"3.14"`). El nodo generará un error para cadenas vacías, texto que no pueda interpretarse como un número o valores que no sean finitos (como `"inf"` o `"nan"`). Para entradas booleanas, `true` se convierte en 1.0 (FLOAT) y 1 (INT), mientras que `false` se convierte en 0.0 (FLOAT) y 0 (INT). Para entradas flotantes, la salida entera se obtiene truncando la parte decimal.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `FLOAT` | FLOAT | El valor de entrada convertido a un número de punto flotante. |
| `INT` | INT | El valor de entrada convertido a un número entero. Para entradas flotantes, esto realiza un truncamiento. |

---
**Source fingerprint (SHA-256):** `961fbea05b22c68f768f9ecaae2ee455b1913afe4a65d8c0e6b6497b1e24ce72`
