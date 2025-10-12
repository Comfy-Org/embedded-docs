> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/es.md)

El nodo T5TokenizerOptions permite configurar los ajustes del tokenizador para varios tipos de modelos T5. Establece parámetros de relleno mínimo y longitud mínima para múltiples variantes de modelos T5 incluyendo t5xxl, pile_t5xl, t5base, mt5xl y umt5xxl. El nodo toma una entrada CLIP y devuelve un CLIP modificado con las opciones de tokenizador especificadas aplicadas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP para el cual configurar las opciones del tokenizador |
| `mín_relleno` | INT | No | 0-10000 | Valor de relleno mínimo a establecer para todos los tipos de modelos T5 (por defecto: 0) |
| `mín_longitud` | INT | No | 0-10000 | Valor de longitud mínima a establecer para todos los tipos de modelos T5 (por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | CLIP | El modelo CLIP modificado con las opciones de tokenizador actualizadas aplicadas a todas las variantes T5 |
