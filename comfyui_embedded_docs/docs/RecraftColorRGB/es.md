> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/es.md)

Crear color Recraft eligiendo valores RGB específicos. Este nodo permite definir un color especificando valores individuales de rojo, verde y azul, que luego se convierten a un formato de color Recraft que puede utilizarse en otras operaciones Recraft.

## Entradas

| Parámetro | Tipo de Datos | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `r` | INT | Sí | 0-255 | Valor rojo del color (por defecto: 0) |
| `g` | INT | Sí | 0-255 | Valor verde del color (por defecto: 0) |
| `b` | INT | Sí | 0-255 | Valor azul del color (por defecto: 0) |
| `recraft_color` | COLOR | No | - | Color Recraft existente opcional para extender |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `recraft_color` | COLOR | El objeto de color Recraft creado que contiene los valores RGB especificados |