> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddTextPrefix/es.md)

El nodo Add Text Prefix modifica texto añadiendo una cadena específica al principio de cada texto de entrada. Toma el texto y un prefijo como entrada, y luego devuelve el resultado combinado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Sí | | El texto al que se le añadirá el prefijo. |
| `prefix` | STRING | No | | La cadena que se añadirá al principio del texto (valor por defecto: ""). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `text` | STRING | El texto resultante con el prefijo añadido al frente. |
