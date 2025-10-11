> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/es.md)

El nodo CLIPAdd combina dos modelos CLIP fusionando sus parches clave. Crea una copia del primer modelo CLIP y luego añade la mayoría de los parches clave del segundo modelo, excluyendo los ID de posición y los parámetros de escala logit. Esto permite combinar características de diferentes modelos CLIP preservando la estructura del primer modelo.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `clip1` | CLIP | Requerido | - | - | El modelo CLIP principal que se utilizará como base para la fusión |
| `clip2` | CLIP | Requerido | - | - | El modelo CLIP secundario que proporciona parches adicionales para ser añadidos |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Devuelve un modelo CLIP fusionado que combina características de ambos modelos de entrada |