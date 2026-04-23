> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/es.md)

El nodo Convertir Número transforma varios tipos de datos de entrada en valores numéricos. Acepta una única entrada de tipo entero, flotante, cadena de texto o booleano y produce dos salidas: un número de punto flotante y un entero. Esto es útil para convertir texto o valores lógicos a un formato que pueda ser utilizado por otros nodos matemáticos o de procesamiento en tu flujo de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `value` | INT, FLOAT, STRING, BOOLEAN | Sí | N/A | El valor que se convertirá en salidas numéricas. Acepta un entero, un número de punto flotante, una cadena de texto o un booleano verdadero/falso. |

**Nota:** Cuando la entrada es una cadena de texto, esta no debe estar vacía y debe contener una representación válida de un número (por ejemplo, `"123"`, `"3.14"`). El nodo generará un error para cadenas vacías, texto que no pueda interpretarse como un número o valores que no sean finitos (como `"inf"` o `"nan"`).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `FLOAT` | FLOAT | El valor de entrada convertido a un número de punto flotante. |
| `INT` | INT | El valor de entrada convertido a un entero. Para entradas flotantes, esto realiza un truncamiento. |