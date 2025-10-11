> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/es.md)

El nodo CLIPSubtract realiza una operación de sustracción entre dos modelos CLIP. Toma el primer modelo CLIP como base y resta los parches clave del segundo modelo CLIP, con un multiplicador opcional para controlar la intensidad de la sustracción. Esto permite una mezcla de modelos afinada al eliminar características específicas de un modelo utilizando otro.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | Requerido | - | - | El modelo CLIP base que será modificado |
| `clip2` | CLIP | Requerido | - | - | El modelo CLIP cuyos parches clave serán sustraídos del modelo base |
| `multiplier` | FLOAT | Requerido | 1.0 | -10.0 a 10.0, paso 0.01 | Controla la intensidad de la operación de sustracción |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CLIP` | CLIP | El modelo CLIP resultante después de la operación de sustracción |